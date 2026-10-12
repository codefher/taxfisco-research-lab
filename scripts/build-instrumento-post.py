#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Genera el instrumento de medicion posterior a partir del instrumento original.

No modifica el original: copia el paquete OOXML completo y antepone el anexo
de comparacion justo antes del <w:sectPr> final. De ese modo se conservan
intactos estilos, tablas, numeracion y fuentes del instrumento de pretest.
"""

import shutil
import zipfile
from pathlib import Path

SRC = Path(
    r"C:\Users\fernando.mendoza\.minimax\v2\assets\2026\10\12"
    r"\14-49-12-600-asset_20261012-144912-600_14af3f8b4015_1bd29ecd"
    r"-2026-06-11_Instrumento_Diagnostico_NEUTRAL_v06.docx"
)
DST = Path(
    r"F:\Maestria\tesis\taxfisco-research-lab\instrumentos"
    r"\2026-10-12_Instrumento_Diagnostico_MEDICION_POSTERIOR_v07.docx"
)

TBL = "Tablaconcuadrcula"          # estilo de tabla del documento original
H1, H2, H3 = "Ttulo1", "Ttulo2", "Ttulo3"
GREY = "D9D9D9"


def esc(t):
    return (
        t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )


def run(text, bold=False, italic=False, size=None):
    rpr = ""
    if bold:
        rpr += "<w:b/>"
    if italic:
        rpr += "<w:i/>"
    if size:
        rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def para(text="", style=None, bold=False, italic=False, size=None,
         align=None, space_after=120):
    ppr = ""
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if align:
        ppr += f'<w:jc w:val="{align}"/>'
    ppr += f'<w:spacing w:after="{space_after}"/>'
    body = run(text, bold, italic, size) if text else ""
    return f"<w:p><w:pPr>{ppr}</w:pPr>{body}</w:p>"


def bullet(text, num):
    ppr = '<w:ind w:left="454" w:hanging="284"/><w:spacing w:after="80"/>'
    return f"<w:p><w:pPr>{ppr}</w:pPr>{run(f'{num}. {text}')}</w:p>"


def cell(text, width, bold=False, shade=None, size=18):
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ""
    tcpr = f'<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shd}</w:tcPr>'
    ppr = '<w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr>'
    return f"<w:tc>{tcpr}<w:p>{ppr}{run(text, bold=bold, size=size)}</w:p></w:tc>"


def table(rows, widths, header=True):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    xml = (
        f'<w:tbl><w:tblPr><w:tblStyle w:val="{TBL}"/>'
        f'<w:tblW w:w="0" w:type="auto"/>'
        f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0"'
        f' w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
        f"</w:tblPr><w:tblGrid>{grid}</w:tblGrid>"
    )
    for i, r in enumerate(rows):
        head = header and i == 0
        tcs = "".join(
            cell(v, widths[j], bold=head, shade=GREY if head else None)
            for j, v in enumerate(r)
        )
        xml += f'<w:tr><w:trPr><w:cantSplit/></w:trPr>{tcs}</w:tr>'
    return xml + "</w:tbl>" + para("", space_after=120)


PAGE_BREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def build_annex():
    x = PAGE_BREAK

    x += para(
        "MEDICIÓN POSTERIOR DE LA MADUREZ EN SEGURIDAD DE LA INFORMACIÓN",
        style=H1, align="center", bold=True,
    )
    x += para(
        "Instrumento de Diagnóstico de Madurez · Segunda aplicación · "
        "versión 2 (postest)",
        align="center", italic=True,
    )
    x += para(
        "Institución: __________________________   "
        "Rol del respondente: __________________________   "
        "Fecha: ____/____/______",
    )

    x += para("Nota de comparabilidad", style=H2)
    x += para(
        "Este documento reproduce sin alteración las catorce subdimensiones y "
        "los cuarenta y dos ítems del instrumento aplicado entre los meses de "
        "mayo y junio de 2026. La redacción de cada pregunta, la escala ordinal "
        "de cinco puntos, la columna de justificación y el criterio de "
        "calificación se mantienen idénticos a los de la primera aplicación, "
        "de modo que los resultados obtained en esta segunda aplicación puedan "
        "compararse con los de la anterior sobre la misma escala.",
    )
    x += para(
        "La única precisión que se incorpora se refiere al corte del nivel "
        "Básico. En la ficha técnica de la primera aplicación el nivel se "
        "definió como el comprendido entre el 26 % y el 50 % de cumplimiento. "
        "El Instrumento 10, sobre gestión de vulnerabilidades, obtuvo 50,56 % y "
        "fue reportado como Básico. La presente versión fija el corte en el "
        "comprendido entre el 26 % y menos del 51 %, con lo que ese valor "
        "permanece en el mismo nivel y ninguna otra cifra de la medición "
        "anterior cambia. La corrección se aplica por igual a las dos "
        "mediciones para que la comparación se realice sobre un criterio único.",
    )
    x += para(
        "El objetivo de esta aplicación es cuantificar el efecto de la "
        "metodología de honeypot sobre el proceso institucional. Los "
        "respondentes deben responder respecto del estado actual de su "
        "proceso y no respecto del laboratorio de la investigación.",
        italic=True,
    )

    x += para("A. Referencia de contraste del laboratorio", style=H2)
    x += para(
        "La tabla siguiente muestra, para cada una de las seis subdimensiones "
        "que la primera aplicación reportó en nivel Básico, el valor obtenido "
        "en el diagnóstico y la evidencia que el laboratorio de la "
        "investigación produjo sobre esa misma subdimensión. Se incluye como "
        "referencia de lo que la metodología es capaz de resolver, no como "
        "respuesta esperada.",
    )

    rows_a = [
        ["Instr.", "Subdimensión", "Antes (2026)",
         "Evidencia producida en el laboratorio", "Relación con la metodología"],
        ["1", "Detección y registro de eventos", "48,54 %\nBásico",
         "Tiempo medio de detección de 2,02 s en los diez escenarios de la "
         "campaña, con cinco fuentes de detección independentes",
         "Atendida directamente por la Fase 3"],
        ["4", "Lecciones aprendidas y mejora", "49,17 %\nBásico",
         "Catorce lecciones registradas (L1 a L14), de las cuales once "
         "quedaron cerradas y tres permanecen abiertas",
         "Atendida directamente por la Fase 5"],
        ["7", "Retención y acceso a evidencias", "47,92 %\nBásico",
         "Noventa y un archivos de evidencia con huella SHA-256 y puntaje de "
         "calidad cien sobre cien",
         "Atendida directamente por la Fase 3"],
        ["8", "Accesos y mínimos privilegios", "49,72 %\nBásico",
         "Aislamiento verificado desde el atacante: dos objetivos alcanzables "
         "en el segmento expuesto y cuatro servicios bloqueados en el "
         "segmento de gestión",
         "Atendida por la Fase 2"],
        ["10", "Gestión de vulnerabilidades", "50,56 %\nBásico",
         "Diecisiete técnicas de MITRE ATT&CK implementadas, diez detectadas, "
         "distribuidas en seis tácticas",
         "Atendida por las Fases 1 y 3"],
        ["13", "Capacitación y cobertura", "47,78 %\nBásico",
         "El laboratorio no produce evidencia sobre esta subdimensión",
         "Derivada al plan institucional"],
    ]
    x += table(rows_a, [620, 1700, 900, 3400, 2020])

    x += para(
        "Nota. La columna de evidencia recoge hechos verificables del "
        "laboratorio y no modifica la respuesta que corresponde a la "
        "institución. La subdimensión 13 se declara sin evidencia de forma "
        "deliberada, porque la metodología no aborda la formación del personal "
        "y esa brecha se deriva al plan institucional.",
        italic=True, size=18,
    )

    x += para("B. Indicadores técnicos del laboratorio", style=H2)
    x += para(
        "Los valores siguientes corresponden a las tres ejecuciones "
        "documentadas en la investigación. Se emplean como referencia de "
        "comportamiento esperado del sistema de detección.",
    )

    rows_b = [
        ["Indicador", "Prototipo I", "Prototipo II, vuelta 1",
         "Prototipo II, vuelta 2"],
        ["Escenarios de la campaña", "10 de 10", "10 de 10", "10 de 10"],
        ["Escenarios con tiempo de detección medido", "9 de 10", "4 de 10",
         "10 de 10"],
        ["Tiempo medio de detección", "41,598 s", "5,22 s", "2,02 s"],
        ["Tiempo mínimo de detección", "0,141 s", "1,06 s", "0,00 s"],
        ["Tiempo máximo de detección", "260,108 s", "16,85 s", "15,91 s"],
        ["Fuentes que el cálculo pudo atribuir", "n/d", "2", "5"],
        ["Técnicas ATT&CK detectadas", "10 de 17", "10 de 17", "10 de 17"],
        ["Tácticas ATT&CK cubiertas", "6", "6", "6"],
        ["Servicios desplegados", "25", "25", "25"],
        ["Campaña completada", "10 de 10", "10 de 10", "10 de 10"],
    ]
    x += table(rows_b, [3200, 1813, 1813, 1814])

    x += para(
        "Nota. La segunda vuelta del Prototipo II no modifica el señuelo "
        "expuesto al atacante, el conjunto de escenarios, los sensores de red "
        "ni el criterio de cálculo. La diferencia entre la primera y la "
        "segunda vuelta corresponde a correcciones aplicadas a los programas "
        "de medición, no al sistema de detección, que registraba los ataques "
        "desde la primera vuelta.",
        italic=True, size=18,
    )

    x += para("C. Procedimiento de cierre de la comparación", style=H2)
    steps = [
        "Aplicar el instrumento a la misma población de respondentes que "
        "participó en la primera aplicación, respetando la misma distribución "
        "por los catorce roles funcionales.",
        "Recolectar la matriz de respuestas con la misma dimensión de treinta "
        "filas por cuarenta y dos columnas y valores enteros entre cero y "
        "cuatro.",
        "Calcular el porcentaje de cumplimiento por instrumento como el "
        "puntaje obtenido sobre el puntaje máximo, multiplicado por cien, "
        "promediado sobre los respondentes válidos.",
        "Asignar el nivel de madurez con los cortes fijados en la nota de "
        "comparabilidad de este documento.",
        "Comparar cada instrumento con su valor de 2026 y registrar la "
        "diferencia en puntos porcentuales, firmada o no según la dirección "
        "del cambio.",
        "Adjuntar a cada ítem la justificación y el documento de respaldo, "
        "igual que en la primera aplicación.",
    ]
    for i, s in enumerate(steps, 1):
        x += bullet(s, i)

    x += para(
        "Registro de aplicación. Aplico el instrumento (nombre, cargo y "
        "firma): ______________________________   "
        "Fecha: ____/____/______",
        space_after=240,
    )
    return x


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, DST)

    zin = zipfile.ZipFile(DST, "r")
    items = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    xml = items["word/document.xml"].decode("utf-8")
    i = xml.rfind("<w:sectPr")
    if i < 0:
        raise SystemExit("No se encontro el sectPr final")

    items["word/document.xml"] = (
        xml[:i] + build_annex() + xml[i:]
    ).encode("utf-8")

    zout = zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED)
    for info in infos:
        zout.writestr(info.filename, items[info.filename])
    zout.close()

    print("OK ->", DST)


if __name__ == "__main__":
    main()