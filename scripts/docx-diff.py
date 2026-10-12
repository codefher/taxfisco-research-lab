#!/usr/bin/env python3
"""Compara el texto de dos DOCX y muestra solo las diferencias reales.

Se usa para ver que cambio entre dos versiones del documento sin abrirlas.
"""
import difflib
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def parrafos(ruta):
    with zipfile.ZipFile(ruta) as z:
        raiz = ET.fromstring(z.read("word/document.xml"))
    cuerpo = raiz.find(f"{W}body")
    out = []
    for p in cuerpo.iter(f"{W}p"):
        ppr = p.find(f"{W}pPr")
        estilo = ""
        if ppr is not None:
            st = ppr.find(f"{W}pStyle")
            if st is not None:
                estilo = st.get(f"{W}val", "")
        txt = "".join((t.text or "") for t in p.iter(f"{W}t")).strip()
        if txt:
            out.append(f"<{estilo}> {txt}")
    return out


def main():
    a, b = sys.argv[1], sys.argv[2]
    solo = sys.argv[3] if len(sys.argv) > 3 else ""
    pa, pb = parrafos(a), parrafos(b)
    print(f"A: {a}")
    print(f"   parrafos con texto: {len(pa)}")
    print(f"B: {b}")
    print(f"   parrafos con texto: {len(pb)}")
    print()
    sm = difflib.SequenceMatcher(None, pa, pb, autojunk=False)
    cambios = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        cambios += 1
        if solo and solo not in "".join(pa[i1:i2] + pb[j1:j2]):
            continue
        print(f"--- {tag.upper()}  A[{i1}:{i2}]  B[{j1}:{j2}]")
        for x in pa[i1:i2][:6]:
            print(f"   - {x[:200]}")
        for y in pb[j1:j2][:6]:
            print(f"   + {y[:200]}")
    print()
    print(f"bloques de cambio: {cambios}")


if __name__ == "__main__":
    main()
