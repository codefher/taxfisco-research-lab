#!/usr/bin/env python3
"""Lista los estilos usados en el DOCX y los parrafos de cada estilo no-Normal,
para localizar los titulos reales del cuerpo."""
import sys
import collections
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def main():
    ruta = sys.argv[1]
    solo = sys.argv[2] if len(sys.argv) > 2 else None
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml")
    raiz = ET.fromstring(xml)
    cuerpo = raiz.find(f"{W}body")
    filas = []
    for i, p in enumerate(cuerpo.iter(f"{W}p")):
        ppr = p.find(f"{W}pPr")
        estilo = "(sin estilo)"
        if ppr is not None:
            st = ppr.find(f"{W}pStyle")
            if st is not None:
                estilo = st.get(f"{W}val", "(sin estilo)")
        txt = "".join((t.text or "") for t in p.iter(f"{W}t")).strip()
        filas.append((i, estilo, txt))

    cuenta = collections.Counter(e for _, e, _ in filas)
    print("=== ESTILOS USADOS ===")
    for e, c in cuenta.most_common(30):
        print(f"  {c:5d}  {e}")

    print()
    print("=== PARRAFOS CON ESTILO NO NORMAL ===")
    for i, e, t in filas:
        if e in ("(sin estilo)", "Normal", "Predeterminado"):
            continue
        if not t:
            continue
        if solo and solo not in t:
            continue
        print(f"{i:5d}  {e:<16} {t[:140]}")


if __name__ == "__main__":
    main()
