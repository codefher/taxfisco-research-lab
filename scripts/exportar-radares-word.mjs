// Rasteriza los SVG inline de las figuras 17 y 18 del capitulo 4 a PNG de alta
// resolucion, de modo que la figura en Word sea identica a la del HTML.
// Uso: node scripts/exportar-radares-word.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
import fs from 'fs';

const raiz = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const capitulo = path.join(raiz, 'resultados-prototipos', 'cap4-nuevo.html');
const salida = path.join(raiz, 'resultados-prototipos', 'evidencia-visual', 'radares');
fs.mkdirSync(salida, { recursive: true });

const fuente = fs.readFileSync(capitulo, 'utf8');
const svgs = [...fuente.matchAll(/<svg viewBox="0 0 1240 960"[\s\S]*?<\/svg>/g)].map((m) => m[0]);
if (svgs.length !== 2) {
  console.error('Se esperaban 2 radares en el capitulo y se hallaron ' + svgs.length);
  process.exit(1);
}
const nombres = ['radar-cap4-libelula', 'radar-cap4-sin'];

const envoltorio = svgs
  .map(
    (svg, i) =>
      '<div id="f' + i + '" style="width:1240px;height:960px;background:#FFFFFF;line-height:0">' +
      svg +
      '</div>'
  )
  .join('\n');
const paginaTemporal = path.join(salida, '_radares-word.html');
fs.writeFileSync(
  paginaTemporal,
  '<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#FFFFFF}</style></head><body>' +
    envoltorio +
    '</body></html>',
  'utf8'
);

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage({
  viewport: { width: 1300, height: 1000 },
  deviceScaleFactor: 2,
});
await pagina.goto('file:///' + paginaTemporal.replace(/\\/g, '/'), { waitUntil: 'load' });
await pagina.waitForTimeout(500);

for (let i = 0; i < svgs.length; i++) {
  const archivo = path.join(salida, nombres[i] + '.png');
  const caja = await pagina.$('#f' + i);
  await caja.screenshot({ path: archivo });
  console.log('OK  ' + path.basename(archivo));
}

await navegador.close();
fs.unlinkSync(paginaTemporal);
console.log('Exportacion terminada en ' + salida);
