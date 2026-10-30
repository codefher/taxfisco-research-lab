# -*- coding: utf-8 -*-
"""Inserta el apartado 4.5.3 (Distribucion de referencia y verificacion de los
supuestos) en el maestro y renumera los subapartados siguientes.

Conserva las terminaciones CRLF del maestro y no introduce BOM.
"""
import os
import shutil

MASTER = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\Redaccion_Marco_Practico_v13.md"
NEW    = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\_cap453_borrador.tmp.md"

with open(MASTER, "rb") as fh:
    raw = fh.read()
text = raw.decode("utf-8")

# 1) renumerar de mayor a menor para evitar colisiones
RENUM = [
    ("#### 4.5.5 Decisión sobre la hipótesis y alcance de la comprobación",
     "#### 4.5.6 Decisión sobre la hipótesis y alcance de la comprobación"),
    ("#### 4.5.4 Comprobación de los anclajes normativos de la hipótesis",
     "#### 4.5.5 Comprobación de los anclajes normativos de la hipótesis"),
    ("#### 4.5.3 Ejecución de la prueba de Wilcoxon pareada",
     "#### 4.5.4 Ejecución de la prueba de Wilcoxon pareada"),
]
for viejo, nuevo in RENUM:
    if viejo not in text:
        raise SystemExit(f"No se localizo el encabezado: {viejo}")
    text = text.replace(viejo, nuevo, 1)

# 2) renumerar las referencias internas al apartado de ejecucion
text = text.replace(
    "La trazabilidad del diseño queda asegurada",
    "La trazabilidad del diseño queda asegurada", 1)

# 3) anadir la remision desde el apartado de ejecucion al nuevo apartado
ANCLA = ("La validación de la eficacia de la metodología mediante la comparación de antes "
         "y después se sostiene en la lectura de los indicadores de cobertura, de rapidez "
         "y de custodia, con la salvedad declarada en el apartado 4.4.4 sobre el hecho "
         "de que el Prototipo 1 admite una sola ejecución.")
REMISION = (ANCLA + " La ejecución que sigue se apoya en el estadístico cuya distribución "
            "de referencia se declaró en el apartado 4.5.3, de manera que el valor p que "
            "produce tenga una interpretación verificada y no una atribución convencional.")
if ANCLA not in text:
    raise SystemExit("No se localizo el parrafo de la seccion de ejecucion.")
text = text.replace(ANCLA, REMISION, 1)

# 4) insertar el nuevo apartado antes del de ejecucion
with open(NEW, "r", encoding="utf-8", newline="") as fh:
    bloque = fh.read().replace("\r\n", "\n").replace("\n", "\r\n")
if not bloque.endswith("\r\n"):
    bloque += "\r\n"
bloque += "\r\n"

MARCA = "#### 4.5.4 Ejecución de la prueba de Wilcoxon pareada"
i = text.index(MARCA)
texto = text[:i] + bloque + text[i:]

backup = MASTER + ".bak-cap5"
if not os.path.exists(backup):
    shutil.copy2(MASTER, backup)

with open(MASTER, "wb") as fh:
    fh.write(texto.encode("utf-8"))

print("apartado 4.5.3 insertado y subapartados renumerados")
print("  bytes antes  :", len(raw))
print("  bytes despues:", len(texto.encode("utf-8")))
print("  lineas nuevas:", bloque.count("\r\n"))
