// Extrae la prosa del documento Word (parrafos de cuerpo y notas de tabla) para
// su revision editorial. Uso: node scripts/extraer-prosa.mjs <docx>
import { execFileSync } from 'child_process';

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
  const estilo = p.match(/<w:pStyle w:val="([^"]+)"/)?.[1] ?? '';
  const tieneSangria = /w:firstLine="720"/.test(p);
  const enTabla = /<w:tbl>/.test(p);
  return { txt, estilo, tieneSangria, enTabla };
});

// Solo la prosa argumentativa: parrafos con sangria de primera linea.
const prosa = parrafos.filter((p) => p.tieneSangria && p.txt.trim().length > 0);
console.log('Parrafos de prosa: ' + prosa.length);
console.log('');
for (const p of prosa) {
  const n = p.txt.trim().split(/\s+/).length;
  console.log('[' + n + '] ' + p.txt.trim());
  console.log('');
}
