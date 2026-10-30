# -*- coding: utf-8 -*-
"""Depuracion del perfil de verosimilitud de la log-logistica."""
import json
import os
import sys

import numpy as np
from scipy import optimize
from scipy.special import expit

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"


def cargar(ruta):
    d = json.load(open(ruta, encoding="utf-8-sig"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    return np.array([x["mttd_seconds"] for x in det], float)


P1 = cargar(os.path.join(RAIZ, "evidencias", "07-metricas", "07_kpi-report.json"))
x = P1[P1 > 0]
t = np.log(x)
n = len(t)


def logpdf_ll(a, b, tt):
    w = tt - np.log(a)
    z = b * w
    return np.log(b) - np.log(a) + (b - 1.0) * w - 2.0 * np.logaddexp(0.0, z)


def u_por_b(b):
    def h(u):
        return 2.0 * expit(b * (t - u)).sum() - n
    lo, hi = t.min() - 15.0, t.max() + 15.0
    if h(lo) < 0:
        return lo
    if h(hi) > 0:
        return hi
    return float(optimize.brentq(h, lo, hi, xtol=1e-12))


def perfil(b):
    u = u_por_b(b)
    return float(logpdf_ll(np.exp(u), b, t).sum()), float(np.exp(u))


print(f"n = {n}")
print("\n  b            a            log-verosimilitud")
for b in (0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0, 500.0):
    ll, a = perfil(b)
    print(f"  {b:>8.3f} {a:>12.5f} {ll:>18.5f}")

print("\n  Ahora la escala libre, maximizando sobre a y b sin restriccion:")
def nll(q):
    a, b = np.exp(q[0]), np.exp(q[1])
    return -float(logpdf_ll(a, b, t).sum())


for caja, etiqueta in (
        ([(-20, 20), (-10, 10)], "caja amplia"),
        ([(np.log(0.05), np.log(400)), (np.log(0.05), np.log(500))], "caja con forma hasta 500"),
):
    r = optimize.minimize(nll, x0=[np.log(0.826), 0.0], method="L-BFGS-B", bounds=caja,
                          options={"maxiter": 50000, "ftol": 1e-16, "gtol": 1e-14})
    a, b = np.exp(r.x[0]), np.exp(r.x[1])
    print(f"  {etiqueta:<28} a = {a:>12.5f}  b = {b:>12.5f}  log-veros = {-r.fun:>14.5f}")

print("\n  Comprobacion directa de la verosimilitud en el punto con forma enorme:")
for b in (50.0, 200.0):
    # se ajusta a sobre una rejilla fina, sin usar la condicion de primer orden
    mejor = None
    for a in np.exp(np.linspace(np.log(1e-4), np.log(400.0), 20001)):
        ll = float(logpdf_ll(a, b, t).sum())
        if mejor is None or ll > mejor[0]:
            mejor = (ll, a)
    print(f"  b = {b:>7.1f}   maximo sobre la rejilla de a: log-veros = {mejor[0]:>14.5f}  a = {mejor[1]:.5f}")
