// Exporta las figuras de radar del HTML comparativo a PNG de alta resolucion.
// Uso: node scripts/exportar-radares.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const html = path.join(raiz, 'resultados-prototipos', 'radares-comparativos.html');
const salida = path.join(raiz, 'resultados-prototipos', 'evidencia-visual', 'radares');
fs.mkdirSync(salida, { recursive: true });

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({
  viewport: { width: 1500, height: 1200 },
  deviceScaleFactor: 2,
});
await pagina.goto('file:///' + html.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(700);

for (const id of ['figura-sin', 'figura-libelula']) {
  const tarjeta = await pagina.$('#' + id);
  const archivo = path.join(salida, id.replace('figura-', 'radar-') + '.png');
  await tarjeta.screenshot({ path: archivo });
  console.log('OK  ' + path.basename(archivo));
}

await navegador.close();
console.log('Exportacion terminada en ' + salida);
