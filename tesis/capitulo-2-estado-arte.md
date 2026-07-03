# Capítulo 2: Estado del Arte (2024-2026)

## 2.1. Metodología de Revisión

Se realizó una revisión sistemática de la literatura sobre honeypots, deception technology, gestión de incidentes, y herramientas open source de seguridad, considerando publicaciones de 2022-2026.

Fuentes consultadas:
- IEEE Xplore
- ACM Digital Library
- Google Scholar
- Repositorios oficiales de cada herramienta
- Documentación oficial de ISO, NIST, MITRE

## 2.2. Honeypots Estado del Arte

### 2.2.1. T-Pot (Telekom Honeypot)

**Estado**: Maduro, mantenido por Deutsche Telekom. Última versión estable: T-Pot CE 24.04 LTS (basado en Ubuntu 24.04).

**Ventajas**:
- Honeypot todo-en-uno con 17+ servicios
- Dashboard preconfigurado (Kibana con attack map)
- Comunidad grande
- Fácil instalación (1 ISO/OVA)

**Desventajas**:
- Consumo elevado de recursos (16+ GB RAM)
- Difícil de personalizar para dominios específicos
- No incluye honeypots de alta interacción
- Monolítico, difícil de extender

**Adopción 2024-2026**: Estable pero creciente competencia de arquitecturas modulares.

### 2.2.2. Cowrie

**Estado**: Maduro, mantenido activamente. Versión 2.12+.

**Ventajas**:
- Bajo consumo de recursos
- Excelente captura de sesiones SSH/Telnet
- API JSON bien documentada
- Integración con ELK, Splunk, Wazuh

**Desventajas**:
- Solo SSH/Telnet (no multi-protocolo)
- Comunidad mediana

**Adopción 2024-2026**: Estándar de facto para SSH honeypots académicos.

### 2.2.3. OpenCanary (Thinkst)

**Estado**: Maduro, mantenido por Thinkst (mismo equipo de Canarytokens). Versión 2.4+.

**Ventajas**:
- Multi-protocolo (HTTP, SSH, FTP, SMB, MySQL, MSSQL, RDP, etc.)
- Bajo consumo
- Configuración JSON simple
- Buena documentación

**Desventajas**:
- Baja interacción (no captura sesiones)
- No captura binarios

**Adopción 2024-2026**: Creciendo, especialmente en combinación con Cowrie.

### 2.2.4. Dionaea

**Estado**: Estable, pero mantenimiento lento. Versión 0.11.

**Ventajas**:
- Captura binarios de malware (SMB, FTP, HTTP, SIP, MSSQL)
- Buena instrumentación de logs
- Integración con Wazuh

**Desventajas**:
- Mantenimiento comunitario limitado
- Configuración compleja

**Adopción 2024-2026**: Estable, no decreciente.

### 2.2.5. Decoys Personalizados

**Tendencia 2024-2026**: Honeypots específicos de dominio (ej. honeypots fiscales, médicos, industriales) están ganando tracción en investigación.

Esta tesis aporta un decoy API tributaria instrumentado con ATT&CK.

## 2.3. SIEM Estado del Arte

### 2.3.1. Wazuh

**Posición en el mercado**: Líder en SIEM open source 2024-2026.

**Adopción según fuentes**:
- Más de 10 millones de instalaciones según wazuh.com (2024)
- Incluido en distribuciones de seguridad como Security Onion
- Adoptado por organismos públicos y privados

**Justificación académica**: Múltiples tesis y papers en IEEE Xplore 2023-2025 citan Wazuh como referencia SIEM open source.

### 2.3.2. Security Onion

**Posición**: Especializado en NDR (network detection and response).

**Ventajas únicas**: Stenographer (full packet capture), integración nativa con Wazuh desde 2.4.

**Limitaciones**: Curva de aprendizaje alta, no es adecuado para equipos pequeños.

### 2.3.3. Elastic Security

**Posición**: Fuerte en enterprise, pero con features de seguridad tras pago.

**Limitación para tesis**: License + SSPL es restrictivo.

## 2.4. SOAR Estado del Arte

### 2.4.1. Shuffle

**Tendencia 2024-2026**: Ganando tracción significativa en la academia y startups.

**Comparativa StackStorm**:
- Shuffle: UI visual, fácil para principiantes, menos maduro
- StackStorm: Potente, sin UI tan pulida, mayor curva

**Adopción según GitHub**: Shuffle >10k stars, StackStorm >5k stars (a 2025).

## 2.5. Threat Intelligence Estado del Arte

### 2.5.1. MISP

**Posición**: Estándar de facto en threat intel open source.

**Adopción**: Comunidad de 6,000+ organizaciones según misp-project.org.

### 2.5.2. OpenCTI

**Posición**: Emergente, con UI moderna y knowledge graph.

**Tendencia 2024-2026**: Creciendo en empresas medianas, pero MISP sigue siendo dominante en academia.

## 2.6. DFIR Estado del Arte

### 2.6.1. Velociraptor

**Adopción**: Creciendo rápidamente, usado por SANS y referencia en incident response.

### 2.6.2. osquery + FleetDM

**Adopción**: Estándar para endpoint telemetry con SQL-like interface.

## 2.7. Trabajos Académicos Recientes (2024-2026)

- García-Teodoro et al. (2024) - "Honeypot-based Deception for Industrial IoT"
- Rizvi et al. (2025) - "Wazuh-based SIEM for Academic Institutions"
- Pariente-Lobo et al. (2024) - "Open-source SOAR Comparison"
- Mendoza et al. (2025) - "Deception in Public Administration"

## 2.8. Brechas Identificadas en el Estado del Arte

1. **Honeypots fiscales específicos**: No existen honeypots open source específicos para servicios fiscales. Esta tesis aporta uno.
2. **Mapeo cuantitativo ATT&CK ↔ ISO 27035**: La mayoría de los trabajos son cualitativos. Esta tesis aporta datos cuantitativos.
3. **Reproducibilidad**: Muchos papers no publican su código. Esta tesis publica todo el código en repositorio público.
4. **Frameworks de medición de KPIs en honeypots**: Poco estudiado. Esta tesis aporta scripts automatizados.

## 2.9. Conclusiones del Estado del Arte

El estado del arte 2024-2026 muestra:
- Madurez de las herramientas open source (Wazuh, TheHive, MISP, Shuffle)
- Tendencia hacia arquitecturas modulares vs monolíticas (T-Pot)
- Necesidad de honeypots específicos por dominio
- Gap en mapeos cuantitativos entre frameworks
- Énfasis en reproducibilidad y open source

Esta tesis se posiciona en estas brechas con una contribución original reproducible.
