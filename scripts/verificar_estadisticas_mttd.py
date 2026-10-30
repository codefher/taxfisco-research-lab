# -*- coding: utf-8 -*-
"""
Verificacion de las medidas descriptivas del MTTD (Mean Time to Detect) usadas
en el analisis estadistico de los tiempos de deteccion de los dos prototipos
Honeypot (TaxFisco Research Lab y laboratorio del Servicio de Impuestos
Nacionales, SIN).

Ejecucion:
    py -3 scripts/verificar_estadisticas_mttd.py

Salida:
    resultados-prototipos/estadisticas_mttd.json

Ese JSON es la unica fuente de los indicadores numericos del analisis
estadistico del MTTD: lo consumen el documento visual
(resultados-prototipos/mttd-analisis-estadistico.html) y su version en Word
(resultados-prototipos/analisis-estadistico-mttd.docx), de modo que ninguno
puede divergir de los calculos verificados.

Los datos crudos son los registros de los capitulos de resultados
(resultados-prototipos/capitulo-4-resultados.docx y
resultados-prototipos/capitulo-4-4-resultados.docx), transcritos aqui para que
el calculo sea reproducible sin depender de los documentos.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import stats

# Raiz del repositorio: el script vive en scripts/, un nivel por debajo.
RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "resultados-prototipos" / "estadisticas_mttd.json"

# --------------------------------------------------------------------------
# Datos crudos de los tres momentos de medicion (capitulos de resultados)
# --------------------------------------------------------------------------
DATOS = {
    "p1": {
        "etiqueta": "Prototipo 1 - TaxFisco Research Lab",
        "clave": "TaxFisco",
        "escenarios": ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10"],
        "valores": [16.405, 0.826, 85.000, 260.108, 0.141, 0.824, 0.543, 0.533, 10.000],
        "sin_registro": ["S10"],
        "bins": 30.0,
        "bin_max": 270.0,
    },
    "p2v1": {
        "etiqueta": "Prototipo 2 - SIN, primera vuelta",
        "clave": "SIN vuelta 1",
        "escenarios": ["S01", "S02", "S05", "S07"],
        "valores": [16.851, 1.214, 1.734, 1.063],
        "sin_registro": ["S03", "S04", "S06", "S08", "S09", "S10"],
        "bins": 1.0,
        "bin_max": 17.0,
    },
    "p2fin": {
        "etiqueta": "Prototipo 2 - SIN, medicion final",
        "clave": "SIN medicion final",
        "escenarios": ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10"],
        "valores": [15.910, 1.095, 0.000, 0.137, 1.145, 0.460, 0.264, 0.562, 0.000, 0.646],
        "sin_registro": [],
        "bins": 1.0,
        "bin_max": 16.0,
    },
}

COMUNES = {"S01": (16.851, 15.910), "S02": (1.214, 1.095), "S05": (1.734, 1.145), "S07": (1.063, 0.264)}


def percentil_inclusive(x: np.ndarray, p: float) -> float:
    """PERCENTILE.INC de Excel: h = 1 + (n-1)*p con interpolacion lineal."""
    xs = np.sort(x)
    n = xs.size
    h = 1.0 + (n - 1) * p
    lo = math.floor(h)
    hi = math.ceil(h)
    if lo == hi:
        return float(xs[int(h) - 1])
    return float(xs[lo - 1] + (h - lo) * (xs[hi - 1] - xs[lo - 1]))


def bloque(datos: dict) -> dict:
    x = np.array(datos["valores"], dtype=float)
    n = x.size
    orden = np.sort(x)
    media = float(x.mean())
    mediana = float(np.median(x))
    sd = float(x.std(ddof=1))
    p95 = percentil_inclusive(x, 0.95)

    # Histograma con los intervalos declarados en el capitulo de resultados
    ancho = datos["bins"]
    cortes = np.arange(0.0, datos["bin_max"] + ancho * 0.5, ancho)
    freq, _ = np.histogram(x, bins=cortes)
    histograma = [
        {
            "desde": float(cortes[i]),
            "hasta": float(cortes[i + 1]),
            "frecuencia_absoluta": int(freq[i]),
            "frecuencia_relativa": float(freq[i] / n),
        }
        for i in range(len(freq))
    ]

    shapiro = stats.shapiro(x)
    bloque_out = {
        "etiqueta": datos["etiqueta"],
        "clave": datos["clave"],
        "escenarios": datos["escenarios"],
        "valores": [float(v) for v in x],
        "sin_registro": datos["sin_registro"],
        "n": int(n),
        "suma": float(x.sum()),
        "media": media,
        "mediana": mediana,
        "minimo": float(x.min()),
        "maximo": float(x.max()),
        "rango": float(x.max() - x.min()),
        "desviacion_estandar": sd,
        "cv": float(sd / media) if media else None,
        "p95_inclusivo": p95,
        "h_p95": float(1 + (n - 1) * 0.95),
        "ordenados": [float(v) for v in orden],
        "sesgo_fisher_pearson": float(stats.skew(x, bias=False)),
        "curtosis_exceso": float(stats.kurtosis(x, bias=False)),
        "shapiro_wilk": {"w": float(shapiro.statistic), "p": float(shapiro.pvalue)},
        "histograma": histograma,
        "ancho_bin": ancho,
    }
    return bloque_out


def main() -> None:
    salida = {"fuente": "scripts/verificar_estadisticas_mttd.py", "datasets": {k: bloque(v) for k, v in DATOS.items()}}

    p1, p2v1, p2fin = (salida["datasets"][k] for k in ("p1", "p2v1", "p2fin"))

    # Comparacion de medias reportadas (muestras de distinto tamano)
    dif = p2v1["media"] - p2fin["media"]
    salida["comparacion_reportada"] = {
        "media_vuelta_1": p2v1["media"],
        "media_final": p2fin["media"],
        "diferencia_absoluta": dif,
        "reduccion_relativa_pct": dif / p2v1["media"] * 100,
    }

    # Comparacion homogenea: los mismos cuatro escenarios en ambas vueltas
    ini = np.array([v[0] for v in COMUNES.values()])
    fin = np.array([v[1] for v in COMUNES.values()])
    m_ini, m_fin = float(ini.mean()), float(fin.mean())
    salida["comparacion_comparable"] = {
        "escenarios": [
            {
                "escenario": k,
                "vuelta_1": float(v[0]),
                "final": float(v[1]),
                "diferencia": float(v[0] - v[1]),
                "reduccion_relativa_pct": float((v[0] - v[1]) / v[0] * 100),
            }
            for k, v in COMUNES.items()
        ],
        "media_inicial": m_ini,
        "media_final": m_fin,
        "diferencia_absoluta": m_ini - m_fin,
        "reduccion_relativa_pct": (m_ini - m_fin) / m_ini * 100,
    }

    # Cobertura temporal de registros
    salida["cobertura"] = {
        "p1": {"medidos": p1["n"], "declarados": 10, "pct": p1["n"] / 10 * 100},
        "p2v1": {"medidos": p2v1["n"], "declarados": 10, "pct": p2v1["n"] / 10 * 100},
        "p2fin": {"medidos": p2fin["n"], "declarados": 10, "pct": p2fin["n"] / 10 * 100},
    }

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")

    # Resumen en consola para verificacion rapida
    for clave in ("p1", "p2v1", "p2fin"):
        d = salida["datasets"][clave]
        print(
            f"{d['clave']:<22} n={d['n']:<3} media={d['media']:.4f}  mediana={d['mediana']:.4f}  "
            f"min={d['minimo']:.3f}  max={d['maximo']:.3f}  R={d['rango']:.3f}  "
            f"s={d['desviacion_estandar']:.3f}  P95={d['p95_inclusivo']:.4f}  "
            f"h={d['h_p95']:.2f}  sesgo={d['sesgo_fisher_pearson']:.3f}"
        )
        print(f"    histograma: {[(h['desde'], h['hasta'], h['frecuencia_absoluta']) for h in d['histograma'] if h['frecuencia_absoluta'] > 0]}")
    c = salida["comparacion_comparable"]
    r = salida["comparacion_reportada"]
    print(f"comparacion reportada : {r['media_vuelta_1']:.4f} -> {r['media_final']:.4f} "
          f"(-{r['diferencia_absoluta']:.4f} s, -{r['reduccion_relativa_pct']:.2f} %)")
    print(f"comparacion comparable: {c['media_inicial']:.4f} -> {c['media_final']:.4f} "
          f"(-{c['diferencia_absoluta']:.4f} s, -{c['reduccion_relativa_pct']:.2f} %)")
    print(f"JSON escrito en: {DESTINO}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
