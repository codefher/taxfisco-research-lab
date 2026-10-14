# Guía de cumplimiento de las indicaciones de la tutora

**Capítulo de resultados del Prototipo II, laboratorio SIN.**
Documento de respaldo que relaciona cada indicación recibida con el entregable que la atiende y con el apartado del capítulo donde se desarrolla.

---

## Cómo se organiza el capítulo de resultados

El capítulo de resultados sigue siete apartados. Cada uno responde a una función distinta dentro del argumento de la metodología.

| Apartado | Función | Contenido |
| --- | --- | --- |
| 4.4.1 | Línea base institucional y reglas de presentación | Madurez de los catorce instrumentos, distancia al corte Gestionado y criterio de comparación |
| 4.4.2 | Resultados del primer prototipo | Indicadores del primer laboratorio con su archivo de origen y lectura de su valor |
| 4.4.3 | Primera vuelta | Diez escenarios, medición en cuatro, catálogo de siete lecciones |
| 4.4.4 | Segunda vuelta | Correcciones aplicadas y medición en los diez escenarios |
| 4.4.5 | Antes y después cuantificado | Indicadores que cambian, indicadores constantes y reducción por escenario |
| 4.4.6 | Aportación de cada fase y trazabilidad de las brechas | Qué entrega cada fase al resultado y qué indicador verifica cada brecha |
| 4.4.7 | Resultado global del libro oficial de la institución | El 99,09 % que calcula el libro oficial y la operación que lo produce |
| 4.4.8 | Síntesis de los resultados | Lectura conjunta del valor del producto y enlace entre el antes y el después |

El apartado 4.4 se incorpora a `tesis/Redaccion_Marco_Practico_v11_v1.5.md` entre el apartado 4.3.7 y el Capítulo V, con las tablas 11 a 20 y las figuras 57 a 59.

### Sobre el resultado global del libro oficial

El libro oficial de resultados del Servicio de Impuestos Nacionales calcula la madurez global como el promedio simple de los catorce instrumentos sobre la matriz de treinta participantes, y ese cálculo arroja 99,0873015873016 %, cifra que redondea a 99,09 %. El apartado 4.4.7 presenta el valor con la operación que lo produce, con el nombre de la hoja que lo calcula y con el tamaño de la matriz, de manera que el lector puede reproducirlo en el archivo. La cifra de 99,06 % que el propio libro menciona es la meta que declara haber tomado como objetivo, no un resultado.

La matriz de treinta filas y cuarenta y dos columnas que circula en el libro de cálculo recibido no se utiliza. Cuarenta y siete de sus celdas contienen el valor 3 y las restantes 1 213 el valor 4, de modo que el 96,3 % de las respuestas coincide. Veintiocho de los treinta participantes alcanzan el puntaje perfecto de 168 sobre 168, proporción que no aparece en un autoinforme. La suma de varianzas de esa matriz es 1,555 y produce un alfa de 0,9975, valor que se alcanza únicamente cuando la matriz carece de variación. Además, el promedio que la matriz produce es 99,09 % mientras que la meta declarada en la hoja *Comparación pre-post* es 99,06 %, de modo que la matriz se construyó hacia un número objetivo y no hacia una medición.

El archivo de evidencia es `resultados-cap4/v05/evidencia-institucional/resultado-oficial-sin-99-09.md` y el verificador `scripts/verificar-matriz-postest.py` comprueba cualquier archivo que la institución entregue en el futuro.

La estructura respeta la separación entre el primer y el segundo prototipo, de modo que cada uno conserve su propio apartado y las fases se analicen dentro de cada uno.

---

## Indicación 1 · Presentar los resultados mediante un dashboard

La indicación pide resultados visibles, ordenados y profesionales. El tablero reúne los indicadores en diez secciones que se leen de arriba hacia abajo.

**Entregable**

- `dashboard-resultados.html` es el tablero navegable, sin dependencias externas.
- `dashboard-resultados.pdf` es la versión para consultar o imprimir.
- `dashboard-resultados.docx` es la versión para insertar en el capítulo.

**Las diez secciones del tablero**

1. Indicadores principales, con ocho cifras de cabecera.
2. Antes y después de la medición, con la lectura del cambio en tabla.
3. Tiempo de detección de los cuatro escenarios comparables.
4. Distribución del tiempo de detección en la medición final.
5. Fuentes que registran la detección, de tres a seis componentes.
6. Cobertura de MITRE ATT&CK, con inventario y detección separados.
7. Ciclo de iteraciones, con la línea de tiempo del ciclo de corrección.
8. Aportación de cada fase de la metodología.
9. Registro de lecciones aprendidas, con las catorce cerradas.
10. Volumen de actividad de la campaña en las dos vueltas.
11. Evidencia visual del tablero de alertas, con la captura de cada vuelta.

**Sobre la sección undécima.** Los dos tableros del laboratorio existen como evidencia y ninguno estaba citado en el capítulo. La sección los incorpora ahora como figura 1 y figura 2, cada uno con su nota al piepegada debajo. Los paneles conservan ventanas temporales distintas, tres horas en la línea base y veinticuatro horas en la medición final, porque la cadena de indexación se puso en marcha entre una captura y la otra. El tablero declara esa diferencia para que el lector no interprete los totales de los paneles como una serie homogénea. La comparación numérica entre las dos vueltas se sostiene en los reportes de indicadores, que comparten escenario, criterio de cálculo y ventana de ejecución.

**Nota.** Las fuentes de cada cifra se declaran al pie del tablero. Todo dato procede de los archivos de evidencia del repositorio y ninguno es estimado.

**Sobre la versión en Word.** El documento contiene diez figuras y diecisiete tablas. Los gráficos son imágenes capturadas a tres veces la resolución de pantalla, de modo que conservan el color y la nitidez al imprimirse. Los textos, los títulos y las tablas son objetos nativos de Word, con lo cual puede editarse cualquier palabra sin degradar el diseño. El número de cada figura va en redonda y el título en cursiva, con la nota inmediatamente debajo, sin nada en medio. La paleta azul institucional del tablero se reproduce en los títulos de nivel uno y dos, en el encabezado de cada tabla y en los recuadros de lectura.

---

## Indicación 2 · Presentar los resultados sin comprobación de hipótesis

La indicación pide presentación y análisis, sin inferencia estadística. El capítulo no contiene pruebas de hipótesis, valores p, intervalos de confianza ni decisiones de rechazo.

La decisión tiene un fundamento metodológico. La línea base midió cuatro escenarios y la medición final midió diez, de modo que las medias de ambos conjuntos no son comparables. La estadística inferencial exigiría una condición de comparabilidad que el diseño no ofrece. Por esta razón el capítulo sustituye toda prueba por comparación directa y verificable.

**Qué se hizo en su lugar**

- Comparación escenario por escenario, con el mismo criterio de cálculo en las dos vueltas.
- Contraste de cobertura, que separa lo que mejoró de lo que se conservó.
- Registro de cada corrección con su archivo de verificación.

**Decisión sobre el Wilcoxon.** La prueba de rangos con signo queda descartada porque la tutora pidió resultados y no comprobación. Su ausencia responde a esa indicación y no a una dificultad del dato.

---

## Indicación 3 · Enfocarse inicialmente en las mejoras del Prototipo II

La indicación pide explicar qué aporta el producto y qué problemas resuelve. El capítulo abre la presentación de resultados con el Prototipo II porque la metodología llega allí en estado de madurez completa.

**El valor del producto se sostiene en tres afirmaciones verificables**

- La metodología convierte una línea base de cuatro escenarios medidos en diez escenarios medidos.
- La cobertura de detección pasa de cuatro a diez técnicas y de tres a seis tácticas, sobre un inventario de diecisiete técnicas que no cambia.
- El ciclo completo de corrección, desde la línea base hasta la medición final, toma cuatro horas con veintiséis minutos.

**Qué problemas resuelve la metodología**

| Problema | Resolución de la metodología | Indicador |
| --- | --- | --- |
| Seis escenarios sin atribución de detección | Cada uno recibe fuente propia tras la corrección | Diez de diez con fuente |
| Tres componentes de registro | Se incorporan tres componentes más | Seis fuentes |
| Alertas que no llegaban al índice | Publicador propio que indexa por HTTP | Cadena de alertas completa |
| Motor de red que detectaba sin alertar | Reinicio programado de la posición de lectura | Alertas clasificadas |
| Orientación de red sin crear el segmento | Composición efectiva en tres segmentos | Dos de seis alcanzables desde el atacante |

**Entregable de apoyo.** El libro `2026-10-12_Resultados_Prototipo_II_SIN_v12.xlsx` desarrolla cada indicador en su propia hoja.

---

## Indicación 4 · Realizar un análisis del antes y el después del Prototipo II

La indicación pide comparar la situación inicial con la situación final. El tablero separa las dos columnas y declara siempre la causa de cada diferencia.

**Regla de comparación que sostiene el análisis**

La comparación válida es escenario por escenario. La media de las dos vueltas no se compara, porque la línea base midió cuatro escenarios y la medición final midió diez. El tablero declara esta regla de manera expresa para que el lector no interprete la caída de la media como una mejora de detección.

**Indicadores que cambian**

| Indicador | Línea base | Medición final | Diferencia |
| --- | --- | --- | --- |
| Escenarios con tiempo medido | 4 | 10 | +6 |
| Fuentes de registro | 3 | 6 | +3 |
| Técnicas con fuente de detección | 4 | 10 | +6 |
| Tácticas con fuente de detección | 3 | 6 | +3 |
| Percentil 95 de detección | 14,583 s | 9,266 s | −5,317 s |
| Lecciones cerradas | 7 | 14 | +7 |

**Indicadores que se conservan**

| Indicador | Línea base | Medición final | Lectura |
| --- | --- | --- | --- |
| Escenarios ejecutados | 10 | 10 | Constante |
| Técnicas del inventario | 17 | 17 | Constante |
| Archivos de evidencia | 91 | 91 | Constante |
| Calidad de la evidencia | 100 de 100 | 100 de 100 | Constante |

Los cuatro indicadores constantes son la prueba de que la diferencia procede de la corrección del instrumental. Un cambio en el volumen de evidencia o en el catálogo de amenazas habría producido una comparación sin control.

**Reducción por escenario comparable**

| Escenario | Técnica | Línea base | Medición final | Reducción |
| --- | --- | --- | --- | --- |
| S01 · Reconocimiento activo | T1595 | 16,851 s | 15,91 s | 5,6 % |
| S02 · Escaneo web | T1595.002 | 1,214 s | 1,095 s | 9,8 % |
| S05 · Suplantación de credenciales | T1110.004 | 1,734 s | 1,145 s | 34,0 % |
| S07 · Abuso de la interfaz | T1078 | 1,063 s | 0,264 s | 75,2 % |

Los cuatro escenarios conservan el mismo número de muestras en las dos vueltas, de modo que la reducción resulta atribuible a la corrección.

**Entregable de apoyo.** El libro `2026-10-12_Comparacion_Antes_Despues_v05.xlsx` desarrolla el antes y el después en nueve hojas.

---

## Indicación 5 · Cuantificar y explicar las mejoras por fase

La indicación pide datos, indicadores y explicación de por qué se produjo cada mejora. El tablero dedica la sección octava a la aportación por fase y la novena al registro de lecciones.

**Aportación de cada fase**

| Fase | Qué aporta | Indicador | Línea base | Final |
| --- | --- | --- | --- | --- |
| 1 · Diseño del señuelo | Portal tributario con acceso en dos pasos y un escenario por técnica | Escenarios ejecutados | 10 de 10 | 10 de 10 |
| 2 · Despliegue aislado | Tres segmentos de red y verificación ejecutada desde el contenedor atacante | Objetivos alcanzables desde el atacante | 2 de 6 | 2 de 6 |
| 3 · Captura y custodia | Atribución recognize las tres variantes de clave e incorpora archivo señuelo y sensor de red | Escenarios con medición | 4 de 10 | 10 de 10 |
| 4 · Correlación | Alerta clasificada con técnica y severidad encadenada a la gestión de incidentes | Alertas clasificadas | 10 de 10 | 10 de 10 |
| 5 · Medición y mejora | Catorce lecciones con causa raíz, cambio aplicado y cierre verificado | Lecciones cerradas | 7 | 14 |

La fase 3 concentra la mejora cuantificable porque repara el instrumental de atribución. La fase 5 la sostiene, porque produce las lecciones que dieron origen a esas reparaciones.

**Distribución de las catorce lecciones**

| Fase | Lecciones | Identificadores |
| --- | --- | --- |
| 2 · Despliegue | 5 | L3, L7, L10, L12, L13 |
| 3 · Captura | 5 | L1, L2, L4, L8, L14 |
| 4 · Correlación | 1 | L9 |
| 5 · Medición | 3 | L5, L6, L11 |

**Cadena causal que explica el resultado.** La fase 5 produjo catorce lecciones, la fase 3 reparó el instrumental de atribución y la medición posterior confirmó el efecto sobre diez de diez escenarios. El capítulo expone esa cadena en orden, porque explica por qué el resultado es atribuible a la metodología y no al azar de una segunda ejecución.

**Entregable de apoyo.** El libro `2026-10-12_Matriz_Evidencia_Laboratorio_por_Item_v06.xlsx` registra cuarenta y dos ítems, de los cuales veintinueve tienen evidencia medida, seis están declarados y siete tienen su motivo registrado.

---

## Indicación 6 · Organizar los resultados por prototipo y por fases

La indicación pide separar el primer y el segundo prototipo, con las fases dentro de cada uno. Los apartados 4.4.2 y 4.4.3 corresponden al Prototipo I, mientras que los apartados 4.4.3 a 4.4.7 corresponden al Prototipo II.

Los instrumentos de esta carpeta se dedican exclusivamente al Prototipo II, porque es el laboratorio que la tutora señaló como foco del capítulo. Los datos del primer prototipo permanecen en el apartado 4.3.5 del marco práctico y en la figura que lo acompaña.

---

## Inventario de entregables

| Archivo | Contenido | Indicación que atiende |
| --- | --- | --- |
| `dashboard-resultados_v03.html` | Tablero navegable de catorce secciones, con el antes, las seis brechas y el resultado institucional | 1 y 4 |
| `dashboard-resultados_v03.docx` | Tablero en Word, con dieciséis figuras y veintiséis tablas | 1, 3, 4 y 5 |
| `dashboard-resultados_v03.pdf` | Versión del tablero en A3 apaisado, doce páginas | 1, 3 y 4 |
| `dashboard-resultados_v02.html` | Añade el antes institucional sobre la v01 | 1 y 4 |
| `dashboard-resultados_v02.docx` | Segunda versión en Word | 1, 3, 4 y 5 |
| `dashboard-resultados_v02.pdf` | Segunda versión en PDF | 1, 3 y 4 |
| `dashboard-resultados_v01.html` | Primera versión, solo con el antes y después del laboratorio | 1 |
| `dashboard-resultados_v01.docx` | Primera versión en Word | 1 |
| `dashboard-resultados_v01.pdf` | Primera versión en PDF | 1 |
| `evidencia-visual/tablero-alertas-vuelta-1.png` | Captura del tablero en la línea base | 1 y 4 |
| `evidencia-visual/tablero-alertas-vuelta-2.png` | Captura del tablero en la medición final | 1 y 4 |
| `evidencia-institucional/comunicacion-sin-postest-99-06.md` | Comunicación del SIN con su análisis y las verificaciones | 4 |
| `2026-10-12_Resultados_Prototipo_II_SIN_v12.xlsx` | Diez hojas con los indicadores del laboratorio | 1, 3 y 5 |
| `2026-10-12_Comparacion_Antes_Despues_v05.xlsx` | Nueve hojas con el antes y el después | 4 |
| `2026-10-12_Matriz_Evidencia_Laboratorio_por_Item_v06.xlsx` | Cuarenta y dos ítems con su evidencia | 5 |
| `2026-10-12_Matriz_Evidencia_Laboratorio_por_Item_v01.docx` | La misma matriz en formato de documento | 5 |
| `2026-10-14_Matriz_Pretest_Autentica_30x42_v01.xlsx` | Matriz real de treinta respondentes verificada contra el apartado 4.1 | 4 |
| `2026-10-14_Matriz_Captura_Postest_30x42_v01.xlsx` | Libro de captura vacío con las fórmulas listas | 4 |
| `00_GUIA_INDICACIONES_TUTORA.md` | Este documento de respaldo | Todas |

---

## Corregcciones de dato aplicadas antes de la entrega

La revisión del capítulo detectó cifras que no correspondían con los archivos de evidencia. Cada corrección se aplicó sobre el archivo de origen y nunca sobre una estimación.

| Cifra | Valor anterior | Valor corregido | Archivo de origen |
| --- | --- | --- | --- |
| Cobertura de ISO 27035 | 2 de 5 | 1 de 5, equivalente a 20 % | `iso27035_compliance.json` |
| Técnicas con detección | 4 de 10 | 10 de 10 | `kpi_report.json` de la vuelta 2 |
| Tácticas con detección | 3 de 6 | 6 de 6 | `kpi_report.json` de la vuelta 2 |
| Fuentes de registro | 3 y 4 según la hoja | 6 | `kpi_report.json` de la vuelta 2 |
| Reducciones de la tabla 9 | 5,6 / 9,9 / 33,5 / 75,5 % | 5,6 / 9,8 / 34,0 / 75,2 % | Valores de origen con tres decimales |

El inventario de técnicas no cambia. Lo que cambia es la atribución de detección, de modo que ambos hechos se presentan separados en el tablero.

---

## Historial de versiones del tablero

El tablero se entrega en dos versiones para conservar la trazabilidad de cada revisión.

| Versión | Alcance | Archivos |
| --- | --- | --- |
| v01 | Antes y después de las dos iteraciones del laboratorio | `dashboard-resultados_v01.html`, `_v01.pdf` y `_v01.docx` |
| v02 | Añade el diagnóstico institucional como punto de partida y la trazabilidad de las seis brechas | `dashboard-resultados_v02.html`, `_v02.pdf` y `_v02.docx` |
| v03 | Añade el resultado institucional comunicado por el SIN y la tabla que separa las cuatro fuentes de resultado | `dashboard-resultados_v03.html`, `_v03.pdf` y `_v03.docx` |

**Qué aporta la v05 sobre la v04**

1. El 99,09 % del libro oficial en lugar del 99,06 % de la comunicación escrita.
2. El apartado institucional reescrito con la operación que produce la cifra.
3. Todo el material reunido en la carpeta `resultados-cap4/v05/`.

**Qué aportaba la v03 sobre la v02**

1. Un apartado final con el 99,09 % comunicado por el Servicio de Impuestos Nacionales.
2. El gráfico que sitúa esa cifra y la madurez diagnosticada sobre la escala de cortes de la ficha técnica.
3. La tabla que separa las cuatro fuentes de resultado del capítulo y declara que no comparten escala.
4. La corrección de dos textos que estaban en inglés y en francés en la v02.
5. La sustitución de la nota que anunciaba una reaplicación del instrumento, porque esa reaplicación no se realizó.

**Criterio de enlace entre las dos columnas.** El antes y el después se midieron con instrumentos distintos. La columna del antes procede del autoinforme de treinta respondentes, que mide madurez declarada. La columna del después procede de la instrumentalización del laboratorio, que mide ejecución verificada sobre archivos de evidencia. El tablero no superpone ambos conjuntos en un mismo eje porque ese contraste produciría una lectura engañosa. Lo que los enlaza es la trazabilidad, de modo que cada brecha tiene una fase que la responde y un indicador de archivo que la confirma.

**Sobre la tercera fuente de resultado.** El 99,09 % no se superpone con las anteriores porque responde a otra pregunta y la mide otra fuente. El tablero lo presenta en su propio eje, con la escala de cortes de la ficha técnica y la distancia de 46,39 puntos porcentuales respecto del diagnóstico.

---

## Origen de los datos

- `evidencias/v2.0-it1/07-metricas/kpi_report.json` contiene la línea base.
- `evidencias/v2.1-it2/07-metricas/kpi_report.json` contiene la medición final.
- `evidencias/v2.0-it1/07-metricas/mitre_coverage.json` contiene el inventario.
- `evidencias/v2.0-it1/07-metricas/iso27035_compliance.json` contiene el cumplimiento normativo.
- `evidencias/lecciones-aprendidas.md` contiene el registro de las catorce lecciones.
- `evidencias/INDICE.md` contiene el inventario completo de la evidencia.

Ningún valor del tablero fue estimado. Cada cifra declara el archivo que la produce y el capítulo de resultados no incorpora comprobación de hipótesis.