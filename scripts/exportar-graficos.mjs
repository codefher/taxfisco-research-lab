// Exporta cada grafico del tablero integrado a PNG, a su tamano natural de viewBox.
// Uso: node scripts/exportar-graficos.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

// La raiz del repositorio puede venir como argumento para poder ejecutar el
// script desde un directorio donde este instalado el paquete de Playwright.
const raiz = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = path.join(raiz, 'resultados-prototipos', 'dashboard-resultados-integrado.html');
const salida = path.join(raiz, 'resultados-prototipos', 'evidencia-visual', 'graficos');
fs.mkdirSync(salida, { recursive: true });

// id del grafico en el tablero -> nombre del archivo generado
const graficos = [
  ['ch-nivel', 'b-escala-cortes'],
  ['ch-p1-tiempo', 'd-tiempo-prototipo-1'],
  ['ch-p1-dist', 'd-distribucion-tiempo-1'],
  ['ch-p1-fuentes', 'd-componentes-deteccion'],
  ['ch-p1-tacticas', 'd-tecnicas-por-tactica'],
  ['ch-p1-red', 'd-contenedores-por-segmento'],
  ['ch-p2-cob', 'f-cobertura-prototipo-2'],
  ['ch-p2-fuentes', 'f-fuentes-que-registran-deteccion'],
  ['ch-p2-tiempo', 'g-tiempo-escenarios-comparables'],
  ['ch-dist', 'h-distribucion-tiempo-final'],
  ['ch-ciclo', 'i-ciclo-iteraciones'],
  ['ch-attack', 'j-cobertura-mitre-attack'],
  ['ch-lecciones', 'l-lecciones-por-fase'],
  ['ch-sintesis', 'o-sintesis'],
];

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({
  viewport: { width: 1400, height: 1000 },
  deviceScaleFactor: 2,
});
const url = 'file:///' + html.replace(/\\/g, '/');
await pagina.goto(url, { waitUntil: 'load' });
await pagina.waitForTimeout(900);

for (const [id, nombre] of graficos) {
  const caja = await pagina.evaluate((id) => {
    const cont = document.getElementById(id);
    if (!cont) return null;
    const svg = cont.querySelector('svg');
    if (!svg) return null;
    const vb = svg.getAttribute('viewBox').split(/\s+/).map(Number);
    const w = vb[2];
    const h = vb[3];
    const envoltura = document.createElement('div');
    envoltura.id = 'envoltura-export';
    envoltura.style.cssText =
      'position:fixed;left:0;top:0;z-index:99999;background:#FFFFFF;padding:14px;' +
      'width:' + (w + 28) + 'px;box-sizing:content-box;';
    const copia = svg.cloneNode(true);
    copia.setAttribute('width', String(w));
    copia.setAttribute('height', String(h));
    copia.style.display = 'block';
    envoltura.appendChild(copia);
    document.body.appendChild(envoltura);
    return { w: w + 28, h: h + 28 };
  }, id);
  if (!caja) {
    console.log('FALTA  ' + id);
    continue;
  }
  const archivo = path.join(salida, nombre + '.png');
  const elemento = await pagina.$('#envoltura-export');
  await elemento.screenshot({ path: archivo });
  console.log('OK     ' + nombre + '.png  ' + caja.w + 'x' + caja.h);
  await pagina.evaluate(() => {
    const e = document.getElementById('envoltura-export');
    if (e) e.remove();
  });
}

await navegador.close();
console.log('Exportacion terminada en ' + salida);
