// Captura los bloques de tarjetas de indicadores de los tres tableros de
// resultados. Cada bloque se guarda como una imagen independiente, de manera
// que ninguna tarjeta quede sin registro visual.
// Uso: node scripts/capturar-tarjetas-kpi.mjs <raiz>
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

const salida = path.join(raiz, 'resultados-prototipos', 'evidencia-visual', 'tarjetas-kpi');
fs.mkdirSync(salida, { recursive: true });

// Tablero -> lista de [seccion, clase, nombre del archivo]
const tableros = [
  {
    nombre: 'integrado',
    archivo: path.join(raiz, 'resultados-prototipos', 'dashboard-resultados-integrado.html'),
    bloques: [
      ['base', 'kpis', 'integrado-01-linea-base-institucional'],
      ['antes', 'kpis', 'integrado-02-antes-y-despues'],
      ['p1', 'kpis', 'integrado-03-prototipo-1-indicadores'],
      ['p1', 'strip', 'integrado-04-volumen-de-la-ejecucion'],
    ],
  },
  {
    nombre: 'prototipo-1',
    archivo: path.join(raiz, 'resultados-prototipos', 'prototipo-1', 'dashboard-resultados_prototipo_1.html'),
    bloques: [
      ['kpi', 'kpis', 'prototipo-1-01-indicadores-principales'],
    ],
  },
  {
    nombre: 'prototipo-2',
    archivo: path.join(raiz, 'resultados-prototipos', 'prototipo-2', 'dashboard-resultados_prototipo_2.html'),
    bloques: [
      ['kpi', 'kpis', 'prototipo-2-01-indicadores-principales'],
      ['inst', 'kpis', 'prototipo-2-02-resultado-global-del-libro-oficial'],
    ],
  },
];

const navegador = await chromium.launch({ channel: 'chrome' });
let total = 0;

for (const t of tableros) {
  const pagina = await navegador.newPage({
    viewport: { width: 1400, height: 1000 },
    deviceScaleFactor: 2,
  });
  await pagina.goto('file:///' + t.archivo.replace(/\\/g, '/'), { waitUntil: 'load' });
  await pagina.waitForTimeout(1500);

  for (const [seccion, clase, nombre] of t.bloques) {
    // Se elige el bloque nth de esa clase dentro de la seccion indicada.
    const manejador = await pagina.evaluateHandle(
      ({ seccion, clase }) => {
        const cont = document.getElementById(seccion);
        if (!cont) return null;
        return cont.querySelectorAll('.' + clase)[cont.querySelectorAll('.' + clase).length > 0 ? 0 : 0] ?? null;
      },
      { seccion, clase });
    const elemento = manejador.asElement();
    if (!elemento) { console.log('FALTA  ' + t.nombre + '/' + seccion + '/' + clase); continue; }
    const archivo = path.join(salida, nombre + '.png');
    await elemento.screenshot({ path: archivo });
    const tarjetas = await pagina.evaluate(
      (el) => el.querySelectorAll('.kpi, .strip > div').length, elemento);
    console.log('OK  ' + path.basename(archivo) + '  ·  ' + tarjetas + ' tarjetas');
    total++;
  }

  await pagina.close();
}

await navegador.close();
console.log('\nBloques capturados: ' + total + ' en ' + salida);
