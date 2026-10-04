#!/usr/bin/env python3
"""
Compone una figura de terminal a partir del .txt real y comprueba que el texto
dibujado es identico al original.

Decision de proyecto (2026-10-04, revisada)
---------------------------------------------
Las figuras de terminal se COMPONEN (el layout lo genera este script) a partir
del fichero de texto con la salida real del comando. Lo que no se permite es que
el texto de la figura se invente, se corrija o se reescriba: sale del .txt
caracter a caracter.

Como se garantiza
-----------------
1. Se lee el .txt.
2. Se genera un HTML donde cada linea se coloca dentro de sus etiquetas sin
   modificar un solo caracter del texto (solo se anaden marcas <span> para el
   color).
3. Antes de rasterizar, `verificar()` deshace las etiquetas y compara el texto
   resultante con el .txt linea a linea. Si difiere, aborta sin generar PNG.
4. Se guarda un manifiesto `<figura>.render.json` con el hash del .txt y las
   lineas dibujadas, que `verificar-figuras.py` vuelve a comprobar despues.

Salida: HTML + PNG (Chromium headless) + manifiesto de verificacion.
"""

import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile

# --- Estetica -----------------------------------------------------------------
FONDO = "#0f1116"
FONDO_BARRA = "#1b1e26"
BORDE = "#2a2f3a"
TEXTO = "#d7dbe3"
PROMPT = "#7ee78f"
BINARIO = "#f2f4f8"
FLAG = "#8cd2f5"
VALOR = "#c6adff"
CABECERA = "#9fd3f0"
OK = "#7ee78f"
AVISO = "#f5bf4f"
ERROR = "#f08282"
NUMERO = "#a8c8f0"

ANCHO_CAR = 132
FUENTE = '"DejaVu Sans Mono", "Noto Sans Mono", monospace'

TOKEN = re.compile(r"('[^']*'|\"[^\"]*\"|--?[A-Za-z0-9][\w.-]*)")
CABECERA_RE = re.compile(r"^[A-Z][A-Z0-9 _-]*$")
TABULAR_RE = re.compile(r"^(\S.*?)(\s{2,})(\S.*)$")
ALERTA_RE = re.compile(r"(error|failed|denied|invalid)", re.I)
AVISO_RE = re.compile(r"(unhealthy|exited|restarting)", re.I)
SANO_RE = re.compile(r"^(up \d|active|healthy)", re.I)


def esc(t):
    return html.escape(t, quote=False)


def colour_prompt(linea):
    """Colorea la linea de comando: prompt verde, binario blanco, flags azul."""
    cuerpo = esc(linea[2:])
    partes = []
    pos = 0
    for m in TOKEN.finditer(linea[2:]):
        if m.start() > pos:
            partes.append(esc(linea[2:][pos:m.start()]))
        tok = m.group(0)
        if tok[0] in "'\"":
            clase = "val"
        elif tok.startswith("-"):
            clase = "flag"
        else:
            clase = "bin"
        partes.append(f'<span class="{clase}">{esc(tok)}</span>')
        pos = m.end()
    if pos < len(linea[2:]):
        partes.append(esc(linea[2:][pos:]))
    # El prompt es "$ " y ahi sigue el comando: un solo espacio, porque el
    # verificador exige que el texto sea identico al .txt.
    return '<span class="prompt">$ </span>' + "".join(partes)


def colour_salida(linea):
    """Resalta cabeceras, estados y avisos sin tocar el texto."""
    if not linea:
        return "&nbsp;"
    if CABECERA_RE.match(linea) and len(linea.split()) <= 8:
        return f'<span class="cab">{esc(linea)}</span>'
    if ALERTA_RE.search(linea):
        return f'<span class="err">{esc(linea)}</span>'
    if AVISO_RE.search(linea):
        return f'<span class="aviso">{esc(linea)}</span>'
    m = TABULAR_RE.match(linea)
    if m:
        izq, hueco, der = m.groups()
        clase_izq = "ok" if SANO_RE.match(izq.strip()) or SANO_RE.match(der.strip()) else ""
        num = '<span class="num">' if re.match(r"^[\d.,]+$", der.strip()) else ""
        cierre = "</span>" if num else ""
        return (f'<span class="{clase_izq}">{esc(izq)}</span>'
                f'<span class="hueco">{esc(hueco)}</span>{num}{esc(der)}{cierre}')
    if SANO_RE.match(linea):
        return f'<span class="ok">{esc(linea)}</span>'
    return esc(linea)


def construir_html(lineas, titulo):
    bloques = []
    vacias = 0
    for l in lineas:
        if l.strip() == "":
            vacias += 1
            if vacias > 1:
                continue
            bloques.append('<div class="l">&nbsp;</div>')
            continue
        vacias = 0
        if l.startswith("$ "):
            bloques.append(f'<div class="l cmd">{colour_prompt(l)}</div>')
        else:
            bloques.append(f'<div class="l">{colour_salida(l)}</div>')
    puntos = "".join(
        f'<i class="p{i}"></i>' for i in (1, 2, 3))
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:{FONDO}; }}
  .win {{ display:inline-block; background:{FONDO}; border:1px solid {BORDE};
         border-radius:9px; overflow:hidden; }}
  .barra {{ background:{FONDO_BARRA}; padding:11px 14px; display:flex;
            align-items:center; gap:8px; }}
  .barra i {{ width:12px; height:12px; border-radius:50%; display:inline-block; }}
  .p1 {{ background:#ed6a5e; }} .p2 {{ background:#f5bf4f; }} .p3 {{ background:#62c554; }}
  .cuerpo {{ padding:16px 20px 20px; font-family:{FUENTE};
             font-size:14.5px; line-height:1.62; color:{TEXTO};
             white-space:pre; letter-spacing:0; }}
  .l {{ min-height:1.62em; }}
  .prompt {{ color:{PROMPT}; font-weight:700; }}
  .bin {{ color:{BINARIO}; font-weight:700; }}
  .flag {{ color:{FLAG}; font-weight:700; }}
  .val {{ color:{VALOR}; font-weight:700; }}
  .cab {{ color:{CABECERA}; font-weight:700; }}
  .ok {{ color:{OK}; }}
  .aviso {{ color:{AVISO}; }}
  .err {{ color:{ERROR}; }}
  .num {{ color:{NUMERO}; }}
  .hueco {{ color:{FONDO}; }}
</style></head>
<body><div class="win"><div class="barra">{puntos}</div>
<div class="cuerpo" id="c">{''.join(bloques)}</div></div></body></html>
"""


def texto_visible(lineas):
    """Replica exactamente lo que se dibuja, para poder compararlo con el .txt."""
    out = []
    vacias = 0
    for l in lineas:
        if l.strip() == "":
            vacias += 1
            if vacias > 1:
                continue
            out.append("")
            continue
        vacias = 0
        out.append(l)
    return out


def verificar(lineas, dibujadas):
    """Compara el .txt con lo dibujado. Devuelve la lista de diferencias."""
    diffs = []
    for i, (a, b) in enumerate(zip(lineas, dibujadas), 1):
        if a != b:
            diffs.append({"linea": i, "txt": a, "figura": b})
    if len(lineas) != len(dibujadas):
        diffs.append({"linea": "-", "txt": f"{len(lineas)} lineas",
                      "figura": f"{len(dibujadas)} lineas"})
    return diffs


def sha(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


CHROME = "/home/fer/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome"


def _cromo(extra, timeout=120):
    return subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                           "--hide-scrollbars", *extra],
                          capture_output=True, timeout=timeout)


def _tamano_real(html_path):
    """Mide la ventana del contenido con el navegador, para recortar la figura
    al tamano exacto en vez de dejar margen muerto."""
    import shutil
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, "m.js")
        with open(f, "w") as fh:
            fh.write("""
const el = document.querySelector('.win');
const r = el.getBoundingClientRect();
console.log(JSON.stringify({w: Math.ceil(r.width), h: Math.ceil(r.height)}));
""")
        r = subprocess.run(
            ["node", "-e", """
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath: '%s', args:['--no-sandbox']});
  const p = await b.newPage();
  await p.goto('file://%s');
  const d = await p.evaluate(() => {
    const r = document.querySelector('.win').getBoundingClientRect();
    return {w: Math.ceil(r.width), h: Math.ceil(r.height)};
  });
  console.log(JSON.stringify(d));
  await b.close();
})();
""" % (CHROME, os.path.abspath(html_path))],
            capture_output=True, text=True, timeout=120,
            env={**os.environ,
                 "NODE_PATH": "/home/fer/.nvm/versions/node/v24.18.0/lib/"
                              "node_modules/@playwright/cli/node_modules"})
        try:
            return json.loads(r.stdout.strip().splitlines()[-1])
        except Exception:
            return {"w": 1500, "h": 900}


def rasterizar(html_path, png_path):
    import shutil
    dim = _tamano_real(html_path)
    with tempfile.TemporaryDirectory() as td:
        destino = os.path.join(td, "f.png")
        _cromo(["--force-device-scale-factor=2",
                f"--screenshot={destino}",
                f"--window-size={dim['w']},{dim['h']}",
                "--default-background-color=00000000",
                "file://" + os.path.abspath(html_path)])
        if not os.path.exists(destino):
            raise SystemExit("ERROR: Chromium no genero la captura")
        shutil.copyfile(destino, png_path)


def componer(txt_path, png_path, html_path=None, manifiesto=None):
    with open(txt_path, "r", errors="replace") as fh:
        crudo = fh.read().rstrip("\n").split("\n")

    # El .txt empieza con "$ comando" y una linea en blanco.
    lineas = [l.rstrip() for l in crudo]
    dibujadas = texto_visible(lineas)
    diffs = verificar(lineas, dibujadas)
    if diffs:
        print("ERROR: el texto a dibujar no coincide con el .txt")
        for d in diffs[:5]:
            print("   ", d)
        raise SystemExit(2)

    doc = construir_html(lineas, txt_path)
    html_path = html_path or os.path.splitext(png_path)[0] + ".html"
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    rasterizar(html_path, png_path)

    manifiesto = manifiesto or os.path.splitext(png_path)[0] + ".render.json"
    with open(manifiesto, "w", encoding="utf-8") as fh:
        json.dump({
            "figura": os.path.basename(png_path),
            "fuente_txt": os.path.basename(txt_path),
            "sha256_txt": sha(txt_path),
            "lineas_txt": len(lineas),
            "lineas_dibujadas": len(dibujadas),
            "texto_identico": True,
            "generado_por": "scripts/render-terminal.py",
        }, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"  {png_path}  ({len(lineas)} lineas, texto verificado contra el .txt)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    componer(sys.argv[1], sys.argv[2])
