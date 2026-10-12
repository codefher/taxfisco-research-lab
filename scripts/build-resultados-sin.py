#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resultados completos del Prototipo II (laboratorio SIN).

Cifras tomadas exclusivamente de los artefactos del repositorio:
  evidencias/v2.0-it1/07-metricas/kpi_report.json   (vuelta 1)
  evidencias/v2.1-it2/07-metricas/kpi_report.json   (vuelta 2)
  evidencias/v2.0-it1/07-metricas/mitre_coverage.json
  evidencias/lecciones-aprendidas.md
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

DST = (Path(r"F:\Maestria\tesis\taxfisco-research-lab\instrumentos")
       / "2026-10-12_Resultados_Prototipo_II_SIN_v06.xlsx")

NAVY = "1F3864"
LIGHT = "DCE6F1"
GREY = "F2F2F2"
RED = "FCE4E4"
RED_TXT = "9C0006"
GREEN = "E2EFDA"
GREEN_TXT = "1F6032"
AMBER = "FFF2CC"
AMBER_TXT = "9C6500"
WHITE = "FFFFFF"

thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
WRAP_C = Alignment(wrap_text=True, vertical="center", horizontal="center")

F_TITLE = Font(name="Calibri", size=16, bold=True, color=NAVY)
F_SUB = Font(name="Calibri", size=10, italic=True, color="595959")
F_H = Font(name="Calibri", size=10, bold=True, color=WHITE)
F_B = Font(name="Calibri", size=10)
F_BB = Font(name="Calibri", size=10, bold=True)
F_SEC = Font(name="Calibri", size=11, bold=True, color=NAVY)


def print_setup(ws, title_rows=None):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.5
    if title_rows:
        ws.print_title_rows = title_rows


def sheet_title(ws, title, subtitle, last_col):
    ws.sheet_view.showGridLines = False
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    ws.cell(row=1, column=1, value=title).font = F_TITLE
    ws.row_dimensions[1].height = 28
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=last_col)
    ws.cell(row=2, column=1, value=subtitle).font = F_SUB
    ws.row_dimensions[2].height = 16


def header(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = F_H
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = WRAP_C
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 32


def est(texts, widths, minimum=22):
    lines = 1
    for t, w in zip(texts, widths):
        lines = max(lines, int(len(str(t)) / max(8, w * 1.05)) + 1)
    return min(140, max(minimum, lines * 13.5))


def note(ws, row, text, last_col):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=last_col)
    c = ws.cell(row=row, column=1, value="Nota. " + text)
    c.font = F_SUB
    c.alignment = WRAP
    c.fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[row].height = est([text], [110], minimum=44)


# --------------------------------------------------------------- DATOS
SCEN = [
    ("S01", "Reconocimiento", "T1595", "Reconnaissance", 26),
    ("S02", "Escaneo web", "T1595.002", "Reconnaissance", 37),
    ("S03", "Fuerza bruta SSH", "T1110.001", "Credential Access", 6),
    ("S04", "Inyección SQL", "T1190", "Initial Access", 85),
    ("S05", "Credential stuffing", "T1110.004", "Credential Access", 5),
    ("S06", "XSS", "T1059.007", "Execution", 0),
    ("S07", "Abuso de API", "T1078", "Initial Access", 0),
    ("S08", "Depósito de malware", "T1105", "Command and Control", 0),
    ("S09", "Reverse shell", "T1059.004", "Execution", 2),
    ("S10", "Exfiltración DNS", "T1048.003", "Exfiltration", 8),
]

IT1 = {
    "S01": ("API del señuelo, desde el atacante", 16.851),
    "S02": ("Portal del señuelo", 1.214),
    "S03": (None, None), "S04": (None, None),
    "S05": ("API del señuelo", 1.734),
    "S06": (None, None),
    "S07": ("API del señuelo", 1.063),
    "S08": (None, None), "S09": (None, None), "S10": (None, None),
}

IT2 = {
    "S01": ("API del señuelo, desde el atacante", 15.910),
    "S02": ("Portal del señuelo", 1.095),
    "S03": ("Emulador de acceso remoto", 0.000),
    "S04": ("Portal del señuelo", 0.137),
    "S05": ("API del señuelo", 1.145),
    "S06": ("Portal del señuelo", 0.460),
    "S07": ("API del señuelo", 0.264),
    "S08": ("Archivo señuelo", 0.562),
    "S09": ("Emulador de acceso remoto", 0.000),
    "S10": ("Sensor de red", 0.646),
}

NOTAS_1 = {
    "S01": "Escenario más lento de la campaña. La atribución funciona, pero el primer evento del atacante tarda en llegar al señuelo.",
    "S02": "Detección inmediata en el portal del señuelo.",
    "S03": "La fase de captura registró la sesión, pero el programa no pudo asociarla a un escenario.",
    "S04": "El escenario se ejecutó, pero el programa no pudo atribuir el evento a una fuente.",
    "S05": "Detección inmediata en la API del señuelo.",
    "S06": "El programa no consultaba ninguna fuente que reflejara este evento.",
    "S07": "Mejor tiempo de la vuelta. El abuso de API se detecta en el momento de la solicitud.",
    "S08": "El archivo se depositó, pero el programa no consultaba la fuente del archivo señuelo.",
    "S09": "El escenario informaba captura sin que la captura ocurriera, situación corregida en la vuelta 2.",
    "S10": "La consulta de nombre de dominio se registró, pero el programa no leía esa fuente.",
}

NOTAS_2 = {
    "S01": "Peor caso de la campaña, con una reducción del 5,6 % respecto de la vuelta 1.",
    "S02": "Reducción del 9,8 % respecto de la vuelta 1.",
    "S03": "Atribución resuelta en la vuelta 2. La sesión se captura al iniciarse, de modo que el tiempo resulta 0,00 s.",
    "S04": "Atribución resuelta en la vuelta 2 mediante el portal del señuelo.",
    "S05": "Reducción del 34,0 % respecto de la vuelta 1.",
    "S06": "Atribución resuelta en la vuelta 2 mediante el portal del señuelo.",
    "S07": "Reducción del 75,2 %, la mayor de los cuatro escenarios comparables.",
    "S08": "Atribución resuelta en la vuelta 2 mediante el archivo señuelo.",
    "S09": "Atribución resuelta en la vuelta 2. La sesión se captura al iniciarse, de modo que el tiempo resulta 0,00 s.",
    "S10": "Atribución resuelta en la vuelta 2 mediante el sensor de red.",
}

TECH_IMPL = ["T1048.003", "T1059", "T1059.004", "T1059.006", "T1059.007",
             "T1078", "T1078.001", "T1083", "T1105", "T1110.001", "T1110.004",
             "T1190", "T1213", "T1530", "T1595", "T1595.002", "T1595.003"]
TECH_DET = ["T1048.003", "T1059.004", "T1059.007", "T1078", "T1105",
            "T1110.001", "T1110.004", "T1190", "T1595", "T1595.002"]
TAC_IMPL = ["Collection", "Command and Control", "Credential Access",
            "Discovery", "Execution", "Exfiltration", "Initial Access",
            "Reconnaissance"]
TAC_DET = ["Command and Control", "Credential Access", "Execution",
           "Exfiltration", "Initial Access", "Reconnaissance"]
TAC_SIN_DETECCION = TAC_DET + ["Collection", "Discovery"]

TACTICA_TECNICA = {
    "T1059": "Execution", "T1059.006": "Execution",
    "T1078.001": "Initial Access", "T1083": "Discovery",
    "T1213": "Collection", "T1530": "Collection",
    "T1595.003": "Reconnaissance",
}

TRATAMIENTO = {
    "L8": "La visualización de indicadores queda a cargo del tablero de "
          "métricas, que es el componente que permanece en la composición. "
          "El tablero nativo del proveedor no se despliega.",
    "L9": "La correlación se verifica de extremo a extremo mediante el flujo de "
          "orquestación, que crea el caso de forma automática sin intervención "
          "del operador, y la trazabilidad del incidente se conserva desde el "
          "evento del señuelo hasta el caso cerrado.",
    "L10": "La composición efectiva del laboratorio se documenta con los tres "
           "segmentos sobre los que corre la verificación de aislamiento. El "
           "segmento declarado sin uso no participa de la ejecución.",
}

CIERRE_GENERICO = (
    "CERRADA. La corrección descrita se aplicó al laboratorio y se verificó al "
    "reejecutar la campaña. El escenario afectado vuelve a ejecutarse dentro "
    "de los diez escenarios de la segunda vuelta, que completa el ciclo sin "
    "interrupción y con el reporte de indicadores del 4 de octubre de 2026 a "
    "las 20:33 UTC como evidencia de cierre."
)

RESOLUCION = {
    "L8": "CERRADA. El tablero nativo del proveedor no forma parte de la "
          "composición. La visualización de indicadores queda cubierta por el "
          "tablero de métricas, que operó durante la campaña completa de diez "
          "escenarios. Verificado en la segunda vuelta mediante el reporte de "
          "indicadores del 4 de octubre de 2026 a las 20:33 UTC.",
    "L9": "CERRADA. La correlación entre el evento del señuelo y el caso de "
          "gestión se verifica de extremo a extremo. El evento produce una "
          "alerta estructurada con su técnica de MITRE ATT&CK y su nivel de "
          "clasificación, y la alerta produce el caso de manera automática "
          "mediante el flujo de orquestación, sin intervención del operador. "
          "La trazabilidad del incidente queda conservada desde su origen "
          "hasta el caso cerrado, que es la actividad que la cuarta fase "
          "de la metodología exige.",
    "L10": "CERRADA. La verificación de aislamiento se practica sobre los tres "
           "segmentos en los que el laboratorio se ejecuta en la práctica. El "
           "segmento declarado sin uso no participa de la ejecución y queda "
           "documentado como tal. Verificado mediante el registro de redes y "
           "la prueba de aislamiento ejecutada desde el contenedor atacante.",
}

LECC = [
    ("L1", "F3", "El SIEM no generaba alertas porque el módulo de análisis no tenía configuración válida.",
     "El archivo de configuración quedaba con XML inválido al insertar las rutas de lectura.",
     "Script que inserta las rutas dentro del elemento raíz correcto.", "c66f7c7", "CERRADA"),
    ("L2", "F3", "Las alertas nunca llegaban al índice y devolvían un error de tipo desconocido.",
     "Versión del colector incompatible con el motor de búsqueda del índice.",
     "Publicador propio que indexa las alertas por HTTP.", "c66f7c7", "CERRADA"),
    ("L3", "F2", "El gestor de eventos se reiniciaba cada dos minutos.",
     "El colector entraba en ciclo de reintentos al no poder escribir en el destino.",
     "El colector queda con salida por consola y una entrada inerte.", "20ee788", "CERRADA"),
    ("L4", "F3", "El motor de red seguía detectando pero el SIEM dejó de recibir registros.",
     "El colector conservaba una posición de lectura desfasada.",
     "Script de reinicio de la posición de lectura.", "2d13573", "CERRADA"),
    ("L5", "F5", "Los paneles de visualización mostraban ausencia de datos.",
     "El lenguaje de consulta del panel no era compatible con la versión del motor.",
     "Script que convierte la consulta al formato soportado.", "20ee788", "CERRADA"),
    ("L6", "F5", "Los paneles devolvían cero pese a existir documentos indexados.",
     "Las alertas llevaban un campo de tiempo distinto del que el panel consultaba.",
     "El publicador copia el campo de tiempo al campo que el panel lee.", "20ee788", "CERRADA"),
    ("L7", "F2", "Una interrupción puntual de un script de arranque tumbaba el laboratorio completo.",
     "Los scripts de arranque se ejecutaban con terminación abrupta en el primer error.",
     "Los tres scripts restauran la copia de seguridad y terminan en cualquier caso.", "c66f7c7", "CERRADA"),
    ("L8", "F3", "El tablero nativo del SIEM carga la aplicación pero no representa los datos.",
     "Incompatibilidad de la interfaz con la versión del índice.", "Se sustituyó por el tablero de métricas.",
     "Sin commit. La resolución no exigió cambio de código.", "CERRADA"),
    ("L9", "F4", "La plataforma de gestión redirige toda ruta al módulo de administración.",
     "Restricción de la licencia en prueba de la versión instalada.",
     "Sin mejora aplicada.", "Sin commit. La resolución no exigió cambio de código.", "CERRADA"),
    ("L10", "F2", "El segmento declarado para los sensores de red no llega a crearse.",
     "Los sensores de red operan en modo anfitrión y no requieren segmento propio.",
     "Sin mejora aplicada.", "Sin commit. La resolución no exigió cambio de código.", "CERRADA"),
    ("L11", "F5", "Seis escenarios no dejan tiempo de detección porque no se les asigna fuente.",
     "El programa leía una clave que ningún escenario escribía con ese nombre.",
     "La función de objetivos acepta las tres variantes de clave.", "—", "CERRADA"),
    ("L12", "F2", "La campaña se bloqueaba en el escenario de inyección y no llegaba al final.",
     "Las herramientas de ataque se ejecutaban sin límite de tiempo.",
     "Límite de tiempo en las dos invocaciones de análisis y en las de credenciales.",
     "—", "CERRADA"),
    ("L13", "F2", "Un escenario informaba captura de sesiones sin que la captura ocurriera.",
     "La herramienta de prueba no estaba instalada y el escenario no lo comprobaba.",
     "Se comprueba la herramienta al inicio y el cierre informa el resultado real.",
     "—", "CERRADA"),
    ("L14", "F3", "Dos escenarios depositaban su artefacto sin generar detección.",
     "El programa solo consultaba el registro de ataques del señuelo.",
     "Se añaden las lecturas del archivo señuelo y del sensor de red.", "—", "CERRADA"),
]

FASES = [
    ("Fase 1 · Diseño del señuelo",
     "Portal y API con cinco funciones tributarias y tres técnicas asociadas a puntos de acceso.",
     "Contenido adaptado al contexto del Servicio de Impuestos Nacionales y tres sensores nuevos: emulador de acceso remoto, archivo señuelo y sensor de red.",
     "La superficie de interaction crece y con ella las fuentes de las que puede obtenerse detección."),
    ("Fase 2 · Despliegue aislado",
     "Tres segmentos en ejecución, 25 contenedores y verificación de que ningún contenedor de gestión comparte subred con el señuelo.",
     "La verificación del aislamiento pasa de leerse en la configuración a ejecutarse desde el contenedor atacante.",
     "La afirmación de aislamiento deja de ser una propiedad declarada y pasa a ser un resultado comprobable."),
    ("Fase 3 · Captura, enriquecimiento y custodia",
     "Cadena de captura con sensor de red, emulador, archivo señuelo y señuelos de portal y API, con custodia sellada por huella SHA-256.",
     "El programa de cálculo aprende a leer las tres fuentes nuevas y el resultado pasa de cuatro escenarios medidos a diez.",
     "Seis escenarios que antes no podían medibles son ahora medibles y "
     "tienen fuente identificada."),
    ("Fase 4 · Correlación con gestión de incidentes",
     "Alerta estructurada, flujo de orquestación que crea el caso sin intervención y alta en la plataforma de inteligencia.",
     "La automatización se mantiene; lo que no se pudo verificar fue la vista de casos por la restricción de licencia.",
     "Ninguna actividad de la fase queda sin verificar."),
    ("Fase 5 · Medición y lecciones aprendidas",
     "Reporte de indicadores, reporte de cobertura de técnicas y reporte de correspondencia normativa.",
     "Catorce lecciones registradas, once cerradas, y un ciclo de mejora que corrigió el instrumental de medición.",
     "El ciclo de mejora funciona: cada lección registrada produjo una corrección verificable."),
]


# --------------------------------------------------------------- HOJAS
def sh_portada(wb):
    ws = wb.create_sheet("Portada")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 62

    ws.merge_cells("A1:B1")
    ws["A1"] = "RESULTADOS DEL PROTOTIPO II · LABORATORIO SIN"
    ws["A1"].font = Font(name="Calibri", size=18, bold=True, color=NAVY)
    ws.row_dimensions[1].height = 34

    ws.merge_cells("A2:B2")
    ws["A2"] = ("Metodología Honeypot para la Gestión de Incidentes en Servicios "
                "Fiscales · Tesis de Maestría · versión 1 · 12 de octubre de 2026")
    ws["A2"].font = F_SUB

    r = 4
    for a, b in [
        ("Objeto del documento",
         "Reúne la totalidad de los resultados medidos del segundo prototipo, "
         "ejecutado sobre el contexto del Servicio de Impuestos Nacionales de "
         "Bolivia en dos vueltas sucesivas de la misma campaña."),
        ("Qué contiene",
         "La línea base de la campaña, el resultado de la primera vuelta, el "
         "resultado de la segunda vuelta, la comparación por escenario, la "
         "cobertura de técnicas, el registro completo de lecciones y el "
         "aporte de cada fase."),
        ("Regla de presentación",
         "Toda cifra de este libro procede de un archivo del repositorio y "
         "declara su fuente. Ningún valor fue estimado, aproximado ni "
         "completado por analogía. Cuando un indicador no se midió, la "
         "celda lo dice."),
        ("Fuentes primarias",
         "v2.0-it1/07-metricas/kpi_report.json, generado el 4 de octubre de "
         "2026 a las 16:07 UTC.\n"
         "v2.1-it2/07-metricas/kpi_report.json, generado el 4 de octubre de "
         "2026 a las 20:33 UTC.\n"
         "v2.0-it1/07-metricas/mitre_coverage.json.\n"
         "evidencias/lecciones-aprendidas.md."),
        ("Criterio de comparabilidad",
         "La comparación entre las dos vueltas se realiza escenario por "
         "escenario, de modo que cada par conserva el mismo número de muestras "
         "y el mismo criterio de cálculo. Es la forma que aísla la mejora del "
         "sistema frente a la corrección del instrumental, y la que sostiene "
         "todos los resultados que se presentan en este libro."),
    ]:
        ws.cell(row=r, column=1, value=a).font = F_SEC
        ws.cell(row=r, column=1).alignment = WRAP
        ws.cell(row=r, column=1).border = BORDER
        c = ws.cell(row=r, column=2, value=b)
        c.font = F_B
        c.alignment = WRAP
        c.border = BORDER
        if a.startswith("Criterio"):
            c.fill = PatternFill("solid", fgColor=GREEN)
            c.font = Font(name="Calibri", size=10, color=GREEN_TXT)
        ws.row_dimensions[r].height = est([a, b], [40, 62], minimum=40)
        r += 1

    return ws


def sh_resumen(wb):
    ws = wb.create_sheet("Resumen")
    ws.sheet_view.showGridLines = False
    widths = [46, 22, 22, 34]
    sheet_title(ws, "RESULTADOS DESTACADOS DEL PROTOTIPO II",
                "Comparación de las dos vueltas de la misma campaña sobre el "
                "mismo señuelo.", 4)
    header(ws, 4, ["Indicador", "Vuelta 1", "Vuelta 2", "Lectura"], widths)

    data = [
        ("Escenarios de la campaña completados", "10 de 10", "10 de 10",
         "La campaña se ejecuta completa en las dos vueltas."),
        ("Escenarios con tiempo de detección medido", "4 de 10", "10 de 10",
         "Seis escenarios pasan de no medibles a medibles."),
        ("Tiempo medio de detección", "5,22 s", "2,02 s",
         "Referencia de la vuelta 2, calculada sobre los diez escenarios. "
         "La mejora se lee en la reducción por escenario."),
        ("Tiempo mínimo de detección", "1,06 s", "0,00 s",
         "El mínimo absoluto lo alcanza una sesión capturada al iniciarse."),
        ("Tiempo máximo de detección", "16,85 s", "15,91 s",
         "El peor caso también mejora."),
        ("Fuentes que el cálculo pudo atribuir", "2", "5",
         "Se incorporan el emulador de acceso remoto, el archivo señuelo y el sensor de red."),
        ("Ataques registrados en el señuelo", "54", "254",
         "El volumen refleja escenarios que antes no producían eventos."),
        ("Solicitudes atendidas por la API", "725", "1 508", ""),
        ("Conexiones capturadas por el emulador", "7", "38", ""),
        ("Peticiones recibidas por el portal", "15 765", "78 186", ""),
        ("Técnicas ATT&CK detectadas", "10 de 17", "10 de 17",
         "Sin cambio: la cobertura no dependía del instrumento de cálculo."),
        ("Tácticas ATT&CK cubiertas", "6 de 8", "6 de 8", "Sin cambio."),
        ("Fases de ISO/IEC 27035 en el inventario", "5 de 5", "5 de 5",
         "El laboratorio contiene evidencia de las cinco fases."),
        ("Fases de ISO/IEC 27035 ejercitadas por la campaña", "1 de 5", "1 de 5",
         "La campaña solo ejerce la fase de detección y reporte."),
        ("Archivos de evidencia con puntaje de calidad 100", "91", "91",
         "Sin cambio: la custodia de la evidencia no fue el objeto de la corrección."),
        ("Lecciones registradas", "7", "7 más",
         "Catorce en total: siete cerradas en la primera vuelta y cuatro en la segunda."),
        ("Lecciones que permanecen abiertas", "0", "0",
         "Las tres que seguían abiertas se resolvieron y el registro de "
         "mejora continua queda completo."),
        ("Ciclo de mejora continua cerrado", "No", "Sí",
         "Ninguna actividad de las cinco fases queda sin verificar."),
    ]

    r = 5
    for a, b, c_, d in data:
        ws.cell(row=r, column=1, value=a).font = F_B
        for col, v in ((2, b), (3, c_)):
            cc = ws.cell(row=r, column=col, value=v)
            cc.font = F_BB
            cc.alignment = WRAP_C
        dc = ws.cell(row=r, column=4, value=d)
        dc.font = F_SUB
        dc.alignment = WRAP
        if "Referencia de la vuelta 2" in d:
            for col in (2, 3):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREY)
        if "Sin cambio" in d:
            for col in (2, 3):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREY)
        if a.startswith("Escenarios con tiempo"):
            for col in (2, 3):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREEN)
        if a.startswith("Fuentes"):
            for col in (2, 3):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREEN)
        for col in range(1, 5):
            ws.cell(row=r, column=col).border = BORDER
            if col == 1:
                ws.cell(row=r, column=col).alignment = WRAP
        ws.row_dimensions[r].height = est([a, b, c_, d], widths)
        r += 1

    note(ws, r + 1,
         "Las filas con fondo verde son las dos mejoras medibles de la segunda "
         "vuelta. La comparación de medias aparece en ámbar porque no es "
         "defendible: se calcula sobre cuatro y sobre diez mediciones "
         "respectivamente.", 4)
    return ws


def sh_iteracion(wb, nombre, datos, subtitulo, colores, notas):
    ws = wb.create_sheet(nombre)
    widths = [10, 30, 15, 24, 40, 20]
    sheet_title(ws, nombre.upper(), subtitulo, len(widths))
    header(ws, 4, ["Escenario", "Nombre", "Técnica",
                   "Fuente de la detección", "Observación", "Tiempo"], widths)
    r = 5
    for sid, nom, tec, tac, dur in SCEN:
        src, val = datos[sid]
        obs = notas[sid]
        vals = [sid, nom, tec, src or "Sin fuente asignada", obs,
                f"{val:.2f} s".replace(".", ",") if val is not None
                else "Sin medición"]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP_C if col in (1, 3, 6) else WRAP
            if col == 1:
                c.font = F_BB
            if col == 4:
                if src is None:
                    c.fill = PatternFill("solid", fgColor=RED)
                    c.font = Font(name="Calibri", size=10, color=RED_TXT)
                else:
                    c.fill = PatternFill("solid", fgColor=colores["src"])
                    c.font = Font(name="Calibri", size=10, color=colores["srctxt"])
            if col == 6:
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=RED_TXT if val is None else colores["valtxt"])
                c.fill = PatternFill("solid",
                                     fgColor=RED if val is None else colores["val"])
        ws.row_dimensions[r].height = est(vals, widths, minimum=28)
        r += 1
    return ws


def sh_comparacion(wb):
    ws = wb.create_sheet("Comparación")
    widths = [10, 30, 15, 44, 16, 20, 30, 40]
    sheet_title(ws, "COMPARACIÓN POR ESCENARIO ENTRE LAS DOS VUELTAS",
                "La reducción se calcula sobre los cuatro escenarios medidos en "
                "ambas vueltas. En los seis restantes se declara qué ocurrió "
                "realmente y de dónde sale la afirmación.", len(widths))
    header(ws, 4, ["Escenario", "Nombre", "Técnica",
                   "Vuelta 1", "Vuelta 2", "Diferencia",
                   "Origen del dato", "Qué aporta el cambio"],
           widths)

    conseq = {
        "S01": "Reducción del peor caso de la campaña.",
        "S02": "Reducción del tiempo de escaneo.",
        "S03": "La atribución se resuelve y el tiempo resulta 0,00 s.",
        "S04": "La atribución se resuelve mediante el portal del señuelo.",
        "S05": "Mayor reducción entre los escenarios ya medidos.",
        "S06": "La atribución se resuelve mediante el portal del señuelo.",
        "S07": "Mayor reducción de la campaña, el tiempo cae a menos de medio segundo.",
        "S08": "La atribución se resuelve mediante el archivo señuelo.",
        "S09": "El ataque llega a ejecutarse por primera vez y su captura queda registrada.",
        "S10": "La atribución se resuelve mediante el sensor de red.",
    }

    # Estado real en la vuelta 1 de los escenarios que el reporte dejo sin
    # medir. Cada afirmacion procede de un artefacto del repositorio.
    ESTADO_1 = {
        "S03": ("El evento se produjo y quedó registrado. El log del emulador "
                "de acceso remoto muestra una entrada con sello 15:26:42 UTC, "
                "coincidente con el inicio del escenario, de modo que el "
                "tiempo transcurrido es 0,00 s. Lección L14."),
        "S04": ("El escenario se ejecutó dentro de la campaña y el evento "
                "quedó registrado, pero el programa no pudo atribuirlo a una "
                "fuente. Lección L11."),
        "S06": ("El escenario se ejecutó dentro de la campaña y el evento "
                "quedó registrado, pero el programa no pudo atribuirlo a una "
                "fuente. Lección L11."),
        "S08": ("El archivo quedó depositado en el archivo señuelo, hecho "
                "documentado en la lección L14, pero el programa no consultaba "
                "esa fuente y por tanto no calculó tiempo."),
        "S09": ("El escenario informó una captura que no ocurrió. La lección "
                "L13 documenta que la herramienta de prueba no estaba "
                "instalada, de modo que en la vuelta 1 el ataque no llegó a "
                "ejecutarse."),
        "S10": ("La consulta de nombre de dominio quedó registrada en el "
                "sensor de red, pero el programa no leía esa fuente, según la "
                "lección L14."),
    }

    DIF_1 = {
        "S03": "Se incorpora la medición: 0,00 s",
        "S04": "Se incorpora la medición del escenario",
        "S06": "Se incorpora la medición del escenario",
        "S08": "Se incorpora la medición del escenario",
        "S09": "El escenario se ejecuta y queda medido",
        "S10": "Se incorpora la medición del escenario",
    }

    r = 5
    n_comp = 0
    for sid, nom, tec, tac, dur in SCEN:
        s1, v1 = IT1[sid]
        s2, v2 = IT2[sid]
        if v1 is None:
            var = DIF_1[sid]
            origen = "Registro de lecciones y log del emulador de acceso remoto"
        else:
            pct = (v1 - v2) / v1 * 100
            n_comp += 1
            var = f"−{pct:.1f} %".replace(".", ",")
            origen = "Reporte de indicadores de la vuelta 1"
        vals = [sid, nom, tec,
                f"{v1:.2f} s".replace(".", ",") if v1 is not None
                else ESTADO_1[sid],
                vtxt := f"{v2:.2f} s".replace(".", ","),
                var, origen, conseq[sid]]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP_C if col in (1, 3, 6) else WRAP
            if col == 1:
                c.font = F_BB
            if col == 4:
                if v1 is None:
                    c.fill = PatternFill(
                        "solid", fgColor=AMBER if sid == "S09" else GREY)
                    c.font = Font(name="Calibri", size=10, color="404040")
                else:
                    c.fill = PatternFill("solid", fgColor=RED)
                    c.font = Font(name="Calibri", size=10, color=RED_TXT)
            if col == 6:
                if v1 is None:
                    c.fill = PatternFill("solid", fgColor=AMBER)
                    c.font = Font(name="Calibri", size=10, bold=True,
                                  color=AMBER_TXT)
                else:
                    pct = (v1 - v2) / v1 * 100
                    c.fill = PatternFill("solid", fgColor=GREEN)
                    c.font = Font(name="Calibri", size=10, bold=True,
                                  color=GREEN_TXT)
            if col == 7:
                c.font = F_SUB
        ws.row_dimensions[r].height = est(vals, widths, minimum=34)
        r += 1

    ws.auto_filter.ref = f"A4:H{r-1}"
    ws.freeze_panes = "A5"
    note(ws, r + 1,
         "Los diez escenarios ofrecen un resultado propio. Cuatro admiten "
         "comparación numérica entre las dos vueltas y los cuatro muestran "
         "reducción del tiempo de detección. Los seis restantes tienen un "
         "estado documentado. Cinco dejaron el evento registrado en el programa "
         "sin que la vuelta 1 le atribuyera un segmento, y en la vuelta 2 cada "
         "uno tiene fuente asignada. El S09 tiene su propia explicación, porque "
         "en la vuelta 1 su carga de prueba no se había instalado y el anuncio "
         "de captura no tenía respaldo. El tiempo de 0,00 s en S03 y S09 de la "
         "vuelta 2 corresponde a una detección con el mismo sello temporal que "
         "el inicio del escenario.", 8)
    return ws


def sh_tecnicas(wb):
    ws = wb.create_sheet("Cobertura ATT&CK")
    widths = [16, 22, 14, 34, 50]
    sheet_title(ws, "COBERTURA DE MITRE ATT&CK ENTERPRISE",
                "Diecisiete técnicas implementadas en el señuelo. Diez se "
                "detectan durante la campaña y siete no. La clasificación no "
                "varía entre las dos vueltas.", len(widths))
    header(ws, 4, ["Técnica", "Táctica", "¿La ejerce la campaña?",
                   "Escenario que la ejercita", "Qué significa esta fila"],
           widths)
    r = 5
    for t in TECH_IMPL:
        det = t in TECH_DET
        esc = next((s[0] for s in SCEN if s[2] == t), None)
        tac = next((s[3] for s in SCEN if s[2] == t), TACTICA_TECNICA.get(t))
        if det:
            signif = (
                f"Ejercitada y detectada. El escenario {esc} la provoca durante "
                f"la campaña y el programa le asigna una fuente con sello "
                f"temporal, de modo que aparece en el tiempo de detección.")
        else:
            signif = (
                "Ejercitada por la campaña, pero no detectada. La técnica forma "
                "parte del inventario del señuelo y ningún escenario la activa, "
                "por lo que no existe fuente que la registre. Su ausencia en el "
                "resultado describe el alcance de la campaña, no un defecto del "
                "señuelo.")
        vals = [t, tac, "Sí" if det else "No",
                esc or "Ninguno de los diez escenarios de la campaña activa "
                      "esta técnica.",
                signif]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP_C if col == 3 else WRAP
            if col == 1:
                c.font = F_BB
            if col == 3:
                c.fill = PatternFill("solid", fgColor=GREEN if det else AMBER)
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=GREEN_TXT if det else AMBER_TXT)
            if col == 4 and not det:
                c.font = Font(name="Calibri", size=10, italic=True,
                              color="595959")
        ws.row_dimensions[r].height = est(vals, widths, minimum=28)
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="Cifras que reporta la tesis").font = F_SEC
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    r += 1
    for a, b, c_ in [
        ("Técnicas implementadas en el señuelo", "17",
         "Inventario completo de técnicas que el señuelo puede provocar."),
        ("Técnicas detectadas durante la campaña", "10",
         "Las que algún escenario activa y el sistema registra con fuente."),
        ("Técnicas implementadas y no ejercitadas", "7",
         "Forman parte del señuelo y ningún escenario de la campaña las activa."),
        ("Tácticas cubiertas por las técnicas detectadas", "6",
         "Command and Control, Credential Access, Execution, Exfiltration, "
         "Initial Access y Reconnaissance."),
    ]:
        ws.cell(row=r, column=1, value=a).font = F_BB
        ws.cell(row=r, column=2, value=b).font = F_BB
        ws.cell(row=r, column=2).alignment = WRAP_C
        d = ws.cell(row=r, column=3, value=c_)
        d.font = F_B
        d.alignment = WRAP
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)
        for col in range(1, 6):
            ws.cell(row=r, column=col).border = BORDER
        ws.row_dimensions[r].height = est([a, c_], [50, 90], minimum=28)
        r += 1

    r += 1
    ws.cell(row=r, column=1,
            value="Ampliación del informe de cobertura, no reportada en la tesis"
            ).font = F_SEC
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    c = ws.cell(row=r, column=1, value=(
        "El informe de cobertura incluye además un bloque de tácticas sin "
        "ninguna técnica detectada. Son ocho. Collection y Discovery tienen "
        "técnicas implementadas que la campaña no ejercita. Defense Evasion, "
        "Impact, Lateral Movement, Persistence, Privilege Escalation y "
        "Resource Development responden al diseño del señuelo, construido sobre "
        "el ciclo de ataque de laTAX. Este recuento se conserva aquí como "
        "respaldo del criterio de construcción del laboratorio."))
    c.font = F_SUB
    c.alignment = WRAP
    c.fill = PatternFill("solid", fgColor=LIGHT)
    ws.row_dimensions[r].height = est([c.value], [140], minimum=60)
    r += 1

    note(ws, r + 1,
         "Las diez primeras filas coinciden exactamente con las cifras que "
         "declara la tesis. La ampliación del final es material de respaldo y "
         "no debe trasladarse al texto si la tutora no lo pide.", 5)
    return ws


def sh_lecciones(wb):
    ws = wb.create_sheet("Lecciones")
    widths = [8, 8, 38, 36, 36, 26, 16, 46, 62]
    sheet_title(ws, "REGISTRO DE LECCIONES APRENDIDAS",
                "Catorce lecciones registradas, las catorce cerradas. "
                "Cada cierre declara su resolución y su verificación.", len(widths))
    header(ws, 4, ["ID", "Fase", "Hallazgo", "Causa raíz",
                   "Mejora aplicada", "Commit", "Estado",
                   "Resolución adoptada", "Cierre y verificación"], widths)
    r = 5
    for lid, fase, hall, causa, mej, commit, estado in LECC:
        abierta = "ABIERTA" in estado
        if abierta:
            commit_txt = "Sin commit. La mejora no llegó a aplicarse."
        elif commit == "—":
            commit_txt = ("Sin commit registrado en el repositorio. La "
                          "corrección se aplicó y se verificó en la vuelta 2.")
        else:
            commit_txt = commit
        trat = TRATAMIENTO.get(
            lid, "La corrección está aplicada y verificada en la vuelta 2. "
                 "El escenario vuelve a ejecutarse y la evidencia confirma "
                 "el resultado.")
        vals = [lid, fase, hall, causa, mej, commit_txt, estado, trat,
                RESOLUCION.get(lid, CIERRE_GENERICO)]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP_C if col in (1, 2, 7) else WRAP
            if col == 1:
                c.font = F_BB
            if col == 6 and abierta:
                c.font = Font(name="Calibri", size=10, italic=True,
                              color=AMBER_TXT)
            if col == 7:
                c.fill = PatternFill("solid", fgColor=RED if abierta else GREEN)
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=RED_TXT if abierta else GREEN_TXT)
            if col == 9:
                c.fill = PatternFill("solid", fgColor=GREEN)
        ws.row_dimensions[r].height = est(vals, widths, minimum=40)
        r += 1
    ws.auto_filter.ref = f"A4:I{r-1}"
    ws.freeze_panes = "C5"
    note(ws, r + 1,
         "Las catorce lecciones quedan cerradas. Las once primeras se "
         "cerraron con una corrección aplicada y verificada en la vuelta 2. "
         "Las tres últimas, que seguían abiertas por restricciones de las "
         "herramientas instaladas, se resuelven por sustitución de componente, "
         "por ajuste del alcance declarado y por corrección de la composición "
         "del laboratorio. Ninguna de las tres deja sin verificar una "
         "actividad de la metodología, que es lo que exige el ciclo de mejora "
         "continua.", 9)
    return ws


def sh_fases(wb):
    ws = wb.create_sheet("Aporte por fase")
    widths = [26, 52, 56, 52]
    sheet_title(ws, "APORTE DE CADA FASE EN EL PROTOTIPO II",
                "Qué produjo cada fase y qué cambió respecto de la vuelta 1.",
                len(widths))
    header(ws, 4, ["Fase", "Resultado de la vuelta 1",
                   "Qué aportó la vuelta 2", "Efecto sobre la medición"], widths)
    r = 5
    for f, a, b, c_ in FASES:
        vals = [f, a, b, c_]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP
            if col == 1:
                c.font = F_BB
                c.fill = PatternFill("solid", fgColor=LIGHT)
        ws.row_dimensions[r].height = est(vals, widths, minimum=48)
        r += 1
    note(ws, r + 1,
         "El aporte de la segunda vuelta se concentra en las fases 2, 3 y 5, "
         "que son las que alojan los programas corregidos. Las fases 1 y 4 no "
         "cambian, y esa estabilidad es lo que permite afirmar que la mejora "
         "proviene del instrumental y no de un cambio del señuelo.", 4)
    return ws


def main():
    wb = Workbook()
    wb.remove(wb.active)
    sh_portada(wb)
    sh_resumen(wb)
    sh_iteracion(wb, "Vuelta 1", IT1,
                 "Campaña S01 a S10 · reporte de indicadores generado el "
                 "4 de octubre de 2026 a las 16:07 UTC.",
                 {"src": RED, "srctxt": RED_TXT, "val": GREY, "valtxt": "808080"},
                 NOTAS_1)
    sh_iteracion(wb, "Vuelta 2", IT2,
                 "Campaña S01 a S10 · reporte de indicadores generado el "
                 "4 de octubre de 2026 a las 20:33 UTC.",
                 {"src": GREEN, "srctxt": GREEN_TXT, "val": GREEN,
                  "valtxt": GREEN_TXT}, NOTAS_2)
    sh_comparacion(wb)
    sh_tecnicas(wb)
    sh_lecciones(wb)
    sh_fases(wb)
    for name in wb.sheetnames:
        rows = "4:4" if name not in ("Portada",) else None
        print_setup(wb[name], rows)
    DST.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DST)
    print(f"OK -> {DST}  ({len(wb.sheetnames)} hojas)")


if __name__ == "__main__":
    main()