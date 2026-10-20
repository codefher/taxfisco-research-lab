// Captura paginas del PDF en PNG para revisar la maquetacion visualmente.
// Uso: node scripts/capturar-pdf.mjs <raiz> <paginas separadas por coma>
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2] ? path.resolve(process.argv[2]) : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const paginas = (process.argv[3] || '1').split(',').map(Number);
const pdf = process.argv[4]
  ? path.resolve(process.argv[4])
  : path.join(raiz, '.render', 'pdf3', 'capitulo-4-resultados.pdf');
const salida = path.join(raiz, '.render', 'paginas');
fs.mkdirSync(salida, { recursive: true });

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({ viewport: { width: 1100, height: 1500 }, deviceScaleFactor: 1.5 });
await pagina.goto('file:///' + pdf.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(3500);

for (const n of paginas) {
  const archivo = path.join(salida, 'pagina-' + String(n).padStart(2, '0') + '.png');
  const p = await navegador.newPage({ viewport: { width: 1000, height: 1320 }, deviceScaleFactor: 2 });
  await p.goto('file:///' + pdf.replace(/\\/g, '/') + '#page=' + n + '&zoom=page-fit', { waitUntil: 'load' });
  await p.waitForTimeout(3000);
  await p.screenshot({ path: archivo });
  await p.close();
  console.log('OK ' + archivo);
}

await navegador.close();
