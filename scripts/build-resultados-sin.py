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
       / "2026-10-12_Resultados_Prototipo_II_SIN_v11.xlsx")

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

F_TITLE = Font(name="Calibri", size=17, bold=True, color=NAVY)
F_SUB = Font(name="Calibri", size=10, italic=True, color="595959")
F_H = Font(name="Calibri", size=10, bold=True, color=WHITE)
F_B = Font(name="Calibri", size=10)
F_BB = Font(name="Calibri", size=10, bold=True)
F_SEC = Font(name="Calibri", size=11, bold=True, color=NAVY)
F_NOTE = Font(name="Calibri", size=9, italic=True, color="404040")

ACCENT = PatternFill("solid", fgColor=NAVY)
BAND = PatternFill("solid", fgColor="EDF2F8")
TAB_PALETA = {
    "Portada": "1F3864", "Resumen": "1F4E79", "Vuelta 1": "2E75B6",
    "Vuelta 2": "1F6032", "Comparación": "9C6500", "Indicadores": "7030A0",
    "Dashboards": "C55A11", "Cobertura ATT&CK": "385723",
    "Lecciones": "833C00", "Aportación por fase": "0F5B8A",
    "Las seis brechas": "1F3864", "El ciclo completo": "2E75B6",
    "Secuencia": "0F5B8A", "Clasificación": "7030A0",
    "Matriz por fases": "1F6032", "Cobertura ISO 27035": "C55A11",
    "Respuestas": "808080",
}


def sum_width(ws, last_col):
    total = 0.0
    for i in range(1, last_col + 1):
        d = ws.column_dimensions.get(get_column_letter(i))
        total += (d.width if d and d.width else 10)
    return total


def est(texts, widths, minimum=22, line=13.2):
    """Altura estimada contando el ajuste de linea real de cada celda."""
    lines = 1
    for t, w in zip(texts, widths):
        if t is None:
            continue
        chars = max(6, int(w * 1.12) - 1)
        n = 0
        for par in str(t).split("\n"):
            words = par.split()
            if not words:
                n += 1
                continue
            cur = 0
            for word in words:
                add = len(word) + (1 if cur else 0)
                if cur + add > chars and cur:
                    n += 1
                    cur = len(word)
                else:
                    cur += add
            n += 1
        lines = max(lines, n)
    return min(180, max(minimum, lines * line + 5))


def print_setup(ws, title_rows=None, tab=None):
    """Margenes comodos, titulo repetido, encabezado con el nombre de la
    hoja y pie con numeracion."""
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_margins.left = 0.4
    ws.page_margins.right = 0.4
    ws.page_margins.top = 0.85
    ws.page_margins.bottom = 0.7
    ws.page_margins.header = 0.35
    ws.page_margins.footer = 0.35
    ws.oddHeader.left.text = ws.title
    ws.oddHeader.left.size = 8
    ws.oddHeader.left.color = "808080"
    ws.oddHeader.right.text = "Metodología Honeypot para la gestión de incidentes"
    ws.oddHeader.right.size = 8
    ws.oddHeader.right.color = "808080"
    ws.oddFooter.left.text = "Tesis de maestría"
    ws.oddFooter.left.size = 8
    ws.oddFooter.left.color = "808080"
    ws.oddFooter.right.text = "Página &P de &N"
    ws.oddFooter.right.size = 8
    ws.oddFooter.right.color = "808080"
    ws.sheet_properties.tabColor = tab or TAB_PALETA.get(ws.title, NAVY)
    if title_rows:
        ws.print_title_rows = title_rows


def sheet_title(ws, title, subtitle, last_col):
    """Barra de acento, titulo y bajada, con aire por encima y por debajo."""
    ws.sheet_view.showGridLines = False
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    for i in range(1, last_col + 1):
        ws.cell(row=1, column=i).fill = ACCENT
    ws.row_dimensions[1].height = 7

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=last_col)
    c = ws.cell(row=2, column=1, value=title)
    c.font = F_TITLE
    c.alignment = Alignment(vertical="center", horizontal="left", indent=1)
    ws.row_dimensions[2].height = 32

    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=last_col)
    s = ws.cell(row=3, column=1, value=subtitle)
    s.font = F_SUB
    s.alignment = Alignment(vertical="center", horizontal="left",
                            wrap_text=True, indent=1)
    ws.row_dimensions[3].height = max(
        17, est([subtitle], [sum_width(ws, last_col) * 0.95], minimum=17,
                line=12))
    ws.row_dimensions[4].height = 8


def header(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = F_H
        c.fill = ACCENT
        c.alignment = Alignment(wrap_text=True, vertical="center",
                                horizontal="left", indent=1)
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = est(headers, widths, minimum=28, line=12.5)


def note(ws, row, text, last_col):
    """Nota al pie, en cursiva y sobre fondo claro."""
    ws.merge_cells(start_row=row, start_column=1, end_row=row,
                   end_column=last_col)
    for i in range(1, last_col + 1):
        ws.cell(row=row, column=i).fill = PatternFill("solid", fgColor=LIGHT)
    c = ws.cell(row=row, column=1, value="Nota. " + text)
    c.font = F_NOTE
    c.alignment = Alignment(wrap_text=True, vertical="top", indent=1)
    ws.row_dimensions[row].height = est(
        [text], [sum_width(ws, last_col) * 0.94], minimum=30, line=12)


def zebra(ws, r, ncols, skip=()):
    """Aplica la banda alterna a las celdas que no llevan color propio."""
    if r % 2 != 0:
        return
    for col in range(1, ncols + 1):
        if col in skip:
            continue
        c = ws.cell(row=r, column=col)
        rgb = getattr(getattr(c.fill, "fgColor", None), "rgb", None)
        if rgb in (None, "00000000"):
            c.fill = BAND


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

# Fuente que el reporte de indicadores asigna a cada escenario. El valor None
# significa que el programa no atribujo el evento a ninguna fuente.
FUENTE_1 = {
    "S01": "Interfaz de servicios del atacante",
    "S02": "Portal del señuelo",
    "S03": None, "S04": None,
    "S05": "Interfaz de servicios del señuelo",
    "S06": None,
    "S07": "Interfaz de servicios del señuelo",
    "S08": None, "S09": None, "S10": None,
}

FUENTE_2 = {
    "S01": "Interfaz de servicios del atacante",
    "S02": "Portal del señuelo",
    "S03": "Emulador de acceso remoto",
    "S04": "Portal del señuelo",
    "S05": "Interfaz de servicios del señuelo",
    "S06": "Portal del señuelo",
    "S07": "Interfaz de servicios del señuelo",
    "S08": "Archivo señuelo",
    "S09": "Emulador de acceso remoto",
    "S10": "Sensor de red",
}

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
    "L1": "La corrección se acepta y el módulo de análisis vuelve a leer las "
          "rutas. El componente de alerta es requisito de toda la cadena, de "
          "modo que ninguna otra fase puede verificarse hasta que esta quede "
          "resuelta.",
    "L2": "La corrección se acepta y el publicador propio queda como "
          "componente permanente de la cadena, en lugar del colector que "
          "fallaba. La indexación pasa a ser una responsabilidad del "
          "laboratorio y no del componente de terceros.",
    "L3": "La corrección se acepta y el colector queda sin función de envío. "
          "La gestión de eventos conserva su función de análisis y pierde la "
          "de entrega, que asume el publicador propio.",
    "L4": "La corrección se acepta y el reinicio de la posición de lectura "
          "pasa a ejecutarse de forma programada. La interrupción del "
          "análisis se vuelve una operación rutinaria y no una recuperación "
          "manual.",
    "L5": "La corrección se acepta y la consulta del panel queda en el "
          "formato que admite la versión del motor. La conversión se aplica "
          "al panel y no al dato, de modo que la evidencia conserva su forma "
          "original.",
    "L6": "La corrección se acepta y el publicador copia el campo de tiempo "
          "con el nombre que el panel consulta. El dato original se conserva "
          "y se añade el campo derivado que la visualización necesita.",
    "L7": "La corrección se acepta y los tres scripts de arranque terminan en "
          "cualquier caso. La restauración de la copia de seguridad se "
          "declara antes de la operación principal, con lo que un fallo "
          "puntual ya no interrumpe el laboratorio.",
    "L8": "La visualización de indicadores queda a cargo del tablero de "
          "métricas, que es el componente que permanece en la composición. "
          "El tablero nativo del proveedor no se despliega.",
    "L9": "La correlación se verifica hasta la generación de la alerta y "
          "hasta la disponibilidad del flujo de orquestación que la enlaza "
          "con la plataforma de gestión. La vista del caso corresponde a la "
          "versión en licencia de prueba de esa plataforma, de modo que la "
          "inspección del caso cerrado queda fuera del conjunto de "
          "verificaciones de esta campaña.",
    "L10": "La composición efectiva del laboratorio se documenta con los tres "
           "segmentos sobre los que corre la verificación de aislamiento. El "
           "segmento declarado sin uso no participa de la ejecución.",
    "L11": "La corrección se acepta y la función de objetivos reconoce las "
           "tres variantes de clave. Los escenarios sin objetivo declaran esa "
           "circunstancia de forma explícita, de modo que la ausencia de "
           "atribución deja de ser un fallo silencioso.",
    "L12": "La corrección se acepta y cada herramienta de ataque recibe un "
           "límite de tiempo. El guion de la campaña deja de depender de que "
           "ninguna invocación se bloquee.",
    "L13": "La corrección se acepta y el escenario comprueba la herramienta "
           "antes de ejecutarse. El cierre del guion informa el resultado "
           "real, de modo que la captura anunciada y la captura ocurrida "
           "coinciden.",
    "L14": "La corrección se acepta y el cálculo incorpora las dos fuentes "
           "que faltaban. El programa consulta el registro del señuelo, el "
           "portal, el emulador de acceso remoto, el archivo señuelo y el "
           "sensor de red.",
}

CIERRE = {
    "L1": "CERRADA. La cadena de alerta reanuda su operación con la "
          "configuración corregida. La verificación consiste en que la "
          "segunda vuelta registra detección con fuente en los diez "
          "escenarios, lo que exige que las alertas se generen, se "
          "indexen y conserven su marca temporal. Evidencia: reporte de "
          "indicadores del 4 de octubre de 2026 a las 20:33 UTC.",
    "L2": "CERRADA. El publicador propio entrega las alertas al índice sin "
          "el parámetro que rechazaba el motor de búsqueda. La verificación "
          "es que el índice contiene los documentos y que el tablero de la "
          "Figura 52 los presenta con su nivel de severidad. Evidencia: "
          "captura del tablero de la segunda vuelta.",
    "L3": "CERRADA. El laboratorio permanece en pie durante toda la "
          "campaña de la segunda vuelta. La verificación es que la campaña "
          "recorre los diez escenarios sin detenerse, que es el recuento de "
          "la Figura 55. Evidencia: registro de escenarios completados.",
    "L4": "CERRADA. La generación de alertas se mantiene durante toda la "
          "campaña. La verificación es doble, porque el tablero presenta "
          "alertas de las últimas veinticuatro horas y la campaña completa "
          "los diez escenarios. Evidencia: Figuras 52 y 55.",
    "L5": "CERRADA. El tablero deja de mostrar ausencia de datos y "
          "presenta el volumen de alertas registradas. La verificación es la "
          "captura de la Figura 52, que muestra distribución por severidad "
          "sobre datos reales de la campaña.",
    "L6": "CERRADA. Los tableros devuelven los eventos con su nivel de "
          "severidad después de que el publicador copiara el campo de tiempo "
          "con el nombre que el panel consulta. La verificación es la misma "
          "captura del tablero, que ya no devuelve cero documentos. "
          "Evidencia: Figura 52.",
    "L7": "CERRADA. Una interrupción puntual de un script de arranque ya no "
          "detiene el laboratorio. La verificación es que los tres scripts "
          "terminan correctamente y la campaña alcanza el décimo "
          "escenario. Evidencia: Figura 55.",
    "L8": "CERRADA. La visualización de indicadores queda cubierta por el "
          "tablero de métricas, que es el componente que permanece en la "
          "composición y que operó durante la campaña completa de diez "
          "escenarios. Verificado en la segunda vuelta mediante la captura "
          "del tablero y el reporte de indicadores de las 20:33 UTC.",
    "L9": "CERRADA CON RESERVA EXPRESA. La correlación se verifica hasta la "
          "generación de la alerta, que conserva su técnica de MITRE ATT&CK "
          "y su nivel de clasificación, y hasta la disponibilidad del flujo "
          "de orquestación que la enlaza con la plataforma de gestión. La "
          "versión instalada de la plataforma de incidentes se encuentra en "
          "estado de licencia en prueba y redirige toda ruta a su módulo de "
          "organizaciones, de modo que la vista del caso no pudo "
          "inspeccionarse. En consecuencia, el tiempo de contención y el "
          "tiempo de respuesta a la resolución permanecen sin medir, tal "
          "como registran los campos MTTR, MTTC y MTTContain del reporte de "
          "indicadores. La resolución adoptada es declarar la verificación "
          "hasta la alerta y consignar la reserva.",
    "L10": "CERRADA. La verificación de aislamiento se practica sobre los "
           "tres segmentos en los que el laboratorio se ejecuta en la "
           "práctica. El segmento declarado para los sensores de red no "
           "participa de la ejecución porque los sensores operan en modo "
           "anfitrión, y queda documentado como tal. Verificado mediante el "
           "registro de redes y la prueba de aislamiento ejecutada desde el "
           "contenedor atacante.",
    "L11": "CERRADA. La función de objetivos acepta las tres variantes de "
           "clave y los escenarios sin objetivo la declaran de forma "
           "explícita. La verificación es que el tiempo de detección se "
           "registra en los diez escenarios y no en cuatro. Evidencia: "
           "reporte de indicadores de la segunda vuelta.",
    "L12": "CERRADA. El límite de tiempo evita que una herramienta bloquee "
           "el guion. La verificación es que la campaña alcanza el décimo "
           "escenario. Evidencia: Figura 55.",
    "L13": "CERRADA. El escenario comprueba la herramienta al inicio y el "
           "cierre distingue la ejecución completa de la parcial. La "
           "verificación es que el noveno escenario registra tiempo de "
           "detección, atribuido al emulador de acceso remoto. Evidencia: "
           "detalle por escenario de la segunda vuelta.",
    "L14": "CERRADA. El cálculo consulta además el archivo señuelo y el "
           "sensor de red. La verificación es que el octavo y el décimo "
           "escenario registran tiempo de detección, con 0,56 y 0,65 "
           "segundos. Evidencia: detalle por escenario de la segunda vuelta.",
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
     "Seis escenarios que antes no podían medirse ahora son medibles y "
     "tienen fuente identificada."),
    ("Fase 4 · Correlación con gestión de incidentes",
     "Alerta estructurada con su técnica y su severidad en el momento de la "
     "captura, flujo de orquestación configurado y alta en la plataforma de "
     "inteligencia.",
     "La correlación queda verificada hasta la generación de la alerta. La "
     "inspección del caso cerrado corresponde a la versión en licencia de "
     "prueba de la plataforma de incidentes, que redirige toda ruta a su "
     "módulo de organizaciones.",
     "La correlación se comprueba en el punto en que el evento se convierte "
     "en alerta clasificada. El tiempo de respuesta y el de contención "
     "permanecen sin medir, y así lo registran los campos MTTR, MTTC y "
     "MTTContain del reporte de indicadores."),
    ("Fase 5 · Medición y lecciones aprendidas",
     "Reporte de indicadores, reporte de cobertura de técnicas y reporte de "
     "correspondencia normativa.",
     "Catorce lecciones registradas y las catorce cerradas con su resolución "
     "documentada, y un ciclo de mejora que corrigió el instrumental de "
     "medición.",
     "El ciclo de mejora funciona: cada lección registrada produjo una "
     "corrección verificable o una reserva declarada."),
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
    widths = [40, 13, 13, 58]
    sheet_title(ws, "RESULTADOS DESTACADOS DEL PROTOTIPO II",
                "Comparación de las dos vueltas de la misma campaña sobre el "
                "mismo señuelo.", 4)
    header(ws, 5, ["Indicador", "Vuelta 1", "Vuelta 2", "Lectura"], widths)

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
        ("Fuentes de registro que el cálculo pudo atribuir", "3", "6",
         "Componentes distintos con sello temporal. En la vuelta 1 "
         "atribuyen la interfaz de servicios del atacante, la interfaz de "
         "servicios del señuelo y el portal del señuelo. En la vuelta 2 se "
         "suman el emulador de acceso remoto, el archivo señuelo y el sensor "
         "de red."),
        ("Ataques registrados en el señuelo", "54", "254",
         "El volumen refleja escenarios que antes no producían eventos."),
        ("Solicitudes atendidas por la API", "725", "1 508", ""),
        ("Conexiones capturadas por el emulador", "7", "38", ""),
        ("Peticiones recibidas por el portal", "15 765", "78 186", ""),
        ("Técnicas ATT&CK con fuente de detección", "4 de 10", "10 de 10",
         "Mejora principal de la segunda vuelta. En la vuelta 1 solo "
         "atribuyen detección las técnicas de S01, S02, S05 y S07."),
        ("Tácticas ATT&CK con fuente de detección", "3 de 6", "6 de 6",
         "Reconocimiento, Acceso a credenciales y Acceso inicial en la vuelta "
         "1; las seis en la vuelta 2."),
        ("Técnicas ATT&CK del inventario del señuelo", "17 de 17",
         "17 de 17", "Sin cambio: el señuelo expone el mismo inventario en "
         "las dos vueltas."),
        ("Tácticas ATT&CK del inventario del señuelo", "8 de 8", "8 de 8",
         "Sin cambio, por la misma razón."),
        ("Fases de ISO/IEC 27035 en el inventario", "5 de 5", "5 de 5",
         "El laboratorio contiene evidencia de las cinco fases."),
        ("Fases de ISO/IEC 27035 ejercitadas por la campaña", "1 de 5", "1 de 5",
         "La campaña solo ejerce la fase de detección y reporte."),
        ("Archivos de evidencia con puntaje de calidad 100", "91", "91",
         "Sin cambio: la custodia de la evidencia no fue el objeto de la corrección."),
        ("Lecciones registradas", "7", "7 más",
         "Catorce en total: siete cerradas en la primera vuelta y cuatro en la segunda."),
        ("Lecciones que permanecen abiertas", "0", "0",
         "El registro de la primera vuelta cierra sus siete lecciones. Las "
         "tres que exigieron decisión documentada se resolvieron por escrito "
         "y el ciclo queda completo con catorce cierres."),
        ("Ciclo de mejora continua cerrado", "No", "Sí",
         "Las catorce lecciones tienen cierre. Una de ellas, la L9, lo hace "
         "con reserva expresa, porque la inspección del caso cerrado "
         "corresponde a la versión en licencia de prueba de la plataforma."),
    ]

    r = 6
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
        if "con fuente de dete" in a or "con fuente de detec" in a:
            for col in (2, 3):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREEN)
        for col in range(1, 5):
            ws.cell(row=r, column=col).border = BORDER
            if col == 1:
                ws.cell(row=r, column=col).alignment = WRAP
        ws.row_dimensions[r].height = est([a, b, c_, d], widths)
        r += 1

    note(ws, r + 1,
         "Las cuatro filas con fondo verde son las mejoras medibles de la "
         "segunda vuelta: escenarios con medición, fuentes de registro, "
         "técnicas con fuente de detección y tácticas con fuente de "
         "detección. La comparación de medias aparece en gris porque no es "
         "defendible, dado que se calcula sobre cuatro y sobre diez "
         "mediciones respectivamente. Las filas marcadas como sin cambio "
         "declaran constantes que sirven de contraste.", 4)
    return ws


def sh_iteracion(wb, nombre, datos, subtitulo, colores, notas):
    ws = wb.create_sheet(nombre)
    widths = [10, 30, 15, 24, 40, 20]
    sheet_title(ws, nombre.upper(), subtitulo, len(widths))
    header(ws, 5, ["Escenario", "Nombre", "Técnica",
                   "Fuente de la detección", "Observación", "Tiempo"], widths)
    r = 6
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
    header(ws, 5, ["Escenario", "Nombre", "Técnica",
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

    r = 6
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

    ws.auto_filter.ref = f"A5:H{r-1}"
    ws.freeze_panes = "A6"
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
    widths = [15, 20, 13, 11, 26, 26, 44]
    sheet_title(ws, "COBERTURA DE MITRE ATT&CK ENTERPRISE",
                "El inventario del señuelo comprende diecisiete técnicas. Diez "
                "las activa algún escenario de la campaña y siete no. La "
                "tabla muestra, para cada técnica, la fuente que el reporte "
                "de indicadores le atribuyó en cada vuelta, de modo que se "
                "aprecie qué cambió y qué no.", len(widths))
    header(ws, 5, ["Técnica", "Táctica", "¿La ejerce la campaña?",
                   "Escenario", "Fuente en la vuelta 1",
                   "Fuente en la vuelta 2", "Qué significa esta fila"],
           widths)
    r = 6
    for t in TECH_IMPL:
        det = t in TECH_DET
        s = next((x for x in SCEN if x[2] == t), None)
        esc, f1, f2 = (s[0], FUENTE_1.get(s[0]), FUENTE_2.get(s[0])) if s \
            else (None, None, None)
        if det:
            signif = (
                "Ejercitada y atribuida. El escenario la provoca durante la "
                "campaña y el reporte le asigna una fuente con sello "
                "temporal, de modo que aparece en el tiempo de detección."
                + ("" if f1 else
                   " La vuelta 1 no le asignó fuente y la vuelta 2 sí, lo "
                   "que explica la ampliación de la cobertura de medición."))
        else:
            signif = (
                "No ejercitada. La técnica forma parte del inventario del "
                "señuelo y ninguno de los diez escenarios la activa, de modo "
                "que no existe fuente que la registre y no aparece en el "
                "tiempo de detección. Su ausencia describe el alcance de la "
                "campaña y no un defecto del señuelo.")
        vals = [t, s[3] if s else TACTICA_TECNICA.get(t, ""),
                "Sí" if det else "No", esc or "Ninguno",
                f1 or "Sin atribución", f2 or "Sin atribución", signif]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = F_B
            c.border = BORDER
            c.alignment = WRAP_C if col in (3, 4) else WRAP
            if col == 1:
                c.font = F_BB
            if col == 3:
                c.fill = PatternFill("solid", fgColor=GREEN if det else AMBER)
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=GREEN_TXT if det else AMBER_TXT)
            if col in (5, 6):
                c.fill = PatternFill(
                    "solid", fgColor=GREEN if v != "Sin atribución" else LIGHT)
                if v == "Sin atribución":
                    c.font = Font(name="Calibri", size=10, italic=True,
                                  color="595959")
        ws.row_dimensions[r].height = est(vals, widths, minimum=28)
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="Cifras del inventario y de la atribución"
            ).font = F_SEC
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    r += 1
    for a, b, c_ in [
        ("Técnicas del inventario del señuelo", "17",
         "Inventario completo de técnicas que el señuelo puede provocar. "
         "No cambia entre las dos vueltas."),
        ("Técnicas que activa algún escenario de la campaña", "10",
         "Las que la Tabla 6 asocia a un escenario. Tampoco cambia entre "
         "vueltas, porque el conjunto de escenarios es el mismo."),
        ("Técnicas del inventario que ningún escenario activa", "7",
         "Forman parte del señuelo y ninguna de las diez campañas las "
         "ejercita."),
        ("Técnicas con fuente de detección en la vuelta 1", "4 de 10",
         "T1595, T1595.002, T1110.004 y T1078. Las otras seis quedaron "
         "registradas sin atribución."),
        ("Técnicas con fuente de detección en la vuelta 2", "10 de 10",
         "Las diez. La ampliación proviene de las lecciones L11, L13 y L14, "
         "que repararon el instrumental de atribución."),
        ("Tácticas con fuente de detección en la vuelta 1", "3 de 6",
         "Reconnaissance, Credential Access e Initial Access."),
        ("Tácticas con fuente de detección en la vuelta 2", "6 de 6",
         "Las seis tácticas de la campaña. Command and Control y Execution "
         "aparecen con la reparación del instrumental."),
    ]:
        ws.cell(row=r, column=1, value=a).font = F_BB
        ws.cell(row=r, column=2, value=b).font = F_BB
        ws.cell(row=r, column=2).alignment = WRAP_C
        d = ws.cell(row=r, column=3, value=c_)
        d.font = F_B
        d.alignment = WRAP
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
        for col in range(1, 8):
            ws.cell(row=r, column=col).border = BORDER
        ws.row_dimensions[r].height = est([a, c_], [50, 90], minimum=28)
        r += 1

    r += 1
    ws.cell(row=r, column=1,
            value="Ampliación del informe de cobertura, no reportada en la tesis"
            ).font = F_SEC
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
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
    header(ws, 5, ["ID", "Fase", "Hallazgo", "Causa raíz",
                   "Mejora aplicada", "Commit", "Estado",
                   "Resolución adoptada", "Cierre y verificación"], widths)
    r = 6
    for lid, fase, hall, causa, mej, commit, estado in LECC:
        abierta = "ABIERTA" in estado
        if abierta:
            commit_txt = "Sin commit. La mejora no llegó a aplicarse."
        elif commit == "—":
            commit_txt = ("Sin commit registrado en el repositorio. La "
                          "corrección se aplicó y se verificó en la vuelta 2.")
        else:
            commit_txt = commit
        trat = TRATAMIENTO[lid]
        vals = [lid, fase, hall, causa, mej, commit_txt, estado, trat,
                CIERRE[lid]]
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
    ws.auto_filter.ref = f"A5:I{r-1}"
    ws.freeze_panes = "C6"
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
    header(ws, 5, ["Fase", "Resultado de la vuelta 1",
                   "Qué aportó la vuelta 2", "Efecto sobre la medición"], widths)
    r = 6
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


DASHBOARDS = [
    ("Tablero de métricas sobre el índice",
     "Prototipo II, vuelta 1",
     "Figura 52, apartado 4.3.6.6.3",
     "Volumen de alertas, distribución por severidad y detalle del sensor "
     "de red",
     "Índice de la plataforma de gestión, alimentado por el publicador "
     "propio de la lección L2",
     "Que la cadena de captura, indexación y visualización operó en la "
     "primera vuelta",
     "Que la visualización se reparó tras las lecciones L5 y L6",
     "La ventana de consulta corresponde a la segunda vuelta. Para sostener "
     "una comparación visual con la vuelta 1 hace falta capturar ese tablero "
     "con la misma ventana, y la captura existe en el repositorio pero no "
     "está incorporada al documento."),
    ("Captura del tablero de la vuelta 1",
     "Prototipo II, vuelta 1",
     "No incorporada al documento",
     "Lo que muestra el archivo de la vuelta 1",
     "Índice de la plataforma de gestión",
     "Que el laboratorio de la primera vuelta produjo y conservó alertas",
     "Nada todavía, porque la figura no está en el texto",
     "Incorporarla al apartado 4.4 con su nota al pie. El archivo existe en "
     "evidencias/v2.0-it1/04-captura-eventos/."),
    ("Pantalla de acceso de la herramienta de métricas",
     "Prototipo I",
     "Figura del apartado 4.3.5.2",
     "Disponibilidad del componente, sin datos",
     "Ninguna, es una pantalla de acceso",
     "Que el componente se despliega en el segmento de operaciones",
     "Nada, porque no presenta indicadores",
     "No sirve como evidencia de resultado. Se conserva como evidencia de "
     "despliegue."),
    ("Consolas de las plataformas de gestión",
     "Prototipo II, ambas vueltas",
     "No incorporadas al documento",
     "Disponibilidad de la interfaz de cada plataforma",
     "Las cinco plataformas que integran el laboratorio",
     "Que las cinco plataformas están desplegadas y accesibles",
     "Nada sobre el resultado de la correlación",
     "Sirven como evidencia de la Fase 2. Cinco capturas en "
     "evidencias/consolas/."),
]

INDICADOR_CLASE = [
    ("Tiempo medio de detección", "Medible y medido",
     "Intervalo entre el inicio del escenario y el primer evento que lo "
     "registra", "Segundos",
     "kpi_report.json, campo MTTD",
     "5,216 s con cuatro muestras y 2,022 s con diez muestras",
     "No comparable entre vueltas, porque cambia el número de muestras. "
     "La comparación válida es escenario por escenario.",
     "Ninguna en el valor. La restricción es la cobertura de las muestras."),
    ("Tiempo medio de respuesta", "Declarado, no medido",
     "Intervalo entre la generación del incidente y su resolución",
     "Segundos", "kpi_report.json, campo MTTR",
     "Sin valor. El campo aparece en null con samples igual a cero y estado "
     "no_medido",
     "No comparable, porque no existe valor en ninguna vuelta",
     "Requiere las marcas temporales de los casos en la plataforma de "
     "gestión, que la versión en licencia de prueba no expone."),
    ("Tiempo medio de triaje", "Declarado, no medido",
     "Intervalo entre la captura y la clasificación del evento",
     "Segundos", "kpi_report.json, campo MTTC",
     "Sin valor. El campo aparece en null con samples igual a cero",
     "No comparable, porque no existe valor en ninguna vuelta",
     "Comparte la limitación del tiempo de respuesta."),
    ("Tiempo de contención", "Declarado, no medido",
     "Intervalo entre la generación del incidente y su contención",
     "Segundos", "kpi_report.json, campo MTTContain",
     "Sin valor. El campo aparece en null con samples igual a cero",
     "No comparable, porque no existe valor en ninguna vuelta",
     "Comparte la limitación del tiempo de respuesta."),
    ("Cobertura de medición", "Medible y medido",
     "Proporción de escenarios con tiempo de detección registrado",
     "Porcentaje", "kpi_report.json, campo MTTD.samples",
     "Cuatro de diez escenarios y diez de diez escenarios",
     "Comparable, porque la campaña ejecuta los mismos diez escenarios en "
     "las dos vueltas",
     "Mide la capacidad del instrumental de atribución, no la velocidad de "
     "la detección."),
    ("Fuentes de registro atribuidas", "Medible y medido",
     "Componentes distintos a los que el programa asoció un sello temporal",
     "Cantidad", "kpi_report.json, campo MTTD.details",
     "Tres componentes y seis componentes",
     "Comparable, porque el criterio de atribución es el mismo",
     "El conteo depende de qué se considere componente distinto. Aquí se "
     "cuenta la interfaz de servicios del atacante como componente separado "
     "de la del señuelo."),
    ("Cobertura de técnicas con fuente de detección", "Medible y medido",
     "Técnicas del marco de comportamiento adversario que algún escenario "
     "activa y a las que el reporte asigna fuente",
     "Cantidad sobre el total de la campaña",
     "kpi_report.json, campo MTTD.details",
     "Cuatro de diez técnicas y diez de diez técnicas",
     "Comparable, porque el conjunto de escenarios es el mismo",
     "No debe confundirse con el inventario del señuelo, que comprende "
     "diecisiete técnicas y no varía."),
    ("Cobertura de tácticas con fuente de detección", "Medible y medido",
     "Tácticas del marco que cuentan con al menos una técnica atribuida",
     "Cantidad sobre el total de la campaña",
     "kpi_report.json, campo MTTD.details",
     "Tres de seis tácticas y seis de seis tácticas",
     "Comparable, porque el conjunto de escenarios es el mismo",
     "La campaña cubre seis tácticas de las ocho que declara el inventario."),
    ("Falsos positivos", "Declarado, no calculado",
     "Alertas que describen actividad sin ataque real, sobre el total de "
     "alertas", "Porcentaje", "Sin fuente",
     "Sin valor. La campaña no definió una definición operativa de falso "
     "positivo ni llevó un registro de clasificación manual de alertas",
     "No comparable, porque no existe valor en ninguna vuelta",
     "No puede afirmarse que el valor sea cero. El señuelo responde a "
     "actividad automatizada, pero eso no sustituye a la verificación "
     "operativa de cada alerta."),
    ("Integridad de la evidencia", "Medible y medido",
     "Archivos de evidencia con huella criptográfica y puntaje de calidad",
     "Cantidad y escala de cero a cien",
     "kpi_report.json, campo evidence",
     "Noventa y un archivos con calidad cien en las dos vueltas",
     "Comparable, y además constante entre vueltas",
     "El puntaje lo asigna el propio laboratorio, de modo que es una "
     "medición interna y no una verificación externa."),
    ("Fases de ISO/IEC 27035 inventariadas", "Medible y medido",
     "Fases del estándar que el laboratorio declara en su composición",
     "Cantidad sobre cinco",
     "iso27035_compliance.json, campo phases_implemented",
     "Cinco de cinco en el inventario del laboratorio",
     "No comparable entre vueltas, porque el inventario no cambia",
     "Describe el diseño declarado del laboratorio, no lo ejecutado."),
    ("Fases de ISO/IEC 27035 ejercitadas", "Medible y medido",
     "Fases del estándar a las que la campaña asigna al menos un escenario",
     "Cantidad sobre cinco",
     "kpi_report.json, campo coverage.iso_27035.phases_covered",
     "Una de cinco, con veinte por ciento de cobertura",
     "Constante entre vueltas",
     "El mapeo de escenarios a fases envía los diez escenarios a la fase de "
     "detección y reporte. Las demás fases del estándar no las ejerce esta "
     "campaña."),
    ("Controles de ISO/IEC 27001 mapeados", "Declarado, no medido",
     "Controles del anexo A con correspondencia declarada en el laboratorio",
     "Cantidad sobre siete",
     "kpi_report.json, campo coverage.iso_27001",
     "Siete de siete con correspondencia textual",
     "Constante entre vueltas",
     "El campo contiene una descripción de la implementación, no una "
     "medición. Declarar la correspondencia no equivale a verificar el "
     "control en operación."),
]


def sh_indicadores(wb):
    ws = wb.create_sheet("Indicadores")
    widths = [30, 18, 40, 12, 30, 40, 40, 42]
    sheet_title(ws, "INDICADORES, DEFINICIÓN Y ESTADO DE MEDICIÓN",
                "Trece indicadores con su definición, su fuente y su estado. "
                "Se separan los que se midieron de los que solo se "
                "declararon, porque un valor declarado no es un resultado.",
                len(widths))
    header(ws, 5, ["Indicador", "Estado", "Definición", "Unidad",
                   "Fuente", "Valores disponibles", "Comparabilidad",
                   "Limitaciones de la medición"], widths)
    r = 6
    for v in INDICADOR_CLASE:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (1, 3, 6, 7, 8) else F_B
            c.alignment = WRAP if i in (1, 3, 6, 7, 8) else WRAP_C
            if i == 2:
                medido = val == "Medible y medido"
                c.fill = PatternFill("solid", fgColor=GREEN if medido
                                     else AMBER)
                c.font = Font(name="Calibri", size=10, bold=True,
                              color=GREEN_TXT if medido else AMBER_TXT)
        ws.row_dimensions[r].height = est(list(v), widths, minimum=44)
        r += 1
    ws.auto_filter.ref = f"A5:H{r-1}"
    ws.freeze_panes = "A6"
    note(ws, r + 1,
         "Ninguno de los indicadores de tiempo de respuesta presenta valor, "
         "porque la campaña no registró las marcas temporales de los casos. "
         "El hecho de que el señuelo responda a actividad automatizada no "
         "permite afirmar que el porcentaje de falsos positivos sea cero.",
         8)
    return ws


def sh_dashboards(wb):
    ws = wb.create_sheet("Dashboards")
    widths = [34, 22, 30, 34, 30, 34, 34, 44]
    sheet_title(ws, "INVENTARIO DE TABLEROS Y CAPTURAS DE INTERFAZ",
                "Qué tablero existe, de qué vuelta es, qué muestra y qué "
                "puede sostener como evidencia. Se distingue el tablero que "
                "presenta resultados del que solo acredita despliegue.",
                len(widths))
    header(ws, 5, ["Tablero o captura", "Prototipo", "Ubicación en el texto",
                   "Qué presenta", "Fuente de los datos",
                   "Qué permite observar", "Qué interpretación respalda",
                   "Qué le falta para ser evidencia de mejora"], widths)
    r = 6
    for v in DASHBOARDS:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (1, 4, 6, 7, 8) else F_B
            c.alignment = WRAP
        ws.row_dimensions[r].height = est(list(v), widths, minimum=52)
        r += 1
    ws.auto_filter.ref = f"A5:H{r-1}"
    ws.freeze_panes = "A6"
    note(ws, r + 1,
         "Un solo tablero presenta resultados y pertenece a la segunda "
         "vuelta. La captura de la primera vuelta existe en el repositorio "
         "y todavía no está incorporada al documento, de modo que la "
         "comparación visual entre las dos vueltas queda pendiente.",
         8)
    return ws


def pulir(ws, desde=6):
    """Bandeado alterno y borde inferior de cierre en las hojas con tabla."""
    if ws.title == "Portada":
        return
    ncols = ws.max_column
    for r in range(desde, ws.max_row + 1):
        fila_vacia = all(ws.cell(row=r, column=c).value in (None, "")
                         for c in range(1, ncols + 1))
        if fila_vacia:
            continue
        zebra(ws, r, ncols)
    # Cierre visual de la tabla en la ultima fila con contenido.
    for r in range(ws.max_row, desde - 1, -1):
        if any(ws.cell(row=r, column=c).value not in (None, "")
               for c in range(1, ncols + 1)):
            for c in range(1, ncols + 1):
                cell = ws.cell(row=r, column=c)
                cell.border = Border(
                    left=cell.border.left, right=cell.border.right,
                    top=cell.border.top,
                    bottom=Side(style="medium", color=NAVY))
            break


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
    sh_indicadores(wb)
    sh_dashboards(wb)
    sh_lecciones(wb)
    sh_fases(wb)
    for name in wb.sheetnames:
        rows = "5:5" if name not in ("Portada",) else None
        print_setup(wb[name], rows)
        pulir(wb[name])
    DST.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DST)
    print(f"OK -> {DST}  ({len(wb.sheetnames)} hojas)")


if __name__ == "__main__":
    main()