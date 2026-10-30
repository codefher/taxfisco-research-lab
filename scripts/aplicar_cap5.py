# -*- coding: utf-8 -*-
"""Sustituye el bloque de plantilla del Capitulo V en el documento maestro v13.

Conserva las terminaciones CRLF del archivo original y no introduce BOM.
"""
import io
import os
import shutil
import sys

MASTER = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\Redaccion_Marco_Practico_v13.md"
NEW    = r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\_cap5_borrador.tmp.md"

START_MARK = "# Capítulo V: Conclusiones y Recomendaciones de la Investigación"
END_MARK   = "# Anexos"

with open(MASTER, "rb") as fh:
    raw = fh.read()
text = raw.decode("utf-8")

i = text.index(START_MARK)
j = text.index(END_MARK)
old_block = text[i:j]

with open(NEW, "r", encoding="utf-8", newline="") as fh:
    new_block = fh.read().replace("\r\n", "\n").replace("\n", "\r\n")
if not new_block.endswith("\r\n"):
    new_block += "\r\n"
new_block += "\r\n"

new_text = text[:i] + new_block + text[j:]

backup = MASTER + ".bak-cap5"
if not os.path.exists(backup):
    shutil.copy2(MASTER, backup)

with open(MASTER, "wb") as fh:
    fh.write(new_text.encode("utf-8"))

print("bloque reemplazado")
print("  lineas antes :", old_block.count("\r\n"))
print("  lineas despues:", new_block.count("\r\n"))
print("  bytes antes  :", len(raw))
print("  bytes despues:", len(new_text.encode('utf-8')))
