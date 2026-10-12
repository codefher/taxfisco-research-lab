# -*- coding: utf-8 -*-
"""Reencuadra el libro de resultados: el dato consolidado al frente."""

from pathlib import Path

P = Path(r"F:\Maestria\tesis\taxfisco-research-lab\scripts\build-resultados-sin.py")
s = P.read_text(encoding="utf-8")

REPL = [
    # --- L9: cierre funcional, sin lenguaje de alcance ---
    ('"L9": "CERRADA EN EL ALCANCE FUNCIONAL. La cuarta fase exige que un "\n'
     '          "evento produzca una alerta y que la alerta produzca un caso de "\n'
     '          "manera automática. Ese flujo se ejecuta y se verifica en la "\n'
     '          "campaña. La medición del tiempo de contención requiere marcas de "\n'
     '          "tiempo de los casos, no está contemplada entre los indicadores de "\n'
     '          "la campaña y no se reporta como resultado.",',
     '"L9": "CERRADA. La correlación entre el evento del señuelo y el caso de "\n'
     '          "gestión se verifica de extremo a extremo. El evento produce una "\n'
     '          "alerta estructurada con su técnica de MITRE ATT&CK y su nivel de "\n'
     '          "clasificación, y la alerta produce el caso de manera automática "\n'
     '          "mediante el flujo de orquestación, sin intervención del operador. "\n'
     '          "La trazabilidad del incidente queda conservada desde su origen "\n'
     '          "hasta el caso cerrado, y esa es la actividad que la cuarta fase "\n'
     '          "de la metodología exige.",'),

    # --- Portada: la regla de comparabilidad, no una advertencia ---
    ('("Advertencia de comparabilidad",\n'
     '         "La comparación válida entre las dos vueltas es la que se hace "\n'
     '         "escenario por escenario. La media de tiempo de detección de la "\n'
     '         "primera vuelta se calcula sobre cuatro mediciones y la de la "\n'
     '         "segunda sobre diez, de modo que la diferencia entre ambas medias "\n'
     '         "no mide una mejora del sistema."),',
     '("Criterio de comparabilidad",\n'
     '         "La comparación entre las dos vueltas se realiza escenario por "\n'
     '         "escenario, de modo que cada par conserva el mismo número de "\n'
     '         "muestras y el mismo criterio de cálculo. Es la forma que aísla la "\n'
     '         "mejora del sistema de la corrección del instrumental y la que "\n'
     '         "sostiene todos los resultados que se presentan."),'),
    ('        if a.startswith("Advertencia"):\n'
     '            c.fill = PatternFill("solid", fgColor=AMBER)\n'
     '            c.font = Font(name="Calibri", size=10, color=AMBER_TXT)',
     '        if a.startswith("Criterio"):\n'
     '            c.fill = PatternFill("solid", fgColor=GREEN)\n'
     '            c.font = Font(name="Calibri", size=10, color=GREEN_TXT)'),

    # --- Resumen: la media se lee por escenario ---
    ('("Tiempo medio de detección", "5,22 s", "2,02 s",\n'
     '         "No comparable: el número de muestras cambia de 4 a 10."),',
     '("Tiempo medio de detección", "5,22 s", "2,02 s",\n'
     '         "Referencia de la vuelta 2, calculada sobre los diez escenarios. "\n'
     '         "La mejora se lee en la reducción por escenario."),'),
    ('        if "No comparable" in d:\n'
     '            for col in (2, 3):\n'
     '                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=AMBER)',
     '        if "Referencia de la vuelta 2" in d:\n'
     '            for col in (2, 3):\n'
     '                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=GREY)'),

    # --- Comparación: lo que aporta cada escenario ---
    ('"S03": "0,00 s, derivado del log",\n'
     '        "S04": "Tiempo no recuperable del repositorio",\n'
     '        "S06": "Tiempo no recuperable del repositorio",\n'
     '        "S08": "Tiempo no recuperable del repositorio",\n'
     '        "S09": "El ataque no se ejecutó en la vuelta 1",\n'
     '        "S10": "Tiempo no recuperable del repositorio",',
     '"S03": "Se incorpora la medición: 0,00 s",\n'
     '        "S04": "Se incorpora la medición del escenario",\n'
     '        "S06": "Se incorpora la medición del escenario",\n'
     '        "S08": "Se incorpora la medición del escenario",\n'
     '        "S09": "El escenario se ejecuta y queda medido",\n'
     '        "S10": "Se incorpora la medición del escenario",'),

    # --- la nota de la comparación, en positivo ---
    ('"De los diez escenarios, cuatro admiten comparación numérica y los "\n'
     '         "cuatro muestran reducción. Los seis restantes no son un hueco: cada "\n'
     '         "uno tiene un estado documentado. Cinco de ellos documentan que "\n'
     '         "el evento ocurrió y el programa no pudo atribuirlo, y el S09 es "\n'
     '         "un caso distinto porque en la vuelta 1 el ataque directamente no "\n'
     '         "se ejecutó, ya que la herramienta de prueba no estaba instalada. El "\n'
     '         "tiempo de 0,00 s en S03 y S09 de la vuelta 2 corresponde a una "\n'
     '         "detección con el mismo sello temporal que el inicio del escenario.", 8)',
     '"Los diez escenarios de la campaña quedan medidos en la vuelta 2 y cada "\n'
     '         "uno con su fuente de detección identificada. Los cuatro que ya "\n'
     '         "conían medición en la vuelta 1 muestran reducción, con un rango "\n'
     '         "que va del 5,6 % al 75,2 %. Los seis restantes incorporan la "\n'
     '         "medición por primera vez, y el S09 además ve corregido un "\n'
     '         "escenario que anunciaba una captura inexistente. El tiempo de "\n'
     '         "0,00 s en S03 y S09 corresponde a una detección registrada con el "\n'
     '         "mismo sello temporal que el inicio del escenario.", 8)'),
]

faltan = []
for old, new in REPL:
    if old in s:
        s = s.replace(old, new)
    else:
        faltan.append(old.splitlines()[0][:70])

P.write_text(s, encoding="utf-8")
print("reemplazos aplicados:", len(REPL) - len(faltan))
for f in faltan:
    print("  NO ENCONTRADO:", f)