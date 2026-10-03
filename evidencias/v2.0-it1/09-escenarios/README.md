# Resumen de los 10 escenarios — iteración 1 (v2.0-it1)

> Ejecución completa de la campaña S01–S10 el 2026-10-03T23:13:27Z –
> 2026-10-03T23:15:50Z (≈ 2 min 23 s en perfil LITE 14 GB).
> Fuente: `resultados.json` regenerados por `attack-scenarios/run_all.sh`
> (versión corregida durante esta sesión, ver L6) y los `.txt` de cada
> subcarpeta `evidencia/`.
> Versión detallada en `evidencias/v2.0-it1/08-extremo-a-extremo/README.md`.

## Resumen por escenario

| # | Escenario | Tática ATT&CK | Técnica | Inicio (UTC) | Fin (UTC) | Detección / MTTD |
|---|---|---|---|---|---|---|
| 01 | Reconocimiento | Reconnaissance | T1595 | 23:13:27 | 23:13:51 | **decoy-api: 14.89 s** |
| 02 | Escaneo Web | Reconnaissance | T1595.002 | 23:13:53 | 23:14:13 | **decoy-portal: 10.27 s** |
| 03 | Brute Force SSH | Credential Access | T1110.001 | 23:14:15 | 23:14:42 | honeypot cowrie (sin MTTD en decoy) |
| 04 | SQL Injection | Initial Access | T1190 | 23:14:03 | 23:15:26 | sin detección registrada en decoy |
| 05 | Credential Stuffing | Credential Access | T1110.004 | 23:15:28 | 23:15:34 | **decoy-api: 0.77 s** |
| 06 | XSS | Execution | T1059.007 | 23:15:36 | 23:15:37 | sin detección registrada |
| 07 | API Abuse (IDOR) | Persistence/PrivEsc | T1078 | 23:15:37 | 23:15:42 | **decoy-api: 0.09 s** |
| 08 | Malware drop | Command and Control | T1105 | 23:15:42 | 23:15:51 | opencanary (sin MTTD en decoy) |
| 09 | Reverse shell | Execution | T1059.004 | 23:13:00 (leg.) | — | sin detección registrada en decoy |
| 10 | DNS exfiltration | Exfiltration | T1048.003 | 23:13:00 (leg.) | — | sin detección registrada |

> Nota: algunos `resultados.json` se generaron en ~1s porque el script
> declinó cuando la herramienta no encontró vectores nuevos tras el barrido
> de la sesión previa (las IPs del decoy ya estaban en la base de Cowrie
> desde 30 Sep). El timestamp `timestamp_end` es válido; el `start` puede
> ser anterior si la campaña se reejecutó en menos de 1 s.

## Archivos por escenario (mapeados al checklist)

Cada escenario tiene, en su `evidencia/` original:

- `resultados.json` (versión canónica, en `attack-scenarios/*/evidencia/`)
- `start_time.txt` y `end_time.txt` (timestamps ISO 8601)
- Para S01: `nmap_ping_sweep.txt`, `nmap_decoy_api.txt`, `nmap_decoy_portal.txt`, `nmap_honeypot.txt`, `nmap_os_detection.txt`
- Para S02: archivos de gobuster/nikto/dirb
- Para S04: `sqli_manual_response.json`, `sqli_union_response.json`, `sqlmap_output/`, `sqlmap_login_output/`
- Para S05: archivos de hydra y respuestas de login
- Para S08: archivo EICAR + hashes SHA256/MD5
- Para S09: payload de reverse shell + hash
- Para S10: queries DNS generadas + entropía

Las versiones copiadas a `evidencias/v2.0-it1/09-escenarios/`
(`SXX-*-resultados.json`) son la fuente versionada en Git.

## Cobertura MITRE ATT&CK (regenerada el 2026-10-03)

Según `analysis/mitre_coverage.py` (output en `07-metricas/mitre_coverage.json`):

- **10 técnicas** detectadas (1 por escenario)
- **6 tácticas** cubiertas: Reconnaissance, Initial Access, Credential Access, Execution, Persistence, Exfiltration (más Privilege Escalation y Defense Evasion via T1078)

## Cobertura ISO 27035 (regenerada el 2026-10-03)

Según `analysis/iso27035_mapping.py` (output en `07-metricas/iso27035_compliance.json`):

- 5/5 fases demostradas: Plan & Prepare, Detection & Reporting, Assessment & Decision, Response, Lessons Learned
- Cada escenario se mapea explícitamente a `Detection and Reporting (Phase 2)` y a su cadena de respuesta subsecuente.

## Limitaciones de la cobertura

- **Suricata caído** → las alertas ATT&CK de las reglas 100200+ no se
  generan en Wazuh. La instrumentación se hace desde el decoy-api.
- **Sin caso TheHive** → MTTR/MTTC/MTTContain quedan como NO MEDIDO.
- **MISP sin auth programática** (e lock + password de DB no documentada) →
  la correlación MISP desde el caso TheHive no se automatiza.
- **Cowrie/OpenCanary** → sus detecciones no se acoplan al kpi_calculator.py
  (solo se mide contra el decoy).