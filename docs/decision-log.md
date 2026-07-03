# Decision Log - Registro de Decisiones Arquitectónicas

Este documento registra las decisiones clave tomadas durante el diseño
del laboratorio, con justificación basada en el análisis del estado del arte
2024-2026.

## Decisiones del Diseño

### DEC-001: Wazuh como SIEM (vs Elastic Security, Security Onion)

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de un SIEM open source para HIDS, FIM, correlación y compliance.

**Opciones consideradas**:
1. Wazuh 4.9
2. Elastic Security 8.x
3. Security Onion 2.4
4. OpenSearch Security

**Decisión**: Wazuh 4.9 con indexer propio (OpenSearch).

**Justificación**:
- Cumplimiento out-of-the-box para ISO 27001, NIST 800-53, PCI DSS, GDPR, HIPAA
- Mapeo nativo a MITRE ATT&CK
- Open source sin límite de eventos (vs Elastic License con features pagas)
- Mayor adopción académica 2024-2026

**Consecuencias**:
- (+) Compliance demostrable
- (-) Mayor complejidad de configuración que Elastic

---

### DEC-002: Docker Compose en lugar de Kubernetes

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Tesis de 3-4 meses en host con 16 GB de RAM + 8 GB de swap.

**Opciones consideradas**:
1. Docker Compose con redes bridge
2. Docker Swarm
3. k3s (Kubernetes ligero)
4. K8s multi-node

**Decisión**: Docker Compose.

**Justificación**:
- Curva de aprendizaje mínima
- Reproducible en 30 minutos
- Cabe en 16 GB de RAM (con swap) de workstations académicas estándar
- K8s single-node consume >1 GB solo del control plane

**Consecuencias**:
- (+) Velocidad de despliegue
- (-) Sin alta disponibilidad nativa
- (-) Sin NetworkPolicy de K8s

---

### DEC-003: TheHive + Cortex como IRP

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de gestión de incidentes con análisis de observables.

**Opciones consideradas**:
1. TheHive 5 + Cortex 3
2. Solo TheHive
3. ServiceNow (comercial)
4. RTIR (Request Tracker for Incident Response)

**Decisión**: TheHive 5 + Cortex 3.

**Justificación**:
- Estándar de facto en academia 2024-2026
- Cortex provee 50+ analyzers
- Integración nativa con MISP
- Open source

**Consecuencias**:
- (+) Análisis de observables automatizado
- (-) Dos servicios que mantener (TheHive + Elasticsearch)

---

### DEC-004: Shuffle como SOAR

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de orquestación de respuestas a incidentes.

**Opciones consideradas**:
1. Shuffle 1.4+
2. StackStorm
3. n8n (low-code general)
4. Apache Airflow (data pipeline)

**Decisión**: Shuffle 1.4+.

**Justificación**:
- UI visual intuitiva (ideal para defensa de tesis)
- 300+ integraciones pre-construidas
- Open source y mantenido activamente
- StackStorm es más maduro pero con curva mucho mayor

**Consecuencias**:
- (+) Workflows visuales fáciles de demostrar
- (-) Menos maduro para enterprise

---

### DEC-005: MISP como plataforma de Threat Intelligence

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de gestionar IOCs y correlacionar con threat intel.

**Opciones consideradas**:
1. MISP 2.4
2. OpenCTI 6
3. AlienVault OSSIM (deprecado)
4. Solo feeds sin plataforma (TAXII/STIX directo)

**Decisión**: MISP 2.4.

**Justificación**:
- Mayor comunidad y feeds públicos
- Integración nativa con Wazuh, TheHive, Cortex
- Galaxies pre-pobladas con ATT&CK

**Consecuencias**:
- (+) Ecosistema rico
- (-) UI menos moderna que OpenCTI (knowledge graph)

---

### DEC-006: Cowrie + Dionaea + OpenCanary (vs T-Pot CE)

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Honeypots para SSH, SMB, HTTP, FTP.

**Opciones consideradas**:
1. T-Pot CE 24.04 (todo-en-uno)
2. Cowrie + Dionaea + OpenCanary por separado
3. Solo Cowrie
4. Solo OpenCanary

**Decisión**: Cowrie + Dionaea + OpenCanary + Heralding por separado.

**Justificación**:
- T-Pot consume >16 GB RAM solo
- Permite instrumentación específica por honeypot
- Permite customización de logs para Wazuh
- Modular y más mantenible

**Consecuencias**:
- (+) Menos consumo de RAM
- (+) Personalización completa
- (-) Sin dashboard pre-hecho (T-Pot tiene Kibana con attack map)
- (-) Hay que configurar cada honeypot individualmente

---

### DEC-007: Decoy API custom en FastAPI

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de una API específica del dominio fiscal.

**Opciones consideradas**:
1. FastAPI custom (esta tesis)
2. Adaptar T-Pot existentes
3. Usar OpenAPI Honeypot genérico

**Decisión**: FastAPI custom con instrumentación ATT&CK.

**Justificación**:
- Contribución original de la tesis
- Cobertura específica de TTPs fiscales
- Permite añadir endpoints que no existen en honeypots genéricos
- Publicable como artefacto

**Consecuencias**:
- (+) Contribución académica
- (-) Trabajo de desarrollo adicional

---

### DEC-008: Decoy Portal custom en Django

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Portal web vulnerable para atraer atacantes.

**Opciones consideradas**:
1. Django custom con vulns intencionales (esta tesis)
2. WordPress vulnerable preconfigurado
3. DVWA (Damn Vulnerable Web App)
4. bWAPP

**Decisión**: Django custom con vulnerabilidades documentadas.

**Justificación**:
- Coherencia con la API (mismo stack FastAPI/Django)
- Vulnerabilidades documentadas con flag académico
- Permite instrumentación específica

---

### DEC-009: Suricata 7.0 como NIDS (vs Snort 3)

**Fecha**: 2024-12
**Estado**: Aceptada

**Contexto**: Necesidad de NIDS de alto rendimiento.

**Opciones consideradas**:
1. Suricata 7.0
2. Snort 3
3. Solo Zeek (sin signature-based NIDS)

**Decisión**: Suricata 7.0 + Zeek 6.0.

**Justificación**:
- Suricata es multi-thread (Snort es single-thread principal)
- EVE JSON output es mejor para SIEM
- Emerging Threats es más maduro que Talos para OSS
- Snort 3 es mantenido por Cisco (Talos propietario)

**Consecuencias**:
- (+) Mejor performance
- (-) Más complejo de configurar

---

### DEC-010: Proxmox descartado

**Fecha**: 2024-12
**Estado**: Aceptada (descartado)

**Contexto**: Necesidad de hipervisor para el host.

**Decisión**: NO usar Proxmox. Usar Ubuntu 24.04 nativo con Docker.

**Justificación**:
- Single host: Proxmox agrega overhead sin beneficio
- Docker nativo ya provee segmentación
- Reduce consumo de RAM

---

### DEC-011: Sin Active Directory

**Fecha**: 2024-12
**Estado**: Aceptada (no implementado)

**Contexto**: Necesidad de demostrar lateral movement y AD attacks.

**Decisión**: NO incluir AD. Escenario queda como línea futura.

**Justificación**:
- AD requiere Samba AD DC + OpenGraphiti + al menos 2 Windows VMs
- Consumiría >8 GB RAM adicional
- El alcance se centra en servicios web/API, no en endpoints internos

---

## Resumen de Decisiones

| ID | Decisión | Estado |
|---|---|---|
| DEC-001 | Wazuh 4.9 como SIEM | Aceptada |
| DEC-002 | Docker Compose | Aceptada |
| DEC-003 | TheHive + Cortex | Aceptada |
| DEC-004 | Shuffle SOAR | Aceptada |
| DEC-005 | MISP Threat Intel | Aceptada |
| DEC-006 | Honeypots individuales (no T-Pot) | Aceptada |
| DEC-007 | Decoy API FastAPI custom | Aceptada |
| DEC-008 | Decoy Portal Django custom | Aceptada |
| DEC-009 | Suricata + Zeek (no Snort) | Aceptada |
| DEC-010 | Sin Proxmox | Aceptada |
| DEC-011 | Sin AD | Aceptada (línea futura) |
