"""Verificador de una matriz de postest del instrumento de madurez.

Corre sobre cualquier libro de Excel que la institucion entregue y responde a las
preguntas que un investigador necesita responder antes de usar un dato:

    1. Cuantos respondentes y cuantos reactivos contiene cada matriz.
    2. Que valores aparecen y con que frecuencia.
    3. Cuantos respondentes alcanzan el puntaje perfecto.
    4. Que alfa de Cronbach produce la matriz.
    5. Si la matriz parece provenir de respuestas reales o de una construccion
       hacia un numero objetivo.

Uso:
    py -3 scripts/verificar-matriz-postest.py archivo.xlsx
"""
import os
import statistics as st
import sys

sys.stdout.reconfigure(encoding="utf-8")

from openpyxl import load_workbook

# Rangos de referencia observados en autoinformes reales con treinta personas.
ALFA_MIN = 0.70
ALFA_MAX = 0.97
PORC_PERFECTOS_MAX = 0.10
VALORES_MINIMOS = 3


ETIQUETAS_NO_RESP = {"var", "k", "total", "tasa", "promedio"}


def matrices_del_libro(wb):
    """Localiza en cada hoja la matriz mas ancha de valores enteros de 0 a 4.

    Solo se consideran filas cuya primera celda sea una etiqueta de respondente,
    de modo que las filas de calculo como la de varianzas no se incorporen.
    """
    encontradas = []
    for nombre in wb.sheetnames:
        ws = wb[nombre]
        filas = []
        for r in range(1, min(ws.max_row, 200) + 1):
            etiqueta = ws.cell(row=r, column=1).value
            if not isinstance(etiqueta, str):
                continue
            if etiqueta.strip().lower().split(" ")[0] in ETIQUETAS_NO_RESP:
                continue
            fila = [ws.cell(row=r, column=c).value
                    for c in range(2, min(ws.max_column, 120) + 1)]
            fila = [v for v in fila if isinstance(v, int) and 0 <= v <= 4]
            if len(fila) >= 20:
                filas.append(fila)
        if filas:
            ancho = min(len(f) for f in filas)
            encontradas.append((nombre, [f[:ancho] for f in filas]))
    return encontradas


def analizar(datos):
    n = len(datos)
    k = min(len(f) for f in datos)
    maximo = 4 * k

    dist = {}
    for f in datos:
        for v in f:
            dist[v] = dist.get(v, 0) + 1
    total = sum(dist.values())

    totales = [sum(f) for f in datos]
    perfectos = sum(1 for t in totales if t == maximo)

    s2 = sum(st.variance([f[i] for f in datos]) for i in range(k))
    st2 = st.variance(totales)
    alfa = (k / (k - 1)) * (1 - s2 / st2) if st2 else 0.0

    return {"n": n, "k": k, "maximo": maximo, "dist": dist, "total": total,
            "totales": sorted(totales), "perfectos": perfectos, "alfa": alfa}


def veredicto(m):
    alertas = []
    if len(m["dist"]) < VALORES_MINIMOS:
        alertas.append(
            "La matriz solo usa %d valores distintos. Un autoinforme real de %d personas "
            "sobre %d reactivos emplea al menos tres." % (len(m["dist"]), m["n"], m["k"]))
    p = m["perfectos"] / m["n"]
    if p > PORC_PERFECTOS_MAX:
        alertas.append(
            "%d de %d respondentes alcanzan el puntaje perfecto de %d sobre %d reactivos "
            "(%.0f %%). En un autoinforme real esa proporcion es baja."
            % (m["perfectos"], m["n"], m["maximo"], m["k"], p * 100))
    if m["alfa"] > ALFA_MAX:
        alertas.append(
            "El alfa de Cronbach de %.4f supera el rango habitual de campo (%.2f a %.2f). "
            "Un valor asi aparece cuando la matriz casi no tiene variacion."
            % (m["alfa"], ALFA_MIN, ALFA_MAX))
    if m["alfa"] < ALFA_MIN:
        alertas.append("El alfa de %.4f queda bajo el minimo aceptable de %.2f."
                       % (m["alfa"], ALFA_MIN))

    if len(m["dist"]) <= 2 and p > 0.5:
        estado = "ALTAMENTE SOSPECHOSO"
    elif alertas:
        estado = "REVISAR"
    else:
        estado = "VERIFICABLE"
    return estado, alertas


def main():
    if len(sys.argv) < 2:
        print("Uso: py -3 scripts/verificar-matriz-postest.py archivo.xlsx")
        return 1
    ruta = sys.argv[1]
    if not os.path.exists(ruta):
        print("No se encuentra el archivo:", ruta)
        return 1

    wb = load_workbook(ruta, data_only=True)
    print("Archivo :", os.path.basename(ruta))
    print("Hojas   :", ", ".join(wb.sheetnames))

    encontradas = matrices_del_libro(wb)
    if not encontradas:
        print("\nNo se encontro ninguna matriz de valores de 0 a 4 en el archivo.")
        return 1

    for nombre, datos in encontradas:
        m = analizar(datos)
        estado, alertas = veredicto(m)
        print()
        print("=" * 68)
        print("MATRIZ en la hoja:", nombre)
        print("  respondentes           :", m["n"])
        print("  reactivos              :", m["k"])
        print("  puntaje maximo posible :", m["maximo"])
        print("  valores distintos      :", dict(sorted(m["dist"].items())))
        print("  respuesta dominante   : %.1f %%"
              % (max(m["dist"].values()) / m["total"] * 100))
        print("  respondentes perfectos : %d de %d (%.0f %%)"
              % (m["perfectos"], m["n"], m["perfectos"] / m["n"] * 100))
        print("  alfa de Cronbach       : %.6f" % m["alfa"])
        print("  VEREDICTO              :", estado)
        for a in alertas:
            print("     - " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())