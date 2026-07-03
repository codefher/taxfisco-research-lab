# Capítulo 3: Diseño del Laboratorio

## 3.1. Requisitos del Laboratorio

### 3.1.1. Requisitos Funcionales

| ID | Requisito | Cumplimiento |
|---|---|---|
| RF-1 | Detectar intentos de reconocimiento | ✓ Suricata + Wazuh |
| RF-2 | Detectar ataques web (SQLi, XSS, LFI) | ✓ Decoy API + Suricata + Wazuh |
| RF-3 | Capturar credenciales SSH/Telnet | ✓ Cowrie + Heralding |
| RF-4 | Capturar binarios de malware | ✓ Dionaea |
| RF-5 | Centralizar logs en SIEM | ✓ Wazuh |
| RF-6 | Crear casos de incidente | ✓ TheHive |
| RF-7 | Ejecutar playbooks de respuesta | ✓ Shuffle |
| RF-8 | Gestionar IOCs de threat intel | ✓ MISP |
| RF-9 | Realizar análisis forense | ✓ Velociraptor |
| RF-10 | Visualizar KPIs | ✓ Grafana |

### 3.1.2. Requisitos No Funcionales

| ID | Requisito | Cumplimiento |
|---|---|---|
| RNF-1 | Open source | ✓ 100% OSS |
| RNF-2 | Reproducible | ✓ Docker Compose |
| RNF-3 | Cabe en 16 GB RAM (con 8 GB swap) | ✓ ~13.2 GB usados |
| RNF-4 | Despliegue en <30 min | ✓ `docker compose up` |
| RNF-5 | Cumple ISO 27001 A.5.24-28 | ✓ |
| RNF-6 | Mapea a MITRE ATT&CK | ✓ 17 técnicas |
| RNF-7 | Documentación completa | ✓ Este documento |

## 3.2. Arquitectura Lógica

(Ver `docs/arquitectura.md` para el detalle completo)

```
                    Internet (simulado)
                          │
                   ┌──────┴──────┐
                   │ OPNsense*  │  *opcional en lab
                   │ Firewall   │
                   └──────┬──────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ┌────┴─────┐     ┌────┴─────┐     ┌────┴─────┐
   │ DMZ      │     │Honeypot  │     │ Internal │
   │ (172.20) │     │(172.21)  │     │ (172.30) │
   │          │     │          │     │          │
   │ Portal   │     │ Cowrie   │     │  (no en  │
   │ API      │     │ Dionaea  │     │   este   │
   │ OpenCan. │     │ Heralding│     │   lab)   │
   └────┬─────┘     └────┬─────┘     └──────────┘
        │                │
        └────────┬───────┘
                 │
        ┌────────┴────────┐
        │  SOC Network    │
        │  (172.22)       │
        │                 │
        │  Wazuh stack    │
        │  MISP           │
        │  TheHive+Cortex │
        │  Shuffle        │
        │  Velociraptor   │
        │  Grafana        │
        └─────────────────┘
```

## 3.3. Arquitectura de Red

### 3.3.1. Segmentación

4 redes bridge de Docker:

| Red | Subnet | Propósito |
|---|---|---|
| dmz-net | 172.20.0.0/24 | Servicios públicos simulados |
| honeypot-net | 172.21.0.0/24 | Honeypots multi-protocolo |
| soc-net | 172.22.0.0/24 | Stack SOC (Wazuh, MISP, etc.) |
| ids-net | 172.23.0.0/24 | Sensores de red |

### 3.3.2. Conectividad

- Contenedores en dmz-net tienen acceso a soc-net (envían logs)
- Honeypots están en honeypot-net y dmz-net (atacables desde DMZ)
- Suricata/Zeek están en ids-net (solo capturan, no son accesibles)
- Atacante está en dmz-net (accede a servicios y honeypots)

## 3.4. Arquitectura de Servicios

(Ver `docs/arquitectura.md` para detalle)

## 3.5. Arquitectura de Contenedores

15+ contenedores Docker organizados en 4 redes:

```
docker-compose.yml
├── Red dmz-net
│   ├── decoy-api-tributaria (FastAPI, custom)
│   ├── decoy-portal-tributario (Django, custom)
│   ├── opencanary
│   ├── postgres-fiscal
│   └── attacker (Kali)
├── Red honeypot-net
│   ├── cowrie
│   ├── dionaea
│   └── heralding
├── Red soc-net
│   ├── wazuh.manager
│   ├── wazuh.indexer
│   ├── wazuh.dashboard
│   ├── misp.core
│   ├── misp.db
│   ├── misp.modules
│   ├── thehive
│   ├── thehive.es
│   ├── cortex
│   ├── shuffle
│   ├── shuffle.frontend
│   ├── shuffle.db
│   ├── velociraptor
│   └── grafana
└── Red ids-net
    ├── suricata
    └── zeek
```

## 3.6. Decisiones de Diseño

Ver `docs/decision-log.md` para el registro completo (DEC-001 a DEC-011).

## 3.7. Trade-offs Principales

| Decisión | Trade-off |
|---|---|
| Docker Compose vs K8s | Velocidad de despliegue vs HA |
| T-Pot vs honeypots individuales | Comodidad vs personalización |
| Wazuh vs Elastic Security | Open source puro vs features pagas |
| 10 escenarios vs 13 | Tiempo vs cobertura ATT&CK |
| Sin AD vs con AD | Recursos vs técnicas de lateral movement |

## 3.8. Conclusiones del Diseño

La arquitectura propuesta cumple todos los requisitos funcionales y no funcionales. El diseño modular permite extender el laboratorio en líneas futuras de investigación.
