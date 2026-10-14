"""Genera el libro de captura del postest del instrumento de madurez.

El libro recibe las respuestas de los respondentes del equipo del laboratorio del
SIN y calcula sola la madurez por instrumento, la madurez por grupo, la madurez
global, la fiabilidad del instrumento y la distancia respecto del pretest.

No contiene datos. Las celdas de respuesta quedan vacias y las formulas estan
listas para calcularse en cuanto se escriban los valores.

Uso:
    py -3 scripts/build-postest-captura.py
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

BASE = r"F:\Maestria\tesis\taxfisco-research-lab"
SRC = os.path.join(BASE, "instrumentos",
                   "2026-10-12_Instrumento_Diagnostico_MEDICION_POSTERIOR_v07.docx")
OUT = os.path.join(BASE, "instrumentos",
                   "2026-10-14_Matriz_Captura_Postest_30x42_v01.xlsx")

N_RESP = 30

AZUL = "1F3864"
VERDE = "1F6032"
GRIS = "5A6878"
H_FILL = PatternFill("solid", fgColor=AZUL)
SUB_FILL = PatternFill("solid", fgColor="D9E2F3")
INP_FILL = PatternFill("solid", fgColor="FFF4E0")
OK_FILL = PatternFill("solid", fgColor="E2EFDA")
H_FONT = Font(color="FFFFFF", bold=True, size=10)
B_FONT = Font(bold=True, size=10)
N_FONT = Font(size=10)
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CTR = Alignment(horizontal="center", vertical="center")

CORTES = [(25, "Inicial"), (50, "Básico"), (75, "Gestionado")]
NIVELES = ["Inicial", "Básico", "Gestionado", "Optimizado"]


def nivel(pct):
    for techo, nombre in CORTES:
        if pct <= techo:
            return nombre
    return "Optimizado"


# --------------------------------------------------------------- extraccion
d = Document(SRC)
body = d.element.body

reactivos = []
instrumento_actual = None
grupo_actual = None
pregunta_pendiente = None

for child in body.iterchildren():
    tag = child.tag.split("}")[-1]
    if tag == "p":
        p = Paragraph(child, d)
        t = p.text.strip()
        if t.startswith("Grupo "):
            grupo_actual = t.split("\u2013")[0].strip()
        elif t.startswith("Instrumento "):
            instrumento_actual = t.split("\u2013")[0].strip()
        elif re.match(r"^\d+\)\s", t):
            pregunta_pendiente = t
    elif tag == "tbl":
        tbl = Table(child, d)
        filas = tbl.rows
        if len(filas) != 6:
            continue
        if pregunta_pendiente is None:
            continue
        opciones = []
        for f in filas[1:]:
            celdas = f.cells
            rango = celdas[0].text.strip()
            valor_txt = rango.split("\n")[-1].strip() if "\n" in rango else rango
            m = re.findall(r"\d+", rango)
            opciones.append({"rango": rango, "valor_txt": valor_txt})
        reactivos.append({
            "instrumento": instrumento_actual,
            "grupo": grupo_actual,
            "pregunta": re.sub(r"^\d+\)\s*", "", pregunta_pendiente),
            "opciones": [o["rango"] for o in opciones],
        })
        pregunta_pendiente = None

print("Reactivos extraidos:", len(reactivos))

# Codigo del instrumento a partir de "Instrumento 3 - ..."
COD = {}
for r in reactivos:
    m = re.match(r"Instrumento (\d+)", r["instrumento"] or "")
    r["num"] = int(m.group(1)) if m else None
    COD[r["num"]] = r["instrumento"].split("\u2013")[-1].strip()

n_inst = len(COD)
orden_inst = sorted(COD)
print("Instrumentos:", n_inst)

# indice de la primera y ultima fila de cada instrumento
INI, FIN = {}, {}
for r in reactivos:
    i = reactivos.index(r) + 2  # fila de Excel, arranca en 2
    INI.setdefault(r["num"], i)
    FIN[r["num"]] = i

# --------------------------------------------------------------- libro
wb = Workbook()

# ---------------------------------------------------- 1. instrucciones
ws = wb.active
ws.title = "Instrucciones"
ws.column_dimensions["A"].width = 3
ws.column_dimensions["B"].width = 118
ws["B1"] = "Captura del postest · instrumento de madurez en seguridad de la informacion"
ws["B1"].font = Font(bold=True, size=14, color=AZUL)
ws["B2"] = "Servicio de Impuestos Nacionales · laboratorio del Prototipo II"
ws["B2"].font = Font(size=10, color=GRIS)

lineas = [
    ("Que contiene este libro", True),
    ("El libro esta vacio de respuestas. Al escribir el valor de cada reactivo en la hoja "
     "Matriz, las hojas siguientes calculan solas la madurez por instrumento, la madurez por "
     "grupo, la madurez global, la fiabilidad del instrumento y la distancia respecto del "
     "pretest. Ninguna cifra esta escrita de antemano.", False),
    ("", False),
    ("Orden de trabajo", True),
    ("1. Abra la hoja Registro y anote los treinta respondentes con su rol y la fecha de "
     "aplicacion.", False),
    ("2. Entregue el instrumento en blanco a cada respondente y recoja las respuestas.", False),
    ("3. Abra la hoja Matriz y escriba en cada celda el valor del reactivo, con un numero "
     "entero de 0 a 4.", False),
    ("4. Lea las hojas Por instrumento, Por grupo y Global, que ya estan calculadas.", False),
    ("5. Use la hoja Fiabilidad para comprobar el alfa de Cronbach antes de informar.", False),
    ("", False),
    ("Como se asigna el valor", True),
    ("Cada reactivo tiene cinco rangos ordenados de mejor a peor. El valor 4 corresponde al "
     "rango mas alto y el valor 0 al mas bajo. Si la metrica no se mide o no existe, el valor "
     "correcto es 0, porque un proceso que no se mide no puede gestionarse ni mejorarse.", False),
    ("", False),
    ("Cortes de madurez de la ficha tecnica", True),
    ("Inicial de 0 a 25 %, Basico de 26 a 50 %, Gestionado de 51 a 75 %, Optimizado de 76 a 100 %.", False),
    ("El porcentaje de un instrumento se obtiene de la suma de sus reactivos dividida entre "
     "su maximo posible. El porcentaje del grupo es el promedio de sus instrumentos y el "
     "porcentaje global es el promedio de los catorce instrumentos, con ponderacion igualitaria.", False),
    ("", False),
    ("Referencia del pretest", True),
    ("El pretest alcanzo una madurez global de 52,70 % en nivel Gestionado, con un alfa de "
     "Cronbach de 0,869 sobre treinta respondentes. La hoja Global contrasta el resultado "
     "del postest con ese valor y con la diferencia en puntos porcentuales.", False),
    ("", False),
    ("Regla de comparabilidad", True),
    ("El pretest y el postest solo son comparables si se aplican a los mismos roles y con el "
     "mismo instrumento. Si cambia el número de respondentes o su composicion, el contraste "
     "debe declararse como comparacion entre grupos y no como medicion del cambio.", False),
]
r = 4
for txt, es_titulo in lineas:
    c = ws.cell(row=r, column=2, value=txt)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if es_titulo:
        c.font = Font(bold=True, size=11, color=AZUL)
    else:
        c.font = Font(size=10)
    r += 1

# ---------------------------------------------------- 2. registro
ws = wb.create_sheet("Registro")
ws.column_dimensions["A"].width = 10
for col, w in zip("BCDE", (34, 24, 18, 20)):
    ws.column_dimensions[col].width = w
ws["A1"] = "ID"
ws["B1"] = "Nombre del respondente"
ws["C1"] = "Rol funcional"
ws["D1"] = "Fecha de aplicacion"
ws["E1"] = "Instrumento recibido"
for c in ws[1][:5]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX
for i in range(1, N_RESP + 1):
    ws.cell(row=i + 1, column=1, value="R%02d" % i).font = N_FONT
    ws.cell(row=i + 1, column=1).border = BOX
    ws.cell(row=i + 1, column=1).alignment = CTR
    for col in range(2, 6):
        cc = ws.cell(row=i + 1, column=col)
        cc.fill = INP_FILL
        cc.border = BOX
        cc.font = N_FONT
ws.freeze_panes = "A2"

# ---------------------------------------------------- 3. matriz
ws = wb.create_sheet("Matriz")
ws.column_dimensions["A"].width = 8
ws.column_dimensions["B"].width = 12
ws.column_dimensions["C"].width = 8
ws.column_dimensions["D"].width = 62
for i in range(1, N_RESP + 1):
    ws.column_dimensions[get_column_letter(5 + i - 1)].width = 5

ws["A1"] = "Reactivo"
ws["B1"] = "Instrumento"
ws["C1"] = "Grupo"
ws["D1"] = "Texto del reactivo"
for i in range(1, N_RESP + 1):
    ws.cell(row=1, column=4 + i, value="R%02d" % i)
for c in ws[1]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX

for idx, rv in enumerate(reactivos):
    row = idx + 2
    ws.cell(row=row, column=1, value="R%02d" % (idx + 1)).font = B_FONT
    ws.cell(row=row, column=2, value="I%02d" % rv["num"]).font = N_FONT
    ws.cell(row=row, column=3, value=rv["grupo"].replace("Grupo ", "G")).font = N_FONT
    tc = ws.cell(row=row, column=4, value=rv["pregunta"])
    tc.alignment = WRAP
    tc.font = N_FONT
    for col in range(5, 5 + N_RESP):
        cc = ws.cell(row=row, column=col)
        cc.fill = INP_FILL
        cc.border = BOX
        cc.alignment = CTR
        cc.font = N_FONT

ult = 1 + len(reactivos)
dv = DataValidation(type="whole", operator="between", formula1="0", formula2="4",
                    allow_blank=True, showErrorMessage=True,
                    errorTitle="Valor fuera de rango",
                    error="Escriba un numero entero de 0 a 4.")
ws.add_data_validation(dv)
dv.add("E2:%s%d" % (get_column_letter(4 + N_RESP), ult))

tot = ult + 1
ws.cell(row=tot, column=4, value="Total de puntos del respondente (sobre 168)").font = B_FONT
for i in range(N_RESP):
    col = get_column_letter(5 + i)
    cc = ws.cell(row=tot, column=5 + i,
                 value="=SUM(%s2:%s%d)" % (col, col, ult))
    cc.font = B_FONT
    cc.alignment = CTR
    cc.fill = OK_FILL
    cc.border = BOX

cont = tot + 1
ws.cell(row=cont, column=4, value="Reactivos contestados por el respondente (de 42)").font = B_FONT
for i in range(N_RESP):
    col = get_column_letter(5 + i)
    cc = ws.cell(row=cont, column=5 + i,
                 value="=COUNTA(%s2:%s%d)" % (col, col, ult))
    cc.font = B_FONT
    cc.alignment = CTR
    cc.fill = OK_FILL
    cc.border = BOX
ws.freeze_panes = "E2"

# ---------------------------------------------------- 4. por instrumento
ws = wb.create_sheet("Por instrumento")
ws.column_dimensions["A"].width = 8
ws.column_dimensions["B"].width = 40
for col in "CDE":
    ws.column_dimensions[col].width = 15
ws.column_dimensions["F"].width = 12
ws.column_dimensions["G"].width = 14
ws.column_dimensions["H"].width = 14

ws["A1"] = "Instr."
ws["B1"] = "Denominacion"
ws["C1"] = "Puntaje de la muestra"
ws["D1"] = "Puntaje maximo"
ws["E1"] = "% de cumplimiento"
ws["F1"] = "Nivel"
ws["G1"] = "% del pretest"
ws["H1"] = "Diferencia en puntos"
for c in ws[1]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX
ws.row_dimensions[1].height = 32

PRETEST = {1: 48.54, 2: 56.94, 3: 58.06, 4: 49.17, 5: 57.22, 6: 58.33, 7: 47.92,
           8: 49.72, 9: 53.06, 10: 50.56, 11: 52.78, 12: 53.89, 13: 47.78, 14: 53.89}

for k, num in enumerate(orden_inst):
    row = k + 2
    f_ini, f_fin = INI[num], FIN[num]
    ws.cell(row=row, column=1, value="I%02d" % num).font = B_FONT
    ws.cell(row=row, column=2, value=COD[num]).font = N_FONT
    ws.cell(row=row, column=2).alignment = WRAP
    ws.cell(row=row, column=3,
            value="=SUM(Matriz!E%d:%s%d)/%d" % (f_ini, get_column_letter(4 + N_RESP), f_fin, N_RESP))
    ws.cell(row=row, column=4, value=4 * (f_fin - f_ini + 1))
    ws.cell(row=row, column=5, value="=IF(D%d=0,0,C%d/D%d*100)" % (row, row, row))
    ws.cell(row=row, column=5).number_format = "0.00"
    ws.cell(row=row, column=6,
            value='=IF(E{0}="","",IF(E{0}<=25,"Inicial",IF(E{0}<=50,"Basico",'
                  'IF(E{0}<=75,"Gestionado","Optimizado"))))'.format(row))
    ws.cell(row=row, column=7, value=PRETEST[num]).number_format = "0.00"
    ws.cell(row=row, column=8, value="=IF(E{0}=\"\",\"\",E{0}-G{0})".format(row))
    ws.cell(row=row, column=8).number_format = "0.00"
    for col in range(3, 9):
        cc = ws.cell(row=row, column=col)
        cc.font = N_FONT
        cc.border = BOX
        cc.alignment = CTR if col != 6 else CTR

row = len(orden_inst) + 3
ws.cell(row=row, column=2, value="Madurez global (promedio de los 14 instrumentos)").font = B_FONT
ws.cell(row=row, column=5, value="=AVERAGE(E2:E%d)" % (len(orden_inst) + 1))
ws.cell(row=row, column=5).number_format = "0.00"
ws.cell(row=row, column=5).font = Font(bold=True, size=11, color=VERDE)
ws.cell(row=row, column=5).fill = OK_FILL
ws.cell(row=row, column=5).alignment = CTR
ws.cell(row=row, column=6,
        value='=IF(E{0}="","",IF(E{0}<=25,"Inicial",IF(E{0}<=50,"Basico",'
              'IF(E{0}<=75,"Gestionado","Optimizado"))))'.format(row))
ws.cell(row=row, column=6).font = Font(bold=True, size=11, color=VERDE)
ws.cell(row=row, column=6).fill = OK_FILL
ws.cell(row=row, column=6).alignment = CTR
ws.freeze_panes = "C2"

# ---------------------------------------------------- 5. por grupo
ws = wb.create_sheet("Por grupo")
ws.column_dimensions["A"].width = 8
ws.column_dimensions["B"].width = 38
ws.column_dimensions["C"].width = 18
ws.column_dimensions["D"].width = 14
ws.column_dimensions["E"].width = 14

GRP = {"G1": [1, 2, 3, 4], "G2": [5, 6, 7], "G3": [8, 9, 10], "G4": [11, 12, 13, 14]}
NOMBRE_GRUPO = {
    "G1": "Gestion de incidentes",
    "G2": "Evidencias y respaldo",
    "G3": "Controles tecnicos",
    "G4": "Gestion organizacional y mejora",
}
PRE_GRUPO = {"G1": 53.18, "G2": 54.49, "G3": 51.53, "G4": 51.85}

ws["A1"] = "Grupo"
ws["B1"] = "Denominacion"
ws["C1"] = "Instrumentos"
ws["D1"] = "% de cumplimiento"
ws["E1"] = "% del pretest"
for c in ws[1]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX
ws.row_dimensions[1].height = 30

for k, g in enumerate(["G1", "G2", "G3", "G4"]):
    row = k + 2
    filas = [orden_inst.index(n) + 2 for n in GRP[g]]
    refs = ",".join("'Por instrumento'!E%d" % f for f in filas)
    ws.cell(row=row, column=1, value=g).font = B_FONT
    ws.cell(row=row, column=2, value=NOMBRE_GRUPO[g]).font = N_FONT
    ws.cell(row=row, column=3, value=", ".join("I%02d" % n for n in GRP[g])).font = N_FONT
    ws.cell(row=row, column=4, value="=AVERAGE(%s)" % refs)
    ws.cell(row=row, column=4).number_format = "0.00"
    ws.cell(row=row, column=5, value=PRE_GRUPO[g]).number_format = "0.00"
    for col in range(1, 6):
        cc = ws.cell(row=row, column=col)
        cc.border = BOX
        cc.alignment = CTR if col != 2 else WRAP
        if col != 2:
            cc.font = N_FONT

rango = 2 + len(reactivos)
ws.cell(row=7, column=2, value="Amplitud entre el grupo mas alto y el mas bajo").font = B_FONT
ws.cell(row=7, column=4, value="=MAX(D2:D5)-MIN(D2:D5)")
ws.cell(row=7, column=4).number_format = "0.00"
ws.cell(row=7, column=4).font = N_FONT
ws.cell(row=7, column=4).alignment = CTR
ws.cell(row=7, column=4).border = BOX

# ---------------------------------------------------- 6. global
ws = wb.create_sheet("Global")
ws.column_dimensions["A"].width = 42
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 46

ws["A1"] = "Indicador"
ws["B1"] = "Valor"
ws["C1"] = "Origen"
for c in ws[1]:
    c.font = H_FONT
    c.fill = H_FILL
    c.alignment = CTR
    c.border = BOX

filas = [
    ("Reactivos del instrumento", 42, "Hoja Matriz"),
    ("Instrumentos", 14, "Hoja Por instrumento"),
    ("Respondentes previstos", N_RESP, "Hoja Registro"),
    ("Respondentes con respuesta completa", None, "Cuenta los respondentes querictional completaron los 42 reactivos"),
    ("Madurez global del postest", "='Por instrumento'!E16", "Promedio de los catorce instrumentos"),
    ("Nivel de madurez del postest", "='Por instrumento'!F16", "Corte de la ficha tecnica"),
    ("Madurez global del pretest", 52.70, "Apartado 4.1 del marco practico"),
    ("Diferencia en puntos porcentuales", None, "Postest menos pretest"),
    ("Alfa de Cronbach del postest", "=Fiabilidad!B3", "Hoja Fiabilidad"),
    ("Alfa de Cronbach del pretest", 0.869, "Apartado 4.1.2.2 del marco practico"),
    ("Instrumentos en nivel Basico", '=COUNTIF(\'Por instrumento\'!F2:F15,"Basico")', "Hoja Por instrumento"),
    ("Instrumentos en nivel Gestionado", '=COUNTIF(\'Por instrumento\'!F2:F15,"Gestionado")', "Hoja Por instrumento"),
    ("Instrumentos en nivel Optimizado", '=COUNTIF(\'Por instrumento\'!F2:F15,"Optimizado")', "Hoja Por instrumento"),
]
filas[3] = ("Respondentes con respuesta completa",
            "=SUMPRODUCT(--(COUNTIF(OFFSET(Matriz!E2,0,0,%d,%d),Matriz!E2:E%d)=%d))"
            % (len(reactivos), N_RESP, len(reactivos), len(reactivos)),
            "Cuenta los respondentes que completaron los %d reactivos" % len(reactivos))

r = 2
for nombre, valor, origen in filas:
    a = ws.cell(row=r, column=1, value=nombre)
    a.font = N_FONT
    a.border = BOX
    a.alignment = WRAP
    b = ws.cell(row=r, column=2, value=valor)
    b.font = Font(bold=True, size=11, color=AZUL)
    b.alignment = CTR
    b.border = BOX
    b.fill = OK_FILL
    if isinstance(valor, (int, float)):
        b.number_format = "0.00" if valor > 2 else "0"
    c = ws.cell(row=r, column=3, value=origen)
    c.font = Font(size=9, color=GRIS)
    c.border = BOX
    c.alignment = WRAP
    r += 1

ws.cell(row=8, column=2).number_format = "0.00"
ws.cell(row=6, column=2).number_format = "0.00"

# ---------------------------------------------------- 7. fiabilidad
ws = wb.create_sheet("Fiabilidad")
ws.column_dimensions["A"].width = 46
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 60

ws["A1"] = "Alfa de Cronbach sobre los 42 reactivos"
ws["A1"].font = Font(bold=True, size=13, color=AZUL)

ult_col = get_column_letter(4 + N_RESP)
ws["A3"] = "Numero de reactivos (k)"
ws["B3"] = len(reactivos)
ws["A4"] = "Numero de respondentes (n)"
ws["B4"] = N_RESP
ws["A5"] = "Suma de las varianzas de los reactivos"
ws["B5"] = ("=SUMPRODUCT(VAR.S(Matriz!E2:%s%d))"
            % (ult_col, len(reactivos) + 1))
ws["A6"] = "Varianza de la suma total por respondente"
ws["B6"] = "=VAR.S(Matriz!%s%d:%s%d)" % (get_column_letter(5),
                                          len(reactivos) + 2,
                                          ult_col,
                                          len(reactivos) + 2)
ws["A7"] = "Alfa de Cronbach"
ws["B7"] = "=(B4/(B4-1))*(1-B5/B6)"
ws["A8"] = "Interpretacion"
ws["B8"] = "Por encima de 0,70 se considera aceptable; por encima de 0,80, buena."

for r_ in range(3, 9):
    a = ws.cell(row=r_, column=1)
    a.font = B_FONT if r_ == 7 else N_FONT
    a.alignment = WRAP
    a.border = BOX
    b = ws.cell(row=r_, column=2)
    b.font = Font(bold=True, size=11, color=AZUL)
    b.alignment = CTR
    b.border = BOX
    b.number_format = "0.0000"
ws["B3"].number_format = "0"
ws["B4"].number_format = "0"
ws["B8"].font = Font(size=9, color=GRIS)
ws["B8"].alignment = WRAP

ws["A11"] = "Nota"
ws["A11"].font = B_FONT
ws["A12"] = ("El alfa se calcula sobre la matriz de respuestas crudas, con el valor de 0 a 4 de cada "
             "reactivo. Si el numero de respondentes cambia, la hoja B4 debe ajustarse a mano.")
ws["A12"].font = Font(size=9, color=GRIS)
ws["A12"].alignment = WRAP

wb.save(OUT)
print("Guardado:", OUT)
print("Instrumentos:", len(orden_inst), "| Reactivos:", len(reactivos))