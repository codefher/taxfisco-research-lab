# Prototipo 1 — aplicación sobre la entidad homologada

Esta carpeta aloja el tablero de resultados del primer prototipo de la
metodología Honeypot y la guía con que se construyó. El tablero está terminado y
verificado en navegador.

| Archivo | Contenido |
| --- | --- |
| `dashboard-resultados_prototipo_1.html` | Tablero de diez secciones, con cuatro gráficos y dos capturas. |
| `GUIA-ARMADO-TABLERO.md` | Datos verificados, mapa de secciones y criterios de cierre. |
| `evidencia-visual/` | Los dos paneles del tablero de alertas del laboratorio. |

## Dónde se reportan estos resultados

La aplicación sobre la entidad homologada del rubro de servicios fiscales
digitales se describe en el capítulo IV de la tesis, en los apartados 4.3.5
(implementación por fases) y 4.4.2 (indicadores del primer prototipo).

## La evidencia sí está versionada

El repositorio la contiene en la rama `prototipo-1-entidad-homologada`, dentro de
la carpeta `evidencias/`, que el archivo `.gitignore` reserva para ese
laboratorio. Allí están el reporte de indicadores, el de cobertura de técnicas,
el de correspondencia normativa, el manifiesto y las capturas de eventos.

El índice de evidencias que se lee desde la rama `prototipo-2-sin` se titula
«Prototipo II (laboratorio SIN)» y solo describe el segundo laboratorio. De ahí
que pareciera que el primero carecía de respaldo.

## Qué queda abierto

Dos asuntos siguen pendientes y ninguno se resuelve dentro del tablero.

| Punto abierto | Estado |
| --- | --- |
| Fases de ISO/IEC 27035 | El capítulo IV declara cinco de cinco y el reporte de indicadores declara una de cinco. El tablero cita el archivo de cumplimiento normativo, que documenta la evidencia de cada fase por separado. |
| Registro de lecciones | El capítulo IV atribuye tres lecciones y no hay registro versionado de este laboratorio. El tablero lo omite por esa razón. |

La discrepancia de ISO/IEC 27035 pide una nota de definición en el capítulo IV,
porque los dos archivos miden cosas distintas y el lector los confundirá.

## Cómo continuar

La guía de armado está en
[`GUIA-ARMADO-TABLERO.md`](GUIA-ARMADO-TABLERO.md). Contiene los datos verificados
de los tres reportes, el mapa de secciones que se trasladan del segundo tablero
y las tres discrepancias que hay que cerrar antes de construir.

El tablero del segundo laboratorio, que sirve de plantilla, está en
[`../prototipo-2/dashboard-resultados_prototipo_2.html`](../prototipo-2/dashboard-resultados_prototipo_2.html).