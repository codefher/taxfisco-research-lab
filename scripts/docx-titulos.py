#!/usr/bin/env python3
"""Lista los titulos reales del cuerpo del DOCX (no el indice de contenido),
para saber que apartados existen de verdad en el documento."""
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def main():
    ruta = sys.argv[1]
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml")
    raiz = ET.fromstring(xml)
    cuerpo = raiz.find(f"{W}body")
    for i, p in enumerate(cuerpo.iter(f"{W}p")):
        ppr = p.find(f"{W}pPr")
        estilo = ""
        if ppr is not None:
            st = ppr.find(f"{W}pStyle")
            if st is not None:
                estilo = st.get(f"{W}val", "")
        if not estilo:
            continue
        # Los estilos de titulo reales llevan outlineLvl o son de nivel 1-4
        lvl = ""
        if ppr is not None:
            ol = ppr.find(f"{W}outlineLvl")
            if ol is not None:
                lvl = ol.get(f"{W}val", "")
        txt = "".join((t.text or "") for t in p.iter(f"{W}t")).strip()
        if not txt:
            continue
        # solo interested in headings: style contains HD or outline level set
        if "TDC" in estilo and not lvl:
            continue  # entrada de indice de contenido
        if "Heading" in estilo or "Titulo" in estilo or "TDC" in estilo or lvl:
            print(f"{i:5d}  {estilo:<12} lvl={lvl:<3} {txt[:150]}")


if __name__ == "__main__":
    main()
