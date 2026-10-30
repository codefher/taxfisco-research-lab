# -*- coding: utf-8 -*-
"""Depuracion del perfil de verosimilitud de la Weibull con localizacion en cero."""
import json
import os
import sys

import numpy as np
from scipy import optimize
from scipy.special import logsumexp, gammaln

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"


def cargar(ruta):
    d = json.load(open(ruta, encoding="utf-8-sig"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    return np.array([x["mttd_seconds"] for x in det], float)


P1 = cargar(os.path.join(RAIZ, "evidencias", "07-metricas", "07_kpi-report.json"))
x = P1[P1 > 0]
n = len(x)
lx = np.log(x)
sum_lx = lx.sum()
print(f"n = {n}   suma de ln(x) = {sum_lx:.6f}")
print("valores ln:", np.array2string(lx, precision=4))


def perfil(c):
    log_lam = (logsumexp(c * lx) - np.log(n)) / c
    ll = n * np.log(c) - n * log_lam + (c - 1.0) * sum_lx - n
    return ll, float(np.exp(log_lam))


def perfil_directo(c):
    """Version sin identidades: todo calculado explicitamente."""
    lam = np.exp((logsumexp(c * lx) - np.log(n)) / c)
    ll = n * np.log(c) - n * np.log(lam) + (c - 1.0) * sum_lx - np.sum((x / lam) ** c)
    return ll, lam


print("\n  c          ll (identidad)      ll (directo)        lambda")
for c in (0.05, 0.1, 0.2, 0.3, 0.424, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 10.0, 50.0):
    l1, lam1 = perfil(c)
    l2, lam2 = perfil_directo(c)
    print(f"  {c:>6.3f}  {l1:>16.4f}  {l2:>16.4f}  {lam1:>14.6f}")

cs = np.exp(np.linspace(np.log(0.05), np.log(50.0), 481))
vals = np.array([perfil(c)[0] for c in cs])
i = int(np.argmax(vals))
print(f"\n  argmax del barrido: c = {cs[i]:.6f}   ll = {vals[i]:.6f}")
print(f"  vecino izquierdo  : c = {cs[i-1]:.6f}   ll = {vals[i-1]:.6f}")
print(f"  vecino derecho    : c = {cs[i+1]:.6f}   ll = {vals[i+1]:.6f}")

lo, hi = cs[i - 1], cs[i + 1]
res = optimize.minimize_scalar(lambda c: -perfil(c)[0], bounds=(lo, hi),
                               method="bounded", options={"xatol": 1e-12})
print(f"  refinado acotado  : c = {res.x:.6f}   ll = {-res.fun:.6f}   exito = {res.success}")
print(f"  argumento de la busqueda: lo = {lo}, hi = {hi}")

# comparacion directa con el estimador numerico del loglik
def nll(q):
    c, lam = abs(q[0]) + 1e-12, np.exp(q[1])
    return -(n * np.log(c) - n * np.log(lam) + (c - 1.0) * sum_lx - np.sum((x / lam) ** c))


r = optimize.minimize(nll, x0=[0.424, np.log(7.93)], method="Nelder-Mead",
                      options={"maxiter": 40000, "maxfev": 40000, "xatol": 1e-10, "fatol": 1e-12})
print(f"  optimizador numerico: c = {abs(r.x[0]):.6f}  lam = {np.exp(r.x[1]):.6f}  ll = {-r.fun:.6f}")
