#!/usr/bin/env python3
"""
Verifica que cada figura de terminal reproduce fielmente su .txt.

Por que existe
--------------
Las figuras de terminal de la evidencia se componen a partir del fichero de
texto con la salida real del comando. La composicion (el diseno) la produce esta
herramienta, pero el TEXTO debe salir del .txt sin una sola modificacion: si una
cifra cambiase, la figura passaria a ser una fabricacion, que es exactamente lo
que motivo la auditoria que rechazo la evidencia anterior.

Este script recorre las figuras, deshace las etiquetas del HTML que se genero
para cada una y lo compara con su .txt linea a linea. Ademas comprueba que el
hash SHA-256 del .txt registrado en el manifiesto sigue coincidiendo, de modo
que el .txt no haya cambiado despues de componer la figura.

Uso:
    python3 scripts/verificar-figuras.py [directorio_evidencia]
"""

import hashlib
import glob
import html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ETIQUETA = re.compile(r"<[^>]+>")
NODOS = re.compile(r'<div class="l[^"]*">(.*?)</div>', re.S)


def sha(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def lineas_del_html(ruta_html):
    """Reconstruye el texto visible del HTML quitando las etiquetas de color."""
    with open(ruta_html, encoding="utf-8") as fh:
        doc = fh.read()
    cuerpo = doc.split('<div class="cuerpo" id="c">', 1)[-1]
    salida = []
    for frag in NODOS.findall(cuerpo):
        limpio = ETIQUETA.sub("", frag)
        limpio = html.unescape(limpio)
        if limpio == "\xa0":
            limpio = ""
        salida.append(limpio.rstrip())
    return salida


def lineas_del_txt(ruta_txt):
    with open(ruta_txt, encoding="utf-8", errors="replace") as fh:
        return [l.rstrip() for l in fh.read().rstrip("\n").split("\n")]


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "evidencias", "v2.0-it1")
    htmls = sorted(glob.glob(os.path.join(base, "**", "*.html"), recursive=True))
    if not htmls:
        print("No hay figuras compuestas que verificar en", base)
        return 0

    ok = fallos = 0
    for ruta_html in htmls:
        nombre = os.path.splitext(os.path.basename(ruta_html))[0]
        dirn = os.path.dirname(ruta_html)
        txt = os.path.join(dirn, nombre + ".txt")
        png = os.path.join(dirn, nombre + ".png")
        man = os.path.join(dirn, nombre + ".render.json")

        if not os.path.exists(txt):
            print(f"  [FALTA .txt] {nombre}")
            fallos += 1
            continue

        a = lineas_del_txt(txt)
        b = lineas_del_html(ruta_html)
        # El compositor colapsa lineas vacias consecutivas: se replica aqui.
        esperado, vacias = [], 0
        for l in a:
            if l.strip() == "":
                vacias += 1
                if vacias > 1:
                    continue
                esperado.append("")
                continue
            vacias = 0
            esperado.append(l)

        if esperado == b and os.path.exists(png):
            detalle = f"{len(b)} lineas"
            if os.path.exists(man):
                with open(man, encoding="utf-8") as fh:
                    m = json.load(fh)
                if m.get("sha256_txt") == sha(txt):
                    detalle += ", sha256 del .txt coincide"
                else:
                    print(f"  [HASH]  {nombre}: el .txt cambio tras componer la figura")
                    fallos += 1
                    continue
            else:
                print(f"  [SIN MANIFIESTO] {nombre}")
                fallos += 1
                continue
            print(f"  [OK]    {nombre} ({detalle})")
            ok += 1
        else:
            print(f"  [DIFIERE] {nombre}")
            for i, (x, y) in enumerate(zip(esperado, b), 1):
                if x != y:
                    print(f"      linea {i}: txt={x!r} figura={y!r}")
                    break
            if len(esperado) != len(b):
                print(f"      numero de lineas: txt={len(esperado)} figura={len(b)}")
            fallos += 1

    print(f"\n  {ok} figura(s) verificadas, {fallos} con problemas")
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
