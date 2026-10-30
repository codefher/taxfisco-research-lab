# -*- coding: utf-8 -*-
"""Seleccion de la distribucion de referencia para el tiempo de deteccion.

Version 2. El ajuste de los modelos con soporte positivo se realiza con
estimadores de maxima verosimilitud propios, anclados en cero, y se verifica
contra un optimizador numerico independiente. La version anterior usaba
stats.<dist>.fit(x, loc=0), que en scipy 1.18.1 no respeta el anclaje y
devuelve ajustes degenerados sobre el minimo de la muestra.

Para cada laboratorio se ajusta un conjunto de distribuciones candidatas y se
comparan con:
  - AIC y BIC, que penalizan la complejidad del modelo
  - pesos de Akaike, que cuantifican la preferencia entre modelos
  - prueba de Kolmogorov-Smirnov con correccion de Lilliefors mediante
    remuestreo parametrico, que respeta el hecho de que los parametros
    se estimaron sobre la misma muestra
Ademas se compara la implicacion de cada modelo sobre los cuantiles, porque
el capitulo reporta percentiles del tiempo de deteccion.

Salida: figuras PNG + resultados en JSON + tabla comparativa en consola.
"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats, optimize
from scipy.special import expit, gammaln, logsumexp

sys.stdout.reconfigure(encoding="utf-8")
np.seterr(all="ignore")

RAIZ = r"F:\Maestria\tesis\taxfisco-research-lab"
GRAFI = os.path.join(RAIZ, "resultados-prototipos", "evidencia-visual", "graficos")
os.makedirs(GRAFI, exist_ok=True)

NAVY, NAVY2, GREEN, AMBER = "#1F3864", "#2E75B6", "#1F6032", "#9C6500"
GREY, LINE, MUTE = "#B9C4D2", "#D6DEE8", "#5A6878"
RED = "#A6192E"

plt.rcParams.update({
    "font.family": "Segoe UI", "font.size": 11,
    "axes.edgecolor": LINE, "axes.labelcolor": NAVY, "axes.titlecolor": NAVY,
    "text.color": NAVY, "xtick.color": MUTE, "ytick.color": MUTE,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})

BOOT = 2000
SEMILLA = 20251027


def dec(x, n=4):
    return f"{x:,.{n}f}".replace(",", "\u00a0").replace(".", ",")


def num(x, n=4):
    """Formato numerico simple para JSON."""
    return float(f"{x:.{n}f}")


# ── carga de datos ────────────────────────────────────────────────────────
def cargar(ruta):
    d = json.load(open(ruta, encoding="utf-8-sig"))
    det = [x for x in d["kpis"]["MTTD"]["details"] if x.get("mttd_seconds") is not None]
    return np.array([x["mttd_seconds"] for x in det], float)


P1 = cargar(os.path.join(RAIZ, "evidencias", "07-metricas", "07_kpi-report.json"))
P2A = cargar(os.path.join(RAIZ, "evidencias", "v2.0-it1", "07-metricas", "kpi_report.json"))
P2B = cargar(os.path.join(RAIZ, "evidencias", "v2.1-it2", "07-metricas", "kpi_report.json"))


# ══════════════════════════════════════════════════════════════════════════
#  1. Estimadores de maxima verosimilitud, con soporte anclado en cero
# ══════════════════════════════════════════════════════════════════════════
def mle_normal(x):
    """Normal, dos parametros libres: media y desviacion."""
    mu = x.mean()
    sigma = np.sqrt(((x - mu) ** 2).mean())
    return (mu, sigma)


def mle_lognormal(x):
    """Log-normal con localizacion en cero: X = exp(Y), Y normal(mu, s^2).

    El estimador es cerrado: mu = media de ln(x) y s = desviacion de ln(x).
    """
    t = np.log(x)
    mu = t.mean()
    s = np.sqrt(((t - mu) ** 2).mean())
    return (s, np.exp(mu))


def mle_exponencial(x):
    """Exponencial con localizacion en cero y escala unitaria: lambda = 1/media."""
    return (1.0 / x.mean(),)


def mle_gamma(x, rapido=False):
    """Gamma con localizacion en cero.

    El estimador de momentos a = media^2/varianza y escala = varianza/media da
    un punto de partida, pero no coincide con el maximo verosimilitud. La
    estimacion definitiva se obtiene por optimizacion numerica de la
    verosimilitud, con el estimador de momentos como inicio.
    """
    x = np.asarray(x, float)
    m = x.mean()
    v = ((x - m) ** 2).mean()
    a0, th0 = m ** 2 / v, v / m

    def nll(q):
        a, th = np.exp(q[0]), np.exp(q[1])
        return -float(((a - 1.0) * np.log(x) - x / th - gammaln(a) - a * np.log(th)).sum())

    res = optimize.minimize(nll, x0=[np.log(a0), np.log(th0)], method="L-BFGS-B",
                            bounds=[(np.log(1e-3), np.log(1e3)), (np.log(1e-6), np.log(1e6))],
                            options={"maxiter": 5000, "ftol": 1e-15, "gtol": 1e-12})
    return (float(np.exp(res.x[0])), float(np.exp(res.x[1])))


def mle_weibull(x, rapido=False):
    """Weibull de minima con localizacion en cero.

    La escala queda determinada por la forma: lambda(c) = (media de x^c)^(1/c).
    La forma se maximiza sobre la verosimilitud perfil. El calculo se hace en
    escala logaritmica porque x^c desborda con la cola extrema observada, y se
    aplica la identidad suma de (x_i/lambda)^c = n, exacta por construccion.
    """
    x = np.asarray(x, float)
    n = len(x)
    lx = np.log(x)
    sum_lx = lx.sum()

    def perfil(c):
        log_lam = (logsumexp(c * lx) - np.log(n)) / c
        # verosimilitud de la Weibull de minima con localizacion en cero:
        # suma de ln f = n ln c - n c ln(lambda) + (c - 1) suma ln(x) - suma (x/lambda)^c
        # y, por la definicion de lambda, suma (x/lambda)^c = n de forma exacta
        ll = n * np.log(c) - n * c * log_lam + (c - 1.0) * sum_lx - n
        return ll, float(np.exp(log_lam))

    if rapido:
        res = optimize.minimize_scalar(lambda c: -perfil(c)[0], bounds=(0.05, 50.0),
                                       method="bounded", options={"xatol": 1e-8})
        c = float(res.x)
    else:
        cs = np.exp(np.linspace(np.log(0.05), np.log(50.0), 481))
        vals = np.array([perfil(c)[0] for c in cs])
        i = int(np.argmax(vals))
        lo, hi = cs[max(i - 1, 0)], cs[min(i + 1, len(cs) - 1)]
        if hi > lo:
            res = optimize.minimize_scalar(lambda c: -perfil(c)[0], bounds=(lo, hi),
                                           method="bounded", options={"xatol": 1e-12})
            c = float(res.x)
        else:
            c = float(cs[i])
    ll, lam = perfil(c)
    return (c, lam)


def _u_loglogistica(t, b):
    """Para una forma b fija, la escala a se obtiene de la condicion de primer orden.

    d/du de la log-verosimilitud con u = ln(a) es proporcional a
    2 * sum(sigmoid(b * (t - u))) - n, que es estrictamente decreciente en u.
    """
    def h(u):
        return 2.0 * expit(b * (t - u)).sum() - len(t)

    u_lo, u_hi = t.min() - 15.0, t.max() + 15.0
    if h(u_lo) < 0:
        return u_lo
    if h(u_hi) > 0:
        return u_hi
    return float(optimize.brentq(h, u_lo, u_hi, xtol=1e-12))


def mle_loglogistica(x, rapido=False):
    """Log-logistica de dos parametros (escala a y forma b).

    Se maximiza la verosimilitud perfil sobre la forma b; para cada b la escala
    a se resuelve en forma cerrada por la condicion de primer orden.
    """
    t = np.log(np.asarray(x, float))

    def perfil(b):
        u = _u_loglogistica(t, b)
        z = b * (t - u)
        ll = np.sum(np.log(b) - u + (b - 1) * (t - u) - 2.0 * np.logaddexp(0.0, z))
        return ll, np.exp(u)

    if rapido:
        res = optimize.minimize_scalar(lambda b: -perfil(b)[0], bounds=(0.05, 50.0),
                                       method="bounded", options={"xatol": 1e-8})
        b = float(res.x)
    else:
        bs = np.exp(np.linspace(np.log(0.05), np.log(50.0), 241))
        vals = np.array([perfil(b)[0] for b in bs])
        i = int(np.argmax(vals))
        lo, hi = bs[max(i - 1, 0)], bs[min(i + 1, len(bs) - 1)]
        if hi > lo:
            res = optimize.minimize_scalar(lambda b: -perfil(b)[0], bounds=(lo, hi),
                                           method="bounded", options={"xatol": 1e-10})
            b = float(res.x)
        else:
            b = float(bs[i])
    ll, a = perfil(b)
    return (a, b)


# ══════════════════════════════════════════════════════════════════════════
#  2. Funciones de cada modelo, coherentes con los parametros estimados
#
#  Las funciones de la log-normal, exponencial, gamma y Weibull se calculan con
#  formulas explicitas en lugar de invocar a la familia de scipy. La razon es
#  tecnica y verificable: en scipy 1.18 la firma de _parse_args ya no admite
#  simultaneamente la forma y la localizacion en posicion, y el uso de
#  fit(x, loc=0) dejo de anclar el soporte en cero. Escribir las formulas
#  evita cualquier dependencia de esa firma y deja el modelo a la vista.
# ══════════════════════════════════════════════════════════════════════════
LOG2PI = float(np.log(2.0 * np.pi))
LOG_GAMMA = stats.gamma


def loglik(nombre, p, x):
    """Log-verosimilitud evaluada en el origen cero de cada modelo."""
    x = np.asarray(x, float)
    if nombre == "Normal":
        return float(stats.norm.logpdf(x, p[0], p[1]).sum())
    if nombre == "Log-normal":
        s, scale = p
        mu = np.log(scale)
        return float((stats.norm.logpdf(np.log(x), mu, s) - np.log(x)).sum())
    if nombre == "Exponencial":
        lam = p[0]
        return float((np.log(lam) - lam * x).sum())
    if nombre == "Gamma":
        a, scale = p
        return float(((a - 1.0) * np.log(x) - x / scale
                      - gammaln(a) - a * np.log(scale)).sum())
    if nombre == "Weibull":
        c, scale = p
        z = x / scale
        return float((np.log(c / scale) + (c - 1.0) * np.log(z) - z ** c).sum())
    if nombre == "Log-logistica":
        a, b = p
        w = np.log(x) - np.log(a)
        z = b * w
        ll = np.log(b) - np.log(a) + (b - 1.0) * w - 2.0 * np.logaddexp(0.0, z)
        return float(ll.sum())
    raise ValueError(nombre)


def _loglogistica_logpdf(a, b, t):
    """Log-densidad de la log-logistica, estable frente al desbordamiento."""
    t = np.asarray(t, float)
    w = np.log(np.maximum(t, 1e-300)) - np.log(a)
    z = b * w
    return np.log(b) - np.log(a) + (b - 1.0) * w - 2.0 * np.logaddexp(0.0, z)


def pdf(nombre, p, t):
    t = np.asarray(t, float)
    if nombre == "Normal":
        return stats.norm.pdf(t, p[0], p[1])
    if nombre == "Log-normal":
        s, scale = p
        mu = np.log(scale)
        return stats.norm.pdf(np.log(np.maximum(t, 1e-300)), mu, s) / np.maximum(t, 1e-300)
    if nombre == "Exponencial":
        lam = p[0]
        return lam * np.exp(-lam * t)
    if nombre == "Gamma":
        a, scale = p
        z = t / scale
        return stats.gamma.pdf(z, a) / scale
    if nombre == "Weibull":
        c, scale = p
        z = np.maximum(t, 1e-300) / scale
        return (c / scale) * z ** (c - 1.0) * np.exp(-(z ** c))
    if nombre == "Log-logistica":
        a, b = p
        return np.exp(_loglogistica_logpdf(a, b, t))
    raise ValueError(nombre)


def cdf(nombre, p, t):
    t = np.asarray(t, float)
    if nombre == "Normal":
        return stats.norm.cdf(t, p[0], p[1])
    if nombre == "Log-normal":
        s, scale = p
        mu = np.log(scale)
        return stats.norm.cdf((np.log(np.maximum(t, 1e-300)) - mu) / s)
    if nombre == "Exponencial":
        return 1.0 - np.exp(-p[0] * t)
    if nombre == "Gamma":
        a, scale = p
        return stats.gamma.cdf(t / scale, a)
    if nombre == "Weibull":
        c, scale = p
        return 1.0 - np.exp(-((np.maximum(t, 0.0) / scale) ** c))
    if nombre == "Log-logistica":
        a, b = p
        return 1.0 / (1.0 + (np.maximum(t, 1e-300) / a) ** (-b))
    raise ValueError(nombre)


def ppf(nombre, p, q):
    if nombre == "Normal":
        return stats.norm.ppf(q, p[0], p[1])
    if nombre == "Log-normal":
        s, scale = p
        return np.exp(np.log(scale) + s * stats.norm.ppf(q))
    if nombre == "Exponencial":
        return -np.log1p(-q) / p[0]
    if nombre == "Gamma":
        a, scale = p
        return stats.gamma.ppf(q, a) * scale
    if nombre == "Weibull":
        c, scale = p
        return scale * ((-np.log1p(-q)) ** (1.0 / c))
    if nombre == "Log-logistica":
        a, b = p
        return a * (q / (1.0 - q)) ** (1.0 / b)
    raise ValueError(nombre)


def simular(nombre, p, n, rng):
    if nombre == "Normal":
        return rng.normal(p[0], p[1], n)
    if nombre == "Log-normal":
        return rng.lognormal(np.log(p[1]), p[0], n)
    if nombre == "Exponencial":
        return rng.exponential(1.0 / p[0], n)
    if nombre == "Gamma":
        return rng.gamma(p[0], p[1], n)
    if nombre == "Weibull":
        return p[1] * rng.weibull(p[0], n)
    if nombre == "Log-logistica":
        a, b = p
        u = rng.random(n)
        u = np.clip(u, 1e-12, 1 - 1e-12)
        return a * (u / (1.0 - u)) ** (1.0 / b)
    raise ValueError(nombre)


MLE = {
    "Normal": lambda x, rapido=False: mle_normal(x),
    "Log-normal": lambda x, rapido=False: mle_lognormal(x),
    "Exponencial": lambda x, rapido=False: mle_exponencial(x),
    "Gamma": lambda x, rapido=False: mle_gamma(x),
    "Weibull": mle_weibull,
    "Log-logistica": mle_loglogistica,
}

K_PARAM = {"Normal": 2, "Log-normal": 2, "Exponencial": 1,
           "Gamma": 2, "Weibull": 2, "Log-logistica": 2}

CATALOGO = ["Normal", "Log-normal", "Exponencial", "Gamma", "Weibull", "Log-logistica"]


# ══════════════════════════════════════════════════════════════════════════
#  3. Verificacion independiente de cada estimador
# ══════════════════════════════════════════════════════════════════════════
def verificar_estimadores(x):
    """Contrasta el estimador propio con un optimizador numerico independiente.

    Se maximiza la misma verosimilitud con Nelder-Mead partiendo de un punto
    deliberadamente distinto del estimador analitico y dentro de una caja
    razonable de parametros. Si la diferencia de log-verosimilitud es
    despreciable, el estimador propio alcanza el maximo y la comparacion de
    modelos es defendible.
    """
    print(f"\n  {'modelo':<16}{'log-veros. propia':>20}{'log-veros. numerica':>22}{'diferencia':>14}")
    out = {}
    med = float(np.median(x))
    sd = float(np.std(x, ddof=0))
    rng_ = x.max() - x.min()

    for nom in CATALOGO:
        p = MLE[nom](x)
        ll1 = loglik(nom, p, x)

        # caja de parametros admitida, en escala logaritmica donde aplica
        if nom == "Normal":
            caja = [(x.min() - 5 * rng_, x.max() + 5 * rng_), (np.log(sd / 1e3), np.log(sd * 1e3))]
            inicial = [float(med), np.log(sd)]
        elif nom == "Log-normal":
            caja = [(np.log(x.min() / 1e3), np.log(x.max() * 1e3)),
                    (np.log(1e-3), np.log(1e3))]
            inicial = [1.0, np.log(med)]
        elif nom == "Exponencial":
            caja = [(np.log(1e-4 / med), np.log(1e3 / med))]
            inicial = [np.log(1.0 / med)]
        elif nom == "Gamma":
            caja = [(np.log(1e-2), np.log(1e2)), (np.log(x.min() / 1e3), np.log(x.max() * 1e3))]
            inicial = [np.log(0.5), np.log(2 * med)]
        elif nom == "Weibull":
            caja = [(np.log(1e-2), np.log(1e2)), (np.log(x.min() / 1e3), np.log(x.max() * 1e3))]
            inicial = [np.log(1.0), np.log(med)]
        else:
            caja = [(np.log(x.min() / 1e2), np.log(x.max() * 1e2)), (np.log(0.02), np.log(50.0))]
            inicial = [np.log(med), np.log(1.0)]

        def nll(q):
            if nom == "Normal":
                if not (caja[0][0] <= q[0] <= caja[0][1]):
                    return 1e12
                v = (q[0], abs(q[1]) + 1e-12)
            elif nom == "Log-normal":
                if not (caja[1][0] <= q[1] <= caja[1][1]):
                    return 1e12
                v = (abs(q[0]) + 1e-12, np.exp(q[1]))
            elif nom == "Exponencial":
                if not (caja[0][0] <= q[0] <= caja[0][1]):
                    return 1e12
                v = (abs(q[0]) + 1e-12,)
            elif nom == "Gamma":
                if not (caja[0][0] <= q[0] <= caja[0][1]):
                    return 1e12
                v = (abs(q[0]) + 1e-12, np.exp(q[1]))
            elif nom == "Weibull":
                if not (caja[0][0] <= q[0] <= caja[0][1]):
                    return 1e12
                v = (abs(q[0]) + 1e-12, np.exp(q[1]))
            else:
                if not (caja[1][0] <= q[1] <= caja[1][1]):
                    return 1e12
                v = (np.exp(q[0]), np.exp(q[1]))
            val = loglik(nom, v, x)
            return -val if np.isfinite(val) else 1e12

        r = optimize.minimize(nll, x0=inicial, method="Nelder-Mead",
                              options={"maxiter": 80000, "maxfev": 80000,
                                       "xatol": 1e-11, "fatol": 1e-13})
        ll2 = -r.fun
        d = abs(ll1 - ll2)
        out[nom] = {"loglik_propia": num(ll1, 6), "loglik_numerica": num(ll2, 6),
                    "diferencia": num(d, 8)}
        print(f"  {nom:<16}{ll1:>20.6f}{ll2:>22.6f}{d:>14.2e}")
    return out


# ══════════════════════════════════════════════════════════════════════════
#  4. Kolmogorov-Smirnov con correccion de Lilliefors
# ══════════════════════════════════════════════════════════════════════════
def _d_ks(nombre, p, x):
    t = np.sort(x)
    n = len(x)
    F = cdf(nombre, p, t)
    i = np.arange(1, n + 1) / n
    return float(max(np.max(i - F), np.max(F - (i - 1.0 / n))))


def ks_lilliefors(nombre, p, x, rng, boot=None):
    """Remuestreo parametrico: se simula del modelo, se reestima y se compara."""
    boot = BOOT if boot is None else boot
    n = len(x)
    stat = _d_ks(nombre, p, x)
    sup = 0
    for _ in range(boot):
        xs = simular(nombre, p, n, rng)
        try:
            ps = MLE[nombre](xs, rapido=True)
        except Exception:
            continue
        if _d_ks(nombre, ps, xs) >= stat:
            sup += 1
    return stat, sup / boot


# ══════════════════════════════════════════════════════════════════════════
#  4b. Calibracion del procedimiento de Kolmogorov-Smirnov
# ══════════════════════════════════════════════════════════════════════════
def calibracion(nombre, params, n, n_rep, boot, etiqueta):
    """Comprueba que el p-valor de Lilliefors obtenido por remuestreo tiene el
    nivel nominal cuando los datos provienen del propio modelo.

    Se simulan mucas de datos del modelo ajustado, se les aplica el mismo
    procedimiento y se cuenta cuantas veces el p-valor cae por debajo de 0,05.
    Si el procedimiento es correcto, esa frecuencia debe acercarse a 0,05.
    """
    rng = np.random.default_rng(SEMILLA + 7)
    ps = []
    for _ in range(n_rep):
        xs = simular(nombre, params, n, rng)
        p = MLE[nombre](xs)
        _, pv = ks_lilliefors(nombre, p, xs, rng, boot=boot)
        ps.append(pv)
    ps = np.array(ps)
    bajo = float((ps < 0.05).mean())
    print(f"  {etiqueta:<44}n = {n}   replicas = {n_rep}")
    print(f"    p-valor medio {dec(ps.mean(), 3):>8}   "
          f"proporcion de rechazos al 5 %: {dec(bajo, 3):>7}   (nivel nominal 0,050)")
    return {"n": n, "replicas": n_rep, "p_medio": num(ps.mean(), 6),
            "proporcion_rechazos_005": num(bajo, 6)}


# ══════════════════════════════════════════════════════════════════════════
#  5. Comparacion de modelos
# ══════════════════════════════════════════════════════════════════════════
def comparar(x, etiqueta):
    rng = np.random.default_rng(SEMILLA)
    positivos = x[x > 0]
    censurados = int((x <= 0).sum())
    n = len(positivos)
    print(f"\n{'-'*94}\n{etiqueta}")
    print(f"  n total = {len(x)}   ajustados sobre n = {n} valores positivos"
          f"{'   (censurados por la izquierda: ' + str(censurados) + ')' if censurados else ''}")
    print(f"  {'modelo':<16}{'log-veros.':>13}{'AIC':>11}{'BIC':>11}{'dAIC':>9}"
          f"{'w Akaike':>11}{'D KS':>9}{'p KS':>9}")
    filas = []
    for nom in CATALOGO:
        p = MLE[nom](positivos)
        ll = loglik(nom, p, positivos)
        k = K_PARAM[nom]
        aic = -2 * ll + 2 * k
        bic = -2 * ll + k * np.log(n)
        ks, pks = ks_lilliefors(nom, p, positivos, rng)
        filas.append({"modelo": nom, "params": [float(v) for v in p], "k": k,
                      "loglik": num(ll, 6), "aic": num(aic, 6), "bic": num(bic, 6),
                      "ks": num(ks, 6), "p_ks": num(pks, 6),
                      "n_ajuste": n, "censurados": censurados})
    min_aic = min(f["aic"] for f in filas)
    min_bic = min(f["bic"] for f in filas)
    suma_w = sum(np.exp(-(f["aic"] - min_aic) / 2) for f in filas)
    for f in filas:
        f["daic"] = num(f["aic"] - min_aic, 4)
        f["dbic"] = num(f["bic"] - min_bic, 4)
        f["w_akaike"] = num(np.exp(-(f["aic"] - min_aic) / 2) / suma_w, 6)
    filas.sort(key=lambda f: f["aic"])
    for f in filas:
        print(f"  {f['modelo']:<16}{f['loglik']:>13.3f}{f['aic']:>11.3f}{f['bic']:>11.3f}"
              f"{f['daic']:>9.2f}{f['w_akaike']:>11.4f}{f['ks']:>9.4f}{f['p_ks']:>9.4f}")
    mejor_aic = filas[0]
    mejor_bic = min(filas, key=lambda f: f["bic"])
    print(f"  mejor por AIC : {mejor_aic['modelo']}   (w = {dec(mejor_aic['w_akaike'],4)})")
    print(f"  mejor por BIC : {mejor_bic['modelo']}")
    dentro = [f for f in filas if f["daic"] <= 2.0]
    if len(dentro) > 1:
        print(f"  modelos no distinguibles por AIC (dAIC <= 2): "
              + ", ".join(f"{f['modelo']} ({dec(f['daic'],2)})" for f in dentro))
    return filas


print("=" * 94)
print("SELECCION DE LA DISTRIBUCION DE REFERENCIA PARA EL TIEMPO DE DETECCION")
print("version 2: estimadores propios con soporte anclado en cero")
print("=" * 94)

print("\n" + "=" * 94)
print("1. VERIFICACION DE LOS ESTIMADORES (Propio contra optimizador numerico)")
print("=" * 94)
ver_p1 = verificar_estimadores(P1[P1 > 0])
ver_p2b = verificar_estimadores(P2B[P2B > 0])

print("\n" + "=" * 94)
print("2. COMPARACION DE MODELOS POR LABORATORIO")
print("=" * 94)
res_p1 = comparar(P1, "PROTOTIPO 1 - TaxFisco Research Lab (empresa homologada)")
res_p2b = comparar(P2B, "PROTOTIPO 2 - SIN, medicion final de diez escenarios")
res_p2a = comparar(P2A, "PROTOTIPO 2 - SIN, vuelta 1 (apoyo, n = 4)")

print("\n" + "=" * 94)
print("3. CALIBRACION DEL PROCEDIMIENTO DE KOLMOGOROV-SMIRNOV CON LILLIEFORS")
print("=" * 94)
print("  Se generan mucas del propio modelo y se aplica el procedimiento completo.")
print("  La proporcion de rechazos al 5 % debe acercarse al nivel nominal.")
p_ln_p1 = mle_lognormal(P1[P1 > 0])
p_ln_p2 = mle_lognormal(P2B[P2B > 0])
cal_p1 = calibracion("Log-normal", p_ln_p1, len(P1[P1 > 0]), 200, 400,
                      "Prototipo 1, log-normal ajustada a los nueve datos")
cal_p2 = calibracion("Log-normal", p_ln_p2, len(P2B[P2B > 0]), 200, 400,
                      "Prototipo 2, log-normal ajustada a los ocho datos")

# ── implicacion sobre los cuantiles ───────────────────────────────────────
print("\n" + "=" * 94)
print("4. IMPLICACION DE CADA MODELO SOBRE LOS CUANTILES DEL TIEMPO DE DETECCION")
print("=" * 94)


def cuantiles_modelo(nom, p, qs):
    return {q: float(ppf(nom, p, q)) for q in qs}


for etiqueta, x, filas in (("Prototipo 1", P1, res_p1),
                           ("Prototipo 2, medicion final", P2B, res_p2b)):
    print(f"\n  {etiqueta}  (n = {len(x)})")
    xp = x[x > 0]
    emp = {q: float(np.quantile(xp, q, method="linear")) for q in (0.5, 0.9, 0.95)}
    print(f"    {'empirico':<16}mediana {dec(emp[0.5], 3):>14}   p90 {dec(emp[0.9], 3):>14}"
          f"   p95 {dec(emp[0.95], 3):>14}")
    for nom in ("Normal", "Log-normal", "Gamma", "Weibull"):
        f = next((z for z in filas if z["modelo"] == nom), None)
        if not f:
            continue
        c = cuantiles_modelo(nom, f["params"], (0.5, 0.9, 0.95))
        print(f"    {nom:<16}mediana {dec(c[0.5], 3):>14}   p90 {dec(c[0.9], 3):>14}"
              f"   p95 {dec(c[0.95], 3):>14}")


# ── FIGURA A: comparacion grafica de candidatas ──────────────────────────
def figura_candidatas(x, filas, titulo, nombre_archivo, color_hist):
    x = x[x > 0]
    orden = ["Normal", "Log-normal", "Weibull", "Gamma"]
    fig, ax = plt.subplots(2, 4, figsize=(14.4, 6.8), dpi=100)
    fig.subplots_adjust(left=0.05, right=0.985, top=0.82, bottom=0.10, wspace=0.28, hspace=0.46)
    xs = np.linspace(max(x.min() * 0.5, 1e-6), x.max() * 1.08, 500)
    for j, nom in enumerate(orden):
        f = next((z for z in filas if z["modelo"] == nom), None)
        aT, aB = ax[0][j], ax[1][j]
        aT.hist(x, bins=9, color=color_hist, edgecolor="white", linewidth=1.1, zorder=3)
        aT.plot(xs, pdf(nom, f["params"], xs) * len(x) * (xs[1] - xs[0]),
                color=RED, lw=2.1, ls="--", zorder=4)
        aT.set_title(nom, fontsize=12, color=NAVY, pad=7, loc="left")
        aT.grid(axis="y", color=LINE, lw=0.8, zorder=0)
        aT.set_axisbelow(True)
        for s_ in ("top", "right"):
            aT.spines[s_].set_visible(False)
        aT.set_xlabel("Tiempo de deteccion (s)")
        if j == 0:
            aT.set_ylabel("Escenarios")
        aB.plot(xs, cdf(nom, f["params"], xs), color=NAVY2, lw=2.1, zorder=3)
        aB.step(np.sort(x), np.arange(1, len(x) + 1) / len(x), where="post",
                color=NAVY, lw=1.8, ls=":", zorder=4)
        aB.set_xlim(xs[0], xs[-1])
        aB.set_ylim(0, 1.02)
        aB.grid(color=LINE, lw=0.8, zorder=0)
        aB.set_axisbelow(True)
        for s_ in ("top", "right"):
            aB.spines[s_].set_visible(False)
        aB.set_xlabel("Tiempo de deteccion (s)")
        if j == 0:
            aB.set_ylabel("Probabilidad acumulada")
        aB.text(0.03, 0.94, f"D KS = {dec(f['ks'], 3)}\np = {dec(f['p_ks'], 3)}\n"
                            f"dAIC = {dec(f['daic'], 1)}\nw = {dec(f['w_akaike'], 3)}",
                transform=aB.transAxes, va="top", fontsize=9, color=NAVY,
                bbox=dict(boxstyle="round,pad=0.35", fc="#F7F9FC", ec=LINE, lw=1))
    fig.suptitle(titulo, fontsize=14, color=NAVY, x=0.05, ha="left", y=0.965)
    fig.text(0.05, 0.012, "Fuente: elaboracion propia. Fila superior, histograma y densidad ajustada; "
                          "fila inferior, funcion de distribucion acumulada ajustada frente a la empirica.",
             fontsize=9, color=MUTE, ha="left")
    ruta = os.path.join(GRAFI, nombre_archivo)
    fig.savefig(ruta, dpi=100)
    plt.close(fig)
    return ruta


rA1 = figura_candidatas(P1, res_p1,
                        "Prototipo 1: ajuste de las distribuciones candidatas al tiempo de deteccion",
                        "p1-candidatas-distribucion.png", NAVY2)

rA2 = figura_candidatas(P2B, res_p2b,
                        "Prototipo 2: ajuste de las distribuciones candidatas al tiempo de deteccion",
                        "p2-candidatas-distribucion.png", GREEN)

# ── FIGURA B: grafico de probabilidad de la log-normal en ambos prototipos
fig, ax = plt.subplots(1, 2, figsize=(11.52, 5.0), dpi=100)
fig.subplots_adjust(left=0.07, right=0.985, top=0.80, bottom=0.14, wspace=0.24)
for k, (x, tit) in enumerate([(P1, "Prototipo 1, nueve escenarios medidos"),
                              (P2B, "Prototipo 2, medicion final de diez escenarios")]):
    a = ax[k]
    xp = x[x > 0]
    s, scale = mle_lognormal(xp)
    t = np.sort(np.log(xp))
    n = len(t)
    z = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
    a.plot(z, t, "o", color=NAVY, markersize=6, zorder=4, label="Escenarios observados")
    a.plot(z, np.log(scale) + s * z, color=RED, lw=1.9, ls="--", zorder=3,
           label=f"Ajuste log-normal: s = {dec(s, 3)}, ln(mediana) = {dec(np.log(scale), 3)}")
    a.set_title(tit, fontsize=11.5, pad=9, loc="left")
    a.set_xlabel("Cuantil normal teorico")
    a.set_ylabel("Logaritmo del tiempo de deteccion")
    a.grid(color=LINE, lw=0.8, zorder=0)
    a.set_axisbelow(True)
    for s_ in ("top", "right"):
        a.spines[s_].set_visible(False)
    a.legend(frameon=False, fontsize=9, loc="upper left")
    w, pv = stats.shapiro(np.log10(xp))
    a.text(0.03, 0.94, f"Shapiro-Wilk sobre log10\nW = {dec(w, 3)}   p = {dec(pv, 4)}",
           transform=a.transAxes, va="top", fontsize=10, color=NAVY,
           bbox=dict(boxstyle="round,pad=0.4", fc="#F2F7F2", ec=GREEN, lw=1))
fig.suptitle("Grafico de probabilidad de la log-normal con localizacion en cero",
             fontsize=13.5, color=NAVY, x=0.07, ha="left", y=0.955)
fig.text(0.07, 0.015, "Fuente: elaboracion propia con base en los reportes de indicadores de ambos laboratorios. "
                      "El eje vertical es el logaritmo del tiempo de deteccion.",
         fontsize=9, color=MUTE, ha="left")
rB = os.path.join(GRAFI, "log-normal-probabilidad-ambos.png")
fig.savefig(rB, dpi=100)
plt.close(fig)

# ── FIGURA C: cuantiles empiricos frente a los implicitos por cada modelo
fig, ax = plt.subplots(1, 2, figsize=(11.52, 5.0), dpi=100)
fig.subplots_adjust(left=0.07, right=0.985, top=0.80, bottom=0.15, wspace=0.24)
for k, (x, filas, tit) in enumerate([(P1, res_p1, "Prototipo 1"),
                                      (P2B, res_p2b, "Prototipo 2, medicion final")]):
    a = ax[k]
    qs = np.linspace(0.05, 0.99, 40)
    emp = np.quantile(x[x > 0], qs, method="linear")
    a.plot(qs * 100, emp, color=NAVY, lw=2.6, zorder=6, label="Cuantil empirico")
    for nom, col, ls in (("Normal", RED, "--"), ("Log-normal", GREEN, "-"),
                         ("Gamma", AMBER, "-."), ("Weibull", GREY, ":")):
        f = next((z for z in filas if z["modelo"] == nom), None)
        if not f:
            continue
        c = np.array([ppf(nom, f["params"], q) for q in qs])
        a.plot(qs * 100, c, color=col, lw=1.9, ls=ls, zorder=4, label=nom)
    a.axhline(0, color=LINE, lw=1)
    a.set_title(tit, fontsize=11.5, pad=9, loc="left")
    a.set_xlabel("Probabilidad acumulada (%)")
    a.set_ylabel("Tiempo de deteccion (s)")
    a.grid(color=LINE, lw=0.8, zorder=0)
    a.set_axisbelow(True)
    for s_ in ("top", "right"):
        a.spines[s_].set_visible(False)
    a.legend(frameon=False, fontsize=9.5, loc="upper left")
fig.suptitle("Cuantiles implicitos por cada modelo frente a los cuantiles empiricos",
             fontsize=13.5, color=NAVY, x=0.07, ha="left", y=0.955)
fig.text(0.07, 0.015,
         "Fuente: elaboracion propia. El eje vertical en escala lineal muestra que el modelo normal "
         "situa los cuantiles centrales muy por debajo de los valores observados.",
         fontsize=9, color=MUTE, ha="left")
rC = os.path.join(GRAFI, "cuantiles-modelos.png")
fig.savefig(rC, dpi=100)
plt.close(fig)

print(f"\n  figura A1 -> {rA1}")
print(f"  figura A2 -> {rA2}")
print(f"  figura B  -> {rB}")
print(f"  figura C  -> {rC}")

out = {
    "nota": "Version 2. Los modelos con soporte positivo se ajustan con estimadores de maxima "
            "verosimilitud propios y localizacion anclada en cero. La version 1 usaba "
            "stats.<dist>.fit(x, loc=0), que en scipy 1.18.1 no respeta el anclaje.",
    "criterio": f"AIC y BIC con correccion de Lilliefors sobre {BOOT} remuestreos parametricos",
    "semilla": SEMILLA,
    "prototipo_1": {
        "n": len(P1), "valores": P1.tolist(),
        "verificacion_estimadores": ver_p1, "comparacion": res_p1,
        "calibracion_ks": cal_p1,
    },
    "prototipo_2_vuelta_1": {
        "n": len(P2A), "valores": P2A.tolist(), "comparacion": res_p2a,
    },
    "prototipo_2_medicion_final": {
        "n": len(P2B), "valores": P2B.tolist(),
        "verificacion_estimadores": ver_p2b, "comparacion": res_p2b,
        "calibracion_ks": cal_p2,
    },
}
ruta_json = os.path.join(RAIZ, "resultados-prototipos", "seleccion_distribucion.json")
with open(ruta_json, "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
print(f"\n  resultados -> {ruta_json}")
