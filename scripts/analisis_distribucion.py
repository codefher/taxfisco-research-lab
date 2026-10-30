# -*- coding: utf-8 -*-
"""Analisis de la distribucion de los tiempos de deteccion y de la distribucion
nula de la prueba de Wilcoxon pareada.

Datos:
  P1  -> evidencias/07-metricas/07_kpi-report.json (9 escenarios medidos)
  P2  -> evidencias/v2.0-it1/07-metricas/kpi_report.json (vuelta 1, 4 medidos)
         evidencias/v2.1-it2/07-metricas/kpi_report.json (medicion final, 10 medidos)

Salida: figuras PNG en resultados-prototipos/evidencia-visual/graficos/
"""
import itertools
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.lines import Line2D
from scipy import stats

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"
GRAFI = os.path.join(RAIZ, "resultados-prototipos", "evidencia-visual", "graficos")
os.makedirs(GRAFI, exist_ok=True)

# paleta institucional (misma del tablero de resultados)
NAVY, NAVY2, GREEN, AMBER = "#1F3864", "#2E75B6", "#1F6032", "#9C6500"
GREY, LINE, MUTE = "#B9C4D2", "#D6DEE8", "#5A6878"
RED = "#A6192E"

plt.rcParams.update({
    "font.family": "Segoe UI",
    "font.size": 11,
    "axes.edgecolor": LINE,
    "axes.labelcolor": NAVY,
    "axes.titlecolor": NAVY,
    "text.color": NAVY,
    "xtick.color": MUTE,
    "ytick.color": MUTE,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

DEC = 3  # decimales con coma


def dec(x, n=DEC):
    s = f"{x:,.{n}f}"
    return s.replace(",", "\u00a0").replace(".", ",")


def carga_p1():
    p = os.path.join(RAIZ, "evidencias", "07-metricas", "07_kpi-report.json")
    d = json.load(open(p, encoding="utf-8"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    vals = np.array([x["mttd_seconds"] for x in det], float)
    scen = [x["scenario"] for x in det]
    return vals, scen, d["kpis"]["MTTD"]


def carga_p2(tag):
    p = os.path.join(RAIZ, "evidencias", f"v2.0-it1/07-metricas/kpi_report.json" if tag == "it1"
                     else "v2.1-it2/07-metricas/kpi_report.json")
    d = json.load(open(p, encoding="utf-8"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    vals = np.array([x["mttd_seconds"] for x in det], float)
    scen = [x["scenario"] for x in det]
    return vals, scen, d["kpis"]["MTTD"]


def descriptivos(v):
    from scipy.stats import skew, kurtosis
    return {
        "n": len(v),
        "media": float(np.mean(v)),
        "mediana": float(np.median(v)),
        "min": float(np.min(v)),
        "max": float(np.max(v)),
        "desv": float(np.std(v, ddof=1)),
        "cv": float(np.std(v, ddof=1) / np.mean(v)),
        "sesgo": float(skew(v, bias=False)),
        "curtosis": float(kurtosis(v, bias=False)),
    }


def normalidad(v, etiqueta):
    """Bateria de pruebas de normalidad sobre los valores observados."""
    out = {}
    W, p_sw = stats.shapiro(v)
    out["shapiro_wilk"] = {"W": float(W), "p": float(p_sw),
                           "veredicto": "no se rechaza la normalidad" if p_sw > 0.05 else "se rechaza la normalidad"}
    if len(v) >= 8:
        k2, p_k2 = stats.normaltest(v)
        out["dagostino_k2"] = {"k2": float(k2), "p": float(p_k2),
                               "veredicto": "no se rechaza la normalidad" if p_k2 > 0.05 else "se rechaza la normalidad"}
    else:
        out["dagostino_k2"] = {"k2": None, "p": None,
                               "veredicto": "no aplicable, la prueba exige al menos ocho observaciones"}
    jb, p_jb = stats.jarque_bera(v)
    out["jarque_bera"] = {"jb": float(jb), "p": float(p_jb),
                          "veredicto": "no se rechaza la normalidad" if p_jb > 0.05 else "se rechaza la normalidad"}
    # la escala logaritmica exige valores positivos; los nulos se desplazan antes
    if np.any(v <= 0):
        shift = float(abs(v[v <= 0].min()) + 1e-3)
        lv = np.log10(v + shift)
        out["log10_desplazamiento"] = shift
    else:
        shift = 0.0
        lv = np.log10(v)
    Wl, p_l = stats.shapiro(lv)
    out["shapiro_log10"] = {"W": float(Wl), "p": float(p_l),
                            "desplazamiento": shift,
                            "veredicto": "no se rechaza la normalidad" if p_l > 0.05 else "se rechaza la normalidad"}
    out["etiqueta"] = etiqueta
    return out


def nula_wilcoxon(n):
    """Distribucion nula exacta de W+ bajo H0 para una muestra de n pares,
    enumerando las 2^n configuraciones de signos."""
    rangos = list(range(1, n + 1))
    conteo = {}
    for signos in itertools.product([0, 1], repeat=n):
        w = sum(r for r, s in zip(rangos, signos) if s == 1)
        conteo[w] = conteo.get(w, 0) + 1
    total = 2 ** n
    soporte = sorted(conteo)
    probs = {w: conteo[w] / total for w in soporte}
    return soporte, probs, total


# ────────────────────────────────────────────────────────────────────────────
print("=" * 78)
print("A. PROTOTIPO 1 — TaxFisco Research Lab")
print("=" * 78)
v1, s1, k1 = carga_p1()
d1 = descriptivos(v1)
print(f"  n = {d1['n']}  media = {dec(d1['media'])} s  mediana = {dec(d1['mediana'])} s")
print(f"  min = {dec(d1['min'])}  max = {dec(d1['max'])}  desv = {dec(d1['desv'])}  CV = {dec(d1['cv'])}")
print(f"  sesgo = {dec(d1['sesgo'])}  curtosis = {dec(d1['curtosis'])}")
n1 = normalidad(v1, "Prototipo 1 (9 escenarios medidos)")
for k, v in n1.items():
    if k == "etiqueta":
        continue
    print(f"  {k:16s} {v} ")

print()
print("=" * 78)
print("B. PROTOTIPO 2 — Servicio de Impuestos Nacionales")
print("=" * 78)
v2a, s2a, k2a = carga_p2("it1")
v2b, s2b, k2b = carga_p2("it2")
d2a, d2b = descriptivos(v2a), descriptivos(v2b)
print(f"  vuelta 1  n = {d2a['n']}  media = {dec(d2a['media'])}  mediana = {dec(d2a['mediana'])}")
print(f"  medicion  n = {d2b['n']}  media = {dec(d2b['media'])}  mediana = {dec(d2b['mediana'])}")
n2a = normalidad(v2a, "P2 vuelta 1 (4 medidos)")
n2b = normalidad(v2b, "P2 medicion final (10 medidos)")
for etq, dic in (("vuelta 1", n2a), ("medicion final", n2b)):
    print(f"  [{etq}]")
    for k, v in dic.items():
        if k == "etiqueta":
            continue
        print(f"    {k:16s} {v} ")

# ────────────────────────────────────────────────────────────────────────────
print()
print("=" * 78)
print("C. DISTRIBUCION NULA DE W+ BAJO H0 (n = 4 pares)")
print("=" * 78)
sop, probs, total = nula_wilcoxon(4)
for w in sop:
    print(f"  W+ = {w:>2}  P = {probs[w]:.4f}  ({probs[w]*total:.0f}/{total})")
W_obs = 0
p_bilat = 2 * probs[W_obs] / 1  # dos colas simetricas
print(f"  W observado = {W_obs}   p bilateral = {p_bilat:.4f}   p minimo alcanzable = {2/2**4:.4f}")

# verificacion con scipy
pareados = [(16.851, 15.910), (1.214, 1.095), (1.734, 1.145), (1.063, 0.264)]
a = [x for x, _ in pareados]
b = [y for _, y in pareados]
res2 = stats.wilcoxon(a, b, alternative="two-sided", method="exact")
res1 = stats.wilcoxon(a, b, alternative="greater", method="exact")
print(f"  scipy wilcoxon bilateral  : W = {res2.statistic}  p = {res2.pvalue:.4f}")
print(f"  scipy wilcoxon unilateral (medicion posterior < vuelta 1): W = {res1.statistic}  p = {res1.pvalue:.4f}")
assert abs(res2.pvalue - p_bilat) < 1e-9, "discrepancia con scipy"
assert abs(res1.pvalue - p_bilat / 2) < 1e-9, "discrepancia unilateral con scipy"

# la prueba de Wilcoxon solo usa rangos, de modo que es invariante ante
# transformaciones monotonas: repetirla sobre log10 reproduce el mismo W
lg_a = np.log10(a)
lg_b = np.log10(b)
res_log = stats.wilcoxon(lg_a, lg_b, alternative="two-sided", method="exact")
razon = 10 ** (lg_a - lg_b)
print(f"  wilcoxon sobre log10 (invariancia por rangos): W = {res_log.statistic}  p = {res_log.pvalue:.4f}")
print("  razon geometrica de reduccion por par (10^(log antes - log despues)):")
for esc, x, y in [("S01", 16.851, 15.910), ("S02", 1.214, 1.095),
                  ("S05", 1.734, 1.145), ("S07", 1.063, 0.264)]:
    r = 10 ** (np.log10(x) - np.log10(y))
    print(f"    {esc}: razon {r:.4f}  (reduccion del {100*(1-1/r):.1f} %)")
razones = [10 ** (np.log10(x) - np.log10(y)) for x, y in
           [(16.851, 15.910), (1.214, 1.095), (1.734, 1.145), (1.063, 0.264)]]
razon_geo = float(np.exp(np.mean(np.log(razones))))
print(f"  razon geometrica media de los cuatro pares: {razon_geo:.4f} "
      f"(reduccion multiplicativa del {100*(1-1/razon_geo):.1f} %)")
t_log = stats.ttest_rel(lg_a, lg_b)
print(f"  t pareado sobre log10 (sensibilidad): t = {t_log.statistic:.4f}  p = {t_log.pvalue:.4f}  gl = {len(a)-1}")

# ────────────────────────────────────────────────────────────────────────────
# FIGURA 1: distribucion observada del Prototipo 1 + curva normal + Q-Q
# ────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(1, 3, figsize=(11.52, 6.0), dpi=100)
fig.subplots_adjust(left=0.055, right=0.985, top=0.84, bottom=0.115, wspace=0.34)

# A) histograma lineal + normal ajustada
axA = ax[0]
bins = [0, 20, 40, 60, 80, 100, 140, 200, 280]
axA.hist(v1, bins=bins, color=NAVY2, edgecolor="white", linewidth=1.2, zorder=3)
x = np.linspace(0, 280, 600)
pdf = stats.norm.pdf(x, d1["media"], d1["desv"])
axA.plot(x, pdf * len(v1) * (bins[1] - bins[0]), color=RED, lw=2, ls="--", zorder=4)
axA.axvline(d1["media"], color=RED, lw=1.4, ls=":", zorder=4)
axA.axvline(d1["mediana"], color=GREEN, lw=1.8, zorder=4)
axA.set_title("A. Histograma y curva normal ajustada", fontsize=11.5, pad=9, loc="left")
axA.set_xlabel("Tiempo de deteccion (s)")
axA.set_ylabel("Escenarios")
axA.grid(axis="y", color=LINE, lw=0.8, zorder=0)
axA.set_axisbelow(True)
for s_ in ("top", "right"):
    axA.spines[s_].set_visible(False)
ylimA = axA.get_ylim()
legA = axA.legend(handles=[
    Line2D([0], [0], color=GREEN, lw=1.8, label=f"mediana {dec(d1['mediana'])} s"),
    Line2D([0], [0], color=RED, lw=1.5, ls=":", label=f"media {dec(d1['media'])} s"),
    Line2D([0], [0], color=RED, lw=2, ls="--", label="normal ajustada"),
], loc="upper right", fontsize=9.5, frameon=True, facecolor="#F7F9FC",
    edgecolor=LINE, framealpha=1)
legA.get_frame().set_linewidth(1)

# B) grafico Q-Q contra la normal
axB = ax[1]
stats.probplot(v1, dist="norm", plot=axB)
axB.get_lines()[0].set(marker="o", color=NAVY, markersize=6, zorder=3)
axB.get_lines()[1].set(color=RED, lw=1.8, ls="--", zorder=2)
axB.set_title("")
axB.set_title("B. Grafico Q-Q frente a la normal", fontsize=11.5, pad=9, loc="left")
axB.set_xlabel("Teoricos normales")
axB.set_ylabel("Muestra (s)")
axB.grid(color=LINE, lw=0.8, zorder=0)
axB.set_axisbelow(True)
for s_ in ("top", "right"):
    axB.spines[s_].set_visible(False)
axB.text(0.03, 0.94,
         f"Shapiro-Wilk W = {dec(n1['shapiro_wilk']['W'], 3)}\np = 0,0000425",
         transform=axB.transAxes, va="top", fontsize=10, color=RED,
         bbox=dict(boxstyle="round,pad=0.4", fc="#FBF3F4", ec=RED, lw=1))

# C) diagrama de puntos en escala logaritmica
axC = ax[2]
orden = np.argsort(v1)
vs = v1[orden]
ss = [s1[i] for i in orden]
y = np.arange(1, len(vs) + 1)
axC.scatter(vs, y, s=64, color=NAVY, zorder=3)
for xv, yv, sc in zip(vs, y, ss):
    axC.annotate(sc.split("-")[0], (xv, yv), textcoords="offset points", xytext=(0, 10),
                 ha="center", fontsize=9.5, color=NAVY2, fontweight="bold")
axC.axvline(d1["mediana"], color=GREEN, lw=1.8, ls="-", zorder=2)
axC.axvline(d1["media"], color=RED, lw=1.6, ls="--", zorder=2)
axC.set_xscale("log")
axC.set_yticks([])
axC.set_title("C. Escala logaritmica, media y mediana", fontsize=11.5, pad=9, loc="left")
axC.set_xlabel("Tiempo de deteccion (s, escala log)")
axC.grid(axis="x", color=LINE, lw=0.8, zorder=0)
axC.set_axisbelow(True)
for s_ in ("top", "right", "left"):
    axC.spines[s_].set_visible(False)
axC.text(d1["mediana"] * 1.13, 0.45, "mediana", color=GREEN, fontsize=9.5, rotation=90, va="bottom")
axC.text(d1["media"] * 0.91, 0.45, "media", color=RED, fontsize=9.5, rotation=90, va="bottom", ha="right")
axC.set_ylim(0, len(vs) + 1.3)

fig.suptitle("Prototipo 1: distribucion de los nueve tiempos de deteccion frente a la normal",
             fontsize=13.5, color=NAVY, x=0.055, ha="left", y=0.965)
fig.text(0.055, 0.015,
         "Fuente: elaboracion propia con base en evidencias/07-metricas/07_kpi-report.json",
         fontsize=9, color=MUTE, ha="left")
ruta1 = os.path.join(GRAFI, "p1-distribucion-deteccion.png")
fig.savefig(ruta1, dpi=100)
plt.close(fig)
print(f"\n  figura 1 -> {ruta1}")

# ────────────────────────────────────────────────────────────────────────────
# FIGURA 2: distribucion nula de W+ bajo H0 con el estadistico observado
# ────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.52, 5.4), dpi=100)
fig.subplots_adjust(left=0.075, right=0.985, top=0.85, bottom=0.155)

ancho = 0.62
colores = [GREEN if w in (W_obs, 10 - W_obs) else NAVY2 for w in sop]
ax.bar(sop, [probs[w] for w in sop], width=ancho, color=colores,
       edgecolor="white", linewidth=1.2, zorder=3)
for w in sop:
    ax.text(w, probs[w] + 0.004, f"{probs[w]:.4f}".replace(".", ","),
            ha="center", va="bottom", fontsize=9.5,
            color=GREEN if w in (W_obs, 10 - W_obs) else MUTE)

ax.axvline(W_obs, color=GREEN, lw=1.6, ls="--", zorder=4)
ax.annotate(f"Estadistico observado\nW = {W_obs}", xy=(W_obs, probs[W_obs]),
            xytext=(1.9, 0.128), fontsize=10.5, color=GREEN, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.5))

ax.set_xlabel("W+  (suma de rangos de las reducciones observadas)")
ax.set_ylabel("Probabilidad bajo H0")
ax.set_title("Distribucion nula exacta de W+ bajo H0 para n = 4 pares  (16 configuraciones equiprobables)",
             fontsize=12.5, color=NAVY, loc="left", pad=12)
ax.set_xticks(sop)
ax.set_ylim(0, 0.175)
ax.grid(axis="y", color=LINE, lw=0.8, zorder=0)
ax.set_axisbelow(True)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)

ax.text(0.985, 0.965,
        "p bilateral = 0,1250  (2/16)\n"
        "cola inferior: P(W+ = 0) = 1/16\n"
        "cola superior: P(W+ = 10) = 1/16\n"
        "p minimo alcanzable con n = 4: 0,1250",
        transform=ax.transAxes, ha="right", va="top", fontsize=10, color=NAVY,
        bbox=dict(boxstyle="round,pad=0.55", fc="#F2F7F2", ec=GREEN, lw=1.2))

fig.text(0.075, 0.018,
         "Fuente: elaboracion propia. Distribucion nula de la prueba de Wilcoxon de los rangos con signo emparejada, enumeracion exacta de las 2^4 configuraciones de signos.",
         fontsize=9, color=MUTE, ha="left")
ruta2 = os.path.join(GRAFI, "nula-wilcoxon-n4.png")
fig.savefig(ruta2, dpi=100)
plt.close(fig)
print(f"  figura 2 -> {ruta2}")

# ────────────────────────────────────────────────────────────────────────────
# FIGURA 3: distribucion observada del Prototipo 2 (medicion final)
# ────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(1, 3, figsize=(11.52, 6.0), dpi=100)
fig.subplots_adjust(left=0.055, right=0.985, top=0.84, bottom=0.115, wspace=0.34)

axA = ax[0]
bins = [0, 1, 2, 4, 8, 16]
axA.hist(v2b, bins=bins, color=GREEN, edgecolor="white", linewidth=1.2, zorder=3)
x = np.linspace(0, 16, 500)
pdf = stats.norm.pdf(x, d2b["media"], d2b["desv"])
axA.plot(x, pdf * len(v2b) * (bins[1] - bins[0]), color=RED, lw=2, ls="--", zorder=4)
axA.axvline(d2b["media"], color=RED, lw=1.4, ls=":", zorder=4)
axA.axvline(d2b["mediana"], color=NAVY, lw=1.8, zorder=4)
axA.set_title("A. Histograma y curva normal ajustada", fontsize=11.5, pad=9, loc="left")
axA.set_xlabel("Tiempo de deteccion (s)")
axA.set_ylabel("Escenarios")
axA.grid(axis="y", color=LINE, lw=0.8, zorder=0)
axA.set_axisbelow(True)
for s_ in ("top", "right"):
    axA.spines[s_].set_visible(False)
ylimB = axA.get_ylim()
legB = axA.legend(handles=[
    Line2D([0], [0], color=NAVY, lw=1.8, label=f"mediana {dec(d2b['mediana'])} s"),
    Line2D([0], [0], color=RED, lw=1.5, ls=":", label=f"media {dec(d2b['media'])} s"),
    Line2D([0], [0], color=RED, lw=2, ls="--", label="normal ajustada"),
], loc="upper right", fontsize=9.5, frameon=True, facecolor="#F4F8F4",
    edgecolor=LINE, framealpha=1)
legB.get_frame().set_linewidth(1)

axB = ax[1]
stats.probplot(v2b, dist="norm", plot=axB)
axB.get_lines()[0].set(marker="o", color=GREEN, markersize=6, zorder=3)
axB.get_lines()[1].set(color=RED, lw=1.8, ls="--", zorder=2)
axB.set_title("")
axB.set_title("B. Grafico Q-Q frente a la normal", fontsize=11.5, pad=9, loc="left")
axB.set_xlabel("Teoricos normales")
axB.set_ylabel("Muestra (s)")
axB.grid(color=LINE, lw=0.8, zorder=0)
axB.set_axisbelow(True)
for s_ in ("top", "right"):
    axB.spines[s_].set_visible(False)
axB.text(0.03, 0.94,
         f"Shapiro-Wilk W = {dec(n2b['shapiro_wilk']['W'], 3)}\np = 0,0000008",
         transform=axB.transAxes, va="top", fontsize=10, color=RED,
         bbox=dict(boxstyle="round,pad=0.4", fc="#FBF3F4", ec=RED, lw=1))

axC = ax[2]
y = np.arange(1, len(v2b) + 1)
pos = {s: i for i, s in enumerate(s2b)}
axC.scatter(v2b, y, s=64, color=GREEN, zorder=3, label="Medicion final")
axC.scatter([v2a[list(s2a).index(s)] for s in s2a],
            [pos[s] for s in s2a], s=64, marker="D",
            color=AMBER, zorder=4, label="Vuelta 1 (4 medidos)")
for sc, yv in zip(s2b, y):
    axC.annotate(sc.split("-")[0], (v2b[list(s2b).index(sc)], yv),
                 textcoords="offset points", xytext=(0, 10),
                 ha="center", fontsize=9.5, color=GREEN, fontweight="bold")
axC.axvline(d2b["mediana"], color=NAVY, lw=1.8, zorder=2)
axC.set_xscale("log")
axC.set_yticks([])
axC.set_title("C. Escala logaritmica, dos vueltas", fontsize=11.5, pad=9, loc="left")
axC.set_xlabel("Tiempo de deteccion (s, escala log)")
axC.grid(axis="x", color=LINE, lw=0.8, zorder=0)
axC.set_axisbelow(True)
for s_ in ("top", "right", "left"):
    axC.spines[s_].set_visible(False)
axC.legend(frameon=False, fontsize=9.5, loc="lower right")
axC.set_ylim(0, len(v2b) + 1.1)

fig.suptitle("Prototipo 2: distribucion de los diez tiempos de deteccion de la medicion final frente a la normal",
             fontsize=13.5, color=NAVY, x=0.055, ha="left", y=0.965)
fig.text(0.055, 0.015,
         "Fuente: elaboracion propia con base en evidencias/v2.1-it2/07-metricas/kpi_report.json y evidencias/v2.0-it1/07-metricas/kpi_report.json",
         fontsize=9, color=MUTE, ha="left")
ruta3 = os.path.join(GRAFI, "p2-distribucion-deteccion.png")
fig.savefig(ruta3, dpi=100)
plt.close(fig)
print(f"  figura 3 -> {ruta3}")

# ────────────────────────────────────────────────────────────────────────────
resumen = {
    "prototipo_1": {"datos": d1, "normalidad": n1, "valores": v1.tolist(), "escenarios": s1},
    "prototipo_2_vuelta_1": {"datos": d2a, "normalidad": n2a, "valores": v2a.tolist()},
    "prototipo_2_medicion_final": {"datos": d2b, "normalidad": n2b, "valores": v2b.tolist()},
    "nula_wilcoxon_n4": {"soporte": sop, "probabilidades": probs,
                         "w_observado": W_obs, "p_bilateral": p_bilat,
                         "p_minimo": 2 / 2 ** 4, "p_unilateral": p_bilat / 2},
}
with open(os.path.join(RAIZ, "resultados-prototipos", "analisis_distribucion.json"),
          "w", encoding="utf-8") as fh:
    json.dump(resumen, fh, ensure_ascii=False, indent=2)
print("\n  resumen -> resultados-prototipos/analisis_distribucion.json")
