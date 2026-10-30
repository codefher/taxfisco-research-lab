# -*- coding: utf-8 -*-
"""
Auditoria estadistica del apartado de comprobacion de la hipotesis (4.5).

Recalcula, sobre los datos reales y sin heredar resultados previos:
  - Wilcoxon de rangos con signo emparejada sobre los 4 pares comparables
  - Distribucion nula exacta de W+ por enumeracion de las 16 combinaciones
  - Correlacion biserial de rangos y estimador de Hodges-Lehmann
  - Simetria de las diferencias (supuesto de desplazamiento de localizacion)
  - Normalidad de los datos originales y de su transformada logaritmica
  - Ajuste lognormal por maxima verosimilitud
Salida: resultados-prototypes/estadisticas_hipotesis.json
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "resultados-prototipos" / "estadisticas_hipotesis.json"

# --------------------------------------------------------------------------
# Datos crudos (capitulo de resultados)
# --------------------------------------------------------------------------
P1 = [16.405, 0.826, 85.000, 260.108, 0.141, 0.824, 0.543, 0.533, 10.000]
P2V1 = [16.851, 1.214, 1.734, 1.063]
P2FIN = [15.910, 1.095, 0.000, 0.137, 1.145, 0.460, 0.264, 0.562, 0.000, 0.646]

# Pares comparables del Prototipo 2: (escenario, tecnica MITRE, inicial, posterior)
PARES = [
    ("S01", "T1595", 16.851, 15.910),
    ("S02", "T1595.002", 1.214, 1.095),
    ("S05", "T1110.004", 1.734, 1.145),
    ("S07", "T1078", 1.063, 0.264),
]

ALFA = 0.05


def percentil_inclusive(x: np.ndarray, p: float) -> float:
    xs = np.sort(x)
    n = xs.size
    h = 1.0 + (n - 1) * p
    lo, hi = math.floor(h), math.ceil(h)
    if lo == hi:
        return float(xs[int(h) - 1])
    return float(xs[lo - 1] + (h - lo) * (xs[hi - 1] - xs[lo - 1]))


def descriptivos(x: np.ndarray) -> dict:
    sw = stats.shapiro(x)
    return {
        "n": int(x.size),
        "suma": float(x.sum()),
        "media": float(x.mean()),
        "mediana": float(np.median(x)),
        "minimo": float(x.min()),
        "maximo": float(x.max()),
        "rango": float(x.max() - x.min()),
        "desviacion_estandar": float(x.std(ddof=1)),
        "coeficiente_variacion": float(x.std(ddof=1) / x.mean()),
        "p95_inclusivo": percentil_inclusive(x, 0.95),
        "sesgo_fisher_pearson": float(stats.skew(x, bias=False)),
        "curtosis_exceso": float(stats.kurtosis(x, bias=False)),
        "shapiro_wilk": {"w": float(sw.statistic), "p": float(sw.pvalue)},
        "ordenados": [float(v) for v in np.sort(x)],
    }


def normality_log(x: np.ndarray) -> dict:
    """Normalidad de la transformada logaritmica. Los ceros se excluyen del
    logaritmo (no se pueden transformar) y se reportan aparte."""
    positivos = x[x > 0]
    out = {
        "n_total": int(x.size),
        "n_positivos": int(positivos.size),
        "n_ceros_excluidos": int(x.size - positivos.size),
        "ceros": [float(v) for v in x[x == 0]],
    }
    if positivos.size >= 3:
        lg = np.log(positivos)
        sw = stats.shapiro(lg)
        out["shapiro_wilk_log"] = {"w": float(sw.statistic), "p": float(sw.pvalue)}
        out["log_valores"] = [float(v) for v in lg]
        out["log_media"] = float(lg.mean())
        out["log_desviacion"] = float(lg.std(ddof=1))
        out["log_sesgo"] = float(stats.skew(lg, bias=False))
    return out


def ajuste_lognormal(x: np.ndarray) -> dict:
    """Ajuste lognormal por maxima verosimilitud sobre los valores positivos.
    Devuelve los parametros y la desviacion logaritmica observada frente a la
    ajustada: un residuo pequeno indica que la forma lognormal explica bien la
    nube, pero no la demuestra."""
    positivos = x[x > 0]
    if positivos.size < 3:
        return {"n": int(positivos.size)}
    lg = np.log(positivos)
    mu = float(lg.mean())
    sigma = float(lg.std(ddof=1))
    # desviacion logaritmica observada frente a la ajustada
    ordenada = np.sort(lg)
    esperado = np.sort(stats.norm.rvs(mu, sigma, size=ordenada.size, random_state=7))
    ks = stats.kstest(ordenada, stats.norm.cdf, args=(mu, sigma))
    return {
        "n": int(positivos.size),
        "mu_log": mu,
        "sigma_log": sigma,
        "mediana_ajustada": float(math.exp(mu)),
        "ks_D": float(ks.statistic),
        "ks_p": float(ks.pvalue),
        "resolucion_log_min": float(abs(ordenada[0] - esperado[0])),
    }


def wilcoxon_emparejado(pares: list) -> dict:
    dif = np.array([ini - post for _, _, ini, post in pares])
    absd = np.abs(dif)
    rangos = stats.rankdata(absd)
    Wpos = float(rangos[dif > 0].sum())
    Wneg = float(rangos[dif < 0].sum())
    W = float(min(Wpos, Wneg))

    # distribucion nula exacta por enumeracion de las 2^n combinaciones de signos
    n = dif.size
    signos = list(itertools.product([1, -1], repeat=n))
    rango_total = float(rangos.sum())
    dist = {}
    for combo in signos:
        wpos = float(sum(r for r, s in zip(rangos, combo) if s > 0))
        dist[wpos] = dist.get(wpos, 0) + 1
    total = len(signos)
    p_uni = sum(c for w, c in dist.items() if w >= Wpos) / total
    # p bilateral exacto: doble de la cola menor (mismo criterio que scipy method='exact')
    cola_sup = sum(c for w, c in dist.items() if w >= Wpos) / total
    cola_inf = sum(c for w, c in dist.items() if w <= Wpos) / total
    p_bi = min(1.0, 2 * min(cola_sup, cola_inf))

    # contraste con scipy
    sp = stats.wilcoxon(dif, alternative="greater", method="exact")
    sp2 = stats.wilcoxon(dif, alternative="two-sided", method="exact")

    # estimador de Hodges-Lehmann: mediana de los promedios de Walsh (d_i+d_j)/2
    walsh = sorted((dif[i] + dif[j]) / 2 for i in range(n) for j in range(i, n))
    if len(walsh) % 2:
        hl = float(walsh[len(walsh) // 2])
    else:
        hl = float((walsh[len(walsh) // 2 - 1] + walsh[len(walsh) // 2]) / 2)

    # correlacion biserial de rangos
    rrb = float((Wpos - Wneg) / (Wpos + Wneg))

    # simetria de las diferencias (supuesto de desplazamiento de localizacion)
    sw_dif = stats.shapiro(dif)

    # valores minimos alcanzables con n pares (signo exacto)
    min_uni = 1 / total
    min_bi = 2 / total

    # intervalo de confianza exacto por inversion del contraste exacto:
    # se aceptan los theta para los que el contraste bilateral NO rechaza.
    # con n=4 el p minimo bilateral (0,125) supera alfa, luego se aceptan todos.
    invertidos = []
    for theta in np.linspace(-2.0, 2.0, 801):
        dtheta = dif - theta
        at = np.abs(dtheta)
        rt = stats.rankdata(at)
        wt = float(rt[dtheta > 0].sum())
        sup = sum(c for w, c in dist.items() if w >= wt) / total
        inf = sum(c for w, c in dist.items() if w <= wt) / total
        if min(1.0, 2 * min(sup, inf)) > ALFA:
            invertidos.append(float(theta))
    ci_inversion = [min(invertidos), max(invertidos)] if invertidos else None

    # prueba de signos complementaria (no parametrica, sin supuestos de simetria)
    signos_pos = int(np.sum(dif > 0))
    signos_neg = int(np.sum(dif < 0))
    k = max(signos_pos, signos_neg)
    p_signo_bi = float(min(1.0, 2 * sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n))

    return {
        "n_pares": int(n),
        "detalle": [
            {
                "escenario": esc,
                "tecnica": tec,
                "inicial": ini,
                "posterior": post,
                "diferencia": float(ini - post),
                "abs_diferencia": float(abs(ini - post)),
                "rango": float(r),
                "signo": "positivo" if ini - post > 0 else "negativo",
            }
            for (esc, tec, ini, post), r in zip(pares, rangos)
        ],
        "W_positivo": Wpos,
        "W_negativo": Wneg,
        "W": W,
        "rango_total": rango_total,
        "p_exacto_unilateral": float(p_uni),
        "p_exacto_bilateral": float(p_bi),
        "p_unilateral_scipy": float(sp.pvalue),
        "p_bilateral_scipy": float(sp2.pvalue),
        "distribucion_nula_Wpos": {str(int(k)): int(v) for k, v in sorted(dist.items())},
        "combinaciones_nulas": total,
        "correlacion_biserial_rangos": rrb,
        "hodges_lehmann": hl,
        "hodges_lehmann_walsh": [float(v) for v in walsh],
        "media_diferencias": float(dif.mean()),
        "mediana_diferencias": float(np.median(dif)),
        "simetria_diferencias_shapiro": {"w": float(sw_dif.statistic), "p": float(sw_dif.pvalue)},
        "p_minimo_unilateral_alcanzable": float(min_uni),
        "p_minimo_bilateral_alcanzable": float(min_bi),
        "alcanza_alfa_0_05": bool(p_bi < ALFA),
        "decision": "no se rechaza H0" if p_bi >= ALFA else "se rechaza H0",
        "signos": {"positivos": signos_pos, "negativos": signos_neg},
        "p_signo_bilateral": p_signo_bi,
        "ci_exacto_por_inversion": ci_inversion,
        "ci_inversion_util": bool(ci_inversion and (ci_inversion[1] - ci_inversion[0]) < 3.999),
    }


def cobertura_walsh(n: int = 4, n_sim: int = 100000, seed: int = 11) -> dict:
    """Cobertura por simulacion del intervalo exacto del pseudo-median basado en
    los promedios de Walsh, bajo H0 (diferencias simetricas alrededor de 0).
    Sirve para comprobar que el intervalo que se publica es honesto."""
    rng = np.random.default_rng(seed)
    d = rng.standard_normal((n_sim, n))
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    W = np.sort(np.array([(d[:, i] + d[:, j]) / 2 for i, j in idx]).T, axis=1)
    N = W.shape[1]
    res = {}
    for k in range(1, N // 2 + 1):
        lo, hi = W[:, k - 1], W[:, N - k]
        res[f"w({k})..w({N - k + 1})"] = float(np.mean((lo <= 0) & (0 <= hi)))
    return res


def qq(x: np.ndarray, mu: float = None, sigma: float = None) -> dict:
    """Coordenadas para un grafico Q-Q. Con mu/sigma nulos se usa la normal
    estandar (linea de referencia); con ellos, la normal ajustada."""
    xs = np.sort(x)
    n = xs.size
    p = (np.arange(1, n + 1) - 0.375) / (n + 0.25)   # posiciones de plotting (Blom)
    z = stats.norm.ppf(p)
    if mu is not None and sigma is not None:
        z = (xs - mu) / sigma
    return {"cuantiles_teoricos": [float(v) for v in z], "cuantiles_observados": [float(v) for v in xs]}


def main() -> None:
    salida = {"fuente": "scripts/auditar_hipotesis_mttd.py", "alfa": ALFA}

    # ---------------- hipotesis: pares comparables del Prototipo 2 ----------
    salida["wilcoxon_emparejado"] = wilcoxon_emparejado(PARES)

    # ---------------- distribuciones de los tres conjuntos -----------------
    conjuntos = {"p1": P1, "p2v1": P2V1, "p2fin": P2FIN}
    salida["conjuntos"] = {}
    for k, v in conjuntos.items():
        x = np.array(v, dtype=float)
        salida["conjuntos"][k] = {
            "descriptivos": descriptivos(x),
            "normalidad_log": normality_log(x),
            "ajuste_lognormal": ajuste_lognormal(x),
            "qq_original": qq(x),
        }
        lg = x[x > 0]
        if lg.size >= 3:
            lgn = np.log(lg)
            mu, sg = float(lgn.mean()), float(lgn.std(ddof=1))
            salida["conjuntos"][k]["qq_log"] = qq(lgn, mu, sg)

    salida["cobertura_walsh"] = cobertura_walsh()

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")

    # ------------------------------- consola -------------------------------
    w = salida["wilcoxon_emparejado"]
    print("=== WILCOXON DE RANGOS CON SIGNO EMPAREJADA (4 pares) ===")
    for d in w["detalle"]:
        print(f"  {d['escenario']} ({d['tecnica']}): {d['inicial']} - {d['posterior']} = "
              f"{d['diferencia']:.3f}  |d|={d['abs_diferencia']:.3f}  rango={d['rango']:.0f}  {d['signo']}")
    print(f"  W+ = {w['W_positivo']:.0f}   W- = {w['W_negativo']:.0f}   W = {w['W']:.0f}")
    print(f"  p exacto unilateral (mejora) = {w['p_exacto_unilateral']:.4f}   (scipy {w['p_unilateral_scipy']:.4f})")
    print(f"  p exacto bilateral            = {w['p_exacto_bilateral']:.4f}   (scipy {w['p_bilateral_scipy']:.4f})")
    print(f"  correlacion biserial de rangos = {w['correlacion_biserial_rangos']:.4f}")
    print(f"  Hodges-Lehmann (mediana de Walsh) = {w['hodges_lehmann']:.4f} s")
    print(f"  media de las diferencias = {w['media_diferencias']:.4f} s")
    print(f"  mediana de las diferencias = {w['mediana_diferencias']:.4f} s")
    print(f"  simetria de las diferencias: Shapiro W={w['simetria_diferencias_shapiro']['w']:.4f} "
          f"p={w['simetria_diferencias_shapiro']['p']:.4f}")
    print(f"  p minimo alcanzable: unilateral {w['p_minimo_unilateral_alcanzable']:.4f} / "
          f"bilateral {w['p_minimo_bilateral_alcanzable']:.4f}")
    print(f"  decision con alfa={ALFA}: {w['decision']}")
    print(f"  prueba de signos: {w['signos']}  p bilateral = {w['p_signo_bilateral']:.4f}")
    print(f"  CI exacto por inversion del contraste: {w['ci_exacto_por_inversion']} "
          f"(util={w['ci_inversion_util']})")
    print(f"  distribucion nula de W+: {w['distribucion_nula_Wpos']} (total {w['combinaciones_nulas']})")
    print("\n=== COBERTURA POR SIMULACION DEL INTERVALO DE WALSH (n=4) ===")
    for k, v in salida["cobertura_walsh"].items():
        print(f"  {k}: {v:.4f}")

    print("\n=== NORMALIDAD ORIGINAL vs LOGARITMO ===")
    for k in ("p1", "p2v1", "p2fin"):
        c = salida["conjuntos"][k]
        d = c["descriptivos"]
        nl = c["normalidad_log"]
        sw = d["shapiro_wilk"]
        lgn = nl.get("shapiro_wilk_log")
        print(f"  {k}: sesgo={d['sesgo_fisher_pearson']:.3f}  "
              f"Shapiro original W={sw['w']:.4f} p={sw['p']:.3e}")
        if lgn:
            print(f"        log: n={nl['n_positivos']} (ceros excluidos={nl['n_ceros_excluidos']}) "
                  f"Shapiro W={lgn['w']:.4f} p={lgn['p']:.3e}  sesgo_log={nl['log_sesgo']:.3f}")
            aj = c["ajuste_lognormal"]
            if "ks_D" in aj:
                print(f"        ajuste lognormal MLE: mu={aj['mu_log']:.4f} sigma={aj['sigma_log']:.4f} "
                      f"mediana_ajustada={aj['mediana_ajustada']:.4f} s  KS D={aj['ks_D']:.4f} p={aj['ks_p']:.3f}")
        else:
            print("        log: no aplicable (n insuficiente tras excluir ceros)")
    print(f"\nJSON escrito en: {DESTINO}")


if __name__ == "__main__":
    main()
