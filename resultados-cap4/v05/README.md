# Carpeta v05 · Resultado institucional del libro oficial

Esta carpeta reúne la versión vigente del tablero de resultados del capítulo IV, con el **99,09 %** que calcula el libro oficial de resultados del Servicio de Impuestos Nacionales. Las versiones v01 a v04 permanecen en `resultados-cap4/` sin modificación, para que pueda compararse la evolución del material.

## Qué cambió respecto de la v04

| Elemento | v04 | v05 |
| --- | --- | --- |
| Cifra institucional | 99,06 % | **99,09 %** |
| Fuente declarada | Comunicación escrita del SIN | **Libro oficial de resultados, hoja *Resultados postest*** |
| Operación que produce la cifra | No se declaraba | Promedio simple de los 14 instrumentos sobre la matriz de 30 participantes, igual a 99,0873015873016 % |
| Distancia respecto del diagnóstico | 46,36 puntos porcentuales | 46,39 puntos porcentuales |
| Apartado 4.4.7 | Resultado agregado | **Resultado global del libro oficial de la institución** |
| Gráfico de los 14 instrumentos | Una línea verde de 99,06 % | **Los catorce porcentajes posteriores, en dos carriles con escala propia** |
| Origen de cada cifra | No se declaraba | **Tabla de ocho indicadores con su numerador, su denominador y su archivo de origen** |
| Lecciones aprendidas | Catorce, todas cerradas | **Catorce registradas y resueltas, con causa raíz, corrección o mitigación y estado** |
| Aportación de cada fase | Declaraba el entregable | **Redactada como contribución concreta al resultado** |
| Ubicación | `resultados-cap4/` | `resultados-cap4/v05/` |

## Contenido

| Archivo | Qué es |
| --- | --- |
| `dashboard-resultados_v05.html` | Tablero interactivo, catorce secciones y trece gráficos vectoriales |
| `dashboard-resultados_v05.docx` | Tablero en Word con texto y tablas editables, diecisiete figuras y treinta tablas |
| `dashboard-resultados_v05_desde-html.docx` | El mismo tablero tal como se ve en el navegador, una sección por página, con los trece gráficos y las quince tablas tal como los compone el HTML |
| `graficos/instrumentos-antes-despues.html` | Fuente del gráfico de los catorce instrumentos, corregible en el navegador |
| `graficos/instrumentos-antes-despues.png` | Ese mismo gráfico a 2400 px, que es la Figura 60 del capítulo |
| `evidencia-institucional/Matriz_pre_post_99_09_alfa_SIN.xlsx` | Libro oficial recibido, archivado sin modificar |
| `evidencia-institucional/resultado-oficial-sin-99-09.md` | Qué acredita el libro, qué recalcula el verificador y qué declara el propio archivo |
| `evidencia-visual/` | Capturas de los tableros de alertas del SIEM en las dos vueltas |
| `00_GUIA_INDICACIONES_TUTORA.md` | Guía de indicaciones con el apartado 4.4 actualizado |

## Dónde vive cada cosa

- **El capítulo.** `tesis/Redaccion_Marco_Practico_v11_v1.5.md`, apartado 4.4.7 y Figura 60, con el texto y la imagen ya corregidos.
- **El verificador.** `scripts/verificar-matriz-postest.py`, que recalcula el alfa de Cronbach de cualquier matriz de 30 por 42 que la institución entregue en el futuro.
- **La reproducción.** Los generadores están en `.render/`: `build-v05.py`, `build-v05-aclaraciones.py` y `build-docx-v05.py`.

## Si la institución entrega la matriz real

El apartado 4.4.7 y la Figura 60 ya están construidos para absorber ese cambio sin reescribir el argumento. La hoja *Cálculo postest* del libro actual contiene la matriz completa, de modo que basta con sustituir el archivo, volver a ejecutar el verificador y regenerar el gráfico.