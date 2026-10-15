# Prototipo 1 — aplicación sobre la entidad homologada

Esta carpeta queda creada para alojar el tablero de resultados del primer
prototipo de la metodología Honeypot. Todavía no contiene tablero, y la razón
es de trazabilidad, no de alcance.

## Dónde se reportan estos resultados

La aplicación sobre la entidad homologada del rubro de servicios fiscales
digitales se describe en el capítulo IV de la tesis, en dos apartados.

| Apartado | Contenido |
| --- | --- |
| 4.3.5 | Implementación del Prototipo 1, entidad homologada, con sus cinco fases |
| 4.4.2 | Indicadores del primer prototipo y su archivo de origen |

Los indicadores que ambos apartados recogen son nueve escenarios ejecutados,
treinta y nueve milésimas de segundo de tiempo medio de detección, diecisiete
técnicas en el inventario, diez técnicas detectadas, seis tácticas cubiertas y
tres lecciones aprendidas.

## Por qué no hay tablero todavía

El índice de evidencias del repositorio se titula **«Prototipo II (laboratorio
SIN)»**. Todo su contenido corresponde a las dos iteraciones del segundo
laboratorio, con las carpetas `evidencias/v2.0-it1` y `evidencias/v2.1-it2`.

Los nombres de red del primer laboratorio, `taxfisco-dmz`, `taxfisco-honeypot` y
`taxfisco-soc`, no aparecen en ningún archivo del repositorio. Solamente se
mencionan en la tabla comparativa de prototipos del capítulo.

En consecuencia, los reportes de indicadores del primer prototipo **no están
versionados** aquí, y el capítulo IV declara su fuente como «reportes de la
implementación del primer prototipo, apartado 4.3.5».

## Qué haría falta para construir este tablero

1. Localizar los reportes de indicadores, de cobertura y de métricas de la
   aplicación sobre la entidad homologada.
2. Versionarlos en el repositorio dentro de una carpeta de evidencia propia,
   con su manifiesto y su índice.
3. Construir el tablero con el mismo diseño de
   `../prototipo-2/dashboard-resultados_prototipo_2.html`.

El tablero no puede construirse antes de ese paso, porque el capítulo IV
establece que toda cifra presentada procede de un archivo de evidencia del
repositorio y declara su origen. Incorporar cifras sin respaldo rompería esa
regla dentro del propio tablero.

## Referencia

El tablero del segundo laboratorio, que sí cuenta con evidencia completa, está
en [`../prototipo-2/dashboard-resultados_prototipo_2.html`](../prototipo-2/dashboard-resultados_prototipo_2.html).
La comparación entre la madurez declarada en el diagnóstico y el resultado
verificado en el laboratorio se encuentra en el capítulo IV, en los apartados
4.4.1 y 4.4.5, y en el tablero completo que acompaña a los resultados del
diagnóstico institucional.