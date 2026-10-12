# -*- coding: utf-8 -*-
"""Compara el estado de partida de la institución con el estado que deja el
Prototipo II. El libro responde las cinco preguntas de la tutora y no contiene
ninguna celda vacía: cada dato declara su archivo de origen."""
import importlib.util
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import PatternFill

BASE = Path(r"F:\Maestria\tesis\taxfisco-research-lab")
spec = importlib.util.spec_from_file_location(
    "sin", BASE / "scripts" / "build-resultados-sin.py")
sin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sin)

DST = (BASE / "instrumentos"
       / "2026-10-12_Comparacion_Antes_Despues_v01.xlsx")

LIGHT = sin.LIGHT
F_TITLE, F_SUB, F_H, F_B, F_BB, F_SEC = (sin.F_TITLE, sin.F_SUB, sin.F_H,
                                         sin.F_B, sin.F_BB, sin.F_SEC)

# ---------------------------------------------------------------- datos

BRECHAS = [
    (1, "Detección y registro de eventos", "48,54 %", "Básico",
     "El tiempo medio de detección pasa de 5,216 s medidos en cuatro de los "
     "diez escenarios a 2,022 s medidos en los diez. La fuente de detección "
     "pasa de dos segmentos a cinco, de modo que cada escenario tiene una vía "
     "propia de registro.",
     "v2.0-it1/07-metricas/kpi_report.json y "
     "v2.1-it2/07-metricas/kpi_report.json",
     "Fase 3"),
    (4, "Lecciones aprendidas y mejora", "49,17 %", "Básico",
     "El ciclo de mejora continua pasa de un registro informal a catorce "
     "lecciones documentadas con causa raíz, mejora aplicada y archivo de "
     "verificación. Las catorce quedan cerradas.",
     "evidencias/lecciones-aprendidas.md",
     "Fase 5"),
    (7, "Retención y acceso a evidencias", "47,92 %", "Básico",
     "La retención pasa de no registrada a noventa y un archivos con huella "
     "SHA-256 y puntaje de calidad cien sobre cien, con índice navegable en "
     "evidencias/INDICE.md.",
     "evidencias/INDICE.md y cálculo de huellas del cierre de campaña",
     "Fase 3"),
    (8, "Accesos y mínimos privilegios", "49,72 %", "Básico",
     "La separación de entornos se verifica ejecutando la prueba desde el "
     "contenedor atacante. El atacante alcanza dos objetivos del segmento "
     "expuesto y ninguno del segmento de análisis ni del de gestión.",
     "Registro de redes de la campaña y prueba de aislamiento ejecutada desde "
     "el contenedor atacante",
     "Fase 2"),
    (10, "Gestión de vulnerabilidades", "50,56 %", "Básico",
     "El catálogo de técnicas pasa de referenciado a implementado y probado. "
     "Diecisiete técnicas de MITRE ATT&CK se ejecutan en el señuelo, diez "
     "producen detección y seis tácticas quedan cubiertas.",
     "v2.0-it1/07-metricas/mitre_coverage.json",
     "Fases 1 y 3"),
    (13, "Capacitación y cobertura", "47,78 %", "Básico",
     "El laboratorio entrega el material de demostración, con dos vueltas de "
     "campaña sobre diez escenarios, su tablero de métricas y su registro de "
     "lecciones, listos para la formación del personal.",
     "evidencias/consolas/ y evidencias/INDICE.md",
     "Medición posterior en la institución"),
]

INDICADORES = [
    ("Escenarios con tiempo de detección medido", "4 de 10", "10 de 10",
     "Cobertura de medición",
     "La medición deja de depender de que un componente concreto se active y "
     "pasa a registrar los diez escenarios.",
     "kpi_report.json de it1 e it2"),
    ("Segmentos que aportan una fuente de detección", "2", "5",
     "Fuentes de detección",
     "Cowrie, el portal falso, OpenCanary, Zeek y TheHive detectan de manera "
     "independiente.",
     "kpi_report.json de it2"),
    ("Tiempo medio de detección del Prototipo II",
     "5,216 s sobre cuatro escenarios", "2,022 s sobre diez escenarios",
     "Comparación válida escenario por escenario",
     "Las medias no son comparables entre vueltas porque cambia el número de "
     "muestras. La comparación válida se hace en los cuatro escenarios que "
     "miden en ambas vueltas.",
     "kpi_report.json de it1 e it2"),
    ("Tiempo de detección del escenario S01", "16,851 s", "15,91 s",
     "Reducción de 5,6 %", "Ataque de API contra el atacante.", "kpi_report.json"),
    ("Tiempo de detección del escenario S02", "1,214 s", "1,095 s",
     "Reducción de 9,8 %", "Ataque al portal falso.", "kpi_report.json"),
    ("Tiempo de detección del escenario S05", "1,734 s", "1,145 s",
     "Reducción de 34,0 %", "Ataque de API contra el atacante.", "kpi_report.json"),
    ("Tiempo de detección del escenario S07", "1,063 s", "0,264 s",
     "Reducción de 75,2 %", "Ataque de API contra el atacante.", "kpi_report.json"),
    ("Lecciones abiertas del ciclo de mejora",
     "Tres al cierre de la primera vuelta", "Cero", "Ciclo cerrado",
     "Las tres se resolvieron con respuesta documentada y sin exigir cambio "
     "de código.",
     "evidencias/lecciones-aprendidas.md"),
    ("Archivos de evidencia con huella y calidad",
     "Noventa y un archivos, calidad 100/100",
     "Noventa y un archivos, calidad 100/100",
     "Constante entre vueltas",
     "La retención se mantuvo estable durante la corrección del instrumental.",
     "evidencias/INDICE.md"),
    ("Técnicas de MITRE ATT&CK detectadas",
     "Diez de diecisiete en seis tácticas", "Diez de diecisiete en seis tácticas",
     "Constante entre vueltas",
     "La cobertura del señuelo no cambió. La mejora está en el instrumental "
     "que la observa y no en el señuelo.",
     "mitre_coverage.json"),
    ("Madurez global de la institución", "52,70 % en nivel Gestionado",
     "Medición posterior con el instrumento v07",
     "Corresponde a la institución",
     "El instrumento de medición posterior está listo y el contraste con la "
     "evidencia del laboratorio está en su anexo.",
     "instrumentos/2026-10-12_Instrumento_Diagnostico_"
     "MEDICION_POSTERIOR_v07.docx"),
]

SECUENCIA = [
    ("Diagnóstico de 2026", "Estado de partida de la institución",
     "52,70 % de madurez global en nivel Gestionado, con seis subdimensiones "
     "en nivel Básico y alfa de Cronbach de 0,869 sobre treinta participantes.",
     "2026-06-25_Calculo_Alfa_Cronbach_Encuesta_v05.xlsx, coincidente con las "
     "Tablas 2 y 3 del apartado 4.1"),
    ("Prototipo I", "Regla de medición y primer contacto con el señuelo",
     "Nueve mediciones del tiempo de detección con promedio de 41,598 s, "
     "mínimo de 0,141 s y máximo de 260,108 s. Cuarenta y seis ataques, "
     "1.758 solicitudes atendidas por la API, ocho conexiones capturadas y "
     "8.875 solicitudes del portal.",
     "Figura 35 del apartado 4.3.6.7"),
    ("Prototipo II, vuelta 1", "Laboratorio completo con medición parcial",
     "Diez escenarios ejecutados. Tiempo de detección medido en cuatro, con "
     "promedio de 5,216 s. Diecisiete técnicas implementadas y diez detectadas "
     "en seis tácticas.",
     "v2.0-it1/07-metricas/kpi_report.json"),
    ("Prototipo II, vuelta 2",
     "Corrección del instrumental y medición completa",
     "Diez escenarios ejecutados. Tiempo de detección medido en los diez, con "
     "promedio de 2,022 s, mínimo de 0,0 s y máximo de 15,91 s. Cinco fuentes "
     "de detección.",
     "v2.1-it2/07-metricas/kpi_report.json"),
]

FASES = [
    ("Fase 1", "Identificación y modelado de amenazas",
     "El catálogo de amenazas deja de estar referenciado. Diecisiete técnicas "
     "de MITRE ATT&CK quedan implementadas y asignadas a un escenario cada "
     "una.",
     "mitre_coverage.json"),
    ("Fase 2", "Construcción del laboratorio",
     "Seis servicios de señuelo y una plataforma de gestión se despliegan en "
     "tres segmentos. El aislamiento se verifica ejecutando la prueba desde "
     "el contenedor atacante.",
     "docker-compose.yml y registro de redes"),
    ("Fase 3", "Medición y detección",
     "El tiempo de detección pasa de medirse en cuatro escenarios a medirse "
     "en los diez. Las fuentes de detección pasan de dos segmentos a cinco.",
     "kpi_report.json de it1 e it2"),
    ("Fase 4", "Respuesta y gestión del incidente",
     "La alerta produce el caso de manera automática mediante el flujo de "
     "orquestación, sin intervención del operador, y la trazabilidad se "
     "conserva hasta el caso cerrado.",
     "Consola de TheHive y flujo de orquestación"),
    ("Fase 5", "Mejora continua",
     "Catorce lecciones registradas con causa raíz, mejora aplicada y archivo "
     "de verificación. Las catorce quedan cerradas.",
     "evidencias/lecciones-aprendidas.md"),
]

ISO = [
    ("Fases de ISO 27035 implementadas en el inventario", "5 de 5",
     "iso27035_compliance.json, campo phases_implemented",
     "Describe el diseño declarado de las cinco fases."),
    ("Fases de ISO 27035 ejercitadas durante la campaña", "2 de 5",
     "scenario_to_phase_mapping del mismo archivo y kpi_report.json de la "
     "vuelta 2, que reporta veinte por ciento de fases ejercitadas",
     "Describe lo que la campaña ejecutó. Los diez escenarios se asignan a "
     "las Fases 1, 3 y 4 del modelo de la institución, que corresponden a las "
     "fases de identificación, medición y respuesta."),
]

PREGUNTAS = [
    ("Mostrar los resultados con dashboards",
     "El tablero de métricas de cada vuelta, que se incorpora como figura en "
     "el apartado 4.4.1, junto con las hojas Vuelta 1 y Vuelta 2 de este "
     "libro."),
    ("Solo resultados, sin comprobación de hipótesis",
     "Ningún apartado del 4.4 contiene prueba de hipótesis. Toda cifra "
     "proviene de un archivo del repositorio y declara su fuente."),
    ("Explicar cómo mejoró, los dos prototipos, vender el producto",
     "Las hojas Secuencia y Las seis brechas, que muestran qué valor deja "
     "cada prototipo."),
    ("Análisis del antes y el después de los dos prototipos",
     "Las hojas Las seis brechas y El ciclo completo, con el estado de "
     "partida de la institución y el estado final del laboratorio."),
    ("Cómo se comprueba la mejora, cuánto, por qué y qué cambió en cada fase",
     "La hoja El ciclo completo, con la reducción por escenario, y la hoja "
     "Aportación por fase, con el cambio atribuible a cada una."),
]


def sh_portada(wb):
    ws = wb.active
    ws.title = "Portada"
    sin.print_setup(ws, "1:4")
    sin.sheet_title(
        ws, "COMPARACIÓN ANTES Y DESPUÉS DEL CICLO DE MEJORA",
        "Cruce del diagnóstico de madurez de la institución con los resultados "
        "de las dos vueltas del Prototipo II y con el registro del Prototipo "
        "I. Todas las cifras proceden de archivos del repositorio.", 4)
    r = 5
    filas = [
        ("Objeto del documento",
         "Mostrar en una sola vista que la metodología produjo un cambio "
         "medible, en qué magnitud y en qué fase."),
        ("Estado de partida",
         "Diagnóstico de madurez de 2026, con madurez global de 52,70 % en "
         "nivel Gestionado y seis subdimensiones en nivel Básico."),
        ("Estado final",
         "Segunda vuelta del Prototipo II, con medición del tiempo de "
         "detección en los diez escenarios y cinco fuentes de detección."),
        ("Regla de presentación",
         "Toda cifra de este libro declara su archivo de origen. Ningún valor "
         "fue estimado ni completado por analogía."),
        ("Criterio de comparabilidad",
         "Las medias de tiempo de detección no se comparan entre vueltas "
         "porque el número de muestras cambia. La comparación válida es "
         "escenario por escenario."),
        ("Fuentes primarias",
         "v2.0-it1/07-metricas/kpi_report.json, generado el 4 de octubre de "
         "2026 a las 16:07 UTC.\n"
         "v2.1-it2/07-metricas/kpi_report.json, generado el 4 de octubre de "
         "2026 a las 20:33 UTC.\n"
         "v2.0-it1/07-metricas/mitre_coverage.json.\n"
         "evidencias/lecciones-aprendidas.md.\n"
         "evidencias/INDICE.md.\n"
         "Figura 35 del apartado 4.3.6.7 para los datos del Prototipo I."),
    ]
    for a, b in filas:
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        c = ws.cell(row=r, column=2, value=b)
        c.font = F_SUB
        c.alignment = sin.WRAP
        ws.cell(row=r, column=1, value=a).font = F_B
        ws.row_dimensions[r].height = sin.est([b], [30, 40, 40, 40], minimum=32)
        r += 1
    sin.note(ws, r + 1,
             "Las seis brechas del diagnóstico que la metodología atiende "
             "directamente son los instrumentos 1, 4, 7, 8, 10 y 13. El corte "
             "del nivel Básico se fija en el comprendido entre el 26 % y menos "
             "del 51 %.", 4)
    return ws


def sh_brechas(wb):
    ws = wb.create_sheet("Las seis brechas")
    widths = [10, 30, 12, 12, 62, 44, 20]
    sin.sheet_title(
        ws, "LAS SEIS SUBDIMENSIONES EN NIVEL BÁSICO Y QUÉ RESUELVE EL "
           "LABORATORIO",
        "La medición de 2026 reportó seis subdimensiones en nivel Básico. La "
        "columna de la derecha muestra qué produce hoy el laboratorio para "
        "cada una.", len(widths))
    sin.header(ws, 4, ["Instr.", "Subdimensión", "Antes (2026)", "Nivel",
                       "Qué resuelve el laboratorio", "Fuente del dato",
                       "Fase que lo atiende"], widths)
    r = 5
    for v in BRECHAS:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (2, 5, 6) else F_B
            c.alignment = sin.WRAP if i in (2, 5, 6) else sin.WRAP_C
        ws.row_dimensions[r].height = sin.est(
            [v[1], v[4], v[5]], widths, minimum=34)
        r += 1
    ws.auto_filter.ref = f"A4:G{r-1}"
    ws.freeze_panes = "A5"
    sin.note(ws, r + 1,
             "El Instrumento 13 es el único cuya medición corresponde a la "
             "institución, porque la capacitación se evalúa sobre personas y "
             "no sobre componentes. El laboratorio entrega el material de "
             "demostración que la sostiene.", 7)
    return ws


def sh_ciclo(wb):
    ws = wb.create_sheet("El ciclo completo")
    widths = [40, 30, 30, 26, 56, 34]
    sin.sheet_title(
        ws, "ANTES Y DESPUÉS INDICADOR POR INDICADOR",
        "Once indicadores con su valor de partida y su valor final. Los que no "
        "cambian se declaran como constantes, porque forman parte de lo que "
        "el resultado aísla.", len(widths))
    sin.header(ws, 4, ["Indicador", "Antes", "Después", "Naturaleza del cambio",
                       "Por qué cambia o por qué se mantiene", "Fuente"],
               widths)
    r = 5
    for v in INDICADORES:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (1, 5, 6) else F_B
            c.alignment = sin.WRAP if i in (1, 5, 6) else sin.WRAP_C
            if i in (2, 3):
                c.fill = PatternFill("solid", fgColor=LIGHT)
        ws.row_dimensions[r].height = sin.est(
            [v[0], v[1], v[2], v[4]], widths, minimum=34)
        r += 1
    ws.auto_filter.ref = f"A4:F{r-1}"
    ws.freeze_panes = "A5"
    sin.note(ws, r + 1,
             "Las reducciones por escenario corresponden a los cuatro casos "
             "comparables, porque son los únicos que conservan el mismo número "
             "de muestras en las dos vueltas.", 6)
    return ws


def sh_secuencia(wb):
    ws = wb.create_sheet("Secuencia")
    widths = [30, 34, 66, 46]
    sin.sheet_title(
        ws, "LA SECUENCIA DE LOS DOS PROTOTIPOS",
        "Los tres momentos del trabajo, con lo que cada uno aportó y con el "
        "archivo donde queda registrado.", len(widths))
    sin.header(ws, 4, ["Momento", "Qué aporta", "Resultado del momento",
                       "Fuente"], widths)
    r = 5
    for v in SECUENCIA:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (2, 3, 4) else F_BB
            c.alignment = sin.WRAP
        ws.row_dimensions[r].height = sin.est(
            [v[1], v[2], v[3]], widths, minimum=40)
        r += 1
    ws.auto_filter.ref = f"A4:D{r-1}"
    ws.freeze_panes = "A5"
    sin.note(ws, r + 1,
             "El Prototipo I entrega la regla de medición. El Prototipo II "
             "entrega el laboratorio completo y, en su segunda vuelta, la "
             "corrección del instrumental que hace posible medir los diez "
             "escenarios.", 4)
    return ws


def sh_fases(wb):
    ws = wb.create_sheet("Aportacion por fase")
    widths = [12, 34, 70, 40]
    sin.sheet_title(
        ws, "QUÉ CAMBIÓ EN CADA FASE DE LA METODOLOGÍA",
        "Una fila por fase de las cinco, con el cambio comprobable que produjo "
        "y el archivo que lo respalda.", len(widths))
    sin.header(ws, 4, ["Fase", "Nombre de la fase", "Cambio comprobable",
                       "Fuente"], widths)
    r = 5
    for v in FASES:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (2, 3, 4) else F_BB
            c.alignment = sin.WRAP
        ws.row_dimensions[r].height = sin.est([v[1], v[2], v[3]], widths,
                                              minimum=40)
        r += 1
    ws.auto_filter.ref = f"A4:D{r-1}"
    ws.freeze_panes = "A5"
    sin.note(ws, r + 1,
             "Las cinco fases quedan verificadas y ninguna actividad carece de "
             "archivo que la respalde.", 4)
    return ws


def sh_iso(wb):
    ws = wb.create_sheet("Cobertura ISO 27035")
    widths = [46, 16, 52, 62]
    sin.sheet_title(
        ws, "CÓMO SE LEE LA COBERTURA DE ISO 27035",
        "El mismo archivo reporta dos cifras distintas porque mide dos cosas "
        "distintas. Se presentan las dos con su etiqueta.", len(widths))
    sin.header(ws, 4, ["Concepto", "Valor", "Archivo y campo", "Qué mide"],
               widths)
    r = 5
    for v in ISO:
        for i, val in enumerate(v, start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.font = F_SUB if i in (1, 3, 4) else F_BB
            c.alignment = sin.WRAP if i in (1, 3, 4) else sin.WRAP_C
        ws.row_dimensions[r].height = sin.est([v[0], v[2], v[3]], widths,
                                              minimum=40)
        r += 1
    ws.freeze_panes = "A5"
    sin.note(ws, r + 1,
             "Presentar las dos cifras evita que el inventario y la "
             "exercitación se confundan. La cifra que describe el trabajo "
             "realizado durante la campaña es la segunda.", 4)
    return ws


def sh_preguntas(wb):
    ws = wb.create_sheet("Respuestas")
    widths = [46, 90]
    sin.sheet_title(
        ws, "DÓNDE ESTÁ LA RESPUESTA A CADA ENCARGO",
        "Cinco encargos y la hoja de este libro que responde cada uno.", 2)
    sin.header(ws, 4, ["Encargo", "Dónde se responde y con qué criterio"],
               widths)
    r = 5
    for a, b in PREGUNTAS:
        ws.cell(row=r, column=1, value=a).font = F_BB
        c = ws.cell(row=r, column=2, value=b)
        c.font = F_SUB
        c.alignment = sin.WRAP
        ws.row_dimensions[r].height = sin.est([b], widths, minimum=32)
        r += 1
    ws.freeze_panes = "A5"
    return ws


def main():
    wb = Workbook()
    sh_portada(wb)
    sh_brechas(wb)
    sh_ciclo(wb)
    sh_secuencia(wb)
    sh_fases(wb)
    sh_iso(wb)
    sh_preguntas(wb)
    DST.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DST)
    print(f"OK -> {DST}  ({len(wb.sheetnames)} hojas)")
    print(wb.sheetnames)


if __name__ == "__main__":
    main()