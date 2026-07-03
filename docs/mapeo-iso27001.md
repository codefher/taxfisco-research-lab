# Mapeo ISO 27001:2022 - Annex A Controls

Este documento mapea los controles del Anexo A de ISO/IEC 27001:2022 relevantes a la gestión de incidentes, tal como se implementan en el laboratorio TaxFisco Research Lab.

## Controles Implementados (7/7 relevantes)

### A.5.24 - Information security incident management planning

**Objetivo del control**: La organización debe planificar y preparar la gestión de incidentes de seguridad de la información.

**Implementación en el laboratorio**:
- Shuffle con workflows predefinidos para cada tipo de incidente
- TheHive con plantillas de caso (case templates) por tipo de evento
- Wazuh con reglas de correlación que disparan alertas automáticamente
- Runbook de respuesta documentado en `docs/playbooks/`

**Evidencia objetiva**:
- Workflows de Shuffle exportados en `config/shuffle/workflows/`
- Casos de prueba en TheHive por cada escenario ejecutado
- Reglas Wazuh en `config/wazuh/rules/100200-taxfisco-attack-rules.xml`

**Cumplimiento**: ✓ Implementado completamente

---

### A.5.25 - Assessment and decision on information security events

**Objetivo del control**: La organización debe evaluar los eventos de seguridad y decidir si clasifican como incidentes.

**Implementación en el laboratorio**:
- TheHive permite asignar severidad (1-4) a cada alerta
- Cortex ejecuta analyzers sobre observables (VirusTotal, AbuseIPDB, MISP, etc.)
- MISP permite correlacionar IOCs con bases de threat intel
- Reglas Wazuh con niveles 6-14 que categorizan automáticamente

**Evidencia objetiva**:
- 30+ analyzers de Cortex disponibles
- Dashboards Wazuh con vista de "Alerts by Severity"
- MISP events con galaxies ATT&CK

**Cumplimiento**: ✓ Implementado completamente

---

### A.5.26 - Response to information security incidents

**Objetivo del control**: La organización debe responder a incidentes de acuerdo con lo planificado.

**Implementación en el laboratorio**:
- Shuffle ejecuta acciones automáticas (block IP, isolate host, notify)
- Velociraptor permite respuesta forense rápida (VQL queries)
- Wazuh active response puede ejecutar comandos predefinidos
- MISP publishing para distribución de IOCs

**Evidencia objetiva**:
- Workflows Shuffle: `webhook-wazuh-enrichment-create-case.json`
- VQL hunts en Velociraptor
- Reglas Wazuh active-response en `config/wazuh/active-response/`

**Cumplimiento**: ✓ Implementado completamente

---

### A.5.27 - Learning from information security incidents

**Objetivo del control**: La organización debe aprender de los incidentes y mejorar la respuesta.

**Implementación en el laboratorio**:
- TheHive case closure con análisis post-mortem
- Grafana dashboards históricos para análisis de tendencias
- MISP feedback: IOCs de incidentes se suben a MISP
- Scripts de análisis en `analysis/` (kpi_calculator.py, mitre_coverage.py)

**Evidencia objetiva**:
- Reportes `kpi_report.json` generados por análisis
- `mitre_coverage.json` con tendencias de cobertura
- Casos cerrados en TheHive con tareas post-incidente

**Cumplimiento**: ✓ Implementado completamente

---

### A.5.28 - Collection of evidence

**Objetivo del control**: La organización debe establecer procedimientos para la收集, almacenamiento y presentación de evidencia.

**Implementación en el laboratorio**:
- Logs centralizados en Wazuh Indexer con retención
- Archivos de evidencia por escenario con SHA-256 hashes
- Cadena de custodia documentada en `attack-scenarios/*/evidencia/`
- Backup de logs en volúmenes Docker persistentes

**Evidencia objetiva**:
- Archivos `*_hash.txt` en cada escenario
- Volúmenes Docker declarados en `docker-compose.yml`
- Logs firmados con GPG en producción (no habilitado en lab por simplicidad)

**Cumplimiento**: ✓ Implementado con simplificación (sin GPG obligatorio en lab)

---

### A.8.16 - Monitoring activities

**Objetivo del control**: Las redes, sistemas y aplicaciones deben ser monitoreados para detectar eventos de seguridad.

**Implementación en el laboratorio**:
- Wazuh HIDS en todos los contenedores del SOC
- Wazuh FIM detecta cambios en archivos críticos
- Suricata NIDS monitorea tráfico entre segmentos
- Zeek NDR analiza metadata de protocolos
- Honeypots capturan todo acceso no autorizado

**Evidencia objetiva**:
- Wazuh Dashboard con vistas de compliance
- Suricata EVE logs en `config/suricata/`
- Zeek logs en `config/zeek/`
- Honeypot logs: Cowrie, Dionaea, OpenCanary, Heralding

**Cumplimiento**: ✓ Implementado completamente

---

### A.8.20 - Networks security

**Objetivo del control**: Las redes y los servicios deben ser asegurados y monitoreados.

**Implementación en el laboratorio**:
- Segmentación en 4 redes bridge (dmz, honeypot, soc, ids)
- Suricata con reglas custom para TTPs ATT&CK
- Network policies via iptables del host (recomendado en producción)
- Honeypots exponen servicios señuelo mientras los reales están en otra red

**Evidencia objetiva**:
- `docker-compose.yml` con networks declarados
- Reglas Suricata en `config/suricata/rules/`
- Traffic mirroring via iptables (configuración documentada)

**Cumplimiento**: ✓ Implementado completamente

---

## Tabla Resumen de Cumplimiento

| Control | Estado | Evidencia Principal |
|---|---|---|
| A.5.24 Incident planning | ✓ | Shuffle workflows, TheHive templates |
| A.5.25 Assessment & decision | ✓ | Cortex analyzers, MISP correlation |
| A.5.26 Incident response | ✓ | Shuffle playbooks, Velociraptor |
| A.5.27 Lessons learned | ✓ | KPI analysis, MISP feedback |
| A.5.28 Evidence collection | ✓ | Hash SHA-256, logs centralizados |
| A.8.16 Monitoring | ✓ | Wazuh + Suricata + Zeek + honeypots |
| A.8.20 Network security | ✓ | Segmentación + IDS + honeypots |

**Cobertura total: 7/7 controles relevantes = 100%**

## Controles Adicionales (No Implementados - Justificación)

| Control | Razón de No Implementación |
|---|---|
| A.5.26 (full BIA) | Business Impact Analysis formal fuera de alcance |
| A.5.30 (BCP) | Plan de continuidad de negocio fuera de alcance |
| A.8.24 (Cryptography) | No es relevante para honeypots de engagement |
| A.8.32 (Change mgmt) | Cambios gestionados vía IaC, no formalmente |

## Mapeo a Estándares Complementarios

### NIST CSF 2.0 (Feb 2024)

| Función CSF | Controles ISO 27001 que la Cumplen |
|---|---|
| **GOVERN** (nueva) | A.5.24 (planning) |
| **IDENTIFY** | A.5.25, A.5.9 (no implementado) |
| **PROTECT** | A.8.20, A.8.16 |
| **DETECT** | A.8.16, A.5.25 |
| **RESPOND** | A.5.24, A.5.25, A.5.26, A.5.27 |
| **RECOVER** | A.5.27, A.5.28 |

### NIST SP 800-61 Rev.3 (Feb 2024)

| Categoría 800-61 | Controles ISO 27001 |
|---|---|
| Preparation | A.5.24, A.5.25, A.8.16, A.8.20 |
| Detection & Analysis | A.5.25, A.8.16 |
| Containment, Eradication, Recovery | A.5.26 |
| Post-Incident Activity | A.5.27, A.5.28 |

### MITRE ATT&CK (Matriz)

Ver `docs/mapeo-iso27035.md` para el mapeo detallado ATT&CK ↔ ISO 27035.
