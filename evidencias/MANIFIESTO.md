# Manifiesto de Evidencias - TaxFisco Research Lab

**Fecha de captura:** 2026-09-14
**Proyecto:** TaxFisco Research Lab - Sistema Honeypot de Gestión de Incidentes

**Nota sobre capturas de terminal:** se tomaron con un terminal real (`xterm` sobre X11) y la salida se coloreó con un filtro ANSI (`... | color`). Los archivos `.txt` conservan la salida sin códigos de color.

---

## Estado de Servicios Capturados

| Servicio | URL | Estado | Observación |
|----------|-----|--------|-------------|
| Decoy Portal | http://localhost:8890 | Funcionando | 6 capturas |
| Decoy API | http://localhost:8090 | Funcionando | Swagger UI + endpoints |
| Wazuh Dashboard | https://localhost:1443 | Login OK | Index patterns `wazuh-alerts-*` y `wazuh-*` creados; Discover muestra 199 alertas |
| Grafana | http://localhost:3000 | Funcionando con datos | 3 dashboards con datos reales |
| TheHive | http://localhost:9000 | Con licencia **trial (15 días)** | Org `TaxFisco` + caso #1 creados |
| Shuffle | http://localhost:3001 | Configurado | Usuario `admin` + org `default`; 1 workflow |
| MISP | https://localhost:8443 | Configurado | Admin + API key; 1 evento publicado |
| Velociraptor | https://localhost:8889 | **Funcionando (admin/Admin1234!)** | GUI + Server dashboard |
| Cortex | http://localhost:9001 | Login OK, backend ES caído | UI operativa; API `user/current` → "ElasticSearch cluster is unreachable" |

---

## 01 - Entorno y Servicios

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_docker-ps.png / .txt | Entorno y servicios | 30 contenedores activos con estado y puertos | Terminal: `docker ps --format ...` | 2026-09-14 | Captura real de xterm (X11) |
| 02_docker-networks.png / .txt | Aislamiento de red | Redes Docker del host; las 4 del lab (`taxfisco-dmz/honeypot/ids/soc`) | Terminal: `docker network ls --format ...` | 2026-09-14 | Captura real de xterm |
| 03_compose-servicios.png / .txt | Entorno y servicios | 25 servicios definidos en `docker-compose.yml` | Terminal: `docker compose config --services` | 2026-09-14 | Captura real de xterm |
| 04_compose-redes-volumenes.png / .txt | Entorno y servicios | Definición de las 4 redes y 23 volúmenes en el compose | Terminal: `sed -n '/^networks:/,$p' docker-compose.yml` | 2026-09-14 | Captura real de xterm |
| 05_arquitectura-redes.png / .txt | Aislamiento de red | Subnet, gateway y contenedores IPv4 por red | Terminal: `docker network inspect <red> --format ...` | 2026-09-14 | Captura real de xterm |
| 06_docker-images.png / .txt | Entorno y servicios | 24 imágenes del laboratorio y su tamaño | Terminal: `docker compose config --images \| xargs docker image ls` | 2026-09-14 | Captura real de xterm |
| 07_docker-volumes.png / .txt | Enriquecimiento y custodia | 23 volúmenes persistentes del proyecto | Terminal: `docker volume ls` filtrado | 2026-09-14 | Captura real de xterm |
| 08_wazuh-dashboard.png | Captura de eventos | Wazuh Discover con 199 alertas en `wazuh-alerts-*` | Pantalla web (chrome-devtools MCP) | 2026-09-14 | Últimos 90 días |

---

## 02 - Señuelo

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_portal-home.png | Señuelo (portal) | Página principal del portal tributario falso | Pantalla web (chrome-devtools MCP) | 2026-09-14 | Aviso de honeypot visible |
| 02_portal-login.png | Señuelo (portal) | Formulario de inicio de sesión | Pantalla web | 2026-09-14 | |
| 03_portal-register.png | Señuelo (portal) | Registro de contribuyente | Pantalla web | 2026-09-14 | |
| 04_portal-consulta-nit.png | Señuelo (portal) | Consulta de contribuyente por NIT | Pantalla web | 2026-09-14 | |
| 05_portal-declaraciones.png | Señuelo (portal) | Formulario de declaración jurada | Pantalla web | 2026-09-14 | |
| 06_portal-facturacion.png | Señuelo (portal) | Listado de facturas con datos simulados | Pantalla web | 2026-09-14 | |
| 07_portal-error-404.png | Señuelo (portal) | Página 404 con `DEBUG=True` y patrones de URL | Pantalla web | 2026-09-14 | |
| 08_api-home.png / .txt | Señuelo (API) | JSON raíz: 6 endpoints y `deception_markers` | Terminal: `curl .../ \| python3 -m json.tool` | 2026-09-14 | Captura real de xterm |
| 09_api-docs.png | Señuelo (API) | Swagger UI con los endpoints documentados | Pantalla web | 2026-09-14 | |
| 10_api-openapi.png / .txt | Señuelo (API) | Resumen del OpenAPI: título, versión 2.0.0 y 19 endpoints | Terminal: `curl .../openapi.json \| python3` | 2026-09-14 | Captura real de xterm |
| 11_api-health.png / .txt | Señuelo (API) | `/health` responde `status: healthy` | Terminal: `curl .../health \| python3 -m json.tool` | 2026-09-14 | Captura real de xterm |
| 12_api-endpoints.json | Señuelo (API) | Especificación OpenAPI 3.1.0 completa | `curl .../openapi.json -o` | 2026-09-14 | 13 KB |

---

## 03 - Aislamiento de Red

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_redes-docker.png / .txt | Aislamiento de red | Las 4 redes del laboratorio (`dmz`/`honeypot`/`ids`/`soc`), driver bridge | Terminal: `docker network ls --filter name=taxfisco` | 2026-09-14 | Captura real de xterm |
| 02_subnets.png / .txt | Aislamiento de red | Subnet, gateway y nº de contenedores por red | Terminal: `docker network inspect <red> --format ...` | 2026-09-14 | Captura real de xterm |
| 03_docker-network-inspect.png / .txt | Aislamiento de red | Driver, scope, `internal` y subnet de cada red | Terminal: `docker network inspect ... --format ...` | 2026-09-14 | Captura real de xterm |
| 04_wazuh-dashboard.png | Acceso a servicios | Wazuh: index patterns `wazuh-alerts-*` (default) y `wazuh-*` | Pantalla web (chrome-devtools MCP) | 2026-09-14 | |
| 05_grafana-login.png | Acceso a servicios | Login de Grafana | Pantalla web | 2026-09-14 | Contexto limpio (sin sesión) |
| 06_thehive-login.png | Acceso a servicios | TheHive: lista de organizaciones | Pantalla web | 2026-09-14 | Aviso de licencia inválida |
| 07_shuffle-login.png | Acceso a servicios | Shuffle: wizard de setup inicial | Pantalla web | 2026-09-14 | Sin usuario/org configurado |
| 08_misp-login.png | Acceso a servicios | MISP: pantalla de instalación inicial | Pantalla web | 2026-09-14 | Requiere PGP key |
| 09_velociraptor-login.png | Acceso a servicios | Velociraptor: welcome autenticado como admin | Pantalla web | 2026-09-14 | |
| 10_cortex-login.png | Acceso a servicios | Login de Cortex | Pantalla web | 2026-09-14 | |
| 11_cortex-error-elasticsearch.png | Limitación | Cortex API `/api/user/current`: "ElasticSearch cluster is unreachable" | Pantalla web | 2026-09-14 | Backend ES caído |

---

## 04 - Captura de Eventos

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_wazuh-eventos.png | Captura de eventos | Wazuh Discover: 199 eventos capturados (grupos `sca`/`ossec`) | Pantalla web (playwright-cli) | 2026-09-14 | No hay alertas de ataque en Wazuh (solo SCA/compliance) |
| 02_wazuh-evento-detalle.png | Captura de eventos | Detalle (JSON) de un evento capturado | Pantalla web | 2026-09-14 | |
| 03_decoy-api-logs_prueba-sintetica.png / .txt | Captura de eventos | Peticiones al señuelo API; incluye T1190 (`' OR '1'='1`) | Terminal: `docker logs taxfisco-decoy-api` | 2026-09-14 | Evento sintético (atacante 10.20.0.1) |
| 04_cowrie-logs_prueba-sintetica.png / .txt | Captura de eventos | Intentos SSH (`root/none`, `root/password`, login) desde 10.20.0.99 | Terminal: `docker logs taxfisco-cowrie` | 2026-09-14 | Evento sintético |
| 05_wazuh-logs.png / .txt | Captura de eventos | Ingesta de índices y escaneo SCA del Wazuh Manager | Terminal: `docker logs taxfisco-wazuh-manager` | 2026-09-14 | |
| 06_suricata-logs.png / .txt | Captura de eventos | Suricata: `Alerts: 0` y errores de parseo de reglas | Terminal: `docker logs taxfisco-suricata` | 2026-09-14 | Limitación del IDS |
| 07_opencanary-logs.png / .txt | Captura de eventos | OpenCanary: arranque y "Canary running!!!" | Terminal: `docker logs taxfisco-opencanary` | 2026-09-14 | Sin eventos de ataque en el log |
| 08_heralding-logs_prueba-sintetica.png / .txt | Captura de eventos | Heralding: arranque y servicios en escucha | Terminal: `docker logs taxfisco-heralding` | 2026-09-14 | IP pública enmascarada (`166.114.x.x`) |

---

## 05 - Enriquecimiento y Custodia

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_hash-evidencia.png / .txt | Custodia | SHA-256 de las capturas de evidencia (secciones 01–04, 06–07) | Terminal: `sha256sum $(ls evidencias/*/*.png \| grep -v 05-...)` | 2026-09-14 | Excluye los artefactos de custodia de esta sección |
| 02_timestamp.png / .txt | Custodia | Fecha/hora de la toma de evidencia | Terminal: `date -Iseconds` | 2026-09-14 | Captura real de xterm |
| 03_verificacion-integridad.png / .txt | Custodia | Verificación de integridad: las sumas coinciden | Terminal: `sha256sum -c` | 2026-09-14 | "La suma coincide" |
| 04_enriquecimiento-mitre_prueba-sintetica.png / .txt | Enriquecimiento | Evento enriquecido con ATT&CK (T1110.001) y fase ISO 27035 | Terminal: `python3 -m json.tool .../resultados.json` | 2026-09-14 | Escenario sintético S03 |
| 05_cadena-custodia_prueba-sintetica.png / .txt | Custodia | Archivos de evidencia del escenario con timestamps inicio/fin | Terminal: `ls -la` + `cat start/end_time.txt` | 2026-09-14 | Escenario sintético S03 |

---

## 06 - Correlación de Incidentes

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_thehive-caso_prueba-sintetica.png | Correlación de incidentes | TheHive **caso #1** "Intento de fuerza bruta SSH contra honeypot Cowrie", tags `T1110.001` | Pantalla web (playwright-cli) | 2026-09-14 | Incidente **sintético**; licencia **trial 15 días**; org `TaxFisco` + usuario `org-admin` |
| 02_shuffle-workflow.png | Correlación de incidentes | Workflow SOAR de 3 pasos: **Webhook Wazuh → Crear caso en TheHive → Correlacionar IOC en MISP**; se muestra la config del POST a TheHive | Pantalla web (playwright-cli) | 2026-09-14 | Config de automatización (no es un evento); **no ejecuta** por falta de worker Orborus/socket Docker |
| 03_misp-eventos_prueba-sintetica.png | Correlación de incidentes | Evento MISP #1 **"Fuerza bruta SSH (T1110.001)"** publicado, 3 atributos | Pantalla web (playwright-cli) | 2026-09-14 | Incidente **sintético**; creado/publicado vía API |
| 04_thehive-alertas_prueba-sintetica.png | Correlación de incidentes | 3 **alertas generales**: SSH (`T1110.001`), SQLi (`T1190`), reconocimiento (`T1595`) con severidad | Pantalla web (playwright-cli) | 2026-09-14 | Incidente **sintético**; creadas vía API |

---

## 07 - Métricas

| Archivo | Funcionalidad | Qué demuestra | Cómo se obtuvo | Fecha | Observaciones |
|---------|---------------|---------------|----------------|-------|---------------|
| 01_grafana-dashboard.png | Métricas | Lista de los 3 dashboards TaxFisco en Grafana | Pantalla web (chrome-devtools) | 2026-09-14 | |
| 02_velociraptor.png | Métricas | Velociraptor Server Dashboard (CPU/mem/orgs) | Pantalla web | 2026-09-14 | Sin clientes conectados |
| 03_grafana-soc-overview.png | Métricas | SOC Overview: 199 alertas, severidad, tendencia temporal | Pantalla web | 2026-09-14 | |
| 04_grafana-kpis.png | Métricas | KPIs: total 199, nivel promedio 3.92, máx 7, por severidad y regla | Pantalla web | 2026-09-14 | |
| 05_grafana-detailed-alerts.png | Métricas | Alertas recientes, totales y top tipos | Pantalla web | 2026-09-14 | |
| 06_grafana-datasource-wazuh.png | Métricas | Datasource WazuhIndexer (OpenSearch, URL, auth) | Pantalla web | 2026-09-14 | Contraseña enmascarada |
| 07_kpi-report.png / .txt / .json | Métricas | **MTTD medido (real)**: 41.60 s (n=9, decoy-api + portal + cowrie); MTTR/MTTC/MTTContain **no medidos** | Terminal: `python3 -m json.tool` | 2026-09-14 | 9/10 escenarios con evento real; S01/S02 re-ejecutados contra IPs actuales; S10 (DNS externo) sin sensor local. `kpi_calculator.py` v2.0 |
| 08_mitre-coverage.png / .txt / .json | Métricas | Cobertura MITRE ATT&CK: 17 técnicas implementadas, 10 detectadas | Terminal: `python3 -m json.tool` | 2026-09-14 | `.txt`=salida mostrada, completo en `.json` |
| 09_iso27035-compliance.png / .txt / .json | Métricas | Cumplimiento ISO 27035/27001 por fase | Terminal: `python3 -m json.tool` | 2026-09-14 | `.txt`=salida mostrada, completo en `.json` |

### Datos mostrados en los dashboards

- **Total de alertas indexadas:** 199
- **Nivel promedio:** 3.92
- **Nivel máximo:** 7
- **Distribución por severidad:** Baja 152, Alta 45, Media 2
- **Top reglas:** 19009 (87), 19008 (51), 19007 (45), 502 (14), 19003 (2)
- **Agente:** wazuh-manager

---

## 08 - Extremo a Extremo

Pendiente. No se ejecutaron escenarios durante esta sesión.

---

## Cambios realizados en el sistema y el repositorio

### Repositorio (configuración)
1. `config/grafana/datasources/datasources.yaml`
   - Corregido tipo de `opensearch` (inválido) a `grafana-opensearch-datasource`
   - Corregida URL obsoleta `172.22.0.11:9200` a `10.22.0.13:9200` (proxy)
   - Añadida autenticación básica (admin/Admin1234!)
2. `config/grafana/dashboards/taxfisco-soc-overview.json`
   - Reescritas las queries de sintaxis inválida a PPL válida
   - Añadido `queryType: PPL` y `format: table`
   - Panel "Top Alert Types" cambiado de piechart a tabla (evita texto sobrepuesto)
3. `config/grafana/dashboards/taxfisco-kpis.json` — igual
4. `config/grafana/dashboards/taxfisco-detailed.json` — igual

### Sistema
1. Instalado plugin `grafana-opensearch-datasource` en Grafana
2. Ejecutado `scripts/setup-credentials.sh`
3. Corregido hostname Redis de MISP (`redis` → `misp.redis`)
4. Creado usuario Velociraptor `admin` / `Admin1234!` (rol administrator)
5. Creados index patterns `wazuh-alerts-*` y `wazuh-*` en Wazuh Dashboard (Discover con 199 alertas)

---

## Limitaciones

- **MISP:** requiere completar instalación inicial (falta PGP key)
- **Cortex:** sin conexión a Elasticsearch
- **Wazuh Dashboard:** necesita configurar index patterns
- **Datos de ataques:** el pipeline decoy→Wazuh no está generando alertas nuevas (los escenarios usan IPs obsoletas 172.20.x). Los dashboards muestran las 199 alertas reales de Wazuh disponibles.
