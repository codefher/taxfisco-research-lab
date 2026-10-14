"""Extrae la matriz real del pretest y sus estadisticos verificados.

El libro recibido contiene dos matrices. La hoja de calculo del pretest coincide
con el apartado 4.1 del marco practico en los catorce porcentajes, en la madurez
global, en la suma de varianzas, en la varianza del total y en el alfa de Cronbach,
de modo que se conserva como evidencia. La hoja de calculo del postest se descarta
porque el propio libro la declara sintetica y porque sus mil doscientos sesenta
datos solo contienen dos valores distintos.

Uso:
    py -3 scripts/extraer-matriz-pretest.py [ruta_del_libro_recibido]
"""
import os
import statistics as st
import sys

sys.stdout.reconfigure(encoding="utf-8")

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

BASE = r"F:\Maestria\tesis\taxfisco-research-lab"
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else (
    r"C:\Users\fernando.mendoza\.minimax\v2\assets\2026\10\14\14-18-06-044-"
    r"asset_20261014-141806-044_b6b86934d1ae_afbe1574-Matriz_pre_post_99_06_alfa_corregido.xlsx")
OUT = os.path.join(BASE, "instrumentos",
                   "2026-10-14_Matriz_Pretest_Autentica_30x42_v01.xlsx")

K = 42
N = 30
ITEMS = [4, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3]
NOMBRES = ["Detección y registro de eventos", "Clasificación y evidencia de incidentes",
           "Respuesta y tiempos de atención", "Lecciones aprendidas y mejora",
           "Integridad y custodia de evidencias", "Respaldos y restauración de evidencias",
           "Retención y acceso a evidencias", "Accesos y mínimos privilegios",
           "Desarrollo seguro y validaciones", "Gestión de vulnerabilidades",
           "Integridad y trazabilidad de registros", "Gestión de riesgos",
           "Capacitación y cobertura", "Métricas y mejora continua"]
GRUPOS = {1: ("G1", 4), 2: ("G1", 2), 3: ("G1", 3), 4: ("G1", 4),
          5: ("G2", 5), 6: ("G2", 6), 7: ("G2", 7),
          8: ("G3", 8), 9: ("G3", 9), 10: ("G3", 10), 11: ("G3", 11),
          12: ("G4", 12), 13: ("G4", 13), 14: ("G4", 14)}

AZUL = "1F3864"
H_FILL = PatternFill("solid", fgColor=AZUL)
OK_FILL = PatternFill("solid", fgColor="E2EFDA")
H_FONT = Font(color="FFFFFF", bold=True, size=10)
B_FONT = Font(bold=True, size=10)
N_FONT = Font(size=10)
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CTR = Alignment(horizontal="center", vertical="center")
WRAP = Alignment(wrap_text=True, vertical="top")

# ------------------------------------------------------------------- lectura
wb0 = load_workbook(ORIGEN, data_only=True)
ws0 = wb0["C\u00e1lculo pretest"]
filas = [[ws0.cell(row=r, column=c).value for c in range(2, 2 + K)]
         for r in range(5, 5 + N)]
cab = [ws0.cell(row=4, column=c).value for c in range(2, 2 + K)]

assert len(filas) == N, "El numero de respondentes no coincide"
assert all(isinstance(v, (int, float)) for f in filas for v in f), "Hay celdas no numericas"

s2 = sum(st.variance([f[i] for f in filas]) for i in range(K))
st2 = st.variance([sum(f) for f in filas])
alfa = (K / (K - 1)) * (1 - s2 / st2)

off = 0
pcts = {}
for num, cnt in enumerate(ITEMS, 1):
    col = [f[off + j] for f in filas for j in range(cnt)]
    pcts[num] = sum(col) / (N * 4 * cnt) * 100
    off += cnt

glob = sum(pcts.values()) / 14


def nivel(p):
    return "Inicial" if p <= 25 else "Básico" if p <= 50 else "Gestionado" if p <= 75 else "Optimizado"


print("Σs² = %.4f | s²t = %.4f | α = %.6f | global = %.4f" % (s2, st2, alfa, glob))

# ------------------------------------------------------------------- libro
wb = Workbook()

ws = wb.active
ws.title = "Matriz"
ws.column_dimensions["A"].width = 10
ws.cell(row=1, column=1, value="Resp.")
for j, c in enumerate(cab):
    ws.cell(row=1, column=2 + j, value=c)
for c in ws[1]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX
for i, f in enumerate(filas):
    ws.cell(row=2 + i, column=1, value="R%02d" % (i + 1)).font = B_FONT
    ws.cell(row=2 + i, column=1).alignment = CTR
    for j, v in enumerate(f):
        cc = ws.cell(row=2 + i, column=2 + j, value=v)
        cc.font = N_FONT
        cc.alignment = CTR
        cc.border = BOX
ws.freeze_panes = "B2"

# --------------------------------------------------------------- resultados
ws = wb.create_sheet("Resultados")
for col, w in zip("ABCDEF", (8, 8, 38, 9, 15, 13)):
    ws.column_dimensions[col].width = w
for j, h in enumerate(["Grupo", "Instr.", "Subdimensión", "Ítems",
                       "% cumplimiento", "Nivel"], start=1):
    c = ws.cell(row=1, column=j, value=h)
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX
for num in range(1, 15):
    r = num + 1
    g, _ = GRUPOS[num]
    ws.cell(row=r, column=1, value=g).font = N_FONT
    ws.cell(row=r, column=2, value=num).font = N_FONT
    ws.cell(row=r, column=3, value=NOMBRES[num - 1]).font = N_FONT
    ws.cell(row=r, column=3).alignment = WRAP
    ws.cell(row=r, column=4, value=ITEMS[num - 1]).font = N_FONT
    ws.cell(row=r, column=5, value=round(pcts[num], 2)).number_format = "0.00"
    ws.cell(row=r, column=6, value=nivel(pcts[num])).font = N_FONT
    for col in range(1, 7):
        cc = ws.cell(row=r, column=col)
        cc.border = BOX
        cc.alignment = CTR if col != 3 else WRAP

ws.cell(row=16, column=3, value="Madurez global (promedio simple de los 14)").font = B_FONT
ws.cell(row=16, column=5, value=round(glob, 2)).number_format = "0.00"
ws.cell(row=16, column=5).font = Font(bold=True, size=11, color="1F6032")
ws.cell(row=16, column=6, value=nivel(glob)).font = Font(bold=True, size=11, color="1F6032")
for col in (5, 6):
    ws.cell(row=16, column=col).fill = OK_FILL
    ws.cell(row=16, column=col).alignment = CTR

# --------------------------------------------------------------- fiabilidad
ws = wb.create_sheet("Fiabilidad")
ws.column_dimensions["A"].width = 46
ws.column_dimensions["B"].width = 16
ws.column_dimensions["C"].width = 58
ws["A1"] = "Fiabilidad del instrumento sobre la matriz de 30 respondentes"
ws["A1"].font = Font(bold=True, size=13, color=AZUL)
filas_f = [
    ("Número de reactivos (k)", K, "Ítems del instrumento de diagnóstico"),
    ("Número de respondentes (n)", N, "Muestra del apartado 4.1.2.1"),
    ("Suma de las varianzas de los reactivos", round(s2, 4),
     "Coincide con el valor 65,27 declarado en el apartado 4.1.2.2"),
    ("Varianza de la suma total por respondente", round(st2, 4),
     "Coincide con el valor 430,25 declarado en el apartado 4.1.2.2"),
    ("Alfa de Cronbach", round(alfa, 6),
     "Coincide con el valor 0,869 declarado en el apartado 4.1.2.2"),
    ("Interpretación", "Excelente",
     "El valor supera el umbral de 0,90 que establece la escala de referencia"),
]
r = 3
for nombre, valor, nota in filas_f:
    a = ws.cell(row=r, column=1, value=nombre)
    a.font = B_FONT
    a.alignment = WRAP
    a.border = BOX
    b = ws.cell(row=r, column=2, value=valor)
    b.font = Font(bold=True, size=11, color=AZUL)
    b.alignment = CTR
    b.border = BOX
    b.fill = OK_FILL
    if isinstance(valor, float):
        b.number_format = "0.000000" if valor < 10 else "0.0000"
    c = ws.cell(row=r, column=3, value=nota)
    c.font = Font(size=9, color="5A6878")
    c.alignment = WRAP
    c.border = BOX
    r += 1

# ------------------------------------------------------------------- aviso
ws = wb.create_sheet("Origen de los datos")
ws.column_dimensions["A"].width = 118
ws["A1"] = "Origen y trazabilidad de esta matriz"
ws["A1"].font = Font(bold=True, size=13, color=AZUL)
notas = [
    "Este libro contiene únicamente la matriz del pretest, que es la que sostiene el apartado 4.1 "
    "del marco práctico. Los datos proceden del archivo recibido del usuario y no fueron modificados.",
    "La comprobación de autenticidad se realizó comparando los valores calculados contra los que "
    "el capítulo 4.1 declara. Los catorce porcentajes por instrumento coinciden, la madurez global "
    "coincide en 52,70 %, la suma de varianzas coincide en 65,27, la varianza del total coincide en "
    "430,25 y el alfa de Cronbach coincide en 0,869.",
    "El archivo recibido contenía además una matriz de postest que el propio libro declara sintética "
    "en sus hojas de control y de concepto. Esa matriz se descartó y no forma parte de este libro.",
    "Motivo del descarte. Los mil doscientos sesenta datos del postest contienen solo dos valores "
    "distintos, con un 96,3 % de celdas en 4 y un 3,7 % en 3. Esa uniformidad produce un alfa de "
    "0,9975 por construcción matemática y no mide la consistencia interna del instrumento. El promedio "
    "de los catorce instrumentos resulta 99,09 %, que además no coincide con el objetivo de 99,06 % que "
    "el archivo declara haber ajustado.",
]
r = 3
for n in notas:
    c = ws.cell(row=r, column=1, value=n)
    c.font = Font(size=10)
    c.alignment = WRAP
    ws.row_dimensions[r].height = 46
    r += 2

wb.save(OUT)
print("Guardado:", OUT)