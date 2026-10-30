#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrasta las cifras y la coherencia del HTML del analisis estadistico del MTTD.

El documento tiene dos capas: el texto estatico y los valores que dibuja el
JavaScript al cargar. Se revisan las dos contra
resultados-prototypes/estadisticas_mttd.json,
resultados-prototypes/estadisticas_hipotesis.json y
resultados-prototypes/estadisticas_qq.json.

Ademas comprueba que las cinco correcciones de la segunda auditoria siguen
presentas en el texto y que no han reaparecido las afirmaciones incorrectas.

Uso: py -3 scripts/contrastar_html_mttd.py [nombre_html]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).resolve().parent.parent / "resultados-prototipos"
HTML = BASE / (sys.argv[1] if len(sys.argv) > 1 else "mttd-analisis-estadistico-v3.html")
EST = BASE / "estadisticas_mttd.json"
HIP = BASE / "estadisticas_hipotesis.json"
QQ = BASE / "estadisticas_qq.json"

h = HTML.read_text(encoding="utf-8")
e = json.loads(EST.read_text(encoding="utf-8"))
a = json.loads(HIP.read_text(encoding="utf-8"))
q = json.loads(QQ.read_text(encoding="utf-8"))


def variantes(x: float) -> set[str]:
    out = set()
    for dec in range(0, 7):
        s = f"{x:.{dec}f}"
        if "." in s:
            s = s.rstrip("0").rstrip(".")
        out.add(s.replace(".", ","))
        out.add(s)
    return out


# ---------------------------------------------------------------- indicadores
esperados: list[tuple[str, float]] = []
for k in ("p1", "p2v1", "p2fin"):
    ds = e["datasets"][k]
    for c in ("media", "mediana", "minimo", "maximo", "rango",
              "desviacion_estandar", "p95_inclusivo", "suma"):
        esperados.append((f"{k}.{c}", ds[c]))
cc = e["comparacion_comparable"]
for c in ("media_inicial", "media_final", "diferencia_absoluta", "reduccion_relativa_pct"):
    esperados.append((f"comp.{c}", cc[c]))
cr = e["comparacion_reportada"]
for c in ("media_vuelta_1", "media_final", "diferencia_absoluta", "reduccion_relativa_pct"):
    esperados.append((f"rep.{c}", cr[c]))
for k, v in e["cobertura"].items():
    esperados.append((f"cob.{k}.pct", v["pct"]))
    esperados.append((f"cob.{k}.medidos", float(v["medidos"])))

# ------------------------------------------------------------- hipotesis
w = a["wilcoxon_emparejado"]
for nombre, val in [
    ("W+", w["W_positivo"]), ("W-", w["W_negativo"]), ("W", w["W"]),
    ("p_uni", w["p_exacto_unilateral"]), ("p_bi", w["p_exacto_bilateral"]),
    ("p_signo", w["p_signo_bilateral"]), ("p_min_uni", w["p_minimo_unilateral_alcanzable"]),
    ("p_min_bi", w["p_minimo_bilateral_alcanzable"]),
    ("rrb", w["correlacion_biserial_rangos"]), ("hl", w["hodges_lehmann"]),
    ("media_dif", w["media_diferencias"]), ("mediana_dif", w["mediana_diferencias"]),
    ("shapiro_dif_w", w["simetria_diferencias_shapiro"]["w"]),
    ("shapiro_dif_p", w["simetria_diferencias_shapiro"]["p"]),
]:
    esperados.append((f"hip.{nombre}", val))
for d in w["detalle"]:
    esperados.append((f"hip.dif.{d['escenario']}", d["diferencia"]))
for k in ("p1", "p2v1", "p2fin"):
    c = a["conjuntos"][k]["descriptivos"]
    esperados.append((f"{k}.sesgo", c["sesgo_fisher_pearson"]))
    lg = a["conjuntos"][k]["normalidad_log"]
    if lg.get("shapiro_wilk_log"):
        esperados.append((f"{k}.sw_log_w", lg["shapiro_wilk_log"]["w"]))
        esperados.append((f"{k}.sw_log_p", lg["shapiro_wilk_log"]["p"]))
        esperados.append((f"{k}.sesgo_log", lg["log_sesgo"]))

# -------------------------------------------------------- graficos Q-Q
for p in q["paneles"]:
    esperados.append((f"qq.{p['clave']}.n", float(p["n"])))

faltan = [(n_, v) for n_, v in esperados if not any(x in h for x in variantes(v))]

print(f"ARCHIVO: {HTML.name}")
print(f"CIFRAS VERIFICADAS ENCONTRADAS: {len(esperados) - len(faltan)}/{len(esperados)}")
if faltan:
    print("NO ENCONTRADAS:")
    for n_, v in faltan:
        print(f"   {n_} = {v}")
else:
    print("-> todas las cifras clave aparecen en el documento")

# ------------------------------------------------------- coherencia textual
print()
problemas: list[str] = []


def exigir(patron: str, mensaje: str) -> None:
    if not re.search(patron, h, re.I | re.S):
        problemas.append(mensaje)


def prohibir(patron: str, mensaje: str) -> None:
    if re.search(patron, h, re.I | re.S):
        problemas.append(mensaje)


# --- coherencia general (sin cambios respecto de la primera auditoria)
prohibir(r"Hodges-Lehmann\s*[(:=]\s*0,6120", "el valor de la media aparece asociado al nombre de Hodges-Lehmann")
exigir(r"Hodges-Lehmann\s*\(0,6415 s\)", "falta el valor verificado de Hodges-Lehmann (0,6415 s)")
for m in re.finditer(r"p[^.\n]{0,40}bilateral[^.\n]{0,40}?(\d,\d{4})", h):
    if m.group(1) != "0,1250":
        problemas.append(f"valor p bilateral inesperado: {m.group(1)}")
exigir(r"inalcanzable", "falta la advertencia de que el 5 % es inalcanzable")
prohibir(r"distribuci[oó]n\s+lognormal\s+(demostrada|confirmada)", "se afirma la lognormalidad como demostrada")
exigir(r"hipótesis compatible", "falta la calificacion de hipotesis compatible para la lognormal")
prohibir(r"confirma[^<]{0,40}asimetr", "se usa 'confirma' para la asimetria")

# --- correccion 1: Shapiro-Wilk evalua normalidad, no simetria
prohibir(r"sin evidencia en contra de la simetr", "se lee el resultado de Shapiro-Wilk como evidencia sobre la simetria")
prohibir(r"simetr[ií]a (de las diferencias )?(queda|ha sido|esta) (demostrada|comprobada|verificada)", "se afirma la simetria de las diferencias como comprobada")
exigir(r"contrasta la <strong>normalidad</strong>[^<]*?no\s+la\s+simetr", "falta la aclaracion de que Shapiro-Wilk evalua normalidad y no simetria")
exigir(r"normalidad no se rechaza", "falta la lectura correcta del resultado de Shapiro-Wilk sobre las diferencias")

# --- correccion 2: justificacion de la prueba de Wilcoxon
prohibir(r"las diferencias no siguen una distribuci[oó]n normal", "se justifica la prueba por la no normalidad de las diferencias")
prohibir(r"no param[eé]trica, porque\s*\n?\s*las diferencias", "se justifica la prueba por la forma de las diferencias")
exigir(r"No</strong> se elige porque", "falta la aclaracion de que la prueba no se elige por la no normalidad")
exigir(r"exacta</strong>", "falta la mencion del calculo exacto del valor p")
exigir(r"prueba de signos", "falta la prueba de signos como contraste complementario")

# --- correccion 3: recta de referencia y escalas de la Figura 13
prohibir(r"minimos cuadrados sobre los puntos", "la recta de referencia del Q-Q sigue siendo una regresion por minimos cuadrados")
prohibir(r"const a=den\?num/den", "el codigo del Q-Q conserva la regresion por minimos cuadrados")
exigir(r"media \+ desviaci[oó]n est[aá]ndar", "falta la definicion de la recta de referencia del Q-Q")
exigir(r"escalaAgradable", "falta la graduacion automatica de los ejes del Q-Q")
exigir(r"Cuantil te[oó]rico de la normal est[aá]ndar", "falta el titulo del eje de cuantiles del Q-Q")

# --- correccion 4: independencia como supuesto del diseno
prohibir(r"los cuatro pares provienen de escenarios distintos, de modo", "la independencia se sigue afirmando como demostrada")
exigir(r"supuesto del dise[nñ]o", "falta la presentacion de la independencia como supuesto del diseno")
exigir(r"efecto de arrastre", "falta la explicacion de las condiciones que respaldarian la independencia")

# --- correccion 5: hipotesis unilateral y su direccion
exigir(r"unilateral</strong>", "falta la declaracion de la hipotesis alternativa unilateral")
exigir(r"4\.5\.1", "falta el anclaje de la formulacion en la tesis")
exigir(r"Valor p que decide", "falta la declaracion de que decide el valor p bilateral")
exigir(r"cap[ií]tulo III", "falta el anclaje del procedimiento en el capitulo III")

print("COHERENCIA DEL TEXTO:")
if problemas:
    for p in problemas:
        print("   X", p)
else:
    print("   sin contradicciones detectadas")

# ------------------------------------------------------- estructura del doc
print()
figs = re.findall(r"Figura (\d+) ·", h)
tabs = re.findall(r"<caption>Tabla (\d+)\.", h)
print(f"FIGURAS: {len(figs)} -> {figs}")
print(f"numeracion consecutiva: {figs == [str(i) for i in range(1, len(figs) + 1)]}")
print(f"TABLAS con caption en JS: {sorted(set(tabs), key=int)}")
print(f"secciones: {len(re.findall(r'<section class=.bloque', h))}")
print(f"apartados numerados: {len(re.findall(r'class=.kicker.>\d+ ', h))}")
print(f"avisos: {len(re.findall(r'class=.aviso aviso--', h))}")

sys.exit(1 if (faltan or problemas) else 0)
