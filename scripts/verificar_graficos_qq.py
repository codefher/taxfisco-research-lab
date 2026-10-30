#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificación de los gráficos Q-Q (Figura 13) del análisis estadístico del MTTD.

Comprueba tres cosas:
  1. Que las coordenadas teóricas (posiciones de Blom) y los valores observados
     que el documento dibuja coinciden con los datos brutos del capítulo 4.4.
  2. Que la recta de referencia de cada panel es la recta de la normal ajustada
     a la muestra, y = media + desviacion * z, y no una regresion ajustada sobre
     los propios puntos observados.
  3. Que las escalas de los ejes (dominio y marcas) quedan dentro del dominio
     de datos y de la recta, y que las marcas son legibles.

Salida: resultados-prototypes/estadisticas_qq.json
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "resultados-prototipos" / "estadisticas_qq.json"

# ---------------------------------------------------------------- datos brutos
# Escenario: tiempo de deteccion en segundos.
P1 = [16.405, 0.826, 85.000, 260.108, 0.141, 0.824, 0.543, 0.533, 10.000]
P2V1 = [16.851, 1.214, 1.734, 1.063]
P2FIN = [0.000, 0.000, 0.137, 0.264, 0.460, 0.562, 0.646, 1.095, 1.145, 15.910]

# --------------------------------------------------------------- funciones


def blom(n: int) -> np.ndarray:
    """Cuantiles normales de las posiciones de Blom (i - 3/8) / (n + 1/4)."""
    i = np.arange(1, n + 1, dtype=float)
    p = (i - 0.375) / (n + 0.25)
    return stats.norm.ppf(p)


def tipo7(x: np.ndarray, p: float) -> float:
    """Cuantil con interpolacion lineal de tipo 7 (la de R y numpy)."""
    xs = np.sort(np.asarray(x, dtype=float))
    h = (len(xs) - 1) * p
    lo = int(math.floor(h))
    hi = int(math.ceil(h))
    if lo == hi:
        return float(xs[lo])
    return float(xs[lo] + (h - lo) * (xs[hi] - xs[lo]))


def escala_agradable(lo: float, hi: float, objetivo: int = 4):
    """Devuelve (min, max, marcas) con numeros redondos y paso comodo."""
    if hi <= lo:
        hi = lo + 1.0
    bruto = (hi - lo) / max(1, objetivo)
    magnitud = 10 ** math.floor(math.log10(bruto))
    for mult in (1, 2, 2.5, 5, 10):
        paso = mult * magnitud
        if paso >= bruto:
            break
    minimo = math.floor(lo / paso) * paso
    maximo = math.ceil(hi / paso) * paso
    marcas = []
    k = 0
    while minimo + k * paso <= maximo + paso * 1e-9:
        marcas.append(round(minimo + k * paso, 10))
        k += 1
    return minimo, maximo, marcas


def panel(clave: str, etiqueta: str, valores: list[float], transformada: str):
    """Construye el panel Q-Q y sus parametros de dibujo."""
    x = np.sort(np.asarray(valores, dtype=float))
    if transformada == "log":
        # el logaritmo natural no esta definido en cero: los escenarios con tiempo
        # 0,000 s quedan fuera del panel logaritmico (n = 8 en la medicion final)
        x = np.log(x[x > 0])
    z = blom(len(x))
    media = float(np.mean(x))
    sd = float(np.std(x, ddof=1))
    # recta de la normal ajustada a la muestra
    z_ext = np.array([z.min(), z.max()])
    y_ext = media + sd * z_ext
    # recta de cuartiles (qqline de R), para contraste
    z_q = [tipo7(z, 0.25), tipo7(z, 0.75)]
    y_q = [tipo7(x, 0.25), tipo7(x, 0.75)]
    # dominio comun de datos y recta
    y_lo = float(min(x.min(), y_ext.min()))
    y_hi = float(max(x.max(), y_ext.max()))
    if transformada == "lineal":
        # en segundos el eje no baja de cero: la recta se recorta al salir del panel
        y_lo = max(0.0, y_lo)
    y_min, y_max, marcas_y = escala_agradable(y_lo, y_hi)
    z_min, z_max, marcas_z = escala_agradable(float(z.min()), float(z.max()))
    return {
        "clave": clave,
        "etiqueta": etiqueta,
        "transformada": transformada,
        "n": len(x),
        "z": [round(float(v), 4) for v in z],
        "y": [round(float(v), 4) for v in x],
        "media": round(media, 4),
        "desviacion": round(sd, 4),
        "recta_normal": {
            "pendiente": round(sd, 4),
            "ordenada": round(media, 4),
            "z_extremos": [round(float(v), 4) for v in z_ext],
            "y_extremos": [round(float(v), 4) for v in y_ext],
        },
        "recta_cuartiles": {
            "z": [round(v, 4) for v in z_q],
            "y": [round(v, 4) for v in y_q],
        },
        "eje_y": {
            "min": round(y_min, 4),
            "max": round(y_max, 4),
            "marcas": marcas_y,
        },
        "eje_z": {"min": round(z_min, 4), "max": round(z_max, 4), "marcas": marcas_z},
        "shapiro": {
            "w": round(float(stats.shapiro(x).statistic), 4),
            "p": round(float(stats.shapiro(x).pvalue), 4),
        },
    }


def main() -> None:
    paneles = [
        panel("p1_orig", "TaxFisco originales", P1, "lineal"),
        panel("p1_log", "TaxFisco logaritmo", P1, "log"),
        panel("p2v1_orig", "SIN vuelta 1 originales", P2V1, "lineal"),
        panel("p2v1_log", "SIN vuelta 1 logaritmo", P2V1, "log"),
        panel("p2fin_orig", "SIN medicion final originales", P2FIN, "lineal"),
        panel("p2fin_log", "SIN medicion final logaritmo", P2FIN, "log"),
    ]
    salida = {
        "descripcion": (
            "Parametros verificados de la Figura 13 (graficos Q-Q): coordenadas de Blom, "
            "valores observados, recta de referencia de la normal ajustada a cada muestra "
            "y escalas de los ejes."
        ),
        "metodo_recta": (
            "y = media + desviacion estandar por z. Es la recta de la distribucion normal "
            "ajustada a la muestra, no una regresion ajustada sobre los puntos observados."
        ),
        "posiciones": "Blom: p_i = (i - 3/8) / (n + 1/4); cuantiles normales estandar.",
        "paneles": paneles,
    }
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")

    for p in paneles:
        print(f"\n== {p['clave']}  (n = {p['n']})")
        print(f"   recta normal   : y = {p['recta_normal']['ordenada']} + {p['recta_normal']['pendiente']} * z")
        print(f"   recta cuartiles: z {p['recta_cuartiles']['z']} -> y {p['recta_cuartiles']['y']}")
        print(f"   eje z          : [{p['eje_z']['min']}, {p['eje_z']['max']}] marcas {p['eje_z']['marcas']}")
        print(f"   eje y          : [{p['eje_y']['min']}, {p['eje_y']['max']}] marcas {p['eje_y']['marcas']}")
        print(f"   shapiro        : W = {p['shapiro']['w']}  p = {p['shapiro']['p']}")
    print(f"\nSalida: {DESTINO}")


if __name__ == "__main__":
    main()
