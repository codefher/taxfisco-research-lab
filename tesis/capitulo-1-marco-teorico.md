# Capítulo 1: Marco Teórico

## 1.1. Introducción

La gestión de incidentes de seguridad es un proceso crítico para cualquier organización que maneja información sensible. En el contexto de los servicios fiscales, donde se procesan millones de declaraciones juradas y datos personales de contribuyentes, la capacidad de detectar, analizar y responder a incidentes de seguridad es fundamental para preservar la integridad, confidencialidad y disponibilidad de los datos.

## 1.2. Honeypots y Sistemas de Engaño

### 1.2.1. Definición y Taxonomía

Un honeypot es un recurso de seguridad cuyo valor reside en ser sondeado, atacado o comprometido. Según Spitzner (2003), los honeypots se clasifican según su nivel de interacción:

- **Baja interacción**: Simulan servicios parcialmente. Fáciles de desplegar, bajo riesgo, detección limitada.
- **Media interacción**: Simulan servicios más complejos, capturan más información.
- **Alta interacción**: Replican sistemas completos. Mayor información pero mayor riesgo.

### 1.2.2. Honeytokens

Concepto introducido por Spitzner (2003) y formalizado por otros autores, son artefactos señuelo (credenciales, archivos, URLs) que permiten detectar accesos no autorizados sin necesidad de sistemas completos.

### 1.2.3. Cyber Deception

Evolución moderna del concepto de honeypot. Según Fraunholz et al. (2018), el cyber deception utiliza tácticas engañosas para manipular las percepciones del atacante, retrasándolo y exponiendo sus TTPs.

## 1.3. Normas Internacionales Aplicables

### 1.3.1. ISO/IEC 27001:2022

Estándar internacional para Sistemas de Gestión de Seguridad de la Información (SGSI). Los controles del Anexo A relevantes para gestión de incidentes son:

- A.5.24: Information security incident management planning
- A.5.25: Assessment and decision on information security events
- A.5.26: Response to information security incidents
- A.5.27: Learning from information security incidents
- A.5.28: Collection of evidence

### 1.3.2. ISO/IEC 27035-1:2023 e ISO/IEC 27035-2:2023

Estándar específico para la gestión de incidentes. Define un proceso en 5 fases:
1. Plan and Prepare
2. Detection and Reporting
3. Assessment and Decision
4. Responses
5. Lessons Learned

Reemplaza la versión 2011 (27035-1) e introduce cambios significativos:
- Integración con ISO 27001:2022
- Énfasis en la preparación
- Inclusión de la fase de lessons learned como central

### 1.3.3. NIST SP 800-61 Rev.3 (Febrero 2024)

Guía del NIST para manejo de incidentes. La Rev.3 introduce un cambio fundamental: reemplaza las 4 fases tradicionales por una **función unificada "Respond"** dentro del NIST Cybersecurity Framework 2.0.

Categorías:
- Preparation
- Detection & Analysis
- Containment, Eradication & Recovery
- Post-Incident Activity

### 1.3.4. NIST Cybersecurity Framework 2.0

Publicado en febrero de 2024. Las 6 funciones:
- **GOVERN** (nueva en 2.0)
- IDENTIFY
- PROTECT
- DETECT
- RESPOND
- RECOVER

### 1.3.5. MITRE ATT&CK

Matriz de tácticas y técnicas adversariales. Versión actual (v15) incluye 14 tácticas y más de 200 técnicas. Es el estándar de facto para clasificar TTPs de atacantes.

## 1.4. Estado del Arte en SIEM Open Source

### 1.4.1. Wazuh

Plataforma de seguridad open source que combina SIEM, HIDS, FIM, vulnerability detection y compliance. Basado en OSSEC, ha ganado enorme tracción desde 2018.

### 1.4.2. Security Onion

Distribución de seguridad todo-en-uno que incluye Suricata, Zeek, Wazuh, Elasticsearch, Kibana, Stenographer. Mantenido por Doug Burks.

### 1.4.3. Elastic Security

Versión de seguridad del Elastic Stack. Tiene features gratuitas y de pago (License + SSPL).

## 1.5. Estado del Arte en SOAR

### 1.5.1. Shuffle

SOAR open source con UI web, escrito en Go. Integraciones con 300+ herramientas.

### 1.5.2. StackStorm

Orquestador de eventos open source. Más maduro pero con curva de aprendizaje mayor.

## 1.6. Trabajos Relacionados

- Provos y Holz (2007) - Virtual Honeypots
- Spitzner (2003) - Honeypots: Tracking Hackers
- Fraunholz et al. (2018) - "Demystifying Deception Technology"
- Fan et al. (2017) - "HoneyMix: Toward SDN-based Intelligent Honeynet"
- Wang et al. (2020) - "A Survey on Deception Technology"

## 1.7. Conclusiones del Marco Teórico

La combinación de honeypots + SIEM + SOAR + cumplimiento normativo es un área de investigación activa con aplicaciones prácticas en organizaciones modernas. Esta tesis aporta al estado del arte con una implementación open source completa, reproducible, y validada con datos empíricos.
