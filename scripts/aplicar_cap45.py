# -*- coding: utf-8 -*-
"""Inserta el apartado 4.5 (Comprobacion de la hipotesis) antes del Capitulo V
y alinea el parrafo de la hipotesis del Capitulo V con el resultado de la prueba.

Conserva las terminaciones CRLF del maestro y no introduce BOM.
"""
import os
import shutil

MASTER = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\Redaccion_Marco_Practico_v13.md"
NEW    = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\_cap45_borrador.tmp.md"

ANCHOR = "# Capítulo V: Conclusiones y Recomendaciones de la Investigación"

VIEJO = (
    "La hipótesis formulada en el apartado 1.5 se confirma dentro de ese alcance, ya que la metodología "
    "de honeypot, con las normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK, mejora la "
    "gestión de incidentes en los servicios fiscales. La mejora se constata en la detección temprana y en "
    "la recolección de evidencia, aunque los resultados ejecutados no permiten afirmar lo mismo respecto "
    "de los tiempos de contención y cierre."
)

NUEVO = (
    "La hipótesis formulada en el apartado 1.5 no se refuta en la comprobación del apartado 4.5, ya que "
    "la metodología de honeypot, con las normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK, "
    "mejora la gestión de incidentes en los servicios fiscales. Los anclajes normativos de la formulación "
    "se verifican por completo y la dirección del efecto sobre el tiempo de detección es inequívoca, "
    "aunque la prueba no paramétrica comprometida en el diseño no alcanza el nivel de significación fijado "
    "con los cuatro pares disponibles, de manera que la mejora se sostiene como consistente con los datos "
    "y todavía no como estadísticamente concluyente. Los resultados ejecutados tampoco permiten afirmar lo "
    "mismo respecto de los tiempos de contención y cierre."
)

with open(MASTER, "rb") as fh:
    raw = fh.read()
text = raw.decode("utf-8")

if VIEJO not in text:
    raise SystemExit("No se localizo el parrafo de la hipotesis en el Capitulo V.")

with open(NEW, "r", encoding="utf-8", newline="") as fh:
    bloque = fh.read().replace("\r\n", "\n").replace("\n", "\r\n")
if not bloque.endswith("\r\n"):
    bloque += "\r\n"
bloque += "\r\n"

# 1) insertar el apartado 4.5 justo antes del Capitulo V
i = text.index(ANCHOR)
texto = text[:i] + bloque + text[i:]

# 2) alinear el parrafo de la hipotesis del Capitulo V
if VIEJO not in texto:
    raise SystemExit("No se localizo el parrafo tras la insercion.")
texto = texto.replace(VIEJO, NUEVO, 1)

backup = MASTER + ".bak-cap5"
if not os.path.exists(backup):
    shutil.copy2(MASTER, backup)

with open(MASTER, "wb") as fh:
    fh.write(texto.encode("utf-8"))

print("apartado 4.5 insertado y Capitulo V alineado")
print("  bytes antes  :", len(raw))
print("  bytes despues:", len(texto.encode("utf-8")))
print("  lineas 4.5   :", bloque.count("\r\n"))
