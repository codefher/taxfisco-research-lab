# Tabla de comparación entre iteraciones — Prototipo II (SIN)

> Soporta la redacción de los apartados 4.4.5 (análisis de resultados) y
> 4.4.7 (conclusiones por iteración) de la tesis.
> Regla de llenado: cada valor debe citar su fuente (captura, log o
> `kpi_report.json` generado por `kpi_calculator.py`). Sin fuente, sin valor.
>
> **Estado actual: reset a cero (2026-10-03).** Se vaciaron todos los valores
> de la iteración 1 porque estaban anclados a evidencia que se eliminó durante
> el reset del laboratorio (34 PNG renderizadas sin verificar, `kpi_report.json`
> de la sesión del 30 Sep generado en un directorio de trabajo distinto, y
> volúmenes Docker re-inicializados). Bajo la regla "sin fuente, sin valor",
> los valores se regenerarán durante la re-captura limpia de la iteración 1.

## Convención

| Iteración | Tag | Alcance |
|---|---|---|
| it1 | `v2.0-it1` | Primera ejecución completa de la campaña S01–S10 y análisis |
| it2 | `v2.1-it2` | Re-ejecución tras aplicar las mejoras derivadas de las lecciones L1–Ln |

## Comparación cuantitativa

| Métrica | it1 (v2.0-it1) | it2 (v2.1-it2) | Fuente |
|---|---|---|---|
| Escenarios ejecutados | pendiente | pendiente | (se llena tras la re-captura) |
| Servicios accesibles | pendiente | pendiente | (se llena tras la re-captura) |
| MTTD S01 | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTD S02 | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTD S05 | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTD S07 | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTD S03, S04, S06, S08, S09, S10 | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTD medio | pendiente | pendiente | `07-metricas/kpi_report.json` |
| MTTR / MTTC / MTTContain | pendiente | pendiente | TheHive (requiere casos con timestamps) |
| Eventos capturados (campaña S01–S10) | pendiente | pendiente | `07-metricas/kpi_report.json` (execution.*) |
| Alertas Wazuh ATT&CK generadas | pendiente | pendiente | `04-captura-eventos/` |
| Técnicas ATT&CK detectadas | pendiente | pendiente | `07-metricas/mitre_coverage.json` |
| Tácticas ATT&CK cubiertas | pendiente | pendiente | `07-metricas/mitre_coverage.json` |
| Cobertura ISO 27035 (fases) | pendiente | pendiente | `07-metricas/iso27035_compliance.json` |
| Falsos positivos | pendiente | pendiente | Wazuh/Suricata |
| IMGI | pendiente | pendiente | validación OE4 |
| IIAM | pendiente | pendiente | validación OE4 |

## Cambios aplicados entre iteraciones

| Lección | Cambio en it2 | Commit | Métrica esperada afectada |
|---|---|---|---|
| — | (se llena con las lecciones de la re-captura) | | |

## Notas de análisis

- Todos los valores quedan pendientes hasta que la re-captura limpia de it1
 regenere `kpi_report.json`, `mitre_coverage.json` e `iso27035_compliance.json`
  desde una ejecución real y verificable, y esos archivos queden versionados
  en `evidencias/v2.0-it1/07-metricas/`.
- La definición del punto de inicio (momento del ataque) y de detección
  (primer evento registrado por el sensor) debe conservarse entre it1 e it2
  para que la comparación sea pareada. Ver `analysis/kpi_calculator.py`
  (función `parse_ts` y cálculo de MTTD por escenario).
