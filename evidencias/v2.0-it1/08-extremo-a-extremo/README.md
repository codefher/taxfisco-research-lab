# Cadena de custodia extremo a extremo — iteración 1 (v2.0-it1)

> Trazabilidad de la cadena F1 → F5 para los 10 escenarios de la campaña
> S01–S10 ejecutada el 2026-10-03T23:13Z sobre el laboratorio SIN Research Lab.

## Tabla de correlación escenario → detección → custodia → KPI

| Escenario | TTPs | Detección (origen) | Custodia (almacén) | MTTD medido |
|---|---|---|---|---|
| S01-reconocimiento | T1595 (Active Scanning) | decoy-api (attacker) | /var/log/decoy-api/attacks.json + all_requests.jsonl | **14.89 s** |
| S02-escaneo-web    | T1595.002 (Vuln Scanning) | decoy-portal | /var/log/decoy-api/attacks.json + /var/log/suricata/eve.json (legacy) | **10.27 s** |
| S03-bruteforce-ssh | T1110.001 (Password Guessing) | honeypot cowrie | cowrie logs + zeek conn.log | sin detección en decoy (ataca honeypot) |
| S04-sql-injection  | T1190 (Exploit Public-Facing App) | decoy-portal (login + buscar) | /var/log/decoy-api/attacks.json | sin detección registrada (instrumentación MTTD no alineada con timestamps) |
| S05-credential-stuffing | T1110.004 (Credential Stuffing) | decoy-api (/api/v1/auth/login) | /var/log/decoy-api/attacks.json | **0.77 s** |
| S06-xss            | T1059.007 (JavaScript) | decoy-portal | /var/log/decoy-api/attacks.json | sin detección registrada |
| S07-api-abuse (IDOR) | T1078 (Valid Accounts) | decoy-api (admin endpoints) | /var/log/decoy-api/attacks.json | **0.09 s** |
| S08-malware-drop   | T1105 (Ingress Tool Transfer) | opencanary (SMB/FTP/HTTP honeypot) | opencanary logs + zeek http.log | sin detección en decoy (ataca honeypot) |
| S09-reverse-shell  | T1059.004 (Unix Shell) | cowrie | cowrie logs + decoy-portal request log | sin detección registrada |
| S10-exfiltracion-dns | T1048.003 (Exfil Over C2 Channel) | decoy-api (DNS queries) | zeek dns.log | sin detección registrada |

## Cadena F1 → F5 (resumen narrativo)

### F1. Diseño del señuelo SIN
- Decoy API (FastAPI): 10.20.0.20:8000, expone endpoints REST con TTPs instrumentadas (T1190, T1059.007, T1078, T1110.004, T1530)
- Decoy Portal (Django): 10.20.0.21:8000, fachada "Impuestos Nacionales" con 2FA, OWASP top 10 vulns
- Honeypots: Cowrie (SSH/Telnet), OpenCanary (HTTP/FTP/SMB/MSSQL/RDP), Heralding (multi-protocolo)
- Configuración en `decoys/api-tributaria/main.py` + `decoys/portal-tributario/portal/`
- Capturas: `02-senuelo/01-04` (portal landing, dashboard, login, 2FA)

### F2. Despliegue aislado
- 4 redes bridge: `sin-dmz` (10.20.0/24), `sin-honeypot` (10.21.0/24), `sin-ids` (vacía), `sin-soc` (10.22.0/24)
- IDS (Suricata/Zeek) en `network_mode: host` para sniffing del bridge sin-dmz
- Segmentación validada: 100% packet loss desde atacante (10.20.0.99) hacia SIEM (10.22.0.10/30)
- Capturas: `03-aislamiento-red/01-07`

### F3. Captura, enriquecimiento y custodia
- **Detección primaria**: Decoy API instrumentada → 264 ataques, 1455 requests (logs en /var/log/decoy-api/)
- **Detección secundaria**: Honeypots (29 conexiones Cowrie) + Zeek (49 MB conn.log, 692 KB http.log)
- **Suricata caído**: 139 MB eve.json de la sesión anterior pero contenedor en restart loop (no procesa tráfico nuevo)
- **MISP**: 1 evento previo (ID 1) con 8 atributos IOCs + 4 ATT&CK clusters (T1078, T1105, T1190, T1595), tags `tlp:amber` y `sin:escenarios:S01-S10`. API key no documentada en sesión actual (MISP_DB_ROOT_PASSWORD no accesible desde host)
- **TheHive**: 0 casos en esta sesión (permisos `manageCase/create` no concedidos a `admin@thehive.local`); caso de la sesión anterior (`7dd41df`) tampoco persistió tras los reinicios
- **Wazuh Manager**: 3 alertas (2x `Wazuh server started` + 1x `Log file size reduced`). 0 alertas de las reglas 100200-100299 del SIN porque Wazuh no ingesta `/var/log/decoy-api/attacks.json` (solo suricata/zeek según `config/wazuh/entrypoint/10-sin-localfiles.sh`)
- Capturas: `04-captura-eventos/01-03` (Wazuh), `05-enriquecimiento-custodia/01-03` (TheHive + MISP)

### F4. Correlación con gestión de incidentes
- Flujo TheHive + Cortex + MISP **no se ejecutó automáticamente** en esta sesión:
  - El contenedor Cortex responde (200/303) pero no hay jobs ni analizadores invocados
  - El analizador MISP_2_1 documentado en `7dd41df` requiere caso pre-existente y observabilidad
  - Sin caso TheHive durante esta campaña, la cadena se interrumpe en F3 → F4
- Captura: `06-correlacion-incidentes/` queda pendiente (no hay correlación que mostrar)

### F5. Medición y lecciones aprendidas
- KPIs medidos (MTTD): S01 14.89 s, S02 10.27 s, S05 0.77 s, S07 0.09 s → media **6.51 s** (n=4)
- MTTR/MTTC/MTTContain: NO MEDIDO (TheHive sin casos → no hay timestamps de triage/cierre/contención)
- 4 lecciones cerradas (L1-L5) de la sesión previa + 2 nuevas detectadas en esta re-captura:
  - **L6 (CERRADA)**: bug de paths en `attack-scenarios/run_all.sh`
  - **L7 (MONITOREO)**: imagen Kali sin `curl/jq/openssl/python3` por defecto
- Captura: `07-metricas/` + lecciones en `evidencias/lecciones-aprendidas.md`

## Hallazgos relevantes para el siguiente sprint (entrada a it2)

1. **Suricata en crash loop** impide que las alertas ATT&CK (reglas 100200+) se disparen en Wazuh. La causa raíz está en `/start-sin.sh` del entrypoint; no se aborda en esta re-captura.
2. **Wazuh no ingiere `/var/log/decoy-api/attacks.json`**. Esto explica por qué el MTTD se calcula fuera del SIEM central. Acción para it2: añadir el localfile correspondiente.
3. **TheHive sin permisos** para crear casos vía API (`manageCase/create`). Acción para it2: revisar la config del rol `admin` o crear un usuario con `orgAdmin`.
4. **Kali sin herramientas básicas** (`curl`, `jq`, `openssl`, `python3`). Acción para it2: Dockerfile propio con `RUN apt-get install`.
5. **Bug de paths en `run_all.sh`** que impedía la ejecución completa. Acción para it2: limpieza de la inicialización de paths.