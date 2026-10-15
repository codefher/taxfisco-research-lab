# Prototipo 1 — aplicación sobre la entidad homologada

Esta carpeta aloja la guía de armado del tablero de resultados del primer
prototipo de la metodología Honeypot. El tablero todavía no existe, y la razón
es de trazabilidad, no de alcance.

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

## Qué bloquea la construcción

Tres asuntos quedan abiertos y ninguno se resuelve dentro del tablero.

| Punto abierto | Estado |
| --- | --- |
| Fases de ISO/IEC 27035 | El capítulo IV declara cinco de cinco y el reporte declara una de cinco. |
| Número de escenarios | El capítulo IV declara nueve ejecutados y el reporte declara diez con nueve medidos. |
| Registro de lecciones | El capítulo IV atribuye tres lecciones y no hay registro versionado de este laboratorio. |

La primera discrepancia es la más delicada, porque publicar una cifra de
ISO/IEC 27035 obligaría a escoger entre el capítulo y la evidencia.

## Cómo continuar

La guía de armado está en
[`GUIA-ARMADO-TABLERO.md`](GUIA-ARMADO-TABLERO.md). Contiene los datos verificados
de los tres reportes, el mapa de secciones que se trasladan del segundo tablero
y las tres discrepancias que hay que cerrar antes de construir.

El tablero del segundo laboratorio, que sirve de plantilla, está en
[`../prototipo-2/dashboard-resultados_prototipo_2.html`](../prototipo-2/dashboard-resultados_prototipo_2.html).