# Tabla de comparación entre iteraciones — Prototipo II (SIN)

> Soporta la redacción de los apartados 4.4.5 (análisis de resultados) y
> 4.4.7 (conclusiones por iteración) de la tesis.
> Regla de llenado: cada valor debe citar su fuente (captura, log o
> `kpi_report.json` generado por `kpi_calculator.py`). Sin fuente, sin valor.
>
> **Estado actual: iteración 1 regenerada (2026-10-04).** La columna de it1
> se ha rellenado con valores reales, cada uno citando su fuente. La columna de
> it2 permanece pendiente hasta que exista el tag `v2.1-it2`.

## Convención

| Iteración | Tag | Alcance |
|---|---|---|
| it1 | `v2.0-it1` | Primera ejecución completa de la campaña S01–S10 y análisis |
| it2 | `v2.1-it2` | Re-ejecución tras aplicar las mejoras derivadas de las lecciones L1–Ln |

## Comparación cuantitativa

| Métrica | it1 (v2.0-it1) | it2 (v2.1-it2) | Fuente |
|---|---|---|---|
| Escenarios ejecutados | 10 de 10 | pendiente | `07-metricas/kpi_report.json` (`execution.scenarios_executed`) |
| Servicios accesibles | 25 contenedores en ejecución | pendiente | `01-entorno-servicios/01_docker-compose-ps` |
| MTTD S01 | 16,85 s | pendiente | `07-metricas/kpi_report.json` |
| MTTD S02 | 1,21 s | pendiente | `07-metricas/kpi_report.json` |
| MTTD S05 | 1,73 s | pendiente | `07-metricas/kpi_report.json` |
| MTTD S07 | 1,06 s | pendiente | `07-metricas/kpi_report.json` |
| MTTD S03, S04, S06, S08, S09, S10 | sin detección (0 muestras) | pendiente | `07-metricas/kpi_report.json` |
| MTTD medio | 5,22 s (4 muestras; mín 1,06 / máx 16,85) | pendiente | `07-metricas/kpi_report.json` |
| MTTR / MTTC / MTTContain | n/d (0 muestras) | pendiente | `07-metricas/kpi_report.json` |
| Eventos capturados (campaña S01–S10) | 11 eventos IDS en el último ciclo | pendiente | `04-captura-eventos/03_sensores-ndr-suricata-zeek` |
| Alertas Wazuh generadas | 28 alertas IDS; 434 totales en el índice | pendiente | `04-captura-eventos/02_grafana-dashboard-siem` |
| Técnicas ATT&CK implementadas | 17 | pendiente | `07-metricas/mitre_coverage.json` |
| Técnicas ATT&CK detectadas | 10 | pendiente | `07-metricas/mitre_coverage.json` |
| Tácticas ATT&CK cubiertas | 6 | pendiente | `07-metricas/kpi_report.json` (`coverage`) |
| Cobertura ISO 27035 (fases) | 5 de 5 fases con evidencia | pendiente | `07-metricas/iso27035_compliance.json` |
| Reglas IDS propias disparadas | 4 (sid 2024001, 2024010, 2024011, 2024012) | pendiente | `04-captura-eventos/03_sensores-ndr-suricata-zeek` |
| Hash de custodia de la evidencia | SHA-256 `68f39b01…7f855c` | pendiente | `05-enriquecimiento-custodia/01_custodia-hash-sha256` |
| Falsos positivos | no medido | pendiente | requiere revisión manual de `04-captura-eventos/` |
| IMGI | no medido en it1 | pendiente | validación OE4 |
| IIAM | no medido en it1 | pendiente | validación OE4 |

### Lectura de la tabla

Dos filas exigen explicación al redactar, porque son límites de la medición y no
defectos de la captura:

- **MTTD con 4 muestras de 10 escenarios.** S03, S04, S06, S08, S09 y S10 no
  dejaron registro detectable en el señuelo. El valor medio de 5,22 s describe
  los cuatro escenarios que el señuelo sí instrumentó, no la campaña completa.
- **MTTR, MTTC y MTTContain sin muestras.** El cálculo los emite porque
  requieren marcas de tiempo de casos y de respuesta que el laboratorio no
  registra. Con la vista de casos de TheHive inaccesible (ver
  `v2.0-it1/MANIFIESTO.md`, limitación 2), no hay forma de medirlos en it1 sin
  instrumentar el registro de incidentes.

## Cambios aplicados entre iteraciones

| Lección | Cambio en it2 | Commit | Métrica esperada afectada |
|---|---|---|---|
| L1 `ossec.conf` inválido | Inserción de los `localfile` dentro del elemento raíz | `c66f7c7` | Alertas del SIEM (era 0) |
| L2 filebeat 7.10 vs OpenSearch 2.19 | Publicador propio por HTTP `_bulk` | `c66f7c7` | Alertas indexadas |
| L3 crash de filebeat tumba el container | `output.console` con input inerte | `20ee788` | Estabilidad del manager |
| L4 offset de logcollector desfasado | `make ids-reset` | `2d13573` | MTTD por escenario |
| L5 `terms` incompatible en Grafana | Consultas Lucene por rango | `20ee788` | Distribución por severidad |
| L6 campo temporal `@timestamp` ausente | Se añade en el publicador | `20ee788` | Series temporales |
| L7 `set -e` en entrypoint tumba el init | Scripts a prueba de fallos | `c66f7c7` | Estabilidad de todos |

## Notas de análisis

- Todos los valores de it1 proceden de una ejecución real del 2026-10-04 y
  están versionados en `evidencias/v2.0-it1/07-metricas/`
  (`kpi_report.json`, `mitre_coverage.json`, `iso27035_compliance.json`).
- La definición del punto de inicio (momento del ataque) y de detección
  (primer evento registrado por el sensor) debe conservarse entre it1 e it2
  para que la comparación sea pareada. Ver `analysis/kpi_calculator.py`
  (función `parse_ts` y cálculo de MTTD por escenario).
