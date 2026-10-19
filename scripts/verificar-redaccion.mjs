// Verifica las reglas de redaccion v7 sobre el texto del documento Word.
// Uso: node scripts/verificar-redaccion.mjs <docx>
import { execFileSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const docx = process.argv[2];
const xml = execFileSync('powershell', [
  '-NoProfile', '-Command',
  `Add-Type -AssemblyName System.IO.Compression.FileSystem;` +
  `$z=[System.IO.Compression.ZipFile]::OpenRead('${docx.replace(/'/g, "''")}');` +
  `$e=$z.GetEntry('word/document.xml');$sr=New-Object System.IO.StreamReader($e.Open());` +
  `$t=$sr.ReadToEnd();$sr.Close();$z.Dispose();$t`,
], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });

const parrafos = [...xml.matchAll(/<w:p[ >][\s\S]*?<\/w:p>/g)].map((m) => {
  const p = m[0];
  const txt = [...p.matchAll(/<w:t(?:\s[^>]*)?>([\s\S]*?)<\/w:t>/g)]
    .map((x) => x[1]).join('')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
  return { txt, cuerpo: /w:firstLine="720"/.test(p) };
});

const cuerpo = parrafos.filter((p) => p.cuerpo && p.txt.trim().length > 0);
const todo = parrafos.map((p) => p.txt).join('\n');

let fallos = 0;
const avisar = (regla, msg) => { fallos++; console.log('  FALLA [' + regla + '] ' + msg); };

// Regla 32: coma antes de conjuncion coordinante
console.log('\n== Regla 32: coma antes de conjuncion coordinante ==');
const comaY = [...todo.matchAll(/[a-záéíóúñ0-9%]\s*,\s+(y|ni|o|pero|sino)\s/gi)];
if (comaY.length === 0) console.log('  Sin infracciones.');
else comaY.forEach((m) => avisar('32', m[0].replace(/\s+/g, ' ')));

// Regla 8 y 9: dos puntos explicativos y raya larga como inciso
console.log('\n== Regla 8: dos puntos ==');
const colones = [...todo.matchAll(/[^\s:][^:\n]{0,50}:/g)]
  .map((m) => m[0].trim())
  .filter((s) => !/^</.test(s))
  .filter((s) => !/(Rev\. 3|ISO\/IEC 27001|ISO\/IEC 27035-1|Part 1|https|technology:|documented:|16:|18:|20:)/.test(s));
if (colones.length === 0) console.log('  Solo dos puntos de nombres oficiales de normas, horas y citas.');
else colones.forEach((s) => avisar('8', s));

console.log('\n== Regla 9: raya larga como inciso en la prosa ==');
const rayas = cuerpo.filter((p) => p.txt.includes('—'));
if (rayas.length === 0) console.log('  Sin rayas largas en la prosa.');
else rayas.forEach((p) => avisar('9', p.txt.slice(0, 90)));

// Regla 2: longitud de las oraciones de la prosa
console.log('\n== Regla 2: longitud de oraciones (30-60 palabras) ==');
const oraciones = [];
for (const p of cuerpo) {
  for (const s of p.txt.split(/(?<=[.;:])\s+(?=[A-ZÁÉÍÓÚÑ¿¡])/)) {
    const n = s.trim().split(/\s+/).filter(Boolean).length;
    if (n > 0) oraciones.push({ s: s.trim(), n });
  }
}
const cortas = oraciones.filter((o) => o.n < 18);
const medias = oraciones.filter((o) => o.n >= 18 && o.n < 30);
const largas = oraciones.filter((o) => o.n > 60);
console.log('  Oraciones: ' + oraciones.length);
console.log('  Menores de 18: ' + cortas.length + (cortas.length ? '' : ' (ninguna)'));
cortas.forEach((o) => avisar('2', o.n + ' palabras: ' + o.s.slice(0, 80)));
console.log('  De 18 a 29: ' + medias.length);
console.log('  Mayores de 60: ' + largas.length);
largas.forEach((o) => avisar('2', o.n + ' palabras: ' + o.s.slice(0, 80)));

// Regla 31: maximo dos "y" por oracion
console.log('\n== Regla 31: maximo dos "y" por oracion ==');
const conTres = oraciones.filter((o) => (o.s.match(/\by\b/gi) || []).length > 2);
if (conTres.length === 0) console.log('  Sin oraciones con tres o mas "y".');
else conTres.forEach((o) => avisar('31', (o.s.match(/\by\b/gi) || []).length + ' "y": ' + o.s.slice(0, 80)));

// Regla 7: tiempo verbal en presente
console.log('\n== Regla 7: pretérito o futuro en la prosa ==');
const pasado = /\b(se |el |la |los |las )?[a-záéíóúñ]{3,}(ó|aron|ieron|aba|aban|ía|ían|ará|arán|erá|erán|irá|irán)\b/i;
const futuro = /\b(va a|van a|habrá|habrán|se va a|se van a)\b/i;
const Perfecto = /\bha (sido |habido )?[a-záéíóúñ]+\b|\bhan (sido |habido )?[a-záéíóúñ]+\b/i;
let pret = 0;
for (const p of cuerpo) {
  for (const s of p.txt.split(/(?<=[.])\s+/)) {
    if (pasado.test(s) || futuro.test(s) || Perfecto.test(s)) { pret++; avisar('7', s.slice(0, 100)); }
  }
}
if (pret === 0) console.log('  Sin formas de pretérito, futuro o antepresente.');

// Regla 29: numeros del 1 al 9 en palabras
console.log('\n== Regla 29: numeros del 1 al 9 en palabras en la prosa ==');
const digitos = [];
for (const p of cuerpo) {
  // Se retiran las etiquetas (Tabla N, Figura N, L1, S10, T1595), las horas,
  // los porcentajes, los decimales y las cifras de dos o mas digitos.
  const limpio = p.txt
    .replace(/\b(Tabla|Figura|Apartado|apartado|L|S|T|F|N)\s*\d+(\.\d+)?/g, '')
    .replace(/\d{1,2}:\d{2}/g, '')
    .replace(/\d+([.,]\d+)?\s*%/g, '')
    .replace(/\d+([.,]\d+)+/g, '')
    .replace(/\b\d{2,}\b/g, '')
    .replace(/\b[1-9]\b/g, 'X');
  const hit = limpio.match(/(?<![\w.,])[1-9](?![\w.,])/g);
  if (hit) digitos.push(hit.length + ' digito(s): ' + p.txt.slice(0, 100));
}
if (digitos.length === 0) console.log('  Sin cifras de una sola cifra en la prosa.');
else digitos.forEach((d) => avisar('29', d));

console.log('\n== Resultado ==');
console.log(fallos === 0 ? '  Sin infracciones en las reglas automaticas.' : '  Infracciones: ' + fallos);
