# Plan de captura — iteración 1 (`v2.0-it1`)

- **Alcance:** re-captura limpia (la evidencia previa fue borrada en el reset `2fe9f1d` por ser NO VERIFICABLE).
- **Tag:** `v2.0-it1` · **Commit de captura:** `385a2e1` · **Fecha:** 2026-10-04
- **Regla:** captura cruda o nada. Sin retoques, marcos, leyendas ni imágenes generadas. Toda salida de terminal lleva su `.txt` de respaldo.
- **Total estimado:** 40 capturas agrupadas en los 10 números del checklist.

## N.º 1 — Redes `sin-*` → `03-aislamiento-red/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 1.1 | `01_docker-network-ls.png` | Las 6 redes segmentadas del laboratorio | terminal + `01_docker-network-ls.txt` |
| 1.2 | `02_docker-network-inspect-sin-dmz.png` | Subred y gateway de `sin-dmz` | terminal + `.txt` |
| 1.3 | `03_docker-network-inspect-sin-soc.png` | Subred y gateway de `sin-soc` | terminal + `.txt` |

## N.º 2 — Entorno y servicios → `01-entorno-servicios/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 2.1 | `01_docker-compose-ps.png` | Los 25 contenedores en ejecución | terminal + `.txt` |
| 2.2 | `02_docker-images-sin-decoy.png` | Imágenes `sin/decoy-portal` y `sin/decoy-api` | terminal + `.txt` |
| 2.3 | `03_docker-compose-config-services.png` | Los 25 servicios declarados | terminal + `.txt` |
| 2.4 | `04_grafana-dashboard.png` | Dashboards de Grafana con métricas del lab | navegador 1280×720 |
| 2.5 | `05_wazuh-dashboard-overview.png` | Vista general del SIEM | navegador 1280×720 |

## N.º 3 y 4 — Portal SIN (señuelo) → `02-senuelo/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 3.1 | `01_portal-sin-inicio.png` | Página de inicio del portal señuelo | navegador |
| 3.2 | `02_portal-sin-login-form.png` | Formulario de acceso del contribuyente | navegador |
| 4.1 | `03_portal-sin-acceso-exitoso.png` | Acceso con `1020304050` / `Prueba2024!` | navegador |
| 4.2 | `04_portal-sin-declaracion.png` | Contenido adaptado sin datos reales | navegador |
| 4.3 | `05_portal-sin-consulta-ui.png` | Consulta UI deibo/rentas del señuelo | navegador |
| 4.4 | `06_portal-sin-admin-django.png` | Administración Django del portal | navegador |

## N.º 5 — Aislamiento y segmentación → `03-aislamiento-red/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 5.1 | `04_prueba-aislamiento-atacker-sin-dmz.png` | El atacante alcanza el señuelo | terminal + `.txt` |
| 5.2 | `05_prueba-aislamiento-atacker-sin-soc.png` | El atacante NO alcanza la red SOC | terminal + `.txt` |
| 5.3 | `06_prueba-aislamiento-atacker-indexer.png` | El atacante NO alcanza Wazuh Indexer | terminal + `.txt` |
| 5.4 | `07_políticas-red-sin-*.png` | Reglas de red por subcarpeta | terminal + `.txt` |

## N.º 6 — Captura de eventos en el SIEM → `04-captura-eventos/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 6.1 | `01_campaña-s01-s10-ejecución.png` | Salida completa de la campaña S01–S10 | terminal + `execution_log.txt` |
| 6.2 | `02_wazuh-alertas-senuelo.png` | Alertas del señuelo en el SIEM | navegador |
| 6.3 | `03_wazuh-alertas-nivel-alto.png` | Alertas de nivel alto/crítico | navegador |
| 6.4 | `04_thehive-casos-creados.png` | Casos generados en TheHive | navegador |
| 6.5 | `05_thehive-caso-detalle.png` | Detalle de un caso con observables | navegador |
| 6.6 | `06_cortex-analisis.png` | Análisis de observables con Cortex | navegador |
| 6.7 | `07_misp-iocs.png` | IOCs publishados en MISP | navegador |
| 6.8 | `08_grafana-mttd.png` | MTTD por escenario | navegador |
| 6.9 | `09_suricata-alertas.png` | Alertas de Suricata (red) | terminal + `.txt` |
| 6.10 | `10_zeek-conexiones.png` | Registro de conexiones Zeek | terminal + `.txt` |
| 6.11 | `11_cowrie-sesiones-ssh.png` | Sesiones SSH del señuelo Cowrie | navegador |
| 6.12 | `12_shuffle-workflows.png` | Workflows SOAR de Shuffle | navegador |

## N.º 7 — Enriquecimiento y custodia → `05-enriquecimiento-custodia/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 7.1 | `01_thehiveduplico-hash.png` | Hash SHA-256 del artefacto adjunto | navegador |
| 7.2 | `02_velociraptor-tabla-hunt.png` | Plataforma DFIR desplegada | navegador |
| 7.3 | `03_misp-atributos-fuente.png` | Atributos con fuente de origin | navegador |

## N.º 8 — Métricas de la iteración 1 → `07-metricas/`

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 8.1 | `01_kpi_calculator-salida.png` | Ejecución real del calculador de KPIs | terminal + salida completa |
| 8.2 | `02_kpi_report-json.png` | Contenido de `kpi_report.json` | terminal + copia del JSON |
| 8.3 | `03_mitre-coverage-matriz.png` | Matriz MITRE ATT&CK cubierta | terminal + JSON |
| 8.4 | `04_iso27035-reporte.png` | Reporte ISO 27035/27001 | terminal + JSON |
| 8.5 | `05_resultados-json-s01-s10.png` | `resultados.json` de los 10 escenarios | terminal + copia de los 10 JSON |

## N.º 9 — Lecciones aprendidas → raíz de iteración

| # | Archivo | Qué demuestra | Método |
|---|---|---|---|
| 9.1 | `01_lecciones-aprendidas-registro.png` | Registro L1–L5 con su evidencia y commit | documento renderizado en navegador |

## N.º 10 — Iteración 2

Fuera de alcance: el tag `v2.1-it2` no existe. Se registrará como pendiente en el MANIFIESTO.

## Orden de ejecución

1. N.º 1, 2, 5 (terminal, sin dependencias) — 9 capturas
2. N.º 3, 4 (portal) — 6 capturas
3. Campaña S01–S10 (requiere herramientas instaladas en `attacker`)
4. N.º 6, 7 (SIEM y custodia, ya con eventos reales) — 15 capturas
5. N.º 8, 9 (métricas y lecciones) — 6 capturas
6. MANIFIESTO.md, copias de JSON a `07-metricas/`, commits `[P2]`

## Dependencia bloqueante

`sin-attacker` necesita `curl`, `wget`, `nmap`, `hydra`, `sqlmap`, `dig`, `nikto`, `netcat` y `python3` para ejecutar la campaña. La instalación está en curso dentro del contenedor.
