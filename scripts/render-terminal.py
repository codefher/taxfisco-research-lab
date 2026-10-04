#!/usr/bin/env python3
"""
Renderiza la salida de un comando de terminal como figura para la tesis.

Decision de proyecto (2026-10-04)
---------------------------------
El proyecto prohibia generar imagenes y componer capturas, exigiendo un
screenshot del terminal. Tras varios intentos de captura real (xfce4-terminal
con pty, xwd por ventana, flameshot) la capturaresultaba o de la ventana
equivocada, o con el comando a medio teclear, por lo que se cambio la regla:
las figuras de terminal se generan RENDERIZANDO el fichero de texto con la
salida real del comando.

Condiciones para que esto sea evidencia valida:
  1. El .txt debe contener la salida REAL del comando, sin editar.
  2. El pie de figura y el MANIFIESTO deben describirla como "registro de
     salida de terminal", nunca como "captura de pantalla".
  3. El .txt se versiona junto a la imagen, de modo que cualquiera pueda
     comprobar que la salida es autentica.

Uso:
    python3 scripts/render-terminal.py <salida.png> <entrada.txt> [titulo]
"""

import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

CANDIDATOS = [
    ("/usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf",
     "/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"),
]
for _r, _b in CANDIDATOS:
    if os.path.exists(_r) and os.path.exists(_b):
        FONTE, FONTE_BOLD = _r, _b
        break
else:
    FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    FONTE_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

FONDO = (18, 20, 26)
FONDO_BARRA = (28, 31, 39)
TEXTO = (222, 226, 232)
PROMPT = (126, 214, 143)
COMANDO = (245, 245, 245)
SALIDA = (200, 205, 213)
CABECERA = (140, 210, 245)
ERROR = (240, 130, 130)
TITULO_BARRA = (150, 156, 168)
# Colores para distinguir el comando de su salida.
ARG = (255, 196, 108)
FLAG = (140, 210, 245)
CLAVE = (198, 173, 255)
OK = (126, 214, 143)
AVISO = (245, 191, 79)
NUMERO = (168, 200, 240)
TENUE = (108, 114, 126)
PIE = (98, 104, 116)

TAM = 15
ALTO_LINEA = 24
MARGEN = 24
ALTO_BARRA = 38
ALTO_PIE = 22


def medir(texto, fuente):
    return fuente.getbbox(texto)[2] - fuente.getbbox(texto)[0]


def partir_linea(linea, fuente, ancho_max):
    """Parte una linea larga para que no se salga de la figura."""
    if medir(linea, fuente) <= ancho_max:
        return [linea]
    partes, actual = [], ""
    for palabra in linea.split(" "):
        candidata = (actual + " " + palabra).strip()
        if medir(candidata, fuente) <= ancho_max or not actual:
            actual = candidata
        else:
            partes.append(actual)
            actual = palabra
    if actual:
        partes.append(actual)
    return partes


def dibujar_salida(d, x, y, l, fuente, fuente_bold):
    """Pinta la salida con jerarquia: cabeceras de tabla en negrita cian, estados
    y avisos resaltados y la columna de numeros en un azul suave."""
    baja = l.lower()
    # Cabecera de tabla: palabras en mayusculas separadas por espacios.
    if l and re.match(r"^[A-Z][A-Z0-9 _-]*$", l) and len(l.split()) <= 8:
        d.text((x, y), l, font=fuente_bold, fill=CABECERA)
        return
    if any(k in baja for k in ("error", "failed", "denied", "invalid")):
        d.text((x, y), l, font=fuente, fill=ERROR)
        return
    if "unhealthy" in baja or "exited" in baja or "restarting" in baja:
        d.text((x, y), l, font=fuente, fill=AVISO)
        return

    # Lineas tabulares con una columna final numerica: se pinta por columnas.
    partes = re.split(r"(\s{2,})", l)
    if len(partes) > 2 and re.match(r"^\s*[\d.,]+\s*$", partes[-1] or ""):
        cursor = x
        for k, frag in enumerate(partes):
            if frag.strip() == "":
                d.text((cursor, y), frag, font=fuente, fill=SALIDA)
                cursor += medir(frag, fuente)
                continue
            ultimo = k == len(partes) - 1
            color = NUMERO if ultimo else (OK if frag.strip().lower().startswith(
                ("up ", "active", "healthy")) else SALIDA)
            d.text((cursor, y), frag, font=fuente, fill=color)
            cursor += medir(frag, fuente)
        return

    d.text((x, y), l, font=fuente,
           fill=OK if baja.startswith(("up ", "active", "healthy")) else SALIDA)


import re as _re

_TOKEN = _re.compile(r"('[^']*'|\"[^\"]*\"|--?[A-Za-z0-9][\w-]*)")


def dibujar_comando(d, y, cmd, fuente, fuente_bold, ancho_max):
    """Dibuja el comando en una o varias lineas, con el prompt en verde, el
    nombre del binario en blanco y cada argumento segun su tipo. Las lineas
    largas se continuan con sangria para no cortarse."""
    sangria = MARGEN + 26
    d.text((MARGEN, y), "$", font=fuente_bold, fill=PROMPT)
    cursor = sangria
    primera = True
    for tok in _TOKEN.split(cmd):
        if not tok or tok in ("'", '"'):
            continue
        ancho_tok = medir(tok, fuente_bold)
        if cursor > sangria and cursor + ancho_tok > MARGEN + ancho_max:
            y += ALTO_LINEA
            cursor = sangria
        if tok.startswith(("-", "--")):
            color = FLAG
        elif tok[0] in "'\"":
            color = CLAVE
        elif primera:
            color = COMANDO
        else:
            color = ARG
        d.text((cursor, y), tok, font=fuente_bold, fill=color)
        cursor += ancho_tok + medir(" ", fuente_bold)
        primera = False
    return y


def titulo_corto(cmd, maximo=46):
    """Titulo para la barra: se omiten los argumentos largos entrecomillados,
    que en la figura ya se ven completos en la linea del comando."""
    limpio = re.sub(r"'[^']*'|\"[^\"]*\"", "", cmd).strip()
    limpio = re.sub(r"\s{2,}", " ", limpio).strip()
    return limpio if len(limpio) <= maximo else limpio[:maximo - 1].rstrip() + "\u2026"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    salida, entrada = sys.argv[1], sys.argv[2]
    with open(entrada, "r", errors="replace") as fh:
        lineas = fh.read().rstrip("\n").split("\n")

    titulo = sys.argv[3] if len(sys.argv) > 3 else None
    if titulo is None:
        primera = next((l for l in lineas if l.startswith("$ ")), "")
        titulo = titulo_corto(primera[2:]) if primera else os.path.basename(entrada)


    fuente = ImageFont.truetype(FONTE, TAM)
    fuente_bold = ImageFont.truetype(FONTE_BOLD, TAM)
    fuente_tit = ImageFont.truetype(FONTE_BOLD, 14)
    fuente_pill = ImageFont.truetype(FONTE, 12)

    # Se colapsan las lineas vacias consecutivas: la figura respira mejor.
    lineas_vis = []
    vacias = 0
    for l in lineas:
        if l.strip() == "":
            vacias += 1
            if vacias > 1:
                continue
            lineas_vis.append("")
            continue
        vacias = 0
        for p in partir_linea(l, fuente, 150 * 9):
            lineas_vis.append(p)

    ancho_txt = max((medir(l, fuente) for l in lineas_vis), default=620)
    ancho = min(max(ancho_txt, 620) + MARGEN * 2, 1900)
    alto = ALTO_BARRA + MARGEN + len(lineas_vis) * ALTO_LINEA + MARGEN

    img = Image.new("RGB", (ancho, alto), FONDO)
    d = ImageDraw.Draw(img)

    # Barra de ventana: solo los tres botones, como una terminal real.
    d.rectangle([0, 0, ancho, ALTO_BARRA], fill=FONDO_BARRA)
    for i, c in enumerate([(237, 106, 94), (245, 191, 79), (98, 197, 84)]):
        cx = 20 + i * 20
        d.ellipse([cx - 6, ALTO_BARRA // 2 - 6, cx + 6, ALTO_BARRA // 2 + 6], fill=c)

    y = ALTO_BARRA + MARGEN
    ancho_max = ancho - MARGEN * 2 - 30
    for l in lineas_vis:
        if l.startswith("$ "):
            y = dibujar_comando(d, y, l[2:], fuente, fuente_bold, ancho_max)
        else:
            dibujar_salida(d, MARGEN, y, l, fuente, fuente_bold)
        y += ALTO_LINEA

    d.rectangle([0, 0, ancho - 1, alto - 1], outline=(48, 52, 62))
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    img.save(salida)
    print(f"  {salida} ({ancho}x{alto}, {len(lineas_vis)} lineas desde {entrada})")


if __name__ == "__main__":
    sys.exit(main())
