#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matriz de evidencia del laboratorio por item del instrumento de madurez,
en formato Excel para análisis y presentación.

Reutiliza la tabla de datos del generador DOCX para que ambos entregables
no puedan divergir.
"""

import importlib.util
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

BASE = Path(r"F:\Maestria\tesis\taxfisco-research-lab")
SRC = BASE / "scripts" / "build-matriz-evidencia.py"
DST = (BASE / "instrumentos"
       / "2026-10-12_Matriz_Evidencia_Laboratorio_por_Item_v03.xlsx")

spec = importlib.util.spec_from_file_location("mat", SRC)
mat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mat)
ROWS = mat.ROWS

# paleta
NAVY = "1F3864"
BLUE = "2E5C8A"
LIGHT = "DCE6F1"
GREY = "F2F2F2"
RED = "FCE4E4"
RED_TXT = "9C0006"
GREEN = "E2EFDA"
GREEN_TXT = "1F6032"
WHITE = "FFFFFF"

thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
WRAP_C = Alignment(wrap_text=True, vertical="center", horizontal="center")
CENTER = Alignment(vertical="center", horizontal="left")

H_FONT = Font(name="Calibri", size=10, bold=True, color=WHITE)
T_FONT = Font(name="Calibri", size=18, bold=True, color=NAVY)
S_FONT = Font(name="Calibri", size=10, italic=True, color="595959")
B_FONT = Font(name="Calibri", size=10)
BB_FONT = Font(name="Calibri", size=10, bold=True)


def title_block(ws, title, subtitle, last_col):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    c = ws.cell(row=1, column=1, value=title)
    c.font = T_FONT
    c.alignment = Alignment(vertical="center", horizontal="left")
    ws.row_dimensions[1].height = 30

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=last_col)
    c = ws.cell(row=2, column=2 - 1, value=subtitle)
    c.font = S_FONT
    ws.row_dimensions[2].height = 16


def header_row(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = H_FONT
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = WRAP_C
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 34


def est_height(texts, widths, minimum=30):
    """Altura aproximada segun el ajuste de linea de cada celda."""
    lines = 1
    for t, w in zip(texts, widths):
        n = max(1, int(len(str(t)) / max(8, w * 1.05)) + 1)
        lines = max(lines, n)
    return min(150, max(minimum, lines * 13.5))


def gap_of(value):
    v = str(value).lower()
    return any(k in v for k in ("no medido", "sin evidencia",
                                "no aplica", "no calculado"))


CLASES = {
    "medida": "Mejora cuantificada",
    "declarada": "Declarado, no medido",
}

# Items cuya evidencia es una declaración de diseño o de configuración y no
# una medición. Se separan para que la cifra declarada no se lea como resultado.
DECLARADOS = {(11, 2), (12, 1), (10, 2)}


def clase_de(inst, n, valor):
    if gap_of(valor):
        return "Meta todavía no demostrada"
    if (inst, n) in DECLARADOS:
        return "Declarado, no medido"
    return "Resultado operativo observado"


def print_setup(ws, title_rows=None):
    """Landscape, ajustado al ancho y con encabezado repetido al imprimir."""
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.5
    if title_rows:
        ws.print_title_rows = title_rows


# ---------------------------------------------------------------- RESUMEN
def sheet_resumen(wb, gaps):
    ws = wb.active
    ws.title = "Resumen"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 42
    ws.column_dimensions["B"].width = 58
    ws.column_dimensions["C"].width = 46

    ws.merge_cells("A1:C1")
    c = ws["A1"]
    c.value = "MATRIZ DE EVIDENCIA DEL LABORATORIO POR ÍTEM DEL INSTRUMENTO"
    c.font = Font(name="Calibri", size=16, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 34

    ws.merge_cells("A2:C2")
    ws["A2"] = ("Diagnóstico de Madurez en Seguridad de la Información · "
                "Tesis de Maestría · versión 1 · 12 de octubre de 2026")
    ws["A2"].font = S_FONT

    r = 4
    ws.cell(row=r, column=1, value="Objeto del documento").font = BB_FONT
    r += 1
    ws.merge_cells(f"A{r}:C{r}")
    ws.cell(row=r, column=1, value=(
        "Este documento cruza los cuarenta y dos ítems del instrumento de "
        "diagnóstico con la evidencia efectivamente disponible en el "
        "laboratorio de la investigación. Cada fila declara un dato "
        "verificable y el archivo del que procede, o declara de forma "
        "explícita que ese ítem no tiene respaldo medido. Ningún valor fue "
        "estimado, aproximado ni completado por analogía."))
    ws.cell(row=r, column=1).alignment = WRAP
    ws.cell(row=r, column=1).font = B_FONT
    ws.row_dimensions[r].height = 62
    r += 2

    ws.cell(row=r, column=1, value="Cobertura de la evidencia").font = BB_FONT
    r += 1
    header_row(ws, r, ["Indicador", "Valor", "Lectura"], [42, 58, 46])
    ws.column_dimensions["A"].width = 42
    r += 1
    cov = [
        ("Ítems del instrumento", 42,
         "Catorce subdimensiones, tres ítems cada una salvo el Instrumento 7 "
         "que tiene dos."),
        ("Ítems con evidencia del laboratorio", len(ROWS) - gaps,
         "Se sostienen con un archivo del repositorio y pueden citarse en el "
         "capítulo de resultados sin ambigüedad."),
        ("Ítems sin evidencia del laboratorio", gaps,
         "Su atención corresponde a la medición posterior en la institución, "
         "donde esos ítems se responden con la decisión de los responsables."),
    ]
    for a, b, d in cov:
        ws.cell(row=r, column=1, value=a).font = B_FONT
        ws.cell(row=r, column=2, value=b).font = BB_FONT
        ws.cell(row=r, column=3, value=d).font = B_FONT
        for col in (1, 2, 3):
            ws.cell(row=r, column=col).alignment = WRAP
            ws.cell(row=r, column=col).border = BORDER
        ws.row_dimensions[r].height = est_height([a, b, d], [42, 58, 46])
        r += 1
    r += 1

    ws.cell(row=r, column=1, value="Dónde se concentran las ausencias").font = BB_FONT
    r += 1
    ws.merge_cells(f"A{r}:C{r}")
    ws.cell(row=r, column=1, value=(
        "El Instrumento 3, sobre tiempos de respuesta, está entero sin medir "
        "porque requiere marcas de tiempo de los casos en la plataforma de "
        "gestión, que la versión en prueba de la herramienta no expone. El "
        "Instrumento 13, sobre capacitación, está entero sin medir porque la "
        "metodología no trabaja sobre formación del personal. Ambas ausencias "
        "coinciden con restricciones que el propio registro de lecciones deja "
        "documentadas y acotan lo que puede afirmarse con evidencia."))
    ws.cell(row=r, column=1).alignment = WRAP
    ws.cell(row=r, column=1).font = B_FONT
    ws.cell(row=r, column=1).fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[r].height = 72
    r += 2

    ws.cell(row=r, column=1, value="Uso previsto").font = BB_FONT
    r += 1
    header_row(ws, r, ["Apartado del capítulo", "Qué se toma de esta matriz",
                       "Condición que debe cumplirse"], [42, 58, 46])
    r += 1
    uso = [
        ("4.4.5 Antes y después cuantificado",
         "Los 24 valores medidos con su archivo de origen.",
         "Cada cifra debe citar la fuente de la columna G."),
        ("4.4.6 Aportación de cada fase",
         "La atribución de cada ítem a la fase que lo produce.",
         "Los 18 ítems sin evidencia no se presentan como resultado."),
        ("4.4.1 Línea base y forma de presentar los resultados",
         "El recuento de cobertura y la regla de citar la fuente.",
         "El recuento se recalcula si cambia algún dato del laboratorio."),
        ("Medición posterior en la institución",
         "La lista exacta de ítems que el laboratorio no mide.",
         "Esos 18 ítems son los que la institución debe responder."),
    ]
    for a, b, d in uso:
        for col, val in enumerate((a, b, d), start=1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = B_FONT
            c.alignment = WRAP
            c.border = BORDER
        ws.row_dimensions[r].height = est_height([a, b, d], [42, 58, 46])
        r += 1

    return ws


# ---------------------------------------------------------------- MATRIZ
def sheet_matriz(wb):
    ws = wb.create_sheet("Matriz 42 ítems")
    ws.sheet_view.showGridLines = False

    headers = ["Instr.", "N.º", "Ítem del instrumento",
               "Evidencia disponible en el laboratorio",
               "Valor medido", "Estado", "Clasificación", "Fuente"]
    widths = [8, 7, 38, 54, 24, 15, 24, 30]

    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=8)
    ws["A1"] = "MATRIZ DE EVIDENCIA POR ÍTEM"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 26

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=8)
    ws["A2"] = ("Cada fila declara un dato verificable del laboratorio y su "
                "fuente, o declara que el ítem no tiene respaldo medido. La "
                "columna Estado separa el ítem medido del declarado, y la "
                "columna Clasificación lo sitúa en una de las cinco "
                "categorías de evidencia.")
    ws["A2"].font = S_FONT
    ws.row_dimensions[2].height = 16

    header_row(ws, 4, headers, widths)

    r = 5
    prev = None
    for inst, n, item, ev, val, src in ROWS:
        empty = gap_of(val)
        band = GREY if (prev is not None and inst != prev) else WHITE
        prev = inst

        vals = [inst, n, item, ev, val,
                "Sin evidencia" if empty else "Con evidencia",
                clase_de(inst, n, val), src]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = B_FONT
            c.border = BORDER
            c.alignment = WRAP_C if col in (1, 2) else WRAP
            if col == 1:
                c.font = BB_FONT
            if col == 5:
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=RED_TXT if empty else GREEN_TXT)
                c.fill = PatternFill("solid", fgColor=RED if empty else GREEN)
            if col == 6:
                c.alignment = WRAP_C
                c.font = Font(name="Calibri", size=9, bold=True,
                              color=RED_TXT if empty else GREEN_TXT)
            if col == 7:
                c.alignment = WRAP_C
                c.font = Font(name="Calibri", size=9, bold=True,
                              color="7F6000")
            if col not in (5, 6, 7):
                c.fill = PatternFill("solid", fgColor=band)
        ws.row_dimensions[r].height = est_height(
            [item, ev, val, src], [40, 58, 25, 32], minimum=34)
        r += 1

    last = r - 1
    ws.freeze_panes = "C5"
    ws.auto_filter.ref = f"A4:H{last}"

    ws.merge_cells(start_row=last + 2, start_column=1,
                   end_row=last + 2, end_column=8)
    c = ws.cell(row=last + 2, column=1, value=(
        "Nota. La columna Estado resume si existe respaldo medido. La columna "
        "Clasificación aplica las cinco categorías de evidencia y separa una "
        "medición de una declaración de diseño, de modo que una cifra "
        "declarada no se lea como resultado. Un ítem marcado como Sin evidencia "
        "no es un error de la investigación: son dimensiones que dependen del "
        "proceso institucional y no de la infraestructura del señuelo, y su "
        "atención corresponde a la medición posterior en la institución."))
    c.font = S_FONT
    c.alignment = WRAP
    c.fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[last + 2].height = 56
    return ws


# ---------------------------------------------------------------- INDICADORES
def sheet_indicadores(wb):
    ws = wb.create_sheet("Indicadores técnicos")
    ws.sheet_view.showGridLines = False

    headers = ["Indicador", "Prototipo I", "Prototipo II, vuelta 1",
               "Prototipo II, vuelta 2"]
    widths = [42, 24, 24, 24]

    ws.merge_cells("A1:D1")
    ws["A1"] = "INDICADORES TÉCNICOS DE LAS TRES EJECUCIONES"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 26

    ws.merge_cells("A2:D2")
    ws["A2"] = ("Valores extraídos de los reportes de indicadores de cada "
                "campaña. El valor n/d indica que ese dato no se midió.")
    ws["A2"].font = S_FONT

    header_row(ws, 4, headers, widths)

    data = [
        ("Escenarios de la campaña", "10 de 10", "10 de 10", "10 de 10"),
        ("Escenarios con tiempo de detección medido", "9 de 10", "4 de 10",
         "10 de 10"),
        ("Tiempo medio de detección", "41,598 s", "5,22 s", "2,02 s"),
        ("Tiempo mínimo de detección", "0,141 s", "1,06 s", "0,00 s"),
        ("Tiempo máximo de detección", "260,108 s", "16,85 s", "15,91 s"),
        ("Fuentes de registro que el cálculo pudo atribuir", "n/d", "3", "6"),
        ("Técnicas ATT&CK del inventario del señuelo", "17", "17", "17"),
        ("Técnicas ATT&CK con fuente de detección", "n/d", "4 de 10",
         "10 de 10"),
        ("Tácticas ATT&CK con fuente de detección", "n/d", "3 de 6",
         "6 de 6"),
        ("Técnicas ATT&CK que la campaña activa", "n/d", "10", "10"),
        ("Servicios desplegados", "25", "25", "25"),
        ("Campaña completada", "10 de 10", "10 de 10", "10 de 10"),
        ("Fases de ISO/IEC 27035 en el inventario del laboratorio", "5 de 5",
         "5 de 5", "5 de 5"),
        ("Fases de ISO/IEC 27035 ejercitadas por la campaña", "no medido",
         "1 de 5", "1 de 5"),
    ]

    r = 5
    for a, b, c_, d in data:
        ws.cell(row=r, column=1, value=a).font = B_FONT
        ws.cell(row=r, column=1).alignment = WRAP
        for col, v in ((2, b), (3, c_), (4, d)):
            cc = ws.cell(row=r, column=col, value=v)
            cc.font = BB_FONT
            cc.alignment = Alignment(horizontal="center", vertical="center")
            if "no medido" in v or "n/d" in v:
                cc.fill = PatternFill("solid", fgColor=RED)
                cc.font = Font(name="Calibri", size=10, color=RED_TXT)
        for col in range(1, 5):
            ws.cell(row=r, column=col).border = BORDER
        ws.row_dimensions[r].height = est_height([a, b, c_, d], widths,
                                                minimum=22)
        r += 1

    ws.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1,
                   end_column=4)
    c = ws.cell(row=r + 1, column=1, value=(
        "Nota. La segunda vuelta del Prototipo II no modifica el señuelo "
        "expuesto al atacante, el conjunto de escenarios, los sensores de red "
        "ni el criterio de cálculo. La diferencia entre la primera y la "
        "segunda vuelta corresponde a correcciones aplicadas a los programas "
        "de medición y no al sistema de detección, que registraba los ataques "
        "desde la primera vuelta. Por eso la comparación válida entre ejecuciones "
        "es la que se hace escenario por escenario."))
    c.font = S_FONT
    c.alignment = WRAP
    c.fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[r + 1].height = 62
    return ws


# ---------------------------------------------------------------- BRECHAS
def sheet_brechas(wb):
    ws = wb.create_sheet("Brechas del diagnóstico")
    ws.sheet_view.showGridLines = False

    headers = ["Instr.", "Subdimensión", "Antes (2026)", "Nivel",
               "Evidencia producida en el laboratorio",
               "Relación con la metodología"]
    widths = [8, 32, 14, 12, 56, 30]

    ws.merge_cells("A1:F1")
    ws["A1"] = "SEIS SUBDIMENSIONES EN NIVEL BÁSICO Y QUÉ RESUELVE EL LABORATORIO"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 26

    ws.merge_cells("A2:F2")
    ws["A2"] = ("La medición de 2026 reportó seis subdimensiones en nivel "
                "Básico. La metodología atiende cinco de ellas de forma "
                "directa y la sexta, sobre capacitación, se deriva a la "
                "medición posterior en la institución.")
    ws["A2"].font = S_FONT

    header_row(ws, 4, headers, widths)

    data = [
        (1, "Detección y registro de eventos", "48,54 %", "Básico",
         "Tiempo medio de detección de 2,02 s en los diez escenarios, con "
         "seis fuentes de registro atribuidas y con las diez técnicas de la "
         "campaña con fuente de detección.",
         "Atendida directamente por la Fase 3"),
        (4, "Lecciones aprendidas y mejora", "49,17 %", "Básico",
         "Catorce lecciones registradas, todas cerradas con resolución "
         "documentada y con su archivo de verificación.",
         "Atendida directamente por la Fase 5"),
        (7, "Retención y acceso a evidencias", "47,92 %", "Básico",
         "Noventa y un archivos de evidencia con huella SHA-256 y puntaje de "
         "calidad cien sobre cien.",
         "Atendida directamente por la Fase 3"),
        (8, "Accesos y mínimos privilegios", "49,72 %", "Básico",
         "Aislamiento verificado desde el atacante: dos objetivos alcanzables "
         "en el segmento expuesto y cuatro servicios bloqueados en el de "
         "gestión.",
         "Atendida por la Fase 2"),
        (10, "Gestión de vulnerabilidades", "50,56 %", "Básico",
         "El inventario del señuelo comprende diecisiete técnicas de MITRE "
         "ATT&CK. La campaña activa diez de ellas y, tras la corrección del "
         "instrumental, las diez reciben fuente de detección, distribuidas "
         "en seis tácticas.",
         "Atendida por las Fases 1 y 3"),
        (13, "Capacitación y cobertura", "47,78 %", "Básico",
         "El laboratorio aporta el soporte técnico de la cobertura, con "
         "diecisiete técnicas implementadas y dos vueltas de campaña sobre "
         "diez escenarios que sirven de material de Keller. La medición de "
         "esta subdimensión corresponde a la institución por su naturaleza.",
         "Derivada a la medición posterior en la institución"),
    ]

    r = 5
    for inst, sub, antes, nivel, ev, rel in data:
        vals = [inst, sub, antes, nivel, ev, rel]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = B_FONT
            c.border = BORDER
            c.alignment = WRAP_C if col in (1, 3, 4) else WRAP
            if col == 1:
                c.font = BB_FONT
            if col == 4:
                c.font = Font(name="Calibri", size=10, bold=True, color=RED_TXT)
                c.fill = PatternFill("solid", fgColor=RED)
            if col == 6 and inst == 13:
                c.font = Font(name="Calibri", size=10, italic=True,
                              color=RED_TXT)
        ws.row_dimensions[r].height = est_height(
            [sub, ev, rel], [32, 56, 30], minimum=30)
        r += 1

    ws.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1,
                   end_column=6)
    c = ws.cell(row=r + 1, column=1, value=(
        "Nota. El corte del nivel Básico se fija en el comprendido entre el "
        "26 % y menos del 51 %. Con esa definición el Instrumento 10, con "
        "50,56 %, permanece en nivel Básico y ninguna otra cifra de la "
        "medición de 2026 cambia. La subdimensión 13 se declara sin evidencia "
        "de forma deliberada, porque la metodología no aborda la formación "
        "del personal."))
    c.font = S_FONT
    c.alignment = WRAP
    c.fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[r + 1].height = 56
    return ws


def main():
    gaps = sum(1 for r in ROWS if gap_of(r[4]))
    wb = Workbook()
    sheet_resumen(wb, gaps)
    sheet_matriz(wb)
    sheet_indicadores(wb)
    sheet_brechas(wb)
    for ws, rows in ((wb["Resumen"], None), (wb["Matriz 42 ítems"], "4:4"),
                     (wb["Indicadores técnicos"], "4:4"),
                     (wb["Brechas del diagnóstico"], "4:4")):
        print_setup(ws, rows)
    DST.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DST)
    print(f"OK -> {DST}  ({len(ROWS)} items, {gaps} sin evidencia)")


if __name__ == "__main__":
    main()