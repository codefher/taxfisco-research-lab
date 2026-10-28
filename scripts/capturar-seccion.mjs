// Captura una seccion de un HTML como PNG, para revisar la maqueta.
// Uso: node scripts/capturar-seccion.mjs <html> <selector> <salida> [ancho]
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const [htmlRel, selector, salida, ancho] = process.argv.slice(2);
if (!htmlRel || !selector || !salida) {
  console.error('Uso: node scripts/capturar-seccion.mjs <html> <selector> <salida.png> [ancho]');
  process.exit(1);
}
const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = path.resolve(raiz, htmlRel);
fs.mkdirSync(path.dirname(path.resolve(raiz, salida)), { recursive: true });

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({
  viewport: { width: Number(ancho) || 1280, height: 1000 },
  deviceScaleFactor: 2,
});
await pagina.goto('file:///' + html.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(700);

const elemento = await pagina.$(selector);
if (!elemento) {
  console.error('NO SE ENCUENTRA ' + selector);
} else {
  await elemento.screenshot({ path: path.resolve(raiz, salida) });
  console.log('OK  ' + salida);
}
await navegador.close();
