// Verifica el tablero integrado en Chrome: valores clave, errores de consola
// y captura de las secciones corregidas.
// Uso: node scripts/verificar-tablero.mjs <raiz>
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2] ? path.resolve(process.argv[2]) : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = path.join(raiz, 'resultados-prototipos', 'dashboard-resultados-integrado.html');
const salida = path.join(raiz, '.render');
fs.mkdirSync(salida, { recursive: true });

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 1 });

const errores = [];
pagina.on('console', (m) => { if (m.type() === 'error') errores.push(m.text()); });
pagina.on('pageerror', (e) => errores.push('pageerror: ' + e.message));

await pagina.goto('file:///' + html.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(1200);

const info = await pagina.evaluate(() => {
  const svgText = (id) => {
    const el = document.getElementById(id);
    if (!el) return '[falta]';
    return Array.from(el.querySelectorAll('text')).map((t) => t.textContent.trim()).join(' | ');
  };
  const notaH = document.querySelector('#dist .note');
  return {
    secciones: document.querySelectorAll('section').length,
    tablas: document.querySelectorAll('table').length,
    graficos: document.querySelectorAll('svg').length,
    imagenes: document.querySelectorAll('img').length,
    nivel: svgText('ch-nivel'),
    distribucionFinal: svgText('ch-dist'),
    ciclo: svgText('ch-ciclo'),
    sintesis: svgText('ch-sintesis'),
    notaDistribucion: notaH ? notaH.textContent.replace(/\s+/g, ' ').trim() : '[falta]',
  };
});

console.log('Secciones: ' + info.secciones);
console.log('Tablas: ' + info.tablas);
console.log('Graficos SVG: ' + info.graficos);
console.log('Imagenes: ' + info.imagenes);
console.log('Escala de cortes: ' + info.nivel);
console.log('Distribucion final: ' + info.distribucionFinal);
console.log('Ciclo: ' + info.ciclo);
console.log('Sintesis: ' + info.sintesis);
console.log('Nota distribucion: ' + info.notaDistribucion);
console.log('Errores de consola: ' + (errores.length === 0 ? 'ninguno' : errores.join(' / ')));

for (const [id, nombre] of [['dist', 'seccion-distribucion'], ['ciclo', 'seccion-ciclo'], ['sintesis', 'seccion-sintesis']]) {
  const el = await pagina.$('#' + id);
  if (el) await el.screenshot({ path: path.join(salida, nombre + '.png') });
}
console.log('Capturas guardadas en ' + salida);

await navegador.close();
