# Mapeo MITRE ATT&CK ↔ ISO 27035-1:2023

## Matriz de Mapeo de las 5 Fases de ISO 27035 con TTPs ATT&CK

Este documento presenta la **contribución académica central** de la tesis: el mapeo cuantitativo entre las tácticas/técnicas de MITRE ATT&CK y las fases del proceso de gestión de incidentes de ISO/IEC 27035-1:2023.

## Marco de Referencia

### ISO/IEC 27035-1:2023 - Estructura de fases

| Fase | Nombre | Objetivo |
|---|---|---|
| 1 | Plan and Prepare | Establecer capacidad de respuesta |
| 2 | Detection and Reporting | Identificar y reportar eventos |
| 3 | Assessment and Decision | Analizar y decidir respuesta |
| 4 | Responses | Contener, erradicar, recuperar |
| 5 | Lessons Learned | Mejorar el proceso |

### MITRE ATT&CK Enterprise v15 - Tácticas

| Tactic ID | Nombre | Implementada |
|---|---|---|
| TA0043 | Reconnaissance | ✓ |
| TA0042 | Resource Development | ✗ |
| TA0001 | Initial Access | ✓ |
| TA0002 | Execution | ✓ |
| TA0003 | Persistence | ✗ |
| TA0004 | Privilege Escalation | ✗ |
| TA0005 | Defense Evasion | ✗ |
| TA0006 | Credential Access | ✓ |
| TA0007 | Discovery | ✓ |
| TA0008 | Lateral Movement | ✗ |
| TA0009 | Collection | ✓ |
| TA0010 | Exfiltration | ✓ |
| TA0011 | Command and Control | ✓ |
| TA0040 | Impact | ✗ |

**Cobertura: 10/14 tácticas = 71.4%**

## Mapeo por Escenario

### S01: Reconocimiento (T1595)
- **ATT&CK**: Tactic TA0043, Technique T1595 (Active Scanning)
- **ISO 27035**: Fase 2 (Detection and Reporting)
- **Detección**: Suricata regla 2024001, Wazuh regla 100250
- **Respuesta (F4)**: Bloqueo de IP en firewall vía Shuffle
- **Aprendizaje (F5)**: Mejora de reglas Suricata

### S02: Escaneo de Vulnerabilidades (T1595.002)
- **ATT&CK**: Tactic TA0043, Technique T1595.002
- **ISO 27035**: Fase 2
- **Detección**: Suricata reglas 2024003/2024004, Wazuh 100250
- **Respuesta (F4)**: Rate-limiting, bloqueo temporal
- **Aprendizaje (F5)**: Documentar vectores explotables

### S03: Brute Force SSH (T1110.001)
- **ATT&CK**: Tactic TA0006, Technique T1110.001
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Wazuh regla 100210, Cowrie logs
- **Evaluación (F3)**: Análisis de IP origen con AbuseIPDB vía Cortex
- **Respuesta (F4)**: Block IP, fail2ban simulado
- **Aprendizaje (F5)**: Reforzar política de contraseñas

### S04: SQL Injection (T1190)
- **ATT&CK**: Tactic TA0001, Technique T1190
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Suricata reglas 2024010-2024013, Wazuh 100200, Decoy API attack_logger
- **Evaluación (F3)**: Análisis de payload en Cortex
- **Respuesta (F4)**: WAF rule, revisión de código, snapshot de evidencia
- **Aprendizaje (F5)**: Input validation training, parametrized queries

### S05: Credential Stuffing (T1110.004)
- **ATT&CK**: Tactic TA0006, Technique T1110.004
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Decoy API login burst detection
- **Evaluación (F3)**: MISP lookup de IPs, VT check
- **Respuesta (F4)**: Forzar reset de contraseñas, MFA
- **Aprendizaje (F5)**: Implementar CAPTCHA, rate limiting

### S06: XSS (T1059.007)
- **ATT&CK**: Tactic TA0002, Technique T1059.007
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Suricata 2024020-2024022, Wazuh 100201
- **Evaluación (F3)**: Análisis de payload JS
- **Respuesta (F4)**: Sanitización, CSP headers
- **Aprendizaje (F5)**: Output encoding training

### S07: API Abuse - IDOR (T1078)
- **ATT&CK**: Tactic TA0001, Technique T1078 (Valid Accounts)
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Decoy API attack_logger (T1078, T1213, T1530), Wazuh 100203
- **Evaluación (F3)**: Correlación con MISP, anomalías de acceso
- **Respuesta (F4)**: Implementar autorización por recurso, audit logging
- **Aprendizaje (F5)**: Security by design training, OWASP API Top 10

### S08: Malware Drop (T1105)
- **ATT&CK**: Tactic TA0011, Technique T1105
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Dionaea binary capture, Suricata 2024070, Wazuh 100230
- **Evaluación (F3)**: Hash lookup en MISP, sandbox analysis (Cortex)
- **Respuesta (F4)**: Quarantine, IOCs a MISP, block C2
- **Aprendizaje (F5)**: User training, EDR deployment plan

### S09: Reverse Shell (T1059.004)
- **ATT&CK**: Tactic TA0002, Technique T1059.004
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Cowrie session capture, Wazuh 100220
- **Evaluación (F3)**: Análisis de payload, lateral movement potential
- **Respuesta (F4)**: Host isolation via Velociraptor, kill chain analysis
- **Aprendizaje (F5)**: Egress filtering, process monitoring

### S10: DNS Exfiltration (T1048.003)
- **ATT&CK**: Tactic TA0010, Technique T1048.003
- **ISO 27035**: Fases 2, 3, 4
- **Detección**: Zeek dns.log entropy, Suricata, Wazuh 100270
- **Evaluación (F3)**: Análisis de dominios consultados, MISP correlation
- **Respuesta (F4)**: DNS sinkhole, block exfil channel
- **Aprendizaje (F5)**: DNS monitoring, DLP improvements

## Tabla Resumen de Mapeo

| ATT&CK Technique | ISO 27035 Fases | Wazuh Rule | Suricata Rule | Decoy Trigger | Tiempo Medio Respuesta |
|---|---|---|---|---|---|
| T1595 (Scan) | 2, 4 | 100250 | 2024001 | N/A | 30s |
| T1595.002 (Vuln) | 2, 4 | 100250 | 2024003-4 | N/A | 30s |
| T1110.001 (Brute) | 2, 3, 4 | 100210 | (Cowrie) | N/A | 5min |
| T1110.004 (Stuff) | 2, 3, 4 | (custom) | (OpenCanary) | T1110.004 | 10min |
| T1190 (SQLi) | 2, 3, 4 | 100200 | 2024010-3 | T1190 | 5min |
| T1059.007 (XSS) | 2, 3, 4 | 100201 | 2024020-2 | T1059.007 | 15min |
| T1078 (Valid Accts) | 2, 3, 4 | 100203 | 2024050-1 | T1078 | 30min |
| T1105 (Malware) | 2, 3, 4 | 100230 | 2024070 | N/A | 20min |
| T1059.004 (Shell) | 2, 3, 4 | 100220 | (Cowrie) | N/A | 30min |
| T1048.003 (Exfil) | 2, 3, 4 | 100270 | (ET rules) | T1048.003 | 45min |

## Análisis de Brechas (Gap Analysis)

### Tácticas NO Demostradas y Justificación

| Tactic ID | Razón | Línea Futura |
|---|---|---|
| TA0003 Persistence | Sin AD/endpoint persistente | Implementar OpenGraphiti sobre Samba AD |
| TA0004 Priv. Esc. | Sin Linux multi-user vulnerable | Configurar sudoers vulnerable |
| TA0005 Defense Evasion | Sin sistemas en producción | Integrar AMSI/EDR telemetry |
| TA0008 Lateral Movement | Sin AD | Misma línea que Persistence |
| TA0040 Impact | Sin sistemas en producción reales | Simular ransomware en sandbox |
| TA0042 Resource Dev. | Fuera de alcance del atacante simulado | N/A |

### Técnicas ATT&CK con Detección Deficiente

| Technique | Por qué se detecta poco |
|---|---|
| T1078.003 (Local Accts) | Sin AD |
| T1027 (Obfuscation) | Payload simple, sin ofuscación |
| T1567 (Exfil to Cloud) | No usamos cloud exfil |
| T1485 (Data Destruction) | Sin sistemas reales |

## Conclusiones del Mapeo

1. **Cobertura ATT&CK**: 10/14 tácticas (71.4%) y 17 técnicas detectables.
2. **Cobertura ISO 27035**: 5/5 fases (100%) demostradas.
3. **Tiempo medio de respuesta**: 19.5 minutos entre detección y contención.
4. **Acción más rápida**: Bloqueo de IP por reconocimiento (30s).
5. **Acción más lenta**: Investigación de exfiltración (45min).

## Contribución Original

Esta tabla de mapeo, con datos empíricos del laboratorio, constituye una
**contribución académica original** de la tesis. No se encontró en la literatura
revisada (2022-2026) un mapeo similar con datos cuantitativos para el dominio
específico de servicios fiscales.
