// Comprobacion de cobertura: todo grafico y toda tabla de los tableros de los
// Prototipos 1 y 2 debe estar presente en el tablero integrado, con sus mismos
// valores. Los graficos se dibujan con JavaScript, de manera que la comprobacion
// se hace en el navegador con Chrome.
// Uso: node scripts/comprobar-cobertura.mjs <raiz>
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

const rutas = {
  p1: path.join(raiz, 'resultados-prototipos', 'prototipo-1', 'dashboard-resultados_prototipo_1.html'),
  p2: path.join(raiz, 'resultados-prototipos', 'prototipo-2', 'dashboard-resultados_prototipo_2.html'),
  integrado: path.join(raiz, 'resultados-prototipos', 'dashboard-resultados-integrado.html'),
};

const normalizar = (s) => s.replace(/\s+/g, ' ').trim();

// ── Comprobacion estatica de las tablas ────────────────────────────────────
const celdas = (html) => {
  const out = [];
  for (const m of html.matchAll(/<table[^>]*>([\s\S]*?)<\/table>/g)) {
    for (const c of m[1].matchAll(/<t[dh][^>]*>([\s\S]*?)<\/t[dh]>/g)) {
      const t = normalizar(c[1].replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' '));
      if (t) out.push(t);
    }
  }
  return out;
};

const celdasIntegrado = new Set(celdas(fs.readFileSync(rutas.integrado, 'utf8')));

console.log('== Tablas: celdas de origen presentes en el integrado ==');
let problemasTabla = 0;
for (const proto of ['p1', 'p2']) {
  const html = fs.readFileSync(rutas[proto], 'utf8');
  const tablas = [...html.matchAll(/<table[^>]*>([\s\S]*?)<\/table>/g)];
  tablas.forEach((t, i) => {
    const celdasTabla = [...t[1].matchAll(/<t[dh][^>]*>([\s\S]*?)<\/t[dh]>/g)]
      .map((c) => normalizar(c[1].replace(/<[^>]+>/g, ' ')))
      .filter(Boolean);
    const ausentes = [...new Set(celdasTabla)].filter((c) => !celdasIntegrado.has(c));
    if (ausentes.length === 0) {
      console.log(`  OK   ${proto} tabla ${i + 1}  ${celdasTabla.length} celdas presentes`);
    } else {
      console.log(`  FALTA ${proto} tabla ${i + 1}  ${ausentes.length} celda(s) ausente(s):`);
      ausentes.slice(0, 6).forEach((a) => console.log('         - ' + a.slice(0, 90)));
      problemasTabla += ausentes.length;
    }
  });
}

// ── Comprobacion en el navegador de los graficos ───────────────────────────
const graficosFuente = {
  p1: ['ch-tiempo', 'ch-dist', 'ch-fuentes', 'ch-attack'],
  p2: ['ch-vueltas', 'ch-fuentes', 'ch-instrumentos', 'ch-tiempo', 'ch-dist', 'ch-attack', 'ch-ciclo', 'ch-lecciones'],
};

const navegador = await chromium.launch({ channel: 'chrome' });

async function textosDe(pagina, ids) {
  return pagina.evaluate((ids) => {
    const salida = {};
    for (const id of ids) {
      const cont = document.getElementById(id);
      salida[id] = cont
        ? [...cont.querySelectorAll('text')].map((t) => t.textContent.trim()).filter(Boolean)
        : null;
    }
    const todo = document.body.innerText.replace(/\s+/g, ' ');
    return { porGrafico: salida, todo };
  }, ids);
}

const pagina = await navegador.newPage({ viewport: { width: 1400, height: 1000 } });
await pagina.goto('file:///' + rutas.integrado.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(1200);
const integrado = await textosDe(pagina, []);
const textoIntegrado = integrado.todo;
const graficosIntegrado = await pagina.evaluate(() =>
  [...document.querySelectorAll('[id^="ch-"]')].filter((e) => e.querySelector('svg')).map((e) => e.id));
const estructura = await pagina.evaluate(() => ({
  secciones: document.querySelectorAll('section').length,
  tablas: document.querySelectorAll('table').length,
  imagenes: document.querySelectorAll('img').length,
}));

let problemas = 0;
console.log('\n== Graficos: valores de origen presentes en el integrado ==');
for (const [proto, ids] of Object.entries(graficosFuente)) {
  await pagina.goto('file:///' + rutas[proto].replace(/\\/g, '/'), { waitUntil: 'load' });
  await pagina.waitForTimeout(1200);
  const { porGrafico } = await textosDe(pagina, ids);
  for (const id of ids) {
    const chaves = porGrafico[id];
    if (!chaves) { console.log(`  FALTA el grafico ${id} en ${proto}`); problemas++; continue; }
    const vs = new Set();
    for (const t of chaves) for (const n of t.match(/\d+(?:[.,]\d+)?/g) ?? []) vs.add(n);
    const ausentes = [...vs].filter((v) => !textoIntegrado.includes(v));
    if (ausentes.length === 0) {
      console.log(`  OK   ${proto}/${id}  ${vs.size} valores presentes`);
    } else {
      console.log(`  FALTA ${proto}/${id}  ausentes: ${ausentes.join(', ')}`);
      problemas += ausentes.length;
    }
  }
}

console.log('\n== Estructura del integrado ==');
console.log('  Graficos dibujados: ' + graficosIntegrado.length + '  (' + graficosIntegrado.join(', ') + ')');
console.log('  Secciones: ' + estructura.secciones);
console.log('  Tablas: ' + estructura.tablas);
console.log('  Imagenes: ' + estructura.imagenes);
console.log('\n  Celdas de tabla ausentes: ' + problemasTabla);
console.log('  Valores de grafico ausentes: ' + problemas);

await navegador.close();
if (problemasTabla + problemas === 0) {
  console.log('\n  Cobertura completa: todo grafico y toda tabla de los dos prototipos esta en el integrado.');
} else {
  console.log('\n  Revisar los elementos ausentes listados arriba.');
}
