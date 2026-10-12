#!/usr/bin/env python3
"""Control de cumplimiento del skill humanizar-redaccion-v7 sobre un tramo
del documento maestro. Informativo: no modifica nada."""
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
sec = "\n".join(lineas[a:b])

PRETERITO = re.compile(
    r"\b(pud[oi]|lograba|quedaron|hubiera|produjeron|recibió|documentaron|"
    r"operó|registró|indicó|generaba|alcanzaban|seguía|devolvían|entraba|"
    r"interpretaba|ignoraban|tumbaba|mostraban|aceptaba)\b")
COMA_Y = re.compile(r",\s+(y|ni|o|pero|sino)\s")
INGLES = re.compile(r"\b(despite|zero|events|test|check|with)\b")
CJK = re.compile(r"[\u4e00-\u9fff]")


def linea(m):
    for i, l in enumerate(lineas, 1):
        if m.search(l):
            return i
    return None


controles = [
    ("Regla 7  preterito", PRETERITO),
    ("Regla 9  raya larga", re.compile(r"\u2014")),
    ("Regla 32 coma antes de y", COMA_Y),
    ("Markdown negrita **", re.compile(r"\*\*")),
    ("Backticks", re.compile(r"`")),
    ("Regla 13 donde", re.compile(r"\bdonde\b")),
    ("Palabras inglesas", INGLES),
    ("Caracteres CJK", CJK),
]

print(f"Tramo: {ini.strip()} -> {fin.strip()}   ({b - a} lineas)\n")
todo_limpio = True
for nombre, rx in controles:
    n = len(rx.findall(sec))
    if n == 0:
        print(f"  LIMPIO     {nombre}")
    else:
        todo_limpio = False
        L = linea(rx)
        extra = f"   primera en linea {L}" if L else ""
        print(f"  INFRACCION {nombre}: {n} -> {rx.findall(sec)[:6]}{extra}")

print()
if todo_limpio:
    print("RESULTADO: el tramo cumple todos los controles.")
else:
    print("RESULTADO: quedan infracciones por corregir.")