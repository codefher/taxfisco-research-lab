# Tabla de comparación entre iteraciones — Prototipo II (SIN)

> Soporta la redacción de los apartados 4.4.5 (análisis de resultados) y
> 4.4.7 (conclusiones por iteración) de la tesis.
> Regla de llenado: cada valor debe citar su fuente (captura, log o
> `kpi_report.json` generado por `kpi_calculator.py`). Sin fuente, sin valor.
>
> **Estado al 2026-10-03 (re-captura it1):** los valores de it1 que se
> muestran a continuación provienen de la campaña S01–S10 ejecutada en esta
> sesión sobre el laboratorio SIN, con `kpi_report.json` versionado en
> `evidencias/v2.0-it1/07-metricas/`. La columna it2 queda pendiente hasta
> que se ejecute la iteración 2 (tag `v2.1-it2`).

## Convención

| Iteración | Tag | Alcance |
|---|---|---|
| it1 | `v2.0-it1` | Primera ejecución completa de la campaña S01–S10 y análisis |
| it2 | `v2.1-it2` | Re-ejecución tras aplicar las mejoras derivadas de las lecciones L1–Ln |

## Comparación cuantitativa

| Métrica | it1 (v2.0-it1) | it2 (v2.1-it2) | Fuente it1 |
|---|---|---|---|
| Escenarios ejecutados | S01–S10 (10/10) | pendiente | `evidencias/v2.0-it1/09-escenarios/` + `analysis/kpi_calculator.py` |
| Servicios accesibles | 9/9 | pendiente | `docs/ACCESO-SERVICIOS-P2.md` (commit `b1f9eca`) + verificado en sesión 2026-10-03 |
| MTTD S01 | **14.89 s** | pendiente | `07-metricas/kpi_report.json` (regenerado 2026-10-03T23:17Z) |
| MTTD S02 | **10.27 s** | pendiente | `07-metricas/kpi_report.json` (regenerado 2026-10-03T23:17Z) |
| MTTD S05 | **0.77 s** | pendiente | `07-metricas/kpi_report.json` (regenerado 2026-10-03T23:17Z) |
| MTTD S07 | **0.09 s** | pendiente | `07-metricas/kpi_report.json` (regenerado 2026-10-03T23:17Z) |
| MTTD S03, S04, S06, S08, S09, S10 | sin detección registrada en el decoy (atacan honeypots u otros servicios, o la instrumentación del MTTD no quedó alineada con los timestamps del script) | pendiente | `07-metricas/kpi_report.json` + commit `b1f9eca` |
| MTTD medio (n=4) | **6.506 s** | pendiente | `07-metricas/kpi_report.json` (mean=6.506, samples=4) |
| MTTR medio | NO MEDIDO (TheHive sin casos en esta sesión → sin timestamps de triage) | pendiente | `04-captura-eventos/03_hallazgo-wazuh-suricata.txt` |
| MTTC, MTTContain | NO MEDIDO | pendiente | idem MTTR |
| Eventos capturados (campaña S01–S10) | 264 ataques al decoy-api; 1455 requests al decoy; 29 conexiones Cowrie; 14 898 requests al portal; 1 evento MISP previo (ID 1, 8 IOCs, 4 ATT&CK clusters) | pendiente | `07-metricas/kpi_report.json` (execution.*) + `05-enriquecimiento-custodia/03_*` (MISP) |
| Alertas Wazuh ATT&CK generadas | 0 (reglas 100200-100299 no se dispararon: Suricata en crash loop; Wazuh no ingiere `/var/log/decoy-api/attacks.json`) | pendiente | `04-captura-eventos/03_hallazgo-wazuh-suricata.txt` |
| Técnicas ATT&CK detectadas | 10 | pendiente | `07-metricas/mitre_coverage.json` |
| Tácticas ATT&CK cubiertas | 6 (Reconnaissance, Initial Access, Credential Access, Execution, Persistence, Exfiltration — más Privilege Escalation y Defense Evasion vía T1078) | pendiente | `07-metricas/mitre_coverage.json` |
| Cobertura ISO 27035 (fases) | 5/5 (Plan & Prepare, Detection & Reporting, Assessment & Decision, Response, Lessons Learned) | pendiente | `07-metricas/iso27035_compliance.json` |
| Lecciones aprendidas acumuladas | 7 (L1-L5 CERRADAS, L6 CERRADA, L7 MONITOREO) | pendiente | `evidencias/lecciones-aprendidas.md` |
| IMGI | validado en 4.3.6.2 (decoy instrumentado en tiempo real) | pendiente | `02-senuelo/` + `decoys/api-tributaria/` |
| IIAM | validado en 4.3.6.4 (correlación MISP evento #1 con 8 IOCs) | pendiente | `05-enriquecimiento-custodia/03_*` |

## Cambios aplicados entre iteraciones

| Lección | Cambio propuesto en it2 | Commit (cuando se aplique) | Métrica esperada afectada |
|---|---|---|---|
| L1 | (si aplica mejora adicional) | – | disponibilidad de servicios |
| L2 | (si aplica mejora adicional) | – | persistencia de índices / pérdida de eventos |
| L3 | – | – | integridad del cómputo de KPIs |
| L4 | – | – | accesibilidad del servicio de forense |
| L5 | – | – | cobertura de enriquecimiento (MISP) |
| L6 (nueva) | versionar fix de `run_all.sh` en `prototipo-2-sin` | (durante esta sesión) | capacidad de regenerar `kpi_report.json` sin intervención manual |
| L7 (nueva) | Dockerfile del atacante con `nmap, sqlmap, hydra, curl, jq, openssl, python3` preinstalados | – (propuesto) | capacidad de ejecutar `make attacks` sin instalar paquetes a mano |

## Notas de análisis

- **Variabilidad entre ejecuciones**: comparando los MTTD de it1 con los de la
  sesión del 30 Sep (archivados en `evidencias/v2.0-it1/07-metricas/_legacy/`,
  valores 16.40 s / 7.88 s / 1.05 s / 1.03 s), se observa que los órdenes
  de magnitud se conservan (S01 ≈ 15 s, S05 < 1 s, S07 < 1 s). La única
  inversión relevante es S02 (10.27 s vs 7.88 s) — plausible porque S02
  depende del tiempo que tarda el script en ejecutar gobuster/nikto/dirb y
  puede variar por carga del host (en esta sesión, 5.5 GB de RAM libre al
  momento de la campaña, vs 7+ GB el 30 Sep).
- **S04, S06, S09, S10 sin MTTD**: la instrumentación del MTTD usa el
  primer evento en `/var/log/decoy-api/attacks.json` cuyo timestamp sea
  posterior al `start_time.txt`. En esta sesión, los timestamps de los
  eventos del decoy llegaron antes (probable reutilización del log por la
  sesión anterior), por lo que `kpi_calculator.py` no encontró un primer
  evento alineado. Acción para it2: en `attack-scenarios/*/ejecutar.sh`,
  rotar `attacks.json` antes de empezar (`mv attacks.json attacks.json.bak`).
- **Suricata en crash loop**: explica por qué Wazuh no genera alertas de
  las reglas 100200-100299. Acción para it2: revisar `/start-sin.sh` y
  añadir `<localfile>` para `/var/log/decoy-api/attacks.json`.
