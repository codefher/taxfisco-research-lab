# Registro de cambios · `mttd-analisis-estadistico-v9.html`

**Base:** `mttd-analisis-estadistico-v8.html` (commit `caebd86`, sin modificar)
**Versión nueva:** `mttd-analisis-estadistico-v9.html`
**Alcance:** solo el capítulo 4.5 «Comprobación de la hipótesis». El índice 4.5.1 a 4.5.7 con sus 24 subapartados, los apartados 4.4.x, el capítulo III y el `.docx` quedan intactos.

Este registro queda **fuera del documento académico**. No forma parte del capítulo 4.5 ni altera el índice acordado.

---

## 1. Reubicación de los contenidos por función

El v8 había concentrating en 4.5.2.2 el bloque descriptivo completo (medidas, cálculos y síntesis de los tres momentos), que es un apartado dedicado al análisis de la simetría de las diferencias. En el v9 ese bloque se devuelve al apartado cuya función le corresponde y 4.5.2.2 queda centrado en su propio objeto.

| Contenido | Ubicación en el v9 | Razón funcional |
|---|---|---|
| Definición operativa del MTTD | **4.5.1.1** | Define la variable sobre la que se calculan las diferencias |
| Registros originales de los tres momentos | **4.5.1.1** | Material de partida de toda la comprobación |
| Distribución empírica de frecuencias | **4.5.1.1** | Explica cómo se lee la forma de los datos |
| Construcción e interpretación de histogramas | **4.5.1.1** | Expresión gráfica de esa misma distribución |
| Medidas descriptivas (Medida 1 a Medida 5) | **4.5.1.1** *(salen de 4.5.2.2)* | Son la lectura numérica de las distribuciones descritas, no un análisis de simetría |
| Cálculos de media, mediana, rango, desviación estándar y P95 | **4.5.1.1** *(sale de 4.5.2.2)* | Desarrollo numérico de esas mismas medidas |
| Comparación de los tres momentos de medición | **4.5.1.1** *(sale de 4.5.2.2)* | Síntesis de la descripción empírica (Tabla 6 y Figura 9) |
| Distribución de las diferencias emparejadas | **4.5.1.1** (bloque nuevo de cierre) | Da nombre al apartado y anuncia el objeto del contraste |
| Distribución nula de Wilcoxon | **4.5.1.2** | Sin cambios |

**4.5.2.2 «Análisis de la simetría de las diferencias»** queda con tres piezas: el párrafo de entrada, que explica qué supone la prueba y por qué la simetría es un supuesto que esta muestra no puede verificar; un párrafo con la evidencia descriptiva que pone ese supuesto en duda (la media supera a la mediana en los tres conjuntos, con factores de 50,4, 3,5 y 4,0); y el bloque «El supuesto de simetría de las diferencias» con el remalte al contraste de signos, que no lo exige. Los valores de los factores se calculan en 4.5.1.1 y se remiten desde allí, de modo que 4.5.2.2 los utiliza sin volver a cargarlos.

**4.5.1.1 «Distribución de las diferencias entre los tiempos iniciales y finales»** cierra ahora con el bloque «La distribución de las diferencias emparejadas», que expone los cuatro valores (0,941 s en S01, 0,119 s en S02, 0,589 s en S05 y 0,799 s en S07), señala que todos son positivos y encamina la lectura hacia 4.5.3.2, 4.5.3.5, 4.5.2.2 y 4.5.2.3. Así el apartado contiene el contenido que su título anuncia.

### Otros ajustes de estructura

- La etiqueta «Primera · empírica», que había quedado huérfana al final de 4.5.3.1, vuelve a preceder a la tarjeta «Distribución de los tiempos T» en 4.5.1.1. Las tres tarjetas vuelven a formar la secuencia T, D y nula.
- Los textos de las dos tarjetas se reescriben para su nueva ubicación y para que cada una se entienda por sí misma.
- La Tabla 8 se introduce con un párrafo propio, que antes faltaba.
- El índice no cambia: 4.5, los apartados 4.5.1 a 4.5.7 y los 24 subapartados, 32 enlaces en total. La numeración de las 13 tablas y las 15 figuras se mantiene, porque el orden de aparición de los elementos no cambia con la reubicación.

## 2. Eliminación de las expresiones dirigidas al autor o a la tutora

| Texto del v8 | Texto del v9 |
|---|---|
| «La tutora pidió distinguir con precisión la distribución de los datos, la distribución de las diferencias y la distribución de referencia bajo la hipótesis nula.» | «Distinguir con precisión la distribución de los datos observados, la distribución de las diferencias emparejadas y la distribución de referencia bajo la hipótesis nula evita afirmaciones que los datos no sostienen.» |
| «Qué sostiene la evidencia y cómo se presenta ante la tutora» | «Qué sostiene la evidencia y cómo se enuncia la conclusión» |
| «Una precisión que evita contradicciones en la defensa» | «Dos estimadores que no deben confundirse» |
| «Concepto clave para la defensa: la asimetría de los tiempos» | «La asimetría de los tiempos como rasgo de la distribución» |
| «Conclusión correcta de la comparación» | «Conclusión de la comparación» |

Verificado: el capítulo no contiene ninguna aparición de «tutora», «tutor» ni «defensa».

## 3. Corrección de las interpretaciones

**La afirmación corregida.** El v8 sostenía en 4.5.7.1 que «el sentido del cambio es consistente en los cuatro pares, lo que descarta que el resultado dependa de un único escenario extremo». La coincidencia en la dirección de los cuatro pares indica que la reducción no es el producto de un único escenario, pero no permite afirmar independencia frente a los valores extremos, porque las magnitudes de las reducciones difieren entre sí y ningún par resume el conjunto.

El v9 dice: «El sentido del cambio es consistente en los cuatro pares, de modo que la reducción no es el producto de un único escenario. Esta coincidencia en la dirección no equivale a independencia frente a los valores extremos, porque las magnitudes de las reducciones difieren entre sí y ningún par resume por sí solo el conjunto.»

**Otros casos revisados.** «El pareamiento por técnica garantiza que cada comparación enfrente el mismo tipo de ataque» pasa a «hace que cada comparación enfrente el mismo tipo de ataque», porque el pareamiento describe una característica del diseño y no garantiza un resultado. Se mantienen sin cambio las afirmaciones que los datos sostienen: la dirección del efecto, la ocupación del extremo del soporte, el valor p bilateral de 0,1250 como mínimo aritmético de cuatro pares, la cobertura real del 87,5 % del intervalo exacto y la coincidencia del valor p de la prueba de signos con el de la prueba de Wilcoxon.

**Corrección de redacción.** «Solo cuatro escenarios del laboratorio fiscal cuentan con registro» pasa a «solo cuatro escenarios de ese laboratorio», que era una denominación incorrecta del laboratorio del Servicio de Impuestos Nacionales.

## 4. Redacción (`humanizar-redaccion-v7`)

- Presente intemporal en toda la prosa.
- **Regla 31 (máximo dos «y» por oración):** el v8 tenía una oración con tres «y» en la apertura del capítulo; el v9 tiene **0**. Se reescribió con subordinación en lugar de coordinar.
- **Regla 32 (coma antes de la conjunción coordinante): 0** en todo el capítulo.
- Dos puntos que introducen explicaciones: **1**, y es la etiqueta de una fórmula. Rayas largas: **0**.
- Oraciones de la prosa argumentativa: la mayoría entre 30 y 60 palabras. Las oraciones de menos de 18 palabras son rótulos, entradas de lista y pie de figura, y su número **baja de 266 a 257** respecto del v8.
- Capa APA 7: relativos con «cuya» y con «que», voz activa, series con estructura paralela, números del uno al nueve en palabras, cursivas estadísticas, subíndices y superíndices.
- Cada párrafo se lee por sí mismo, con tabla introducida antes de aparecer y figura interpretada después de mostrarse.

## 5. Elementos conservados

| Elemento | v8 | v9 |
|---|---|---|
| Tablas de resultados | 13 | **13** |
| Elementos `<figure>` | 14 | **14** |
| Elementos SVG | 35 | **35** |
| Zonas de gráfico | 14 | **14** |
| Fórmulas | 26 | **26** |
| Rótulos de figura | 1 a 15 | **1 a 15** |
| Rótulos de tabla | 1 a 13 | **1 a 13** |

Ningún dato, tabla, cálculo, fórmula, figura o elemento SVG interactivo se modificó ni se eliminó. Los valores de Wilcoxon (W⁺ = 10), los cuatro pares, el valor p bilateral de 0,1250, el unilateral de 0,0625, la correlación biserial de rangos, el estimador de Hodges-Lehmann (0,6415 s) y la reducción del 11,73 % se conservan sin variación.

## 6. Verificación del documento entregado

| Comprobación | Resultado |
|---|---|
| Errores de JavaScript (Chrome headless) | 0 |
| Desbordes de maquetación | ninguno |
| Enlaces rotos | ninguno |
| Entradas del índice | 32, sin cambios |
| Cifras verificadas | 74/74 |
| Anidamientos HTML inválidos | 0 |
| Párrafos duplicados | 0 |
| Comas antes de conjunción | 0 |
| Oraciones con tres o más «y» | 0 |
| Rayas largas | 0 |
| Dos puntos explicativos en prosa argumentativa | 1 (etiqueta de fórmula) |

### Nota sobre las advertencias del script `scripts/contrastar_html_mttd.py`

El script muestra cinco marcas «X» («falta el valor de Hodges-Lehmann», «falta la graduación de los ejes del Q-Q», etc.). Son **falsos negativos conocidos**: el script busca funciones JavaScript de dibujo que el SVG estático de este documento no usa. El valor 0,6415 s está efectivamente en el documento (Tabla 13) y cuenta entre las 74 cifras verificadas.
