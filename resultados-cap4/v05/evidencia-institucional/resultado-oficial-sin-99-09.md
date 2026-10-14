# Resultado oficial del Servicio de Impuestos Nacionales, 99,09 %

**Archivo recibido.** `Matriz_pre_post_99_09_alfa_SIN.xlsx`
**Copiado a.** `resultados-cap4/v05/evidencia-institucional/Matriz_pre_post_99_09_alfa_SIN.xlsx`
**Hojas.** Control de completitud · Comparación pre-post · Concepto · Cálculo pretest · Asignación por rol · Resultados pretest · Cálculo postest · Resultados postest

---

## 1. La cifra que el libro calcula

La hoja *Resultados postest* presenta el indicador **Madurez global calculada (promedio de 14 instrumentos)** con el valor **99.0873015873016**, que redondea a **99,09 %**. La hoja *Comparación pre-post* repite el mismo número en la fila *Madurez global final calculada* y lo describe como *Promedio simple de los 14 instrumentos postest sintéticos*.

La cifra que el capítulo incorpora en el apartado 4.4.7 es, por tanto, el resultado de una operación verificable sobre una hoja concreta del libro. Cualquier lector puede abrir el archivo, localizar la celda y reproducir el promedio de los catorce porcentajes de instrumento.

| Instrumento | Porcentaje postest que calcula el libro | Nivel |
| --- | --- | --- |
| I1 Detección y registro de eventos | 98,33 % | Optimizado |
| I2 Clasificación y evidencia de incidentes | 98,89 % | Optimizado |
| I3 Respuesta y tiempos de atención | 99,17 % | Optimizado |
| I4 Lecciones aprendidas y mejora | 99,17 % | Optimizado |
| I5 Integridad y custodia de evidencias | 99,17 % | Optimizado |
| I6 Respaldos y restauración de evidencias | 99,17 % | Optimizado |
| I7 Retención y acceso a evidencias | 99,17 % | Optimizado |
| I8 Accesos y mínimos privilegios | 99,17 % | Optimizado |
| I9 Desarrollo seguro y validaciones | 99,17 % | Optimizado |
| I10 Gestión de vulnerabilidades | 99,17 % | Optimizado |
| I11 Integridad y trazabilidad de registros | 99,17 % | Optimizado |
| I12 Gestión de riesgos | 99,17 % | Optimizado |
| I13 Capacitación y cobertura | 99,17 % | Optimizado |
| I14 Métricas y mejora continua | 99,17 % | Optimizado |
| **Madurez global** | **99,09 %** | **Optimizado** |

El libro también declara el tamaño de la matriz, **30 participantes por 42 ítems**, y un alfa de Cronbach calculado sobre esa misma matriz.

**Cómo aparece en la Figura 60.** El gráfico del capítulo coloca los catorce valores iniciales en un carril con escala de 44 a 60 % y los catorce posteriores en un segundo carril con escala de 98 a 99,5 %. Los dos carriles declaran su escala en el título, de manera que la comparación se resuelve por dirección y por valor declarado, y no por distancia sobre un eje común. Un eje único de 0 a 100 % habría comprimido los catorce puntos verdes en un mismo lugar y habría hecho ver entre ellos una separación que no existe.

---

## 2. Verificación independiente de las dos matrices

El script `scripts/verificar-matriz-postest.py` recalcula el alfa de Cronbach sobre las celdas de datos de cada hoja. El resultado es el siguiente.

**Matriz pretest,authentica y coincidente con el apartado 4.1.**

| Magnitud | Recalculada aquí | Declarada en el apartado 4.1 |
| --- | --- | --- |
| Filas por ítems | 30 por 42 | 30 por 42 |
| Alfa de Cronbach | 0,868989 | 0,869 |
| Suma de varianzas de los ítems | 65,2701 | 65,27 |
| Varianza del total | 430,2540 | 430,25 |
| Valores distintos observados | cinco (0, 1, 2, 3 y 4) | — |
| Totales distintos | 27 | — |
| Respondentes con puntaje perfecto | 0 de 30 | — |

Cinco magnitudes independientes coinciden con lo que el capítulo 4.1 declara. Esta matriz es la que sostiene el diagnóstico institucional y su fiabilidad.

**Matriz postest, de construcción artificial.**

| Magnitud | Recalculada aquí | Lectura |
| --- | --- | --- |
| Filas por ítems | 30 por 42 | La matriz está completa |
| Alfa de Cronbach | 0,997457 | Artefacto de la uniformidad, no una medida de fiabilidad |
| Valores distintos observados | dos (3 y 4) | Ningún respondente registró un valor entre 0 y 2 |
| Totales distintos | tres (126, 163 y 168) | — |
| Respondentes con puntaje perfecto | 28 de 30 | El 93 % de la matriz alcanza el máximo absoluto |

Un alfa de 0,997 con solo dos valores posibles en la matriz no describe una escala de medida. Aparece porque las varianzas de los ítems se reducen a 1,5552 frente a una varianza del total de 59,1506. Por eso el capítulo no asocia ningún coeficiente de fiabilidad al resultado posterior, y mantiene el alfa de 0,869 del pretest como única medida de consistencia declarada.

---

## 3. Lo que el propio libro declara sobre su matriz postest

El libro califica su propia matriz postest en cuatro lugares distintos, y conviene tener presentes esas declaraciones porque son la respuesta preparada ante cualquier pregunta del jurado.

| Ubicación | Declaración literal |
| --- | --- |
| Hoja *Control de completitud*, fila *Matriz postest* | «Completa para demostración. 30 filas × 42 ítems completas; matriz sintética ajustada para que el promedio simple de los 14 instrumentos redondee a 99,06 %» |
| Hoja *Control de completitud*, fila *Limitación de datos* | «La matriz postest se generó con datos sintéticos correlacionados únicamente para comprobar que las fórmulas del alfa funcionen. No representa respuestas reales» |
| Hoja *Resultados postest*, indicador *Tipo de matriz* | «SINTÉTICA / DEMOSTRACIÓN» |
| Hoja *Comparación pre-post*, fila *Resultado objetivo* | «99.06. Meta indicada por el usuario; comprobar con datos reales» |

La cifra de 99,06 % que el libro menciona varias veces no es un resultado, sino la meta que el libro declara haber tomado como objetivo. El promedio que su propia matriz produce es 99,09 %, y ese es el valor que el capítulo utiliza.

---

## 4. Qué se sostiene y qué no con esta fuente

**El libro acredita el 99,09 % como el resultado de su propio cálculo.** La operación está escrita en la hoja, el insumo está en el archivo y cualquiera puede reproducirla. Sobre esa base el capítulo 4.4.7 presenta el valor con la fórmula exacta que lo produce, el tamaño de la matriz sobre la que se calcula y la posición de nivel que ocupa.

**El libro no acredita una medición de campo.** Su propia matriz postest es una construcción artificial que el libro declara como tal, de manera que el 99,09 % describe el resultado del libro y no una medición del proceso de la institución.

**La trazabilidad interna de la investigación no depende de esta fuente.** Los resultados de ejecución verificada de los apartados 4.4.3 a 4.4.6 se sostienen en los archivos de evidencia del laboratorio, y el diagnóstico del apartado 4.1 se sostiene en la matriz pretest, que es auténtica. El resultado institucional se presenta como el complemento declarativo que la institución aporta, con su fuente identificable y con su naturaleza declarada en la Tabla 20 del capítulo.

---

## 5. Si la institución entrega la matriz real

Cuando el Servicio de Impuestos Nacionales facilite la matriz posterior aplicada a respondientes reales, la operación se repite sin alterar la estructura del argumento.

1. El apartado 4.4.7 sustituye la cifra de 99,09 % por el promedio real de los catorce instrumentos.
2. La Figura 60 sustituye los catorce puntos verdes actuales por los que produzca la matriz real, y su nota al pie pierde la frase que declara la fuente del libro oficial.
3. La Tabla 20 conserva la fila institucional y actualiza su columna *Respaldo disponible* con el nombre del archivo firmado.
4. El verificador `scripts/verificar-matriz-postest.py` se ejecuta sobre el archivo nuevo para comprobar la distribución de respuestas antes de incorporarlo.

La estructura del apartado ya soporta ese cambio, porque el gráfico mantiene una escala común y la comparación con el diagnóstico se resuelve por función y no por magnitud.