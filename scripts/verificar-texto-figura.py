#!/usr/bin/env python3
"""Comprobacion directa de que el texto de la figura es identico al .txt,
sin depender del hash (que en Windows cambia por los saltos CRLF de Git)."""
import html
import re
import sys

ETIQUETA = re.compile(r"<[^>]+>")
NODOS = re.compile(r'<div class="l[^"]*">(.*?)</div>', re.S)

base = sys.argv[1]

doc = open(base + ".html", encoding="utf-8").read()
cuerpo = doc.split('<div class="cuerpo" id="c">', 1)[-1]

salida = []
for frag in NODOS.findall(cuerpo):
    c = ETIQUETA.sub("", frag)
    c = html.unescape(c)
    if c == "\xa0":
        c = ""
    salida.append(c.rstrip())

txt = [l.rstrip() for l in
       open(base + ".txt", encoding="utf-8", errors="replace")
       .read().rstrip("\n").split("\n")]

esperado, vacias = [], 0
for l in txt:
    if l.strip() == "":
        vacias += 1
        if vacias > 1:
            continue
        esperado.append("")
        continue
    vacias = 0
    esperado.append(l)

print("lineas .txt      :", len(esperado))
print("lineas en figura :", len(salida))
ok = esperado == salida
print("TEXTO IDENTICO   :", "SI" if ok else "NO")

for i, (a, b) in enumerate(zip(esperado, salida), 1):
    if a != b:
        print("  DIFERENCIA linea", i)
        print("    txt    =", repr(a))
        print("    figura =", repr(b))

if ok:
    for i, l in enumerate(esperado, 1):
        print("  linea %d: %r" % (i, l))
    # El .txt con CRLF y con LF deben dar el mismo texto util.
    crudo = open(base + ".txt", "rb").read()
    print("saltos CRLF en el .txt:", crudo.count(b"\r\n"),
          "(Git los introduce al importar en Windows; no altera el texto)")

sys.exit(0 if ok else 1)
