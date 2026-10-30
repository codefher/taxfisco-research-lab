# -*- coding: utf-8 -*-
"""Verificacion independiente del ajuste de los modelos con soporte positivo.

Compara lo que devuelve stats.<dist>.fit(x, loc=0) en scipy 1.18.1 contra el
MLE analitico calculado a mano con el soporte anclado en cero. Si la biblioteca
no respeta loc=0, los AIC/BIC/pesos de Akaike de la version anterior del
analisis estan calculados sobre ajustes erroneos.
"""
import json
import os
import sys

import numpy as np
from scipy import stats

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"


def cargar(ruta):
    d = json.load(open(ruta, encoding="utf-8-sig"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    return np.array([x["mttd_seconds"] for x in det], float)


P1 = cargar(os.path.join(RAIZ, "evidencias", "07-metricas", "07_kpi-report.json"))
P2B = cargar(os.path.join(RAIZ, "evidencias", "v2.1-it2", "07-metricas", "kpi_report.json"))

print("=" * 78)
print("1. Que devuelve cada fit() con loc=0 en scipy 1.18.1")
print("=" * 78)

x = P1[P1 > 0]
print(f"\nPrototipo 1, valores positivos: {np.array2string(x, precision=3)}")
print(f"n = {len(x)}")

print("\n[1.1] lognormal")
p = stats.lognorm.fit(x, loc=0)
print(f"  fit(x, loc=0) -> s={p[0]:.6f} loc={p[1]:.6f} scale={p[2]:.6f}")
mu, sigma = float(np.mean(np.log(x))), float(np.std(np.log(x), ddof=1))
print(f"  MLE analitico -> s={sigma:.6f} loc=0 scale={np.exp(mu):.6f}")
print(f"  mu = {mu:.6f}  sigma = {sigma:.6f}")
print(f"  --> match? {abs(p[1]) < 1e-8 and abs(p[0]-sigma) < 1e-6}")

print("\n[1.2] gamma")
p = stats.gamma.fit(x, loc=0)
m, v = float(np.mean(x)), float(np.var(x, ddof=0))
print(f"  fit(x, loc=0) -> a={p[0]:.6f} loc={p[1]:.6f} scale={p[2]:.6f}")
print(f"  MLE analitico -> a={m**2/v:.6f} loc=0 scale={v/m:.6f}")

print("\n[1.3] weibull_min")
p = stats.weibull_min.fit(x, loc=0)
print(f"  fit(x, loc=0) -> c={p[0]:.6f} loc={p[1]:.6f} scale={p[2]:.6f}")

print("\n[1.4] expon")
p = stats.expon.fit(x, loc=0)
print(f"  fit(x, loc=0) -> {p}  (tupla de {len(p)} elementos)")
print(f"  MLE analitico -> lambda={1/m:.6f} loc=0 scale=1")
print(f"  --> con loc=0 y scale=1 solo queda libre lambda: {len(p) == 1}")

print("\n" + "=" * 78)
print("2. La firma floc todavia existe?")
print("=" * 78)
for nombre, dist in (("lognorm", stats.lognorm), ("gamma", stats.gamma),
                      ("weibull_min", stats.weibull_min), ("expon", stats.expon)):
    try:
        dist.pdf(np.array([1.0]), 1.0, 0.0, 1.0, floc=0)
        print(f"  {nombre}.pdf(..., floc=0) -> OK")
    except Exception as e:
        print(f"  {nombre}.pdf(..., floc=0) -> {type(e).__name__}: {e}")

print("\n" + "=" * 78)
print("3. Consecuencia: verosimilitud y cuantiles de la log-normal")
print("=" * 78)
p = stats.lognorm.fit(x, loc=0)
ll_fit = stats.lognorm.logpdf(x, *p).sum()
ll_manual = stats.lognorm.logpdf(x, sigma, 0.0, np.exp(mu)).sum()
print(f"  log-verosimilitud con fit()   = {ll_fit:.4f}")
print(f"  log-verosimilitud con MLE     = {ll_manual:.4f}")
print(f"  AIC con fit()   = {-2*ll_fit + 4:.4f}")
print(f"  AIC con MLE     = {-2*ll_manual + 4:.4f}")
print(f"  mediana con fit()   = {stats.lognorm.ppf(0.5, *p):.6f}")
print(f"  mediana con MLE     = {stats.lognorm.ppf(0.5, sigma, 0.0, np.exp(mu)):.6f}")
print(f"  p95 con fit()   = {stats.lognorm.ppf(0.95, *p):,.3f}")
print(f"  p95 con MLE     = {stats.lognorm.ppf(0.95, sigma, 0.0, np.exp(mu)):,.3f}")
print(f"  mediana empirica   = {np.median(x):.6f}")
