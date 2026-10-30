# -*- coding: utf-8 -*-
"""Comprobacion de hipotesis: prueba de Wilcoxon de los rangos con signo emparejada.

Datos: segunda vuelta del laboratorio del SIN (dashboard resultados_prototipo_2),
los cuatro escenarios con medicion en ambos momentos.
Fuente de los pares: resultados-prototipos/prototipo-2/dashboard-resultados_prototipo_2.html
"""
import itertools
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

PARES = [
    ("S01", 16.851, 15.910),
    ("S02", 1.214, 1.095),
    ("S05", 1.734, 1.145),
    ("S07", 1.063, 0.264),
]

n = len(PARES)
d = [a - b for _, a, b in PARES]          # d > 0 => reduccion del tiempo de deteccion

print("=== 1. DATOS EMPAREJADOS (vuelta 1 -> medicion posterior), en segundos ===")
for (s, a, b), dd in zip(PARES, d):
    red = (a - b) / a * 100
    print(f"  {s}: {a:>8.3f} -> {b:>8.3f}   d = {dd:+.3f}   reduccion = {red:5.1f} %")

# --- rangos de |d| ---
absd = sorted(range(n), key=lambda i: abs(d[i]))
ranks = [0.0] * n
i = 0
while i < n:
    j = i
    while j + 1 < n and abs(absd[j + 1] - abs(d[absd[i]])) < 1e-12:
        j += 1
    r = (i + 1 + j + 1) / 2.0
    for k in range(i, j + 1):
        ranks[absd[k]] = r
    i = j + 1

Wpos = sum(r for r, dd in zip(ranks, d) if dd > 0)
Wneg = sum(r for r, dd in zip(ranks, d) if dd < 0)
W = min(Wpos, Wneg)

print("\n=== 2. ESTADISTICO DE LA PRUEBA ===")
print(f"  rangos de |d|            : {ranks}")
print(f"  W+ (reducciones)         = {Wpos:g}")
print(f"  W- (aumentos)            = {Wneg:g}")
print(f"  W  = min(W+, W-)          = {W:g}")

# --- p exacto por enumeracion de las 2^n configuraciones de signos ---
def exact_two_sided(w, nn):
    tot = 2 ** nn
    cnt = 0
    for signs in itertools.product([0, 1], repeat=nn):
        s = sum(r for r, bit in zip(sorted(range(nn), key=lambda i: 0), signs) if bit)
        # se recalcula de forma explicita abajo
        cnt = cnt
    # enumeracion explicita
    cnt = 0
    for signs in itertools.product([0, 1], repeat=nn):
        # signos sobre los rangos ya ordenados
        rr = sorted(ranks)
        wpos = sum(r for r, bit in zip(rr, signs) if bit == 1)
        wneg = sum(r for r, bit in zip(rr, signs) if bit == 0)
        if min(wpos, wneg) <= w:
            cnt += 1
    return cnt / tot

p_two = exact_two_sided(W, n)
p_one = exact_two_sided(W, n) / 2.0   # unilateral en la direccion de la hipotesis

print(f"  p exacto bilateral       = {p_two:.4f}")
print(f"  p exacto unilateral      = {p_one:.4f}  (H1: reduccion del tiempo)")
print(f"  p minimo alcanzable (bilateral, n={n}) = {2/2**n:.4f}")

# --- contraste con scipy si esta disponible ---
try:
    from scipy.stats import wilcoxon
    res = wilcoxon([a for _, a, _ in PARES], [b for _, _, b in PARES],
                    alternative="two-sided", method="exact")
    res1 = wilcoxon([a for _, a, _ in PARES], [b for _, _, b in PARES],
                     alternative="less", method="exact")
    print(f"\n  scipy wilcoxon bilateral : statistic={res.statistic}  p={res.pvalue:.4f}")
    print(f"  scipy wilcoxon unilateral: statistic={res1.statistic}  p={res1.pvalue:.4f}")
    try:
        from scipy.stats import ttest_rel
        t = ttest_rel([a for _, a, _ in PARES], [b for _, _, b in PARES])
        print(f"  t pareado (sensibilidad) : t={t.statistic:.4f}  p={t.pvalue:.4f}  df={len(PARES)-1}")
    except Exception as e:
        print("  t pareado: no disponible", e)
except ImportError:
    print("\n  scipy no instalado: se reportan los valores exactos calculados por enumeracion.")

# --- tamano del efecto ---
r_rb = (Wpos - Wneg) / (Wpos + Wneg)
print(f"\n=== 3. TAMANO DEL EFECTO ===")
print(f"  correlacion rangos-biserial pareada r = (W+ - W-)/(W+ + W-) = {r_rb:.3f}")

# --- estimador de Hodges-Lehmann de la mediana de las diferencias ---
pairs = [(d[i] + d[j]) / 2 for i, j in itertools.combinations(range(n), 2)]
pairs.sort()
hl = (pairs[len(pairs)//2 - 1] + pairs[len(pairs)//2]) / 2 if len(pairs) % 2 == 0 else pairs[len(pairs)//2]
print(f"  valores de medias por pares : {[round(p,3) for p in pairs]}")
print(f"  estimador Hodges-Lehmann (mediana de d) = {hl:.3f} s")

# --- descriptivos ---
import statistics as st
antes = [a for _, a, _ in PARES]
desp = [b for _, _, b in PARES]
print(f"\n=== 4. DESCRIPTIVOS DEL SUBMUESTRO EMPAREJADO (n={n}) ===")
print(f"  vuelta 1      : media {st.mean(antes):.4f} s   mediana {st.median(antes):.4f} s")
print(f"  medicion final: media {st.mean(desp):.4f} s   mediana {st.median(desp):.4f} s")
print(f"  reduccion media de la media: {st.mean(antes)-st.mean(desp):.4f} s ({((st.mean(antes)-st.mean(desp))/st.mean(antes))*100:.2f} %)")
print(f"  desviacion tipica de las diferencias d = {st.pstdev(d):.4f} (poblacional) / {st.stdev(d):.4f} (muestral)")

# --- prueba de signos (binomial) como control ---
from math import comb
p_sign = 2 * (1 / 2 ** n)
print(f"\n=== 5. PRUEBA DE SIGNOS (control) ===")
print(f"  4 de 4 diferencias tienen el mismo signo -> p bilateral exacto = {p_sign:.4f}")


# --- distribucion t (implementacion propia, sin scipy) ---
def _betacf(a, b, x):
    MAXIT, EPS, FPMIN = 200, 3.0e-16, 1.0e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < EPS:
            break
    return h

def betai(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
             + a * math.log(x) + b * math.log(1.0 - x))
    bt = math.exp(lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b

def t_sf_two_sided(t, df):
    """Valor p bilateral exacto para la distribucion t de Student."""
    x = df / (df + t * t)
    return betai(df / 2.0, 0.5, x)

import math
mean_d = st.mean(d)
sd_d = st.stdev(d)
se = sd_d / math.sqrt(n)
t_stat = mean_d / se
p_t = t_sf_two_sided(t_stat, n - 1)
print(f"\n=== 6. ANALISIS DE SENSIBILIDAD: t PAREADO (parametrico) ===")
print(f"  t = {mean_d:.4f} / ({sd_d:.4f}/sqrt({n})) = {t_stat:.4f}   gl = {n-1}")
print(f"  p bilateral = {p_t:.4f}   -> {'alcanza' if p_t < 0.05 else 'NO alcanza'} el 0,05")
crit = 3.182446   # t critico bilateral al 0,05 con gl = 3
print(f"  t critico bilateral 0,05 con gl=3 = {crit}  -> el estadistico {'supera' if t_stat > crit else 'no supera'} el valor critico")

# --- tamaño de muestra necesario para alcanzar significancia ---
print(f"\n=== 7. TAMAÑO DE MUESTRA NECESARIO ===")
for k in range(4, 11):
    pmin = 2 / 2 ** k
    print(f"  n = {k:>2} pares, caso de reduccion en todos: p minimo = {pmin:.5f} "
          f"-> {'alcanza 0,05' if pmin < 0.05 else 'no alcanza 0,05'}")
print("  n minimo para que la prueba no parametrica alcance el 0,05 con todas las reducciones: "
      f"{min(k for k in range(4, 40) if 2/2**k < 0.05)}")
print(f"  con los 10 escenarios de la campaña, caso de reduccion en todos: p = {2/2**10:.5f}")


out = {
    "n": n,
    "pares": [{"escenario": s, "antes": a, "despues": b, "diferencia": round(x, 6)}
              for (s, a, b), x in zip(PARES, d)],
    "rangos": ranks,
    "W_pos": Wpos, "W_neg": Wneg, "W": W,
    "p_bilateral_exacto": round(p_two, 6),
    "p_unilateral_exacto": round(p_one, 6),
    "p_minimo_alcanzable_bilateral": round(2 / 2 ** n, 6),
    "r_rangos_biserial": round(r_rb, 6),
    "hodges_lehmann_mediana_d": round(hl, 6),
    "media_antes": round(st.mean(antes), 6),
    "media_despues": round(st.mean(desp), 6),
}
with open(r"F:\Maestria\tesis\taxfisco-research-lab\resultados-prototipos\_wilcoxon_resultado.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
print("\nresultado guardado en _wilcoxon_resultado.json")
