# Tabla de comparación entre iteraciones — Prototipo II (SIN)

> Soporta la redacción de los apartados 4.4.5 (análisis de resultados) y
> 4.4.7 (conclusiones por iteración) de la tesis.
> Regla de llenado: cada valor debe citar su fuente (captura, log o
> `kpi_report.json` generado por `kpi_calculator.py`). Sin fuente, sin valor.
> **Auditoría 2026-10-01 (ver AUDITORIA-v2.0-it1.md):** la evidencia visual
> previa de it1 es NO VERIFICABLE y los `kpi_report.json` no están en el
> repo; los valores de it1 permanecen aquí solo como referencia interna y
> no deben citarse en la tesis hasta su re-captura y regeneración.

## Convención

| Iteración | Tag | Alcance |
|---|---|---|
| it1 | `v2.0-it1` | Primera ejecución completa de la campaña S01–S10 y análisis |
| it2 | `v2.1-it2` | Re-ejecución tras aplicar las mejoras derivadas de las lecciones L1–Ln |

## Comparación cuantitativa

| Métrica | it1 (v2.0-it1) | it2 (v2.1-it2) | Fuente |
|---|---|---|---|
| Escenarios ejecutados | S01–S10 (10/10) | pendiente | pendiente de verificar (evidencia previa NO VERIFICABLE, ver AUDITORIA-v2.0-it1.md) |
| Servicios accesibles | 9/9 | pendiente | commit `b1f9eca` |
| MTTD S01 | 16.40 s | pendiente | pendiente de verificar (`kpi_report.json` no localizado en el repo; regenerar) |
| MTTD S02 | 7.88 s | pendiente | pendiente de verificar (`kpi_report.json` no localizado en el repo; regenerar) |
| MTTD S05 | 1.05 s | pendiente | pendiente de verificar (`kpi_report.json` no localizado en el repo; regenerar) |
| MTTD S07 | 1.03 s | pendiente | pendiente de verificar (`kpi_report.json` no localizado en el repo; regenerar) |
| MTTD S03, S04, S06, S08, S09, S10 | sin detección en el decoy (atacan honeypots u otros servicios) | pendiente | commit `b1f9eca` |
| MTTR medio | pendiente | pendiente | pendiente de verificar (`kpi_report.json` no localizado en el repo; regenerar) |
| Eventos capturados (campaña S01–S10) | 1 evento correlado vía MISP_2_1 | pendiente | commit `7dd41df` |
| Falsos positivos | pendiente | pendiente | Wazuh/Suricata |
| Técnicas ATT&CK detectadas | pendiente (mapear desde eventos) | pendiente | TheHive/Cortex |
| Cobertura ATT&CK (tácticas) | pendiente | pendiente | matriz ATT&CK |
| Cobertura ATT&CK (técnicas) | pendiente | pendiente | matriz ATT&CK |
| IMGI | pendiente (instrumentación demostrada en 4.3) | pendiente | validación OE4 |
| IIAM | pendiente (instrumentación demostrada en 4.3) | pendiente | validación OE4 |

## Cambios aplicados entre iteraciones

| Lección | Cambio en it2 | Commit | Métrica esperada afectada |
|---|---|---|---|
| L1 | (si aplica mejora adicional) | | disponibilidad de servicios |
| L2 | (si aplica mejora adicional) | | persistencia de índices / pérdida de eventos |
| L3 | | | integridad del cómputo de KPIs |
| L4 | | | accesibilidad del servicio de forense |
| L5 | | | cobertura de enriquecimiento (MISP) |
| L6+ | | | |

## Notas de análisis

- El MTTD de it1 ya se midió con eventos reales (no sintéticos); conservar la
  definición del punto de inicio (momento del ataque) y de detección
  (ingesta al SIEM) para que la comparación it1 vs it2 sea pareada.
- Los escenarios sin MTTD en it1 atacan honeypots o servicios sin sensor de
  detección en el decoy; documentar si en it2 se amplía la instrumentación
  (lección asociada: ___).
