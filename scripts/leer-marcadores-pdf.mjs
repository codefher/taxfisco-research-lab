// Lee el indice de marcadores del PDF de LibreOffice y devuelve la pagina de
// cada titulo, para comprobar la tabla de contenido del documento Word.
// Uso: node scripts/leer-marcadores-pdf.mjs <pdf>
import { execFileSync } from 'child_process';
import fs from 'fs';

const pdf = process.argv[2];
const buf = fs.readFileSync(pdf);
const s = buf.toString('latin1');

// Objetos del PDF: "N 0 obj ... endobj"
const objetos = new Map();
const reObj = /(\d+) 0 obj([\s\S]*?)endobj/g;
let m;
while ((m = reObj.exec(s)) !== null) objetos.set(Number(m[1]), m[2]);

// Arbol de paginas
let orden = [];
for (const [num, cuerpo] of objetos) {
  if (/\/Type\s*\/Pages/.test(cuerpo)) {
    const kids = cuerpo.match(/\/Kids\s*\[([\s\S]*?)\]/);
    if (kids) {
      orden = [...kids[1].matchAll(/(\d+) 0 R/g)].map((x) => Number(x[1]));
    }
  }
}
const paginaDe = new Map();
orden.forEach((obj, i) => paginaDe.set(obj, i + 1));

// Titulos del indice
function texto(hex) {
  if (hex.startsWith('<')) {
    const hexPart = hex.slice(1, -1).replace(/\s/g, '');
    let out = '';
    for (let i = 0; i + 3 < hexPart.length; i += 4) {
      out += String.fromCharCode(parseInt(hexPart.substr(i, 4), 16));
    }
    return out;
  }
  return hex.replace(/^\\(|\\)$/g, '').replace(/\\([()\\])/g, '$1');
}

const titulos = [];
for (const [num, cuerpo] of objetos) {
  if (!/\/Title/.test(cuerpo)) continue;
  const t = cuerpo.match(/\/Title\s*(\((?:[^()\\]|\\.)*\)|<[0-9A-Fa-f\s]*>)/);
  const d = cuerpo.match(/\/Dest\s*\[\s*(\d+) 0 R/);
  if (!t || !d) continue;
  titulos.push({ titulo: texto(t[1]), pagina: paginaDe.get(Number(d[1])) ?? null });
}

titulos.sort((a, b) => (a.pagina ?? 0) - (b.pagina ?? 0));
for (const t of titulos) console.log(String(t.pagina).padStart(3) + '  ' + t.titulo);
console.log('Total de marcadores: ' + titulos.length);
