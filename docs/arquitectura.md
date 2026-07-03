# Arquitectura del Laboratorio TaxFisco Research Lab

## Resumen Ejecutivo

El laboratorio TaxFisco Research Lab es una plataforma integrada de **Detección, Engaño, Monitoreo y Respuesta a Incidentes** que simula un ente tributario genérico con fines de investigación de tesis de maestría. La arquitectura se diseñó siguiendo los principios de **reproducibilidad académica**, **modularidad**, **alineación con estándares abiertos** (ISO 27001, ISO 27035, NIST 800-61, NIST CSF 2.0, MITRE ATT&CK) y **uso exclusivo de software open source**.

## Restricciones del Diseño

| Restricción | Solución adoptada |
|---|---|
| Single-host (16 GB RAM + 8 GB swap) | Contenedores Docker con segmentación por redes bridge |
| Tesis de maestría (3-4 meses) | Stack preconfigurado, despliegue en <30 minutos |
| Open source estricto | Todas las herramientas bajo licencias OSS permisivas |
| Reproducibilidad | IaC vía Docker Compose, datos sintéticos versionados |
| Defensa académica | Contribución original (decoy API/Portal instrumentados con ATT&CK) |

## Arquitectura Lógica

```
┌────────────────────────────────────────────────────────────────────────┐
│                    TAXFISCO RESEARCH LAB (Single Host)                  │
│                                                                          │
│  ┌─────────────────────────┐  ┌──────────────────────────────────────┐│
│  │  Red: dmz-net           │  │  Red: honeypot-net                   ││
│  │  172.20.0.0/24          │  │  172.21.0.0/24                       ││
│  │                         │  │                                       ││
│  │  ├ decoy-api (0.20)     │  │  ├ cowrie (0.10) [SSH/Telnet]        ││
│  │  ├ decoy-portal (0.21)  │  │  ├ dionaea (0.11) [SMB/FTP/HTTP]     ││
│  │  ├ opencanary (0.52)    │  │  └ heralding (0.13) [creds]          ││
│  │  ├ postgres-fiscal      │  │                                       ││
│  │  └ attacker (0.99)      │  │                                       ││
│  └─────────────────────────┘  └──────────────────────────────────────┘│
│                                                                          │
│  ┌─────────────────────────┐  ┌──────────────────────────────────────┐│
│  │  Red: soc-net           │  │  Red: ids-net                        ││
│  │  172.22.0.0/24          │  │  172.23.0.0/24                       ││
│  │                         │  │                                       ││
│  │  ├ wazuh-manager        │  │  ├ suricata (NIDS)                    ││
│  │  ├ wazuh-indexer        │  │  └ zeek (NDR)                         ││
│  │  ├ wazuh-dashboard      │  │                                       ││
│  │  ├ misp-core            │  └──────────────────────────────────────┘│
│  │  ├ misp-db              │                                           │
│  │  ├ thehive              │                                           │
│  │  ├ cortex               │                                           │
│  │  ├ shuffle              │                                           │
│  │  ├ velociraptor         │                                           │
│  │  ├ grafana              │                                           │
│  │  └ decoy-api/portal     │                                           │
│  │     (mirror)            │                                           │
│  └─────────────────────────┘                                           │
└────────────────────────────────────────────────────────────────────────┘
```

## Arquitectura de Servicios

### Capa de Engaño (Honeypots y Decoys)

| Servicio | Tecnología | Puerto | Función |
|---|---|---|---|
| Cowrie | SSH/Telnet honeypot | 2222/2323 | Captura credenciales y sesiones |
| Dionaea | Multi-protocolo malware | 445/21/1433 | Captura binarios de malware |
| OpenCanary | Multi-protocolo Thinkst | 80/21/22/etc | Honeypot de baja interacción |
| Heralding | Credential capture | 23/1080/554 | Captura de credenciales |
| Decoy API (custom) | FastAPI Python | 8000 | API tributaria ficticia instrumentada con ATT&CK |
| Decoy Portal (custom) | Django Python | 8000 | Portal web vulnerable controlado |

### Capa de Detección (IDS/NDR)

| Servicio | Tecnología | Función |
|---|---|---|
| Suricata 7.0 | NIDS multi-thread | Detección basada en firmas, Emerging Threats |
| Zeek 6.0 | NDR | Análisis de metadata de red, file extraction |

### Capa de SIEM

| Servicio | Tecnología | Función |
|---|---|---|
| Wazuh Manager 4.9 | SIEM | HIDS, FIM, correlación, compliance |
| Wazuh Indexer 4.9 | OpenSearch | Indexado de eventos |
| Wazuh Dashboard 4.9 | Kibana fork | Visualización SOC |

### Capa de Respuesta (SOAR + IRP)

| Servicio | Tecnología | Función |
|---|---|---|
| Shuffle 1.4+ | SOAR | Orquestación y automatización de playbooks |
| TheHive 5.5 | Case management | Gestión de incidentes, casos |
| Cortex 3.4 | Observable analysis | Analyzers (VT, AbuseIPDB, MISP) |
| Velociraptor 0.7+ | DFIR | Endpoint forensics, VQL queries |

### Capa de Inteligencia de Amenazas

| Servicio | Tecnología | Función |
|---|---|---|
| MISP 2.4 | Threat Intelligence | IOCs, galaxies ATT&CK, taxonomía |

### Capa de Visualización

| Servicio | Tecnología | Función |
|---|---|---|
| Grafana 11 | Dashboards | KPIs, métricas, MISP stats |
| Wazuh Dashboard | SIEM UI | Eventos SOC, ATT&CK heatmap |

## Arquitectura de Datos

```
Honeypots/Decoys ──┐
Suricata/Zeek ─────┼─► Wazuh Manager ─► Wazuh Indexer ─► Wazuh Dashboard
                   │            │
                   │            ├──► Shuffle SOAR ──► TheHive (caso)
                   │            │                  ├──► Cortex (analyze)
                   │            │                  └──► MISP (IOC)
                   │            │
                   │            └──► Grafana (KPIs)
                   │
                   └──► Velociraptor (forense)
```

## Decisiones Arquitectónicas Clave

### ADR-001: Por qué Docker Compose en lugar de Kubernetes

**Contexto**: La tesis debe ejecutarse en un host con 16 GB de RAM + 8 GB de swap en 3-4 meses.

**Decisión**: Usar Docker Compose con segmentación por redes bridge.

**Consecuencias**:
- (+) Despliegue en 30 minutos con `docker compose up`
- (+) Reproducible entre máquinas
- (+) Sin curva de aprendizaje de K8s
- (-) No hay orquestación nativa de alta disponibilidad
- (-) Limitaciones de red (no NetworkPolicies de K8s)

**Justificación académica**: Documentado en `docs/limitaciones.md` como single-host single-tenant.

### ADR-002: Por qué Wazuh como SIEM

**Contexto**: Necesidad de HIDS + FIM + correlación + compliance.

**Decisión**: Wazuh 4.9 con indexer propio (OpenSearch).

**Consecuencias**:
- (+) Compliance ISO 27001/PCI/NIST out-of-the-box
- (+) Mapeo nativo a MITRE ATT&CK
- (+) Open source sin límite de eventos
- (-) Algo más complejo de configurar que Elastic Security

**Justificación**: Wazuh es el SIEM OSS dominante en la academia 2024-2026, con más de 10 millones de instalaciones.

### ADR-003: Por qué TheHive + Cortex en lugar de solo TheHive

**Contexto**: Se necesita gestión de casos + análisis de observables.

**Decisión**: TheHive 5.5 como IRP + Cortex 3.4 para analyzers.

**Consecuencias**:
- (+) 50+ analyzers pre-construidos (VT, AbuseIPDB, MISP, Shodan, etc.)
- (-) 2 servicios que mantener

**Justificación**: La integración es estándar de facto en entornos académicos OSS.

### ADR-004: Por qué Shuffle en lugar de StackStorm

**Contexto**: Necesidad de SOAR visual y fácil de demostrar.

**Decisión**: Shuffle 1.4+.

**Consecuencias**:
- (+) UI web intuitiva, ideal para defensa de tesis
- (+) 300+ integraciones listas
- (-) Menos maduro que StackStorm para enterprise

**Justificación**: Shuffle es el SOAR OSS de preferencia académica 2024-2026, con documentación y comunidad activas.

## Despliegue y Operación

### Requisitos

- Ubuntu 24.04 LTS (o Debian 12) en host con 16 GB RAM + 8 GB de swap
- Docker 26+ y Docker Compose v2
- 100 GB de espacio en disco
- Conexión a Internet para descarga inicial de imágenes

### Inicio rápido

```bash
# 1. Clonar
git clone <repo> taxfisco-research-lab && cd taxfisco-research-lab

# 2. Configurar
cp .env.example .env && nano .env

# 3. Desplegar
docker compose up -d

# 4. Verificar
docker compose ps
```

### Acceso a servicios

Ver `README.md` sección "Acceso a los servicios".

## Limitaciones Documentadas

1. **Sin alta disponibilidad**: Cualquier caída del host afecta a todo el lab
2. **Sin Active Directory**: Excluido por restricción de recursos; queda como línea futura
3. **Sin captura de paquetes full-packet**: Suricata logs JSON pero no PCAP completo
4. **VLAN única**: Segmentación por redes bridge, no por VLANs físicas
5. **Datos sintéticos**: Los datos fiscales son ficticios, no válidos para análisis legal

## Referencias Bibliográficas

Ver `tesis/bibliografia.bib` para las referencias completas del marco teórico.
