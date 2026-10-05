# MANIFIESTO DE EVIDENCIAS — Prototipo II (laboratorio SIN)

## Identificación de la iteración

| Campo | Valor |
|---|---|
| Iteración | 1 (`v2.0-it1`) |
| Rama | `prototipo-2-sin` |
| Commit de captura | `385a2e1` |
| Fecha de captura | 2026-10-04 |
| Laboratorio | 25 contenedores Docker Compose, redes `sin-dmz`, `sin-honeypot`, `sin-soc` |
| Campaña de ataque | S01–S10 ejecutada (10 escenarios) |
| Fuente de métricas | `analysis/kpi_report.json` (copiado en `07-metricas/`) |

## Naturaleza de las figuras de terminal

Por decisión del proyecto del 2026-10-04, las figuras de terminal de esta
iteración son **registros de salida renderizados desde el fichero de texto con
la salida real del comando**, no fotografías de pantalla. Cada figura va
acompañada de su `.txt`, que es la fuente verificable: contiene el comando
literal y su salida sin editar. Cuando la figura se cita en la tesis, el pie
debe describirla como *registro de salida de terminal*, nunca como
*captura de pantalla*.

Las figuras de interfaces web (portal del señuelo, panel de Grafana) sí son
capturas directas del navegador, sin procesamiento.

## Trazabilidad por figura

| Figura | N.º checklist | Qué demuestra | Fuente | Sección de tesis |
|---|---|---|---|---|
| `01-entorno-servicios/01_docker-compose-ps` | 2 | Los 25 contenedores en ejecución | `docker compose ps` | 4.3.6.1 |
| `01-entorno-servicios/05_misp-eventos` | 2 | Consola de MISP autenticada | navegador | 4.3.6.1 |
| `01-entorno-servicios/06_velociraptor-consola` | 2 | Consola DFIR de Velociraptor | navegador | 4.3.6.1 |
| `01-entorno-servicios/07_shuffle-workflows` | 2 | Catálogo de workflows del SOAR | navegador | 4.3.6.1 |
| `01-entorno-servicios/08_thehive-organizaciones` | 2 | Estado que bloquea TheHive (limitación 2) | navegador | 4.3.6.1 |
| `01-entorno-servicios/09_cortex-sin-inicializar` | 2 | Cortex desplegado sin usuario inicial (limitación 6) | navegador | 4.3.6.1 |
| `01-entorno-servicios/02_docker-images` | 2 | Imágenes propias `sin/decoy-portal` y `sin/decoy-api` | `docker images` | 4.3.6.1 |
| `01-entorno-servicios/03_docker-compose-config-services` | 2 | Los 25 servicios declarados | `docker compose config --services` | 4.3.6.1 |
| `01-entorno-servicios/04_wazuh-indexer-indices` | 2 | El SIEM indexando alertas | `_cat/indices` del indexer | 4.3.6.4 |
| `02-senuelo/01_portal-sin-inicio` | 3 | Página de inicio del señuelo | navegador | 4.3.6.2 |
| `02-senuelo/02_portal-sin-login-form` | 3 | Formulario de acceso por NIT | navegador | 4.3.6.2 |
| `02-senuelo/03_portal-sin-otp` | 3 | Verificación en dos pasos (2FA) | navegador | 4.3.6.2 |
| `02-senuelo/04_portal-sin-registro` | 4 | Alta de contribuyente en el señuelo | navegador | 4.3.6.2 |
| `02-senuelo/05_portal-sin-dashboard` | 4 | Contenido adaptado, sin datos reales | navegador | 4.3.6.2 |
| `03-aislamiento-red/01_docker-network-ls` | 1 | Redes `sin-*` del laboratorio | `docker network ls` | 4.3.6.1, 4.3.6.3 |
| `03-aislamiento-red/02_docker-network-inspect-sin-dmz` | 1 | Subred y puerta de enlace de `sin-dmz` | `docker network inspect` | 4.3.6.3 |
| `03-aislamiento-red/03_docker-network-inspect-sin-soc` | 1 | Subred y contenedores de `sin-soc` | `docker network inspect` | 4.3.6.3 |
| `03-aislamiento-red/03_prueba-aislamiento-atacante` | 5 | El atacante alcanza el señuelo y no la red SOC | `nc` desde `sin-attacker` | 4.3.6.3 |
| `04-captura-eventos/01_wazuh-alertas-ids` | 6 | Alertas del SIEM con nivel y MITRE | agregación del índice | 4.3.6.4 |
| `04-captura-eventos/02_grafana-dashboard-siem` | 6 | Panel del SIEM con la actividad | navegador | 4.3.6.4 |
| `04-captura-eventos/03_sensores-ndr-suricata-zeek` | 6 | Reglas IDS disparadas y logs NDR | Suricata y Zeek | 4.3.6.4 |
| `04-captura-eventos/04_cowrie-sesiones-ssh` | 6 | Honeypot SSH escuchando | `docker logs` | 4.3.6.4 |
| `05-enriquecimiento-custodia/01_custodia-hash-sha256` | 7 | Integridad de la evidencia preservada | `sha256sum` | 4.3.6.4 |
| `05-enriquecimiento-custodia/02_decoy-api-registro-ataques` | 7 | Registro de ataques con severidad y TLP | log del señuelo | 4.3.6.4 |
| `06-correlacion-incidentes/01_decoy-api-ataques-detalle` | 6 | Ataques con técnica MITRE y táctica | log del señuelo | 4.3.6.4 |
| `06-correlacion-incidentes/02_shuffle-workflows` | 6 | SOAR disponible para correlación | `curl` de estado | 4.3.6.5 |
| `07-metricas/01_kpi-indicadores` | 8 | MTTD medido; MTTR/MTTC sin datos | `kpi_report.json` | 4.3.6.6.2, 4.4.2 |
| `07-metricas/02_kpi-cobertura-mitre` | 8 | 10 escenarios con técnica y táctica | `kpi_report.json` | 4.4.2 |

## Fuentes de datos

- `07-metricas/kpi_report.json`: informe completo de indicadores.
- `07-metricas/resultados-escenarios/`: `resultados.json` de S01 a S10.

## Limitaciones registradas

1. **Wazuh Dashboard no operativa.** La consola carga el shell pero no
   renderiza las vistas; la imagen local parece incompleta y la descarga
   posterior se corta. La visualización del SIEM se aporta con Grafana, que sí
   funciona contra el mismo índice.
2. **TheHive 5.5 no llega a la vista de casos.** Tras autenticarse, toda ruta
   redirige a `/administration/organisations` por el estado de licencia en
   prueba. La custodia se documenta con el hash SHA-256 de la evidencia
   preservada y el registro de ataques del señuelo.
3. **Red `sin-ids` declarada pero no creada.** Suricata y Zeek corren en
   `network_mode: host`, de modo que la red `10.23.0.0/24` nunca llega a
   existir. En ejecución hay tres segmentos, no cuatro.
4. **Seis escenarios sin MTTD.** S03, S04, S06, S08, S09 y S10 no dejaron
   registro detectable en el señuelo, por lo que el indicador aparece como
   *sin detección*. Es un dato real de la ejecución, no una omisión.
5. **MTTR, MTTC y MTTContain sin muestras.** El cálculo los declara porque
   requieren marcas de tiempo de casos y respuesta que el laboratorio no
   registra.

## Reproducibilidad

| Figura | Cómo regenerar |
|---|---|
| Terminal (`.txt` + `.png`) | `bash scripts/fig.sh <carpeta> <nombre> "<comando>"` |
| Navegador | script de Playwright con viewport 1280×720 |
| Ingesta IDS antes de capturar | `bash scripts/reset-ids-offset.sh` |
| Métricas | `python3 analysis/kpi_calculator.py` |
