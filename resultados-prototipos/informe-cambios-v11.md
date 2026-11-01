# Informe de cambios · `mttd-analisis-estadistico-v11.html`

**Base:** `mttd-analisis-estadistico-v10.html` (commit `b3f55fc`, sin modificar)
**Versión nueva:** `mttd-analisis-estadistico-v11.html`
**Alcance:** redacción y organización del capítulo 4.5 «Comprobación de la hipótesis». No se modifica ningún dato, tabla, figura, fórmula ni resultado.

---

## 1. Retirada del preámbulo

Se eliminó por completo el bloque que encabezaba el apartado:

> **Procedimiento de comprobación y regla de decisión declarada de antemano**
> Los resultados descriptivos muestran que, en los cuatro escenarios medidos en ambas vueltas, el tiempo de detección registrado fue menor en la medición final. Describir ese hecho no es comprobarlo, porque la comprobación exige fijar una hipótesis nula, elegir una prueba que se ajuste a los datos disponibles y decidir el resultado según una regla declarada de antemano.

El bloque reunía dos problemas. Por un lado, el párrafo explica al lector por qué existe un apartado de comprobación, en lugar de limitarse a comprobarlo. Por otro, el título anunciaba una «regla de decisión declarada de antemano» que ya se expone con detalle en 4.5.6.1, donde figuran la hipótesis nula, la alternativa, el nivel α = 0,05, el criterio de significación, el criterio de consistencia direccional y la declaración previa. La retirada no suprime contenido: el argumento de la regla declarada de antemano permanece en 4.5.6.1 y en 4.5.4.2, y la secuencia de apartados ya se anuncia en el párrafo de apertura del apartado 4.5.

La lista de recorrido del apartado (los siete apartados con su enlace) se conserva, porque funciona como índice navegable y no como explicación.

## 2. Títulos de los apartados reescritos

El título de 4.5.1 era el del V9 y describía solo dos de los cinco subapartados que el V10 había colocado debajo. Los títulos se reescribieron para que cada apartado anuncie lo que realmente contiene, y se actualizaron a la vez en los tres lugares donde aparecen: el índice general, la lista de recorrido y el encabezado de la sección.

| Apartado | V10 | V11 |
|---|---|---|
| 4.5.1 | Distribución de las diferencias emparejadas y distribución nula | **Base empírica, diferencias emparejadas y distribución nula** |
| 4.5.2 | Verificación de las condiciones de aplicación de la prueba | **Condiciones de aplicación de la prueba de Wilcoxon** |
| 4.5.3 | Cálculo del estadístico de la prueba de Wilcoxon | **Cálculo del estadístico de Wilcoxon sobre las diferencias emparejadas** |
| 4.5.4 | Determinación del valor p mediante la distribución nula exacta | **Distribución nula exacta y cálculo del valor p** |
| 4.5.5 | Determinación e interpretación del tamaño del efecto | **Determinación del tamaño del efecto y su interpretación** |
| 4.5.6 | Contraste y decisión sobre la hipótesis | Contraste y decisión sobre la hipótesis (sin cambio) |
| 4.5.7 | Síntesis de la comprobación de la hipótesis | Síntesis de la comprobación de la hipótesis (sin cambio) |

Los subtítulos de esos siete apartados, que estaban redactados en forma de pregunta o de didáctica («Qué exige la prueba y qué puede sostener con cuatro observaciones», «El cálculo del estadístico, paso a paso», «Cuánto mejora, con independencia del valor p»), se pasaron a forma nominal:

| Apartado | Subtítulo en el V10 | Subtítulo en el V11 |
|---|---|---|
| 4.5.1 | Distribución empírica, distribución de las diferencias y distribución nula | Descripción empírica de los datos y preparación del contraste |
| 4.5.2 | Qué exige la prueba y qué puede sostener con cuatro observaciones | Requisitos de la prueba y alcance con cuatro observaciones |
| 4.5.3 | El cálculo del estadístico, paso a paso | Cálculo del estadístico a partir de las diferencias emparejadas |
| 4.5.4 | Dónde se ubica el estadístico observado y cómo se obtiene el valor p | Ubicación del estadístico observado y cálculo del valor p |
| 4.5.5 | Cuánto mejora, con independencia del valor p | Magnitud de la mejora con independencia del valor p |
| 4.5.6 | La regla que decide, lo que el resultado permite y la decisión adoptada | Criterio de decisión, alcance del resultado y decisión adoptada |
| 4.5.7 | Qué sostiene la evidencia y cómo se enuncia la conclusión | Evidencia reunida y enunciado de la conclusión |

## 3. Coherencia interna de 4.5.1

Tres ajustes de encaje, derivados de la subdivisión en cinco subapartados:

1. **Párrafo de la base empírica.** Decía que la descripción «se expone en cuatro apartados consecutivos», expresión que quedaba sin referente claro. Ahora dice que los apartados 4.4.2 a 4.4.4 dejan establecida la descripción empírica y que este apartado la reproduce íntegra y la ordena según la función de cada pieza.
2. **Encabezado repetido.** El subapartado 4.5.1.1 se titula «Definición operativa del MTTD y registros de los tres momentos de medición», y dentro repetía el encabezado «Definición operativa del MTTD». Ese encabezado interno pasa a llamarse «Definición de la variable».
3. **Frase didáctica de apertura del apartado 4.5.** «No basta con afirmar que el segundo prototipo presenta una media menor, porque el análisis debe explicar…» se sustituyó por una enunciación directa: «El apartado describe cómo se distribuyen los tiempos, cuáles son los valores habituales, cuáles son excepcionalmente altos y qué se observa después de incorporar las lecciones aprendidas». Es el mismo defecto de tono que el del preámbulo retirado, y estaba en el mismo lugar del texto.

## 4. Elementos conservados

| Elemento | V10 | V11 |
|---|---|---|
| Tablas de resultados | 13 | **13** |
| Elementos `<figure>` | 14 | **14** |
| Elementos SVG | 35 | **35** |
| Zonas de gráfico | 14 | **14** |
| Fórmulas | 26 | **26** |
| Rótulos de figura | 1 a 15 | **1 a 15** |
| Rótulos de tabla | 1 a 13 | **1 a 13** |
| Entradas del índice | 35 | **35** |
| Encabezados numerados 4.5.x.y | 27 | **27** |
| Cifras verificadas | 74/74 | **74/74** |

Ningún valor se modifica: W⁺ = 10, W⁻ = 0, W = 0, valor p bilateral 0,1250, valor p unilateral 0,0625, correlación biserial de rangos 1,000, Hodges-Lehmann 0,6415 s, prueba de signos 0,1250, y las cuatro diferencias 0,941 / 0,119 / 0,589 / 0,799 s. La numeración de apartados, tablas y figuras no se modifica, de modo que no hay referencias que actualizar en el manuscrito.

## 5. Verificación del documento entregado

| Comprobación | Resultado |
|---|---|
| Errores de JavaScript (Chrome headless) | 0 |
| Desbordes de maquetación | ninguno |
| Enlaces rotos | ninguno |
| Coincidencia entre el encabezado de cada apartado y su entrada en la lista de recorrido | 7 de 7 |
| Títulos nuevos presentes en los tres lugares | 5 de 5 |
| Títulos antiguos ausentes | 5 de 5 |
| Subtítulos nuevos presentes y antiguos ausentes | 7 de 7 |
| Referencias cruzadas a apartados 4.5.x.y rotas | ninguna (11 referencias comprobadas) |
| Anidamientos HTML inválidos | 0 |
| Párrafos o elementos vacíos | 0 |
| Títulos o subtítulos en forma de pregunta | 0 |
| Comas antes de conjunción | 0 |
| Rayas largas | 0 |
| Dos puntos explicativos en prosa argumentativa | 1 (etiqueta de fórmula) |

---

## 6. Observaciones que siguen abiertas

Se mantiene lo que el informe del V10 dejó anotado y que no depende de este cambio:

**a) Divergencia entre este capítulo y el Marco Práctico v13.** El capítulo 4.5 de `Redaccion_Marco_Practico_v13.md` usa un índice distinto del que sigue este documento (4.5.1 Formulación operacional y regla de decisión … 4.5.6 Decisión sobre la hipótesis), mientras el HTML mantiene el índice 4.5.1 a 4.5.7 acordado en revisiones anteriores. Ambas redacciones del mismo apartado 4.5 no pueden coexistir en el manuscrito, de modo que hay que fusionarlas o decidir cuál se conserva.

**b) Análisis de sensibilidad paramétrico no incorporado.** El apartado 4.5.4 del Marco Práctico documenta una prueba paramétrica de pares, t(3) = 3,4088 con valor p bilateral de 0,0422, que sí alcanza el nivel de 0,05, y la califica como análisis de sensibilidad que no sustituye al contraste no paramétrico. Ese contenido no se ha incorporado, porque el encargo pide conservar las conclusiones estadísticas y no presentar resultados que puedan leerse como una mejora del veredicto. Queda a decisión del autor incluirlo y cómo contextualizarlo.

**c) Justificación de la prueba no paramétrica divergente.** El Marco Práctico justifica la elección de Wilcoxon por «la ausencia de supuestos de normalidad en la distribución de los tiempos», mientras que este capítulo la justifica por el carácter emparejado del análisis y el tamaño reducido de la muestra, y advierte de forma expresa que no se elige porque «las diferencias no son normales». La formulación de este capítulo es la más precisa y conviene trasladarla al manuscrito.

**d) Tabla 8 y lectura del sesgo.** La Tabla 8 muestra que, en la escala logarítmica, Shapiro-Wilk no rechaza la normalidad en ninguno de los tres conjuntos (p = 0,3019; 0,0506; 0,1763), mientras que la prosa de 4.5.2.3 sostiene que la transformación no resuelve la asimetría del laboratorio del SIN. Ambas afirmaciones son ciertas, porque se refieren a cosas distintas, la normalidad frente al sesgo, pero la redacción no explicita esa diferencia. Se deja tal cual para no alargar la discusión sobre la normalidad.

**e) Coherencia del criterio doble al integrar.** El criterio doble (valor p bilateral inferior a 0,05 y consistencia direccional uniforme) está declarado de antemano en el apartado 4.5.1 del Marco Práctico, de modo que se conserva tal como el encargo pide. Conviene verificar, al integrar este capítulo en el manuscrito, que la versión que finalmente se presente de ese apartado 4.5.1 conserve la doble declaración, porque de ella depende la coherencia de todo el apartado 4.5.6.

**f) Título de 4.5.1 y contenido del apartado.** Con el título reescrito, 4.5.1 reúne cinco piezas (definición de la variable, registros, distribución empírica, medidas descriptivas, diferencias emparejadas y distribución nula) que en el capítulo 4.4 aparecen ya descritas. El apartado 4.5.1.1 lo declara de forma expresa, de modo que la superposición con 4.4.2 a 4.4.4 es intencional y está señalizada. Si en la versión integrada se prefiera evitar la repetición, la alternativa sería remitir a 4.4 sin reproducir las Tablas 1 a 6 ni las Figuras 3 a 9, lo que reduciría el recuento de tablas y figuras del capítulo.
