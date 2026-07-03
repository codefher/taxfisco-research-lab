# Limitaciones del Laboratorio TaxFisco

Este documento enumera las limitaciones reconocidas de la arquitectura single-host,
así como las justificaciones académicas para cada decisión que las causó.

## Limitaciones Arquitectónicas

### L-1: Single Host, Sin Alta Disponibilidad

**Descripción**: Todo el laboratorio corre en una sola máquina física. Si el host cae, todos los servicios caen simultáneamente.

**Impacto en la tesis**: Limitado. La tesis demuestra capacidades de detección y respuesta en condiciones controladas, no en producción 24/7.

**Mitigación**: 
- Snapshots periódicos de Proxmox
- Backups automatizados de volúmenes Docker
- Documentación de RTO/RPO en el capítulo de respuesta a incidentes

**Línea futura**: Migrar la arquitectura a 2-3 nodos con replicación de Wazuh Indexer y PostgreSQL.

### L-2: Sin Active Directory

**Descripción**: El laboratorio no incluye un dominio AD/Windows. Esto excluye escenarios de Kerberoasting, Pass-the-Hash, Golden Ticket, etc.

**Impacto**: 4-5 técnicas ATT&CK del tactic "Lateral Movement" no se demuestran.

**Justificación**: 
- AD requiere Samba AD DC + OpenGraphiti + al menos 2 Windows VMs → consumiría >8 GB RAM adicional
- Complejidad operativa elevada para un período de 3-4 meses
- El alcance de la tesis se centra en servicios fiscales (web/API), no en endpoints internos Windows

**Línea futura**: Implementar con Samba 4.19+ y OpenGraphiti en una segunda fase.

### L-3: Sin Kubernetes

**Descripción**: No se usa K8s para orquestación, solo Docker Compose.

**Impacto**: 
- No se demuestran ataques específicos a clusters (kubelet API, etcd exfil)
- No se valida la portabilidad cloud-native del lab

**Justificación**:
- K8s single-node (k3s) consume >1 GB RAM solo del control plane
- K8s multi-node requiere 3+ hosts (escenario fuera de alcance)
- El thesis no se centra en cloud-native threats

### L-4: Redes Bridge en lugar de VLANs Físicas

**Descripción**: La segmentación se hace con redes bridge de Docker, no con VLANs reales en switches.

**Impacto**: 
- No se demuestra el uso de 802.1Q
- El tráfico entre "segmentos" no se puede inspeccionar en el nivel del switch

**Justificación**: En un single-host esto es lo más cercano a VLANs reales posible. El host Linux puede usar `veth` pairs para simular, pero no aporta valor demostrable para la tesis.

### L-5: Sin PCAP Completo

**Descripción**: Suricata emite logs en formato EVE JSON pero no se capturan los paquetes completos.

**Impacto**: Análisis forense de red limitado (no se puede hacer "follow the stream" en Wireshark).

**Mitigación**: Los logs JSON de Suricata + Zeek proveen metadata suficiente para análisis forense en la mayoría de los escenarios.

**Línea futura**: Integrar Stenographer (de Security Onion) o tcpdump persistente.

## Limitaciones de Datos

### L-6: Datos Sintéticos

**Descripción**: Los datos fiscales en PostgreSQL son ficticios (NITs inventados, no válidos para uso real).

**Impacto**: El laboratorio no se puede usar para análisis fiscal real.

**Justificación**: Uso de datos reales implicaría riesgos legales y de privacidad. Es práctica estándar en investigación de seguridad usar datos sintéticos o anonimizados.

**Dataset**: 10 contribuyentes, 5 declaraciones, 5 facturas - volumen bajo intencionalmente para enfocarse en la instrumentación de detección.

## Limitaciones de Cobertura ATT&CK

### L-7: 10 de 14 Tácticas Cubiertas

**Tácticas NO cubiertas**:
- TA0042 Resource Development (TTPs de preparación, ej. comprar dominio)
- TA0003 Persistence (cron, scheduled tasks en Windows)
- TA0004 Privilege Escalation (UAC bypass, sudo abuse)
- TA0011 Impact (ransomware, defacement, DoS)

**Justificación**: Estas tácticas requieren:
- Persistence: AD o un endpoint persistente
- Privilege Escalation: Linux multi-user con sudoers vulnerable
- Impact: Sistemas en producción reales

**Cobertura lograda**: 10/14 = 71.4% de las tácticas ATT&CK Enterprise.

## Limitaciones de Herramientas

### L-8: Velociraptor Sin Agentes

**Descripción**: Velociraptor Server está desplegado pero los agentes deben instalarse manualmente en endpoints (atacante, decoys).

**Impacto**: Las hunts VQL pre-construidas solo aplican al propio server container, no a los endpoints.

**Mitigación**: Los scripts de ataque ejecutan las acciones en el contenedor "attacker" y los eventos quedan en logs centralizados.

### L-9: MISP Sin Feeds Externos

**Descripción**: MISP se inicia con datos seed pero no se suscribe a feeds externos (CIRCL, AlienVault OTX, etc.).

**Impacto**: La base de IOCs de MISP es limitada.

**Mitigación**: Los escenarios generan IOCs propios que se suben automáticamente a MISP.

**Línea futura**: Integrar feeds MISP-STIX via PyMISP.

## Limitaciones de Tiempo

### L-10: Escenarios Reducidos vs. Plan Original

**Plan original**: 13 escenarios.
**Implementados**: 10 escenarios.

**Excluidos por tiempo/alcance**:
- S11: Lateral Movement (requiere AD)
- S12: Persistence (requiere AD o Linux multi-user persistente)
- S13: DoS / Impact (sin sistemas en producción)

## Resumen

El laboratorio cubre el **alcance mínimo defendible** para una tesis de maestría
en 3-4 meses con 16 GB RAM + 8 GB de swap. Las limitaciones están **explícitamente documentadas**
en la tesis, no son debilidades no reconocidas. Cada limitación es una **línea futura
de investigación** claramente identificada.
