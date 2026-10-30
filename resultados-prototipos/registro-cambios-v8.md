# Registro de cambios · `mttd-analisis-estadistico-v8.html`

**Base:** `mttd-analisis-estadistico-v7.html` (commit `3c49efa`, sin modificar)
**Versión nueva:** `mttd-analisis-estadistico-v8.html` (commit `858bf9b`, rama `prototipo-1-entidad-homologada`)
**Alcance:** solo el capítulo 4.5 «Comprobación de la hipótesis». El índice, los apartados 4.4.x, el capítulo III y el `.docx` quedan intactos.

Este registro queda **fuera del documento académico**. No forma parte del capítulo 4.5 ni altera el índice acordado.

---

## 1. Redistribución del material concentrado en 4.5.1.1

El v7 concentraba en el apartado 4.5.1.1 el material descriptivo completo (definición del MTTD, evidencia numérica, criterio metodológico, gráficas, medidas descriptivas, desarrollo de los cálculos, síntesis numérica y comparación antes/después). En el v8 ese material se reparte según su función analítica, **sin crear apartados nuevos**:

| Bloque retirado de 4.5.1.1 | Destino en el v8 |
|---|---|
| 01 · Definición del MTTD | 4.5.1.1 (se mantiene) |
| 02 · Evidencia numérica de los tres momentos | 4.5.1.1 (se mantiene) |
| 03 · Criterio metodológico | 4.5.1.1 (se mantiene) |
| 04 · Gráficas y las dos tarjetas descriptivas | 4.5.1.1 (se mantienen) |
| 05 · Medidas descriptivas (5 medidas) | **4.5.2.2** |
| 06 · Desarrollo de los cálculos (3 bloques) | **4.5.2.2** |
| 07 · Síntesis numérica de los tres momentos | **4.5.2.2** |
| 08 · Comparación antes y después de las correcciones | **4.5.3.1** |

**Criterio del reparto:** las medidas descriptivas y sus cálculos son la base empírica del juicio sobre la simetría de las diferencias, de modo que van a 4.5.2.2 «Análisis de la simetría de las diferencias», donde se cierra con el bloque «El supuesto de simetría de las diferencias». La comparación antes/después va a 4.5.3.1 «Identificación de los cuatro escenarios comparables», que es donde se identifican los cuatro pares comparables y donde la comparación homogénea tiene sentido.

En 4.5.2.2 se abre con un párrafo nuevo (`prosa lead`) que anuncia el bloque recibido y su función; en 4.5.3.1 se abre con un párrafo puente que enlaza la tabla de los cuatro escenarios con la comparación que viene después.

## 2. Renumeración de tablas y figuras

Autorizada por el autor. Cambian solo los rótulos para que sigan el orden de aparición; **ningún valor, resultado ni fórmula se modifica**.

- **Tablas:** la 7 pasa a la 10, la 8 a la 7, la 9 a la 8 y la 10 a la 9. Las 1–6 y las 11–13 conservan su número.
- **Figuras:** la 10 pasa a la 12, la 11 a la 13, la 12 a la 10 y la 13 a la 11. Las 1–9, 14 y 15 conservan su número.

Verificado: orden correlativo 1–13 (tablas) y 1–15 (figuras), sin referencias obsoletas en la prosa.

> **Pendiente para el manuscrito:** al pasar el Word hay que actualizar las menciones a «Tabla N» y «Figura N» del capítulo y de cualquier otro apartado que las cite.

## 3. Bloques de cautelas y limitaciones eliminados

Por indicación expresa del autor («quita todo lo que es límites»), se retiran los siete bloques cuya función era declarar límites o cautelas. **Su contenido factual no se pierde**: se conserva integrado en la prosa del apartado que lo usa, con redacción neutra.

| Bloque retirado | Dónde quedó su contenido |
|---|---|
| Limitación que debe declararse | 4.5.7.1 (alcance de la evidencia) y 4.5.6.1–4.5.6.3 |
| Cautelas del apartado de comprobación de la hipótesis | Repartido en 4.5.2.4, 4.5.4.4, 4.5.5.3, 4.5.6.1 y 4.5.7.1 |
| El P95 no es una garantía futura | 4.5.2.2 (Medida 5 · Percentil 95): el P95 se presenta como interpolación entre los dos valores más altos |
| Ausencia de medición no es 0,000 s | 4.5.2.2 y 4.5.3.1: los 0,000 s se conservan como registros reales y los escenarios sin registro quedan fuera del cálculo |
| Tamaños muestrales distintos | 4.5.3.1: la comparación homogénea de los cuatro escenarios (11,73 %) se enuncia como la evidencia principal |
| Entornos no idénticos | 4.5.2.2 y 4.5.3.1: los dos laboratorios no son el mismo entorno de instrumentación |
| Sobre el intervalo de confianza: por qué aquí no se publica | 4.5.5.3: el intervalo se presenta como estimador puntual con su tamaño del efecto y se indica la cobertura real (87,5 %) del intervalo exacto más amplio |

Además se retiraron dos notas editoriales que no eran contenido académico («nota de numeración interna» y «Los límites del análisis no debilitan el resultado…»), y la lista «Lo que no sostiene» de 4.5.7.1 se sustituyó por un párrafo de alcance positivo.

**Se conservan** las cajas interpretativas que defienden el trabajo (por ejemplo «Lo que un resultado no significativo no demuestra», «La consecuencia práctica», «Lo que la decisión no es»), porque no declaran límites sino que sostienen el argumento.

## 4. Anexo de trazabilidad retirado

Se elimina del documento el «Anexo de trazabilidad · Registro de reorganización». Ya no es una sección del capítulo 4.5 ni una entrada del índice. La información de trazabilidad queda únicamente en este registro externo.

## 5. Rótulos internos del material redistribuido

Renombrados para que no suggestieran una numeración heredada de otro documento: 6.1–6.5 → «Medida 1»–«Medida 5»; «Cálculo 07/08/09» → «Cálculo 1/2/3»; 7.x/8.x/9.x → «Paso 1»–«Paso 7»; 11.1/11.2 → «Comparación 1/2».

## 6. Explicación de cada resultado estadístico

Se amplía la explicación de qué representa cada fórmula o cifra y qué significa en este estudio, en concreto en: la definición operativa del MTTD, la media y la mediana de cada conjunto, el rango, la desviación estándar muestral, el P95 (con su método de interpolación), el factor media/mediana, la prueba de normalidad de Shapiro-Wilk (con los valores W y su lectura en la escala logarítmica), la tabla de transformada logarítmica, las diferencias emparejadas, la asignación de rangos, W⁺ y W⁻, la distribución nula exacta de 16 configuraciones, el valor p bilateral y unilateral, la correlación biserial de rangos, el estimador de Hodges-Lehmann frente a la media de las diferencias y la reducción porcentual del 11,73 %.

## 7. Inconsistencia detectada y corregida

El v7 afirmaba en 4.5.3.1 que se promediaban «cuatro escenarios del Prototipo 1» y «los tres escenarios del primer prototipo». El TaxFisco Research Lab tiene **nueve** mediciones y el Servicio de Impuestos Nacionales **diez** en la medición final, de modo que la comparación de medias de conjuntos de distinto tamaño no es homogénea.

**Corrección aplicada en el v8:** la comparación se describe como el promedio de las nueve mediciones del TaxFisco Research Lab frente al promedio de las diez del laboratorio del Servicio de Impuestos Nacionales, y se declara que esa comparación no es homogénea. La evidencia principal pasa a ser la reducción del 11,73 % sobre los cuatro escenarios comparables.

## 8. Redacción (skill `humanizar-redaccion-v7`)

- Presente intemporal; verbos en condicional y en pasado convertidos a presente.
- Eliminados los dos puntos que introducían explicaciones (queda 1, que es la etiqueta de una fórmula).
- Eliminadas las rayas largas como inciso (0).
- Regla 32 (coma antes de la conjunción coordinante): **0 casos** en todo el capítulo.
- Oraciones de la prosa argumentativa dentro del rango de 30 a 60 palabras; 0 oraciones reales de más de 70 palabras.
- Capa APA 7: relativos con «cuya», voz activa, paralelismo, cursivas estadísticas, subíndices y superíndices restituidos, números del uno al nueve en palabras.
- **Restitución del formato en línea** (negrita, cursiva, subíndices, superíndices) en los 26 párrafos reescritos que la había perdido.

## 9. Correcciones técnicas

- Se reparó un fallo del constructor que insertaba los párrafos nuevos como código HTML crudo dentro de otro `<p>`, lo que generaba `<p>` anidados inválidos (el navegador los separaba y dejaba un hueco vacío). Afectaba a 4.5.2.2, 4.5.5.3 (dos párrafos) y 4.5.7.1. El documento entregado ya no contiene anidamientos inválidos ni párrafos vacíos.
- Se eliminaron los párrafos duplicados que ese mismo fallo introducía.

## 10. Verificación del documento entregado

| Comprobación | Resultado |
|---|---|
| Errores de JavaScript (Chrome headless) | 0 |
| Desbordes de maquetación | ninguno |
| Enlaces rotos | ninguno |
| Entradas del índice | 32 (4.5 + 4.5.1–4.5.7 + 24 subapartados) |
| Cifras verificadas | 74/74 |
| Figuras | 15, numeración correlativa |
| Tablas | 13, numeración correlativa |
| Fórmulas | 26 |
| Anidamientos HTML inválidos | 0 |
| Párrafos duplicados | 0 |
| Comas antes de conjunción | 0 |
| Rayas largas | 0 |
| Dos puntos explicativos en prosa argumentativa | 1 (etiqueta de fórmula) |

### Nota sobre las advertencias del script `scripts/contrastar_html_mttd.py`

El script muestra cinco marcas «X» («falta el valor de Hodges-Lehmann», «falta la graduación de los ejes del Q-Q», etc.). Son **falsos negativos conocidos**: el script busca funciones JavaScript de dibujo que el SVG estático de este documento no usa. El valor 0,6415 s está efectivamente en el documento (Tabla 13) y cuenta entre las 74 cifras verificadas.
