# -*- coding: utf-8 -*-
"""Compara el estimador de la log-logistica del script principal con el perfil depurado."""
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


def u_por_b(t, b):
    def h(u):
        return 2.0 * expit(b * (t - u)).sum() - len(t)
    u_lo, u_hi = t.min() - 15.0, t.max() + 15.0
    if h(u_lo) < 0:
        return u_lo
    if h(u_hi) > 0:
        return u_hi
    return float(optimize.brentq(h, u_lo, u_hi, xtol=1e-12))


def ll_directa(a, b):
    w = t - np.log(a)
    z = b * w
    return float(np.sum(np.log(b) - np.log(a) + (b - 1.0) * w - 2.0 * np.logaddexp(0.0, z)))


print("  b          u(FOC)          a            ll por FOC       ll en a=2,96755")
for b in (0.40, 0.55, 0.60, 0.65, 0.67556, 0.70, 0.75, 0.80, 0.90, 1.00):
    u = u_por_b(t, b)
    a = np.exp(u)
    ll = ll_directa(a, b)
    print(f"  {b:>7.4f} {u:>12.5f} {a:>12.5f} {ll:>16.5f} {ll_directa(2.96755, b):>16.5f}")

print("\n  Maximizacion libre sobre (a, b) con Nelder-Mead:")
def nll(q):
    return -ll_directa(np.exp(q[0]), np.exp(q[1]))


r = optimize.minimize(nll, x0=[np.log(2.96755), np.log(0.67556)], method="Nelder-Mead",
                      options={"maxiter": 60000, "maxfev": 60000, "xatol": 1e-12, "fatol": 1e-14})
print(f"    a = {np.exp(r.x[0]):.6f}   b = {np.exp(r.x[1]):.6f}   ll = {-r.fun:.6f}")

print("\n  Barrido fino del perfil:")
bs = np.exp(np.linspace(np.log(0.05), np.log(50.0), 20001))
vals = np.array([ll_directa(np.exp(u_por_b(t, b)), b) for b in bs])
i = int(np.argmax(vals))
print(f"    b = {bs[i]:.6f}   ll = {vals[i]:.6f}   (a = {np.exp(u_por_b(t, bs[i])):.6f})")
print(f"    cinco mejores b: {np.round(bs[np.argsort(vals)[-5:]], 4)}")
print(f"    cinco mejores ll: {np.round(np.sort(vals)[-5:], 5)}")
