// Recupera los valores de cada serie de un radar dibujado en PNG/JPEG.
// Uso: node scripts/extraer-valores-radar.mjs <ruta-imagen> [<ruta-imagen> ...]
//
// Metodo:
//  1. El anillo exterior de la retícula, que es el 100 %, se ajusta con un
//     circulo algebraico (Kasa) rejecting outliers, lo que fija el centro y el
//     radio de la escala.
//  2. Los ejes se toman cada 360/14 grados desde el eje superior, en sentido
//     horario, que es la disposicion del grafico.
//  3. En cada eje se lee el primer tramo del color de la serie: es la salida
//     del poligono desde el centro y coincide con el vertice, incluso cuando el
//     eje cae en un valle.
import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';

const rutas = process.argv.slice(2);
const forzado = process.argv.slice(2).filter((a) => a.includes('@'));
if (rutas.length === 0) {
  console.error('Uso: node scripts/extraer-valores-radar.mjs <imagen> [cx@cy@R] [...]');
  process.exit(1);
}

const navegador = await chromium.launch({ channel: 'chrome' });
const pagina = await navegador.newPage();
await pagina.goto('about:blank');

for (const item of rutas) {
  const [ruta, ajustes] = item.split('@');
  const buffer = fs.readFileSync(ruta);
  const dataUrl = 'data:image/png;base64,' + buffer.toString('base64');
  const forzado = ajustes ? ajustes.split(',').map(Number) : null;
  const r = await pagina.evaluate(async ({ url, forzado }) => {
    const img = new Image();
    img.src = url;
    await img.decode();
    const w = img.naturalWidth;
    const h = img.naturalHeight;
    const lienzo = document.createElement('canvas');
    lienzo.width = w; lienzo.height = h;
    const ctx = lienzo.getContext('2d', { willReadFrequently: true });
    ctx.drawImage(img, 0, 0);
    const d = ctx.getImageData(0, 0, w, h).data;
    const px = (x, y) => {
      const i = ((y | 0) * w + (x | 0)) * 4;
      return [d[i], d[i + 1], d[i + 2]];
    };

    const w2 = w * h;
    const tono = new Uint8Array(w2);   // 1 rojo, 2 azul, 3 verde, 4 naranja
    const gris = new Uint8Array(w2);   // trazo de retícula
    for (let i = 0; i < w2; i++) {
      const y = (i / w) | 0, x = i - y * w;
      const [rr, gg, bb] = px(x, y);
      const mx = Math.max(rr, gg, bb), mn = Math.min(rr, gg, bb);
      if (mx - mn < 25) {
        if (mx >= 140 && mx <= 246) gris[i] = 1;
        continue;
      }
      // Solo el trazo saturado cuenta: el relleno y su borde antialiaseado
      // quedan fuera y no contaminan la lectura del vertice.
      if (rr - gg > 60 && rr - bb > 90) tono[i] = 1;
      else if (bb - rr > 100 && bb - gg > 40) tono[i] = 2;
      else if (gg - rr > 60 && gg - bb > 60) tono[i] = 3;
      else if (rr - gg > 30 && gg - bb > 30) tono[i] = 4;
    }

    // ---------- componente conexo mayor por tono (descarta la leyenda) ----------
    const mayorComponente = (t) => {
      const et = new Int32Array(w2).fill(-1);
      const pila = new Int32Array(w2);
      let mejor = { tam: 0, x0: 0, y0: 0, x1: 0, y1: 0 };
      for (let i = 0; i < w2; i++) {
        if (tono[i] !== t || et[i] !== -1) continue;
        let sp = 0; pila[sp++] = i; et[i] = 0;
        let tam = 0, x0 = 1e9, y0 = 1e9, x1 = -1, y1 = -1;
        while (sp > 0) {
          const j = pila[--sp];
          const jy = (j / w) | 0, jx = j - jy * w;
          tam++;
          if (jx < x0) x0 = jx; if (jx > x1) x1 = jx;
          if (jy < y0) y0 = jy; if (jy > y1) y1 = jy;
          const vec = [j - 1, j + 1, j - w, j + w];
          for (const v of vec) {
            if (v < 0 || v >= w2) continue;
            const vy = (v / w) | 0;
            if (Math.abs(vy - jy) > 1) continue;
            if (tono[v] !== t || et[v] !== -1) continue;
            et[v] = 0; pila[sp++] = v;
          }
        }
        if (tam > mejor.tam) mejor = { tam, x0, y0, x1, y1 };
      }
      return mejor;
    };

    const comps = [1, 2, 3, 4]
      .map((t) => ({ t, ...mayorComponente(t) }))
      .filter((c) => c.tam > 3000);
    const mayor = comps.reduce((a, b) => (b.tam > a.tam ? b : a));

    // ---------- ajuste robusto del anillo exterior ----------
    let cx = (mayor.x0 + mayor.x1) / 2;
    let cy = (mayor.y0 + mayor.y1) / 2;
    let R = Math.max(mayor.x1 - mayor.x0, mayor.y1 - mayor.y0) / 2;

    function resolver3(A, B) {
      const M = A.map((f, i) => [...f, B[i]]);
      for (let col = 0; col < 3; col++) {
        let piv = col;
        for (let f = col + 1; f < 3; f++) if (Math.abs(M[f][col]) > Math.abs(M[piv][col])) piv = f;
        if (Math.abs(M[piv][col]) < 1e-9) return null;
        [M[col], M[piv]] = [M[piv], M[col]];
        for (let f = 0; f < 3; f++) {
          if (f === col) continue;
          const factor = M[f][col] / M[col][col];
          for (let c = col; c < 4; c++) M[f][c] -= factor * M[col][c];
        }
      }
      return [M[0][3] / M[0][0], M[1][3] / M[1][1], M[2][3] / M[2][2]];
    }

    const ajustar = (pts) => {
      let Sxx = 0, Syy = 0, Sxy = 0, Sx = 0, Sy = 0, Sxz = 0, Syz = 0, S = 0;
      const n = pts.length;
      for (const [x, y] of pts) {
        const z = x * x + y * y;
        Sxx += x * x; Syy += y * y; Sxy += x * y;
        Sx += x; Sy += y; Sxz += x * z; Syz += y * z; S += z;
      }
      const res = resolver3([[Sxx, Sxy, Sx], [Sxy, Syy, Sy], [Sx, Sy, n]], [-Sxz, -Syz, -S]);
      if (!res) return null;
      const [D, E, F] = res;
      const x0 = -D / 2, y0 = -E / 2;
      const rr = Math.sqrt(x0 * x0 + y0 * y0 - F);
      if (!isFinite(rr) || rr <= 10) return null;
      return { cx: x0, cy: y0, R: rr };
    };

    for (let vuelta = 0; vuelta < 6; vuelta++) {
      const pts = [];
      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          const i = y * w + x;
          if (!gris[i]) continue;
          const dd = Math.hypot(x - cx, y - cy);
          if (dd > R * 0.965 && dd < R * 1.035) pts.push([x, y]);
        }
      }
      if (pts.length < 300) break;
      const a = ajustar(pts);
      if (!a) break;
      // Rechazo de valores atipicos y nuevo ajuste
      const dep = pts.filter(([x, y]) => Math.abs(Math.hypot(x - a.cx, y - a.cy) - a.R) < 4);
      const b = dep.length > 300 ? ajustar(dep) : a;
      const elegido = b || a;
      const cambio = Math.hypot(elegido.cx - cx, elegido.cy - cy) + Math.abs(elegido.R - R);
      cx = elegido.cx; cy = elegido.cy; R = elegido.R;
      if (cambio < 0.6) break;
    }

    // Centro y radio forzados, para contrastar con un grafico de calibracion.
    if (forzado && forzado.length === 3) { cx = forzado[0]; cy = forzado[1]; R = forzado[2]; }

    // ---------- lectura de los vertices ----------
    const n = 14;
    const paso = 360 / n;

    const casiBlanco = (x, y) => {
      if (x < 0 || y < 0 || x >= w || y >= h) return false;
      const [rr, gg, bb] = px(x, y);
      return Math.hypot(255 - rr, 255 - gg, 255 - bb) < 22;
    };

    const radioVertice = (t, grados) => {
      const rad = ((grados - 90) * Math.PI) / 180;
      const dx = Math.cos(rad), dy = Math.sin(rad);
      const tramos = [];
      let ini = -1;
      for (let rr = 4; rr <= R * 1.07; rr += 0.25) {
        const x = Math.round(cx + dx * rr), y = Math.round(cy + dy * rr);
        const hit = x >= 0 && y >= 0 && x < w && y < h && tono[y * w + x] === t;
        if (hit && ini < 0) ini = rr;
        if (!hit && ini >= 0) { tramos.push([ini, rr - 0.25]); ini = -1; }
      }
      if (ini >= 0) tramos.push([ini, R * 1.07]);
      // El vertice lleva un marcador con anillo blanco: el tramo del color
      // acotado por blanco a ambos lados es el marcador y su centro es el
      // vertice. Los tramos que cruzan el relleno no lo estan.
      const candidatos = tramos.filter((s) => s[1] - s[0] >= 2 && s[0] > R * 0.02);
      for (const [a, b] of candidatos) {
        const antes = [Math.round(cx + dx * (a - 2)), Math.round(cy + dy * (a - 2))];
        const despues = [Math.round(cx + dx * (b + 2)), Math.round(cy + dy * (b + 2))];
        if (casiBlanco(antes[0], antes[1]) && casiBlanco(despues[0], despues[1])) {
          return (a + b) / 2;
        }
      }
      if (!candidatos.length) return null;
      const [a, b] = candidatos[0];
      return (a + b) / 2;
    };

    const series = comps.map((comp) => {
      const valores = [];
      for (let k = 0; k < n; k++) {
        const g = k * paso;
        const rv = radioVertice(comp.t, g);
        valores.push(rv === null ? null : Number((rv / R * 100).toFixed(1)));
      }
      return { tono: comp.t, pixeles: comp.tam, valores };
    });

    return {
      imagen: { w, h },
      centro: { x: Number(cx.toFixed(1)), y: Number(cy.toFixed(1)) },
      radio100: Number(R.toFixed(1)),
      series,
    };
  }, { url: dataUrl, forzado });

  console.log('\n=== ' + path.basename(ruta) + ' ===');
  console.log('tamaño', r.imagen.w + 'x' + r.imagen.h);
  console.log('centro', r.centro, '| radio 100 % =', r.radio100);
  const nombres = { 1: 'rojo', 2: 'azul', 3: 'verde', 4: 'naranja' };
  for (const s of r.series) {
    console.log(
      '  ' + (nombres[s.tono] || s.tono).padEnd(8) +
        s.valores.map((v) => (v === null ? '   --' : String(v).padStart(6))).join(' ')
    );
  }
}

await navegador.close();
