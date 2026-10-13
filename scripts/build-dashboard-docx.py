"""Compone el dashboard de resultados del Prototipo II en un DOCX con estilos.

Backend S: la superficie del CLI solo admite texto y saltos de pagina, de modo
que las tablas, las imagenes y las leyendas requieren escribir el grafo OpenXML
por encima de la biblioteca.
"""
import json
import os

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = r"F:\Maestria\tesis\taxfisco-research-lab"
IMG = os.path.join(BASE, ".render", "docx-img")
OUT = os.path.join(BASE, "resultados-cap4", "dashboard-resultados.docx")

NAVY = RGBColor(0x1F, 0x38, 0x64)
NAVY2 = RGBColor(0x2E, 0x75, 0xB6)
GREEN = RGBColor(0x1F, 0x60, 0x32)
INK = RGBColor(0x22, 0x28, 0x30)
MUTE = RGBColor(0x5A, 0x68, 0x78)
HDR_FILL = "1F3864"
BAND = "EDF2F8"
BODY_FONT = "Times New Roman"
UI_FONT = "Calibri"

d = json.load(open(os.path.join(BASE, ".render", "datos-limpio.json"), encoding="utf-8"))
sec = {s["id"]: s for s in d["sections"]}


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def cell_margins(table, top=60, bottom=60, left=110, right=110):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for tag, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{tag}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def add_table(doc, head, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(head))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell_margins(t)

    hdr = t.rows[0]
    repeat_header(hdr)
    for i, h in enumerate(head):
        c = hdr.cells[i]
        c.text = ""
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h)
        r.font.name = UI_FONT
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(c, HDR_FILL)

    for n, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            c = cells[i]
            c.text = ""
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.name = UI_FONT
            r.font.size = Pt(9)
            r.font.color.rgb = INK
            if n % 2 == 1:
                shade(c, BAND)

    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    return t


def add_image(doc, name, alt, width_cm=16.0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run()
    run.add_picture(os.path.join(IMG, name), width=Cm(width_cm))
    # Texto alternativo accesible
    try:
        from docx.oxml.ns import qn as _qn
        inline = run._r.findall(_qn("wp:inline"))[0]
        docPr = inline.find(_qn("wp:docPr"))
        docPr.set("descr", alt)
        docPr.set("title", alt)
    except Exception:
        pass


def add_caption(doc, number, title):
    """Numero en redonda y titulo en cursiva, pegado a la figura."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"Figura {number}. ")
    r1.font.name = BODY_FONT
    r1.font.size = Pt(10)
    r1.font.color.rgb = INK
    r2 = p.add_run(title)
    r2.font.name = BODY_FONT
    r2.font.size = Pt(10)
    r2.font.italic = True
    r2.font.color.rgb = INK


def add_note(doc, text):
    """Nota al pie pegada a la figura, inmediatamente debajo."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run(text)
    r.font.name = BODY_FONT
    r.font.size = Pt(9)
    r.font.color.rgb = MUTE
    return p


def add_body(doc, text, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = BODY_FONT
    r.font.size = Pt(12)
    r.font.color.rgb = INK
    return p


def add_heading(doc, text, level):
    sizes = {1: 16, 2: 13.5, 3: 12}
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18 if level == 1 else 14)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = BODY_FONT
    r.font.size = Pt(sizes.get(level, 12))
    r.font.bold = True
    r.font.color.rgb = NAVY
    # Nivel de esquema para que Word lo reconozca en el panel de navegacion
    pPr = p._p.get_or_add_pPr()
    lvl = OxmlElement("w:outlineLvl")
    lvl.set(qn("w:val"), str(level - 1))
    pPr.append(lvl)
    return p


def add_callout(doc, text):
    """Recuadro de lectura con fondo y filete lateral."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    c.width = Cm(16)
    c.text = ""
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = BODY_FONT
    r.font.size = Pt(10.5)
    r.font.color.rgb = RGBColor(0x33, 0x40, 0x4F)
    shade(c, "F2F6FB")
    tcPr = c._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "24")
    left.set(qn("w:color"), "4A7EBB")
    borders.append(left)
    tcPr.append(borders)
    cell_margins(t, top=120, bottom=120, left=160, right=160)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t


# ---------------------------------------------------------------- documento
doc = Document()

st = doc.styles["Normal"]
st.font.name = BODY_FONT
st.font.size = Pt(12)
st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)

secp = doc.sections[0]
secp.page_width = Cm(21.0)
secp.page_height = Cm(29.7)
secp.top_margin = Cm(2.5)
secp.bottom_margin = Cm(2.5)
secp.left_margin = Cm(2.5)
secp.right_margin = Cm(2.5)

fig = {"n": 0}


def figure(doc, name, alt, title, note):
    fig["n"] += 1
    add_image(doc, name, alt)
    add_caption(doc, fig["n"], title)
    add_note(doc, note)


def section_block(sid, chart=None, chart_alt="", chart_title=None, chart_note=None,
                  table_widths=None):
    s = sec[sid]
    add_heading(doc, s["heading"], 2)
    if s["sub"]:
        add_body(doc, s["sub"])
    if chart:
        figure(doc, chart, chart_alt, chart_title, chart_note)
    if s["tables"]:
        t = s["tables"][0]
        add_table(doc, t["head"], t["rows"], table_widths)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)
    for n in s["notes"]:
        add_callout(doc, n)


# Portada del tablero
add_heading(doc, "Tablero de resultados del Prototipo II", 1)
add_body(doc, d["decl"])
add_callout(doc, "Nota. Los cuatro indicadores destacados cambian entre la "
                 "línea base y la medición final. Los cuatro restantes se "
                 "conservan y sirven de contraste. Cada cifra procede de un "
                 "archivo de evidencia del repositorio y ninguno es estimado.")

# 1
section_block("kpi", "kpi.png", "Panel de los ocho indicadores principales del ciclo",
              "Panel de indicadores principales del ciclo de corrección.",
              "Nota. Los cuatro indicadores destacados cambian entre la línea "
              "base y la medición final. Los cuatro restantes se conservan. "
              "Fuente: reportes de indicadores de la vuelta 1 y de la vuelta 2.")

# 2
section_block("antes", "antes.png", "Cobertura de la medición en la línea base y en la medición final",
              "Cobertura de la medición, en valores absolutos.",
              "Nota. Las cuatro primeras filas crecen porque el instrumental "
              "registra más. Las cuatro últimas no se mueven. Fuente: reportes "
              "de indicadores de las dos vueltas.",
              table_widths=[6.4, 3.2, 3.2, 3.2])

# 3
section_block("tiempo", "tiempo.png", "Tiempo de detección de los cuatro escenarios comparables",
              "Tiempo de detección de los cuatro escenarios comparables.",
              "Nota. La reducción se calcula sobre los valores de origen con "
              "tres decimales, no sobre los valores redondeados de la tabla. "
              "Fuente: reportes de indicadores de las dos vueltas.",
              table_widths=[4.4, 2.0, 2.3, 2.3, 2.0, 3.0])

# 4
section_block("dist", "dist.png", "Distribución del tiempo de detección en la medición final",
              "Distribución del tiempo de detección en la medición final.",
              "Nota. Ocho de los diez escenarios se detectan por debajo de un "
              "segundo. Fuente: reporte de indicadores de la vuelta 2.")

# 5
section_block("fuentes", "fuentes.png", "Fuentes que registran la detección en las dos vueltas",
              "Fuentes que registran la detección.",
              "Nota. Los tres componentes añadidos durante el ciclo son el "
              "emulador de acceso remoto, el archivo señuelo y el sensor de red. "
              "Fuente: reportes de indicadores de las dos vueltas.")

# 6
section_block("attack", "attack.png", "Inventario y detección de técnicas de MITRE ATT&CK",
              "Inventario y detección de técnicas del marco de comportamiento adversario.",
              "Nota. El inventario permanece en diecisiete técnicas y ocho "
              "tácticas. Lo que cambia es la atribución de detección. Fuente: "
              "mitre_coverage.json y reporte de la vuelta 2.",
              table_widths=[2.4, 3.6, 1.8, 8.2])

# 7
section_block("ciclo", "ciclo.png", "Línea de tiempo del ciclo de corrección",
              "Ciclo de iteraciones de la metodología sobre el mismo señuelo.",
              "Nota. La metodología se aplicó dos veces sobre el mismo señuelo. "
              "La primera medición produjo las catorce lecciones que originaron "
              "las correcciones de la segunda. Fuente: marcas de tiempo de ambos "
              "reportes.",
              table_widths=[4.6, 3.4, 4.6, 3.4])

# 8
section_block("fases", None, "", None, None, table_widths=[3.2, 5.4, 3.2, 2.1, 2.1])

# 9
section_block("lecciones", "lecciones.png", "Distribución de las catorce lecciones por fase",
              "Distribución de las lecciones aprendidas por fase.",
              "Nota. Catorce lecciones, todas cerradas. La columna de fase "
              "muestra dónde se produjo cada una. Fuente: "
              "evidencias/lecciones-aprendidas.md.",
              table_widths=[1.4, 1.6, 6.0, 7.0])

# 10
section_block("volumen", None, "", None, None, table_widths=[6.4, 3.2, 3.2, 3.2])

# 11
v = sec["visual"]
add_heading(doc, v["heading"], 2)
add_body(doc, v["sub"])
figure(doc, "v1.png", "Tablero de alertas del SIEM en la línea base",
       "Tablero de alertas del SIEM en la línea base, ventana de tres horas.",
       "Nota. La serie temporal muestra picos aislados y un nivel medio de "
       "alerta de 4,88 sobre cuatrocientas treinta y cuatro alertas indexadas. "
       "Fuente: v2.0-it1/04-captura-eventos/02_grafana-dashboard-siem.png.")
figure(doc, "v2.png", "Tablero de alertas del SIEM en la medición final",
       "Tablero de alertas del SIEM en la medición final, ventana de veinticuatro horas.",
       "Nota. La serie temporal sostiene actividad a lo largo de toda la "
       "ventana y el nivel medio de alerta sube a 6,20. Fuente: "
       "v2.1-it2/04-captura-eventos/05_grafana-dashboard-siem.png.")
add_callout(doc, v["notes"][0])

# Cierre
add_heading(doc, "Origen de los datos", 2)
for t in d["foot"]:
    # Alineado a la izquierda porque contiene rutas largas que la justificacion estira
    add_body(doc, t, align=WD_ALIGN_PARAGRAPH.LEFT)

doc.save(OUT)
print("Guardado:", OUT)
print("Figuras:", fig["n"])
print("Secciones:", len(doc.paragraphs), "parrafos,", len(doc.tables), "tablas")