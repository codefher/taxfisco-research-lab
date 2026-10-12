#!/usr/bin/env python3
"""Extrae el texto de un DOCX y muestra una seccion concreta.

Se usa para revisar el contenido del documento Word sin abrirlo, listando
los parrafos con su estilo y su indice, de modo que se puedan localizar
los marcadores pendientes y las referencias cruzadas.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def parrafos(ruta):
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml")
    raiz = ET.fromstring(xml)
    cuerpo = raiz.find(f"{W}body")
    out = []
    for p in cuerpo.iter(f"{W}p"):
        estilo = ""
        ppr = p.find(f"{W}pPr")
        if ppr is not None:
            st = ppr.find(f"{W}pStyle")
            if st is not None:
                estilo = st.get(f"{W}val", "")
        texto = []
        for t in p.iter(f"{W}t"):
            texto.append(t.text or "")
        linea = "".join(texto)
        # Marca si el parrafo contiene una imagen
        tiene_img = p.find(f".//{W}drawing") is not None or p.find(
            f".//{{http://schemas.openxmlformats.org/drawingml/2006/main}}blip") is not None
        out.append((estilo, linea, tiene_img))
    return out


def main():
    ruta = sys.argv[1]
    desde = sys.argv[2] if len(sys.argv) > 2 else ""
    hasta = sys.argv[3] if len(sys.argv) > 3 else ""
    ps = parrafos(ruta)
    print(f"total parrafos: {len(ps)}")
    activo = not desde
    for i, (est, txt, img) in enumerate(ps):
        if desde and desde in txt:
            activo = True
        if not activo:
            continue
        if hasta and hasta in txt and i > 0:
            break
        marca = "[IMG]" if img else "     "
        t = txt.strip()
        if not t:
            continue
        print(f"{i:5d} {marca} <{est}> {t[:300]}")


if __name__ == "__main__":
    main()
