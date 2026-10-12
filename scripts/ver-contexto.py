#!/usr/bin/env python3
"""Muestra cada coincidencia sospechosa con un fragmento de contexto, para
corregir con el texto a la vista en vez de a ciegas."""
import re
import sys

INI = "### 4.3.6 "
FIN = "## 4.4 "

ruta = sys.argv[1]
ini = sys.argv[2] if len(sys.argv) > 2 else INI
fin = sys.argv[3] if len(sys.argv) > 3 else FIN

lineas = open(ruta, encoding="utf-8").read().split("\n")
a = next((i for i, l in enumerate(lineas) if l.startswith(ini)), 0)
b = next((i for i, l in enumerate(lineas) if l.startswith(fin)), len(lineas))

patrones = [
    ("coma antes de coordinante", re.compile(r",\s+(y|ni|o|pero|sino)\s")),
    ("backtick", re.compile(r"`")),
    ("donde", re.compile(r"\bdonde\b")),
]

for nombre, rx in patrones:
    print(f"===== {nombre} =====")
    for i in range(a, b):
        l = lineas[i]
        for m in rx.finditer(l):
            ini_ = max(0, m.start() - 70)
            fin_ = min(len(l), m.end() + 70)
            frag = l[ini_:fin_].replace("\n", " ")
            print(f"  L{i+1}: ...{frag}...")
            print()