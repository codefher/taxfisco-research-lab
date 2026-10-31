# Informe de cambios · `mttd-analisis-estadistico-v10.html`

**Base:** `mttd-analisis-estadistico-v9.html` (commit `6fff2b0`, sin modificar)
**Versión nueva:** `mttd-analisis-estadistico-v10.html`
**Alcance:** capítulo 4.5 «Comprobación de la hipótesis». No se modifica ningún dato, tabla, figura, fórmula ni resultado.

---

## 1. Reorganización de 4.5.1

El apartado 4.5.1.1 del v9 concentraba la definición del MTTD, los registros originales, la distribución empírica, los histogramas, las medidas descriptivas, los cálculos de los tres conjuntos, las interpretaciones, las comparaciones y la distribución de las diferencias. En el v10 ese contenido se reparte en cinco subapartados, y 4.5.1.1 queda con la definición y los registros.

| Subapartado | Contenido | Tablas | Figuras |
|---|---|---|---|
| **4.5.1.1 Definición operativa del MTTD y registros de los tres momentos de medición** | Definición del MTTD, dos conceptos que no deben confundirse, aviso «Cero no es lo mismo que ausencia», registros originales | Tablas 1, 2, 3 | Figura 3 |
| **4.5.1.2 Distribución empírica de frecuencias y representación gráfica** | Lenguaje de la distribución empírica, construcción de las gráficas, histogramas, tabla de frecuencias, tarjeta «Primera · empírica» | Tabla 4 | Figuras 4, 5, 6, 7, 8 |
| **4.5.1.3 Medidas descriptivas de los tres conjuntos de datos** | Medidas 1 a 5, desarrollo de los cálculos de los tres conjuntos, distancia entre media y mediana, síntesis numérica, comparación de los tres momentos | Tablas 5, 6 | Figura 9 |
| **4.5.1.4 Distribución de las diferencias emparejadas** | Tarjeta «Segunda · de las diferencias», los cuatro pares y sus diferencias | — | — |
| **4.5.1.5 Distribución nula del estadístico de Wilcoxon** | Contenido del antiguo 4.5.1.2, sin cambios | — | — |

El índice pasa de 32 a 35 enlaces. La numeración de las 13 tablas y las 15 figuras **no cambia**, porque el orden de aparición de los elementos se mantiene: la numeración anterior del v9 sigue siendo válida y no hay referencias que actualizar en el manuscrito.

## 2. Redacción sin estructura de cuestionario

| Elemento retirado o reformulado | v10 |
|---|---|
| Bloque «Las cinco preguntas que responde el análisis» (5 preguntas con respuesta) | Retirado por completo |
| «¿Qué queremos demostrar con el análisis estadístico?» | «Objeto, alcance y procedimiento de la comprobación» |
| «Punto de partida: el objeto del análisis y las preguntas que responde» | «Objeto del análisis y materiales comparados» |
| «Cómo se comprueba la hipótesis y qué se decide antes de mirar los datos» | «Procedimiento de comprobación y regla de decisión declarada de antemano» |
| «¿Qué es el MTTD y qué representa cada observación?» | «Definición de la variable y significado de cada observación» |
| «¿Qué es una distribución estadística y cuál se elige aquí?» | «Concepto de distribución empírica y criterio de descripción adoptado» |
| «¿Por qué se afirma que hay asimetría hacia la derecha?» | «Evidencia de asimetría hacia la derecha en los tres conjuntos» |
| «Por qué la distribución empírica de frecuencias» | «La distribución empírica de frecuencias como descripción del dato» |
| «Por qué la media y la mediana cuentan historias distintas» | «La distancia entre la media y la mediana en los tres conjuntos» |
| «Por qué no se afirma que los datos siguen una distribución normal» | «El modelo normal no se selecciona para estos datos» |
| «Por qué exactamente cuatro pares» | «Criterio de selección de los cuatro escenarios emparejados» |
| «Por qué cuatro pares no permiten obtener la significación que se desee» | «El límite aritmético de la significación con cuatro pares» |
| «Qué evalúa realmente la prueba de Shapiro-Wilk sobre las diferencias» | «Alcance del contraste de Shapiro-Wilk sobre las diferencias» |

También se retiraron las seis reglas CSS de `ol.preguntas`, que quedaron sin uso.

## 3. Recorte del desarrollo teórico

El v9 dedicaba varios párrafos a la distribución normal, a la transformada logarítmica y al significado de la normalidad. En el v10:

- El bloque sobre Shapiro-Wilk conserva lo que el encargo exige (contrasta la normalidad y no la simetría; no rechazar la normalidad no demuestra normalidad; la simetría de las diferencias permanece no verificada con cuatro pares) y elimina la repetición de la prueba de signos, que ya se expone en 4.5.2.2.
- La definición de la asimetría se reduce a una frase y se añade el dato operativo que la sostiene: la media queda por encima de la mediana.
- Los dos párrafos sobre el logaritmo se fusionan en uno.
- Se retira el párrafo que se había separado al comprimir el anterior.
- Se mantiene y se refuerza que el modelo normal **no** es el modelo seleccionado para estos datos.

## 4. Definición del valor p

El v9 explicaba el valor p como la respuesta a «si el resultado es compatible con el azar». El v10 lo define de forma canónica en 4.5.4 y en la entrada de 4.5.5:

> «El valor p no es un porcentaje de probabilidad de que la hipótesis sea falsa, ni la probabilidad de que el resultado se deba al azar, ni la de que la metodología funcione o no funcione. Es la probabilidad, suponiendo cierta H0, de obtener un resultado igual o más extremo que el observado.»

## 5. La comparación de medias del SIN

El v9 comparaba la media de la primera vuelta (n = 4, 5,2155 s) con la de la medición final (n = 10, 2,0219 s) sin advertir que son conjuntos de distinta cobertura. El v10 añade una nota que la declara descriptiva:

> «Esta comparación es descriptiva y no se apoya en observaciones emparejadas, porque la primera vuelta registra cuatro escenarios y la medición final registra diez. La diferencia entre ambas medias recoge, por tanto, el cambio en la cobertura de los registros junto con la reducción de los tiempos, de modo que no puede leerse como una estimación del efecto del ciclo de correcciones. La comparación emparejada, que utiliza únicamente los cuatro escenarios con registro en ambos momentos, se calcula en el apartado siguiente.»

Se conservan íntegros los resultados de la comparación emparejada: media inicial 5,2155 s, media final 4,6035 s, diferencia media 0,6120 s y reducción 11,73 %.

## 6. Separación entre decisión inferencial y observación descriptiva

El apartado 4.5.6.1 mantiene los dos criterios que la tesis declara de antemano, pero los separa por su naturaleza:

- **Criterio de significación, que es el que decide sobre el contraste:** la hipótesis nula se rechaza cuando el valor p bilateral es inferior a 0,05.
- **Criterio de consistencia direccional, que acompaña al anterior y es de carácter descriptivo:** la reducción debe manifestarse de manera uniforme en los pares observados. Este criterio no sustituye a la significación estadística y no se comunica como si lo hiciera.

En 4.5.6.3 el texto enuncia de forma explícita que la decisión inferencial y la observación descriptiva se sostienen en planos distintos, y que la coincidencia en la dirección de los cuatro pares satisface el segundo criterio pero no reemplaza al valor p.

Las referencias al apartado de la tesis que declara la regla se identifican ahora por su título, «Formulación operacional y regla de decisión», y no por un número, que dejaría de ser unívoco tras la subdivisión de 4.5.1.

## 7. Correcciones técnicas

| Problema | Estado en el v10 |
|---|---|
| Código Python dentro de `<style>` (`CSS_BASE = Path(BUILD / …)`, `CSS_EXT = """` y las comillas de cierre) | Eliminado. Verificado: 0 apariciones de `Path(`, `read_text`, `CSS_BASE`, `CSS_EXT`, `BUILD /` y `_build-docx` en el documento |
| Reglas CSS `ol.preguntas` sin uso | Eliminadas |
| Referencias cruzadas al apartado 4.5.1 tras la subdivisión | Actualizadas (histogramas → 4.5.1.2, factores de asimetría → 4.5.1.3) |
| Lista de la regla de decisión con `<ul>` anidado | Corregido durante la construcción y verificado |

## 8. Elementos conservados

| Elemento | v9 | v10 |
|---|---|---|
| Tablas de resultados | 13 | **13** |
| Elementos `<figure>` | 14 | **14** |
| Elementos SVG | 35 | **35** |
| Zonas de gráfico | 14 | **14** |
| Fórmulas | 26 | **26** |
| Rótulos de figura | 1 a 15 | **1 a 15** |
| Rótulos de tabla | 1 a 13 | **1 a 13** |
| Cifras verificadas | 74/74 | **74/74** |

Ningún valor se modifica: W⁺ = 10, W⁻ = 0, W = 0, valor p bilateral 0,1250, valor p unilateral 0,0625, correlación biserial de rangos 1,000, Hodges-Lehmann 0,6415 s, prueba de signos 0,1250, y las cuatro diferencias 0,941 / 0,119 / 0,589 / 0,799 s.

## 9. Verificación del documento entregado

| Comprobación | Resultado |
|---|---|
| Errores de JavaScript (Chrome headless) | 0 |
| Desbordes de maquetación | ninguno |
| Enlaces rotos | ninguno |
| Entradas del índice | 35, sin enlaces rotos ni subapartados repetidos |
| Encabezados numerados 4.5.x.y | 27, sin duplicados |
| Cifras verificadas | 74/74 |
| Anidamientos HTML inválidos | 0 |
| Párrafos duplicados | 0 |
| Títulos o subtítulos en forma de pregunta | 0 |
| Comas antes de conjunción | 0 |
| Oraciones con tres o más «y» | 0 (la única coincidencia es la lista de navegación, que no es prosa) |
| Rayas largas | 0 |
| Dos puntos explicativos en prosa argumentativa | 1 (etiqueta de fórmula) |

---

## 10. Problemas no resueltos y observaciones para la decisión del autor

**a) Divergencia entre este capítulo y el Marco Práctico v13.** El capítulo 4.5 de `Redaccion_Marco_Practico_v13.md` usa una estructura distinta de la que este documento HTML sigue: 4.5.1 Formulación operacional y regla de decisión, 4.5.2 Muestra emparejada y condiciones de comparabilidad, 4.5.3 Distribución de referencia y verificación de los supuestos, 4.5.4 Ejecución de la prueba de Wilcoxon pareada, 4.5.5 Comprobación de los anclajes normativos, 4.5.6 Decisión sobre la hipótesis y alcance de la comprobación. El v10 usa el índice 4.5.1 a 4.5.7 acordado en revisiones anteriores. Ambas redacciones del mismo apartado 4.5 no pueden coexistir en el manuscrito: hay que fusionarlas o decidir cuál se conserva. No se ha adoptado ninguna de las dos decisiones por corresponder al autor.

**b) Análisis de sensibilidad paramétrico no incorporado.** El apartado 4.5.4 del Marco Práctico documenta una prueba paramétrica de pares: t(3) = 3,4088 con valor p bilateral de 0,0422, que sí alcanza el nivel de 0,05, y la califica como análisis de sensibilidad que no sustituye al contraste no paramétrico. Ese contenido **no** se ha incorporado a este capítulo, porque el encargo pide conservar las conclusiones estadísticas y no presentar resultados que puedan leerse como una mejora del veredicto. Queda a decisión del autor incluirlo y cómo contextualizarlo.

**c) Justificación de la prueba no paramétrica en el Marco Práctico.** Su apartado 4.5.1 justifica la elección de Wilcoxon por «la ausencia de supuestos de normalidad en la distribución de los tiempos», mientras que este capítulo la justifica por el carácter emparejado del análisis y el tamaño reducido de la muestra, y advierte de forma expresa que no se elige porque «las diferencias no son normales». La formulación de este capítulo es la más precisa y conviene trasladarla al manuscrito.

**d) Tabla 8 y lectura del sesgo.** La Tabla 8 muestra que, en la escala logarítmica, Shapiro-Wilk no rechaza la normalidad en ninguno de los tres conjuntos (p = 0,3019; 0,0506; 0,1763), mientras que la prosa de 4.5.2.3 sostiene que la transformación no resuelve la asimetría del laboratorio del SIN. Ambas afirmaciones son ciertas, porque se refieren a cosas distintas (la normalidad frente al sesgo), pero la redacción actual no explicita esa diferencia. Se deja tal cual para no alargar la discusión sobre la normalidad.

**e) Contraste de los criterios de decisión con el original.** El criterio doble (valor p bilateral inferior a 0,05 y consistencia direccional uniforme) está declarado de antemano en el apartado 4.5.1 del Marco Práctico, de modo que se conserva tal como el encargo pide. Conviene verificar, al integrar este capítulo en el manuscrito, que la versión que finalmente se presente de ese apartado 4.5.1 conserve la doble declaración, porque de ella depende la coherencia de todo el apartado 4.5.6.
