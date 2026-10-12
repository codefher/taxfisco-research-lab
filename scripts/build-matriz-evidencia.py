#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Matriz de evidencia del laboratorio por item del instrumento de madurez.

Cada fila declara un dato real y verificable del laboratorio, o declara
explicitamente la ausencia de evidencia. No se rellena ningun valor que no
proceda de un artefacto del repositorio.
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
    r"\2026-10-12_Matriz_Evidencia_Laboratorio_por_Item_v01.docx"
)

TBL = "Tablaconcuadrcula"
H1, H2, H3 = "Ttulo1", "Ttulo2", "Ttulo3"
GREY, AMBER, GREEN = "D9D9D9", "FFF2CC", "E2EFDA"

# (instrumento, numero, item abreviado, evidencia, valor, fuente)
ROWS = [
    (1, 1, "% de eventos con todos los campos mínimos",
     "El señuelo escribe en cada solicitud la hora, el origen, el tipo y el "
     "identificador de la fuente. El índice del gestor de eventos conserva el "
     "documento íntegro con su índice de almacenamiento y su identificador, de "
     "modo que los cuatro campos mínimos están presentes en todos los "
     "eventos registrados.",
     "Cuatro campos en cada evento",
     "Fig. eventos indexados y documento expandido"),
    (1, 2, "Tiempo promedio del evento a su registro",
     "Tiempo medio de detección sobre los diez escenarios de la campaña de "
     "la segunda vuelta.",
     "2,02 s de media", "07-metricas/kpi_report.json"),
    (1, 3, "Percentil 95 del tiempo de registro",
     "La campaña midió el máximo, no el percentil 95. No se calculó el "
     "percentil.",
     "Máximo 15,91 s; p95 no calculado", "07-metricas/kpi_report.json"),
    (1, 4, "Disponibilidad del sistema de monitoreo",
     "La campaña completó los diez escenarios sin caída del laboratorio. No "
     "se midió el porcentaje de tiempo activo.",
     "10 de 10 escenarios completados", "01-entorno-servicios (campaña S01–S10)"),

    (2, 1, "% de alertas con categoría de ataque",
     "Cada uno de los diez escenarios se registra con su técnica de MITRE "
     "ATT&CK asignada en el reporte de cobertura.",
     "10 de 10 con técnica", "07-metricas/mitre_coverage.json"),
    (2, 2, "% de alertas con evidencia mínima adjunta",
     "Cada escenario conserva su registro crudo y sus capturas. El promedio "
     "por escenario es de 9,1 archivos y el total de la campaña es de 91.",
     "91 archivos en 10 escenarios", "07-metricas/kpi_report.json"),
    (2, 3, "Puntaje de completitud del expediente",
     "La capa de evidencia puntúa 100 sobre 100 en calidad. La completitud "
     "del expediente de caso no se calculó por separado.",
     "Calidad de evidencia 100/100", "07-metricas/kpi_report.json"),

    (3, 1, "Tiempo promedio hasta la contención inicial",
     "No medido. Requiere marcas de tiempo de los casos en la plataforma de "
     "gestión, que la versión en prueba de la herramienta no expone.",
     "No medido", "kpi_report.json, campo MTTR"),
    (3, 2, "% de casos críticos en el tiempo objetivo",
     "No medido. No existe el registro de casos con sello temporal en la "
     "plataforma de gestión durante la campaña.",
     "No medido", "kpi_report.json, campo MTTR"),
    (3, 3, "Escalamientos formales por mes",
     "No medido. La campaña no llevaba un conteo de escalamientos formales.",
     "No medido", "sin registro"),

    (4, 1, "% de incidentes con documento de lecciones",
     "La campaña produjo un registro de catorce lecciones, de la L1 a la L14, "
     "cada una con su hallazgo, su causa y su corrección.",
     "14 lecciones registradas", "evidencias/lecciones-aprendidas.md"),
    (4, 2, "Acciones correctivas derivadas de incidentes",
     "Las catorce lecciones quedaron cerradas, cada una con su resolución "
     "documentada y con el archivo que la verifica.",
     "14 cerradas", "evidencias/lecciones-aprendidas.md"),
    (4, 3, "% de acciones dentro del plazo comprometido",
     "No medido. El registro documenta qué se corrigió, no el plazo de cada "
     "corrección.",
     "No medido", "sin registro de plazos"),

    (5, 1, "% de evidencias con identificador y verificación de integridad",
     "Toda la evidencia de la campaña se selló con huella SHA-256 en el "
     "repositorio de custodia.",
     "91 de 91 con SHA-256", "05-enriquecimiento-custodia"),
    (5, 2, "% de traspasos con cadena de custodia completa",
     "La estructura de custodia se definió y se aplicó a los escenarios, con "
     "sello temporal ISO 8601 y zona horaria. El porcentaje de traspasos no "
     "se calculó.",
     "Estructura definida y aplicada", "Fig. custodia y sello temporal"),
    (5, 3, "Percentil 95 de registro de traspasos",
     "No medido. Solo se registró el instante de cada custodia, no la "
     "distribución de tiempos entre traspasos.",
     "No medido", "sin registro de tiempos"),

    (6, 1, "Respaldos completos del repositorio de evidencias",
     "No medido. La campaña no ejecutó respaldos del repositorio de "
     "evidencias como actividad medida.",
     "No medido", "sin registro"),
    (6, 2, "% de respaldos con verificación de integridad",
     "La verificación por huella SHA-256 está implementada y se aplicó a la "
     "evidencia. No se ejecutaron respaldos para los cuales aplicar ese "
     "porcentaje.",
     "Verificación implementada", "05-enriquecimiento-custodia"),
    (6, 3, "Pruebas de restauración exitosas",
     "No medido. No se ejecutaron pruebas de restauración dentro de la "
     "campaña.",
     "No medido", "sin registro"),

    (7, 1, "Tiempo de retención de evidencias",
     "El laboratorio no define una política de retención en meses. Esa "
     "definición corresponde a la institución.",
     "No aplica al laboratorio", "sin política de retención"),
    (7, 2, "% de solicitudes de acceso resueltas en plazo",
     "No medido. La campaña no llevaba un registro de solicitudes de acceso a "
     "la evidencia.",
     "No medido", "sin registro"),

    (8, 1, "% de cuentas revisadas",
     "El laboratorio separa los segmentos por función, de modo que los "
     "contenedores de gestión no comparten subred con los señuelos. La revisión "
     "periódica de cuentas no se midió.",
     "Separación por segmentos verificada", "03-aislamiento-red"),
    (8, 2, "Cuentas con exceso de privilegios removidas",
     "La prueba de aislamiento ejecutada desde el atacante alcanzó dos "
     "objetivos del segmento expuesto y no alcanzó cuatro servicios del "
     "segmento de gestión.",
     "2 alcanzables, 4 bloqueados", "Fig. prueba de aislamiento"),
    (8, 3, "% de altas y bajas con ticket y aprobación",
     "No medido. La gestión de altas y bajas de cuentas corresponde al "
     "proceso de la institución, no al laboratorio.",
     "No medido", "sin registro"),

    (9, 1, "% de cambios revisados por otra persona",
     "El laboratorio opera bajo control de versiones con historial completo de "
     "commits, cada corrección del registro de lecciones asociada a su commit.",
     "Trazabilidad por commit", "historial del repositorio"),
    (9, 2, "% de canales con pruebas automáticas",
     "El señuelo de la interfaz de programación de aplicaciones incluye un "
     "conjunto de pruebas automáticas sobre su registro de ataques.",
     "Pruebas automáticas presentes", "decoys/api-tributaria/tests"),
    (9, 3, "Tiempo medio de corrección de hallazgos críticos",
     "El registro documenta qué se corrigió en cada una de las once lecciones "
     "cerradas, no el tiempo que tomó cada corrección.",
     "No medido", "sin registro de tiempos"),

    (10, 1, "Escaneos de vulnerabilidades en producción",
     "Los sensores de red y el emulador de acceso remoto operan de forma "
     "continua durante la campaña y alimentan el reporte de cobertura.",
     "Cobertura continua de la campaña", "Fig. alertas de la cadena de detección"),
    (10, 2, "% de vulnerabilidades críticas corregidas en plazo",
     "La campaña no llevaba un registro de vulnerabilidades con plazo de "
     "corrección. El reporte de cobertura distingue diecisiete técnicas del "
     "inventario del señuelo de las diez que la campaña activa y a las que "
     "asigna fuente de detección, lo que mide cobertura y no plazo.",
     "No medido", "07-metricas/mitre_coverage.json"),
    (10, 3, "Tiempo medio de corrección por severidad",
     "No medido. La campaña no llevaba un registro de tiempos de corrección "
     "por severidad.",
     "No medido", "sin registro"),

    (11, 1, "% de fuentes con sincronización horaria activa",
     "Los registros de la campaña llevan marca temporal ISO 8601 con zona "
     "horaria, y el cálculo del tiempo de detección se apoya en esas marcas.",
     "Marcas con zona horaria verificadas", "Fig. sello temporal de custodia"),
    (11, 2, "% de registros en repositorio inalterable",
     "No medido. El laboratorio declara el control de recolección de evidencia "
     "de la norma ISO/IEC 27001 sobre un repositorio de solo escritura con "
     "firma. La declaración documenta la decisión de diseño, no una medición "
     "del porcentaje de registros que efectivamente salieron a ese "
     "repositorio.",
     "No medido", "iso27035_compliance.json, control A.5.28"),
    (11, 3, "Tiempo de retención de los registros operativos",
     "El laboratorio no define una retención en meses para sus registros. Es "
     "una decisión de la institución.",
     "No aplica al laboratorio", "sin política de retención"),

    (12, 1, "% de activos críticos con evaluación vigente",
     "No medido. La metodología declara cuatro decisiones de diseño que acotan "
     "el alcance, la separación, la trazabilidad y la mejora iterativa. La "
     "declaración documenta el diseño y no el porcentaje de activos con "
     "evaluación vigente.",
     "No medido", "4.2.1.3 Decisiones de diseño"),
    (12, 2, "Reevaluaciones de riesgos sobre activos críticos",
     "No medido. La campaña no llevaba un conteo de reevaluaciones.",
     "No medido", "sin registro"),
    (12, 3, "% de riesgos altos con plan de tratamiento activo",
     "De las seis brechas del diagnóstico, tres las atiende la metodología "
     "de forma directa y las otras tres se derivan al plan institucional con "
     "un tratamiento definido.",
     "3 atendidas, 3 derivadas", "matriz de trazabilidad del diagnóstico"),

    (13, 1, "% de personal capacitado en seguridad digital",
     "El laboratorio nocapacita personal. Esta brecha se deriva al plan "
     "institucional.",
     "Sin evidencia en el laboratorio", "brecha G4-13"),
    (13, 2, "Sesiones de capacitación impartidas",
     "Sin evidencia en el laboratorio.", "Sin evidencia en el laboratorio",
     "brecha G4-13"),
    (13, 3, "Puntaje promedio de evaluaciones post-capacitación",
     "Sin evidencia en el laboratorio.", "Sin evidencia en el laboratorio",
     "brecha G4-13"),

    (14, 1, "Indicadores de seguridad revisados en comité",
     "El laboratorio documenta un tablero de métricas y un reporte "
     "consolidado por campaña. La captura de la primera vuelta existe en el "
     "repositorio y aún no está incorporada al texto. No se constitute un "
     "comité de revisión.",
     "1 tablero en el texto y 1 reporte", "Fig. 52 y reportes por campaña"),
    (14, 2, "% de controles ajustados por las revisiones",
     "Las catorce lecciones cerradas modificaron componentes concretos del "
     "laboratorio: reglas del detector, publicador de eventos, posición de "
     "lectura del colector, programa de cálculo y los tres scripts de "
     "arranque.",
     "14 correcciones aplicadas", "evidencias/lecciones-aprendidas.md"),
    (14, 3, "% de procesos con métricas formalmente definidas",
     "Las cinco fases de la metodología tienen al menos un indicador medido "
     "que se reporta al cierre de cada campaña.",
     "5 de 5 fases con indicador", "kpi_report.json"),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def run(text, bold=False, italic=False, size=18, color=None):
    rpr = ""
    if bold:
        rpr += "<w:b/>"
    if italic:
        rpr += "<w:i/>"
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    return (f"<w:r><w:rPr>{rpr}</w:rPr>"
            f'<w:t xml:space="preserve">{esc(text)}</w:t></w:r>')


def para(text="", style=None, bold=False, italic=False, size=20,
         align=None, after=120, color=None):
    ppr = ""
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if align:
        ppr += f'<w:jc w:val="{align}"/>'
    ppr += f'<w:spacing w:after="{after}"/>'
    return (f"<w:p><w:pPr>{ppr}</w:pPr>"
            f"{run(text, bold, italic, size, color) if text else ''}</w:p>")


def cell(text, width, bold=False, shade=None, size=16, color=None):
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ""
    tcpr = f'<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shd}</w:tcPr>'
    ppr = '<w:pPr><w:spacing w:before="30" w:after="30"/></w:pPr>'
    return (f"<w:tc>{tcpr}<w:p>{ppr}"
            f"{run(text, bold, size, color) if text else ''}</w:p></w:tc>")


def build_table():
    widths = [560, 1900, 3000, 1700, 1480]
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    x = (f'<w:tbl><w:tblPr><w:tblStyle w:val="{TBL}"/>'
         f'<w:tblW w:w="0" w:type="auto"/>'
         f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0"'
         f' w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
         f"</w:tblPr><w:tblGrid>{grid}</w:tblGrid>")

    x += ('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>'
          + cell("Inst.", widths[0], True, GREY)
          + cell("Ítem del instrumento", widths[1], True, GREY)
          + cell("Evidencia disponible en el laboratorio", widths[2], True, GREY)
          + cell("Valor medido", widths[3], True, GREY)
          + cell("Fuente", widths[4], True, GREY)
          + "</w:tr>")

    for inst, n, item, ev, val, src in ROWS:
        empty = ("no medido" in val.lower()
                 or "sin evidencia" in val.lower()
                 or "no aplica" in val.lower()
                 or "no calculado" in val.lower())
        shade = "FCE4E4" if empty else None
        col = "9C0006" if empty else None
        x += ('<w:tr><w:trPr><w:cantSplit/></w:trPr>'
              + cell(str(inst), widths[0], False, GREY)
              + cell(f"{n}. {item}", widths[1])
              + cell(ev, widths[2])
              + cell(val, widths[3], bold=True, shade=shade, color=col)
              + cell(src, widths[4])
              + "</w:tr>")
    return x + "</w:tbl>" + para(after=200)


def build_body():
    x = para("MATRIZ DE EVIDENCIA DEL LABORATORIO POR ÍTEM DEL INSTRUMENTO",
             style=H1, align="center", bold=True, size=28)
    x += para("Diagnóstico de Madurez en Seguridad de la Información · "
              "Tesis de Maestría · versión 1", align="center", italic=True)
    x += para(
        "Este documento cruza los cuarenta y dos ítems del instrumento de "
        "diagnóstico con la evidencia efectivamente disponible en el "
        "laboratorio de la investigación. Cada fila declara un dato verificable "
        "y el archivo del que procede, o declara de forma explícita que ese ítem "
        "no tiene respaldo medido.",
    )
    x += para(
        "Ningún valor de esta matriz fue estimado, aproximado ni completado "
        "por analogía. Las filas marcadas en rojo corresponden a ítems que el "
        "laboratorio no mide, y esa ausencia es "
        "información válida: delimita qué puede afirmarse con evidencia y qué "
        "corresponde a la institución.",
        bold=True,
    )

    x += para("Resumen de cobertura", style=H2)
    total = len(ROWS)
    gaps = sum(
        1 for r in ROWS
        if any(k in r[4].lower() for k in ("no medido", "sin evidencia",
                                           "no aplica", "no calculado"))
    )
    x += para(
        f"De los {total} ítems del instrumento, {total - gaps} cuentan con "
        f"evidencia verificable en el laboratorio y {gaps} no la tienen. "
        f"La ausencia se concentra en el Instrumento 3, sobre tiempos de "
        f"respuesta, y en el Instrumento 13, sobre capacitación, y coincide "
        f"con las restricciones que el propio registro de lecciones deja "
        f"documentadas.",
    )

    x += para("Matriz completa", style=H2)
    x += build_table()

    x += para("Lectura para el capítulo de resultados", style=H2)
    for t in [
        "Los ítems con evidencia se sostienen con un archivo del repositorio y "
        "pueden citarse en el capítulo de resultados sin ambigüedad.",
        "Los ítems sin evidencia no deben presentarse como resultado. Se "
        "presentan como límites de lo que el laboratorio mide, y su atención "
        "corresponde al plan institucional.",
        "La medición posterior del instrumento en la institución es la vía que "
        "convierte los ítems sin evidencia en resultados, porque esos ítems "
        "dependen del proceso y no del laboratorio.",
    ]:
        x += para("• " + t.replace("Presentation", ""), italic=True)

    return x


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, DST)

    zin = zipfile.ZipFile(DST, "r")
    items = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    xml = items["word/document.xml"].decode("utf-8")
    i = xml.find("<w:body>") + len("<w:body>")
    j = xml.rfind("<w:sectPr")
    items["word/document.xml"] = (
        xml[:i] + build_body() + xml[j:]
    ).encode("utf-8")

    zout = zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED)
    for info in infos:
        zout.writestr(info.filename, items[info.filename])
    zout.close()
    print("OK ->", DST)


if __name__ == "__main__":
    main()