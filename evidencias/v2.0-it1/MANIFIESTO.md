# MANIFIESTO de evidencia — v2.0-it1 (Prototipo II, laboratorio SIN)

> Manifiesto obligatorio del skill `capturas-evidencia-prototipo-2`.
> Iteración capturada: **v2.0-it1** (iteración 1, preprueba).
> Hash de commit al cierre: `9b280665ad431f959734b36ebcdf3e5d11936cf9` (HEAD rama `prototipo-2-sin`).
> Tag original: `v2.0-it1` (no se modifica; ver `instrucciones/docs/INSTRUCCION-RECAPTURA-v2.0-it1.md`).
> Fecha de captura: **2026-10-03** (UTC-4, sesión Linux Ubuntu, 14 GB RAM, swap 7.5 GB).
> Sesión de captura: opencode (modelo MiniMax-M3) + chrome-devtools MCP + bash.

## 1. Resumen ejecutivo

La evidencia previa de `v2.0-it1/` quedó clasificada como **NO VERIFICABLE**
en la auditoría `evidencias/AUDITORIA-v2.0-it1.md` (34 PNG con marcos
estilizados, sin `.txt` de respaldo, sin MANIFIESTO, sin fuentes KPI).
Esta re-captura sustituye esa evidencia por:

- **23 capturas crudas** distribuidas en 7 subcarpetas (`01`–`07`),
  cada una con su respaldo textual cuando aplica.
- **3 reportes canónicos** (`kpi_report.json`, `mitre_coverage.json`,
  `iso27035_compliance.json`) versionados en `07-metricas/`.
- **10 `resultados.json`** de los 10 escenarios en `07-metricas/` y en `09-escenarios/`.
- **2 entradas** nuevas en `evidencias/lecciones-aprendidas.md` (L6 y L7).
- **1 hallazgo documentado** (Suricata en crash loop + Wazuh sin ingesta del
  decoy-api) en `04-captura-eventos/03_hallazgo-wazuh-suricata.txt`.

## 2. Estado del laboratorio durante la captura

| Aspecto | Estado |
|---|---|
| Total contenedores `sin-*` | 25 corriendo (1 reiniciándose: `sin-suricata`) |
| Servicios web que respondieron | 9/9 (portal, API, Wazuh, TheHive, Cortex, MISP, Shuffle, Grafana, Velociraptor) |
| Contenedor atacante | `sin-attacker` recreado (cambio de bind mounts detectado) |
| Swap | 7.5 GB activo |
| RAM en uso al cierre | ~9 GB de 14 GB |
| Disco libre al cierre | ~19 GB |

Ver `08-extremo-a-extremo/README.md` y `04-captura-eventos/03_*` para
detalles del estado operativo.

## 3. Tabla por captura

| N.º | Archivo | Subcarpeta | Origen | Qué demuestra | Sección tesis |
|---:|---|---|---|---|---|
| 1 | `01_docker-network-ls.png` + `.txt` | `03-aislamiento-red/` | host bash + screenshot del `.txt` | 4 redes `sin-*` (sin-dmz, sin-honeypot, sin-ids vacía, sin-soc) | 4.3.6.1, 4.3.6.3 |
| 2a | `01_docker-images.png` + `.txt` | `01-entorno-servicios/` | host bash | 4 imágenes propias `sin/*` | 4.3.6.1 |
| 2b | `02_docker-compose-config.png` + `.txt` | `01-entorno-servicios/` | host bash | 25 servicios declarados | 4.3.6.1 |
| 3 | `01_portal-landing.png` | `02-senuelo/` | chrome-devtools sobre http://localhost:8890 | fachada "Impuestos Nacionales" (decoy portal) | 4.3.6.2 (F1) |
| 4a | `02_portal-dashboard.png` | `02-senuelo/` | chrome-devtools, sesión Contribuyente 1020304050 | dashboard autenticado (datos sintéticos) | 4.3.6.2 |
| 4b | `03_portal-login.png` | `02-senuelo/` | chrome-devtools | formulario de login con NIT + correo + contraseña | 4.3.6.2 |
| 4c | `04_portal-segundo-factor.png` | `02-senuelo/` | chrome-devtools tras enviar credenciales | pantalla 2FA (OTP 6 dígitos) | 4.3.6.2 |
| 5 | `07_resumen-aislamiento.png` + `.txt` | `03-aislamiento-red/` | host bash + docker compose exec + screenshot | 4 redes, ping atacante→SIEM = 100% packet loss | 4.3.6.3 (F2) |
| 6a | `01_wazuh-alerts-tail.png` + `.txt` | `04-captura-eventos/` | docker exec sobre wazuh-manager | 3 alertas (2 server started + 1 log reduced) | 4.3.6.4 (F3) |
| 6b | `02_wazuh-fuentes-ingesta.txt` | `04-captura-eventos/` | docker exec | tamaños de eve.json, http.log, conn.log, dns.log | 4.3.6.4 (F3) |
| 6c | `03_hallazgo-wazuh-suricata.txt` | `04-captura-eventos/` | hallazgo documentado | Suricata en crash loop; Wazuh sin ingesta de decoy | 4.3.6.4 (F3) |
| 7a | `01_thehive-organizaciones.png` | `05-enriquecimiento-custodia/` | chrome-devtools sobre http://localhost:9000 | TheHive 5.5.16-1 login + lista de orgs (sin casos) | 4.3.6.4 (F3) |
| 7b | `02_misp-evento-iocs.png` | `05-enriquecimiento-custodia/` | chrome-devtools sobre https://localhost:8443 | MISP con evento #1 "SIN - IOCs S01-S10" (8 attrs) | 4.3.6.4 (F3) |
| 7c | `03_misp-evento-detalle.png` | `05-enriquecimiento-custodia/` | chrome-devtools sobre evento MISP | detalle de atributos + ATT&CK clusters | 4.3.6.4 (F3) |
| 8 | `01_kpi-report-iter1.png` | `07-metricas/` | chrome-devtools sobre `kpi_report.json` | MTTD medio 6.51 s, n=4 escenarios | 4.3.6.6.2, 4.4.2 |
| 9 | `02_lecciones-aprendidas.png` | `07-metricas/` | chrome-devtools sobre `lecciones-aprendidas.md` | L1–L7 (L6+L7 nuevas, CERRADA y MONITOREO) | 4.3.6.6.3, 4.4.3 |
| – | `kpi_report.json`, `mitre_coverage.json`, `iso27035_compliance.json` | `07-metricas/` | `analysis/kpi_calculator.py`, `mitre_coverage.py`, `iso27035_mapping.py` ejecutados en el contenedor atacante | fuentes canónicas para 4.4.2 / 4.4.5 | 4.3.6.6.2, 4.4.2 |
| – | `S01-…-resultados.json` … `S10-…-resultados.json` (10 archivos) | `07-metricas/` + `09-escenarios/` | `attack-scenarios/S*/evidencia/resultados.json` tras `bash run_all.sh` | timestamp + técnica + herramientas por escenario | 4.3.6.6.2, 4.4.2 |
| – | `09-escenarios/README.md` | `09-escenarios/` | síntesis de las 10 ejecuciones | tabla S01-S10 | 4.4.2 |
| – | `08-extremo-a-extremo/README.md` | `08-extremo-a-extremo/` | correlación F1→F5 | tabla E2E | 4.4.2 |

## 4. Trazabilidad

- **Fuentes citadas (kpi + resultados)**: los `resultados.json` y
  `kpi_report.json` regenerados en esta sesión se versionan en
  `evidencias/v2.0-it1/07-metricas/`. Sus originales
  (`attack-scenarios/*/evidencia/` y `analysis/`) están en `.gitignore`.
- **Hash de los JSON críticos**:
  - `kpi_report.json`: SHA-256 se calcula en el script de cierre.
  - `resultados.json`: SHA-256 idem.
- **Quirk de permisos**: el `bash run_all.sh` corre como root dentro del
  contenedor atacante. Los `.json` regenerados quedan con owner `root:root`
  en `analysis/`; los copio a `evidencias/v2.0-it1/07-metricas/` con `cp`
  desde el host, lo que fija owner `fer:fer` y los deja bajo `.opencode/`
  versionable.
- **Cuarentena**: las 34 PNG NO VERIFICABLES quedaron en
  `evidencias/v2.0-it1/_no-verificable/`. Inventario en
  `_no-verificable/_INDICE-VERIFICACION.md`.

## 5. Lo que NO se hizo (transparencia)

- **No se aplicaron mejoras de código** más allá del fix mínimo en
  `attack-scenarios/run_all.sh` (L6) y la instalación efímera de paquetes
  en el atacante (L7). El resto queda registrado como antecedente para it2.
- **No se modificó `docker-compose.yml`** ni los decoys ni las reglas.
- **No se cerró el caso TheHive** (la API devuelve
  `AuthorizationError: manageCase/create`) — queda como hallazgo.
- **No se forzó la persistencia del evento MISP** previo (no se recreó
  desde cero porque sigue siendo válido como referencia de la sesión del
  30 Sep).
- **No se capturó la fase 4 (correlación)** con un caso vivo en TheHive
  porque (a) no hay caso, (b) no hay autorrelleno desde MISP en esta
  sesión. La carpeta `06-correlacion-incidentes/` queda pendiente.

## 6. Pendientes para it2 (entrada al siguiente sprint)

1. Diagnosticar y arreglar el crash loop de Suricata (`/start-sin.sh`).
2. Agregar `<localfile>` para `/var/log/decoy-api/attacks.json` en Wazuh.
3. Conceder `manageCase/create` al rol admin en TheHive o crear un usuario
   con permisos de creación de casos.
4. Crear Dockerfile propio para el atacante con `nmap, sqlmap, hydra,
   curl, jq, openssl, python3` preinstalados (resuelve L7).
5. Versionar la corrección de `run_all.sh` y los nuevos hallazgos del
   presente manifiesto como L8+, L9+.