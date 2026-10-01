# Índice propuesto — Apartado 4.4 Validación de la metodología

> Documento de planificación para el nuevo apartado 4.4 del Capítulo IV.
> Materializa el **OE4** (*"Validar la eficacia de la metodología propuesta
> mediante la evaluación de su impacto en la reducción del tiempo promedio de
> detección de incidentes"*) y ejecuta el diseño **preprueba-posprueba** que la
> tesis ya declaró en 3.2 y que la Fase 5 (4.2.7) compromete con una
> **prueba de hipótesis pareada**.
> Instrumento: **Prototipo II (contexto SIN)** con sus dos iteraciones.
> Regla de evidencia: ningún valor se redacta sin su fuente (`kpi_report.json`,
> capturas en `evidencias/`, commits `[P2]`).

## Vínculos de trazabilidad del apartado

| Elemento de la tesis | Ancla | Dónde se demuestra en 4.4 |
|---|---|---|
| OE4 (1.3.2, ítem 4) | Reducción del tiempo promedio de detección | 4.4.7, 4.4.8 |
| Hipótesis (1.5) | Mejora de la gestión de incidentes | 4.4.8 |
| Diseño pre-experimental pre/post (3.2) | Dos mediciones sobre el mismo grupo | 4.4.2 |
| Muestreo por conveniencia, fase validación (3.3.1) | Eventos de campaña en laboratorio | 4.4.2 |
| Fase 5, actividad 2 (4.2.7) | Prueba de hipótesis pareada | 4.4.7 |
| Índices IIAM e IMGI (4.2.2.1, Tabla 1) | Cuantificación del impacto | 4.4.8 |
| Metas de la Tabla 2 (1.6) | MTTD −30 %, FP ≤ 5 %, evidencia ≥ 90 % | 4.4.8 |

## 4.4.1 Propósito, alcance y línea base de la validación

- Propósito: verificar con evidencia cuantitativa que la metodología honeypot
  reduce el tiempo de detección y mejora la gestión de incidentes en el
  contexto de un servicio fiscal nacional (SIN).
- Alcance: validación en entorno controlado (laboratorio), no en producción;
  los resultados se declaran transferibles por diseño (principio P2).
- Línea base: la medición de la iteración 1 (v2.0-it1) constituye la
  **preprueba**; la iteración 2 (v2.1-it2) constituye la **posprueba**.
- Diferencia con 4.3: el 4.3 implementa y verifica componentes (¿existe y
  opera?); el 4.4 mide el efecto (¿mejora?). Redacción sin repetir el 4.3.

## 4.4.2 Diseño de comparación y criterios de pareamiento

- Declaración del esquema preprueba-posprueba sobre un mismo grupo (cita 3.2).
- **Unidad de comparación**: los escenarios de la campaña S01–S10, idénticos
  en ambas iteraciones (mismos ataques, mismos objetivos, mismos criterios
  de medición). El pareamiento es por escenario, no por evento suelto.
- Muestra: eventos generados por la campaña en el entorno controlado
  (muestreo por conveniencia ya justificado en 3.3.1).
- Variables medidas por escenario: MTTD, detección (sí/no), técnica ATT&CK
  detectada, falsos positivos. Invariantes controladas: stack, red, hardware,
  definición de instante de ataque y de instante de detección (del método de
  medición ya documentado en 4.3.9, Figura 35).
- Tabla: *Definición de las condiciones invariantes entre iteraciones*.

## 4.4.3 Contexto de validación: adaptación del prototipo al SIN

- Presentación breve del Prototipo II (rama `prototipo-2-sin`, tag v2.0-it1):
  rebranding del señuelo al portal tributario nacional, aislamiento de red
  verificado, artefactos Docker con prefijo `sin-*` sin colisión con el
  Prototipo I (que permanece congelado en `prototipo-1-entidad-homologada`).
- Trazabilidad de cambios por commits `[P2]` (sin rehacer el 4.3).
- Figura: portal SIN (una sola captura representativa, remitiendo al 4.3 para
  el detalle).
- Tabla: *Diferencias y equivalencias entre el Prototipo I y el entorno de
  validación* (qué cambió: contexto SIN; qué se mantuvo: arquitectura de 25
  servicios, instrumentación, método de medición).

## 4.4.4 Preprueba: ejecución y medición de la iteración 1 (v2.0-it1)

- Ejecución de la campaña S01–S10 sobre el laboratorio en contexto SIN.
- Resultados de la línea base con fuente `kpi_report.json` (valores reales
  ya medidos: S01 16.40 s, S02 7.88 s, S05 1.05 s, S07 1.03 s; escenarios sin
  detección en el decoy declarados como tales).
- Cobertura ATT&CK de la iteración 1 (técnicas implementadas vs. detectadas).
- Figuras: tablero de indicadores y reporte consolidado de la iteración 1
  (de `evidencias/v2.0-it1/`).
- Tabla: *Medición de la línea base por escenario (iteración 1)*.

## 4.4.5 Análisis de resultados y lecciones aprendidas de la iteración 1

- Análisis de la línea base: distribución de MTTD, escenarios sin detección
  en el decoy, brechas de cobertura ATT&CK.
- Registro formal de lecciones L1–Ln (formato del registro de lecciones
  aprendidas del laboratorio: hallazgo, causa raíz, evidencia, commit).
- Cada lección se vincula al bucle F5→F1 del diseño (cita 4.2.7).
- Criterio de aceptación de mejoras: toda mejora de la iteración 2 debe citar
  su lección de origen.
- Tabla: *Registro de lecciones aprendidas de la iteración 1*.

## 4.4.6 Aplicación de mejoras y ejecución de la iteración 2 (v2.1-it2)

- Selección de mejoras derivadas de las lecciones (priorización con criterio:
  impacto en MTTD y en cobertura).
- Aplicación y verificación de cada mejora, trazada a su lección y commiteada
  con prefijo `[P2] … - leccion L<n>`; tag `v2.1-it2`.
- Re-ejecución de la campaña S01–S10 bajo las condiciones invariantes de
  4.4.2.
- Figuras: evidencias de la iteración 2 (`evidencias/v2.1-it2/`).
- Tabla: *Mejoras aplicadas en la iteración 2 con su lección de origen*.

## 4.4.7 Comparación de iteraciones y prueba de hipótesis pareada

- Tabla comparativa escenario por escenario: MTTD it1 vs. it2, detección,
  técnica ATT&CK, FP (alimentar con `evidencias/comparacion-iteraciones.md`).
- **Prueba de Wilcoxon de rangos con signo** sobre las diferencias pareadas
  por escenario (it1 − it2), con α = 0.05, sobre los escenarios con detección
  en ambas iteraciones; justificación del uso de una prueba no paramétrica
  (muestra pequeña, no normalidad garantizada).
- Reporte: estadístico W, valor p, conclusión de significancia, tamaño del
  efecto (r de Rosenthal) si el efecto lo amerita.
- Criterio de lectura: significancia + reducción porcentual media del MTTD.
- Figura: diagrama de diferencias por escenario (barras o de cajas).
- Tabla: *Resultado de la prueba pareada por indicador*.

## 4.4.8 Evaluación de la hipótesis y de las metas

- Contraste de la hipótesis (1.5) con el resultado de 4.4.7: decisión
  (se acepta / no se acepta) con sustento estadístico.
- Cálculo de los índices comprometidos en 4.2.2.1: IIAM e IMGI con sus
  fórmulas y valores medidos.
- Confrontación con las metas de la Tabla 2 (1.6): MTTD −30 %, FP ≤ 5 %,
  evidencia completa ≥ 90 %, lecciones cerradas ≥ 80 %.
- Tabla: *Cumplimiento de metas de la variable dependiente*.

## 4.4.9 Síntesis de la validación, limitaciones y transferibilidad

- Síntesis: qué se validó, con qué evidencia y qué decisión estadística.
- Limitaciones: validez interna del diseño pre-experimental (sin grupo de
  control, ya asumida en 3.2), tamaño de muestra por conveniencia, entorno
  simulado (transferibilidad, no generalización estadística).
- Cierre del OE4 y puente al Capítulo V (conclusiones por objetivo).

## Evidencia pendiente de producir (checklist)

| # | Evidencia | Estado |
|---|---|---|
| 1 | Ejecución completa it1 con campaña S01–S10 en contexto SIN | Pendiente (lab bajo) |
| 2 | kpi_report.json de it1 con MTTD por escenario | Pendiente |
| 3 | Cobertura ATT&CK de it1 | Pendiente |
| 4 | Registro de lecciones L1–Ln de it1 | Pendiente (plantilla lista) |
| 5 | Mejoras aplicadas con tag v2.1-it2 | Pendiente |
| 6 | kpi_report.json de it2 | Pendiente |
| 7 | Tabla comparativa y cálculo Wilcoxon | Pendiente (plantilla lista) |

## Detalles menores detectados en v10 (a corregir al redactar)

- El encabezado «2.8 Síntesis del diseño» debería numerarse **4.2.8**.
- El 4.3.9 remite a «la prueba controlada de extremo a extremo» como
  continuación, pero en el documento el 4.3 salta directo al Capítulo V;
  decidir si la prueba E2E vive en 4.3.10 o si su resultado alimenta 4.4.4.
- En 5.1 el molde de conclusiones lista tres objetivos específicos, pero la
  tesis tiene cuatro (OE4 sin conclusión asignada).
