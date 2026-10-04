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
| Escenarios ejecutados | 10 de 10 | 10 de 10 | `07-metricas/kpi_report.json` |
| Escenarios con MTTD medido | 4 de 10 | **10 de 10** | `07-metricas/kpi_report.json` |
| Servicios accesibles | 25 contenedores | 25 contenedores | `01-entorno-servicios/01_docker-compose-ps` |
| MTTD S01 | 16,85 s | 15,91 s | `07-metricas/kpi_report.json` |
| MTTD S02 | 1,21 s | 1,09 s | `07-metricas/kpi_report.json` |
| MTTD S03 | sin detección | 0,00 s (cowrie) | `07-metricas/kpi_report.json` |
| MTTD S04 | sin detección | 0,14 s (decoy-portal) | `07-metricas/kpi_report.json` |
| MTTD S05 | 1,73 s | 1,15 s | `07-metricas/kpi_report.json` |
| MTTD S06 | sin detección | 0,46 s (decoy-portal) | `07-metricas/kpi_report.json` |
| MTTD S07 | 1,06 s | 0,26 s | `07-metricas/kpi_report.json` |
| MTTD S08 | sin detección | 0,56 s (opencanary) | `07-metricas/kpi_report.json` |
| MTTD S09 | sin detección | 0,00 s (cowrie) | `07-metricas/kpi_report.json` |
| MTTD S10 | sin detección | 0,65 s (zeek-dns) | `07-metricas/kpi_report.json` |
| MTTD medio | 5,22 s (4 muestras) | **2,02 s (10 muestras)** | `07-metricas/kpi_report.json` |
| MTTD mínimo / máximo | 1,06 s / 16,85 s | 0,00 s / 15,91 s | `07-metricas/kpi_report.json` |
| MTTR / MTTC / MTTContain | n/d (0 muestras) | n/d (0 muestras) | requiere casos de TheHive con marcas de tiempo |
| Técnicas ATT&CK implementadas | 17 | 17 | `07-metricas/mitre_coverage.json` |
| Técnicas ATT&CK detectadas | 10 | 10 | `07-metricas/kpi_report.json` |
| Cobertura ISO 27035 (fases) | 5 de 5 | 5 de 5 | `07-metricas/iso27035_compliance.json` |
| Reglas IDS propias disparadas | 4 | 4 | `04-captura-eventos/` |
| Hash de custodia de la evidencia | SHA-256 registrado | SHA-256 registrado | `05-enriquecimiento-custodia/` |
| Falsos positivos | no medido | no medido | requiere revisión manual |
| IMGI | no medido | no medido | validación OE4 |
| IIAM | no medido | no medido | validación OE4 |

### Lectura de la comparación

La diferencia entre it1 e it2 **no está en la detección, sino en la medición**.
Las tres lecciones que cerramos en it2 (L11, L13, L14) no Vinieron a
mejorar el laboratory: el señuelo ya registraba los ataques desde it1. Lo que
estaba roto era el instrumento que los medía:

- **L11**: el calculador nunca lograba saber a qué señuelo atribuir una
  detección, porque leía una clave que ningún escenario escribía con ese
  nombre. Seis escenarios quedaban como "sin detección" aunque el evento
  estuviera registrado.
- **L13**: S09 anunciaba una captura en Cowrie que nunca ocurrió, porque
  `sshpass` no estaba instalado y el escenario no lo comprobaba.
- **L14**: los eventos de OpenCanary y del DNS de Zeek existían pero ninguna
  fuente de detección los leía.

Consecuencia metodológica: **la media de MTTD de it1 (5,22 s) no es comparable
con la de it2 (2,02 s)**, porque it1 media cuatro escenarios y it2 mide diez.
La comparación válida es la de cada escenario por separado (columna a columna),
que sí es pareada. Para la comparación de medias con la prueba de Wilcoxon
habría que recalcular it1 con el instrumento corregido y volver a ejecutar la
campaña de it1; mientras tanto, la tabla de MTTD por escenario es la que
sostiene el argumento.


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
