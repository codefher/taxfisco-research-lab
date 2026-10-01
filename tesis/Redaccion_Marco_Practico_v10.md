**UNIVERSIDAD MAYOR DE SAN ANDRÉS**

**FACULTAD DE CIENCIAS PURAS Y NATURALES**

**POSTGRADO EN INFORMÁTICA**

**MAESTRÍA INFORMÁTICA FORENSE, SEGURIDAD DE LA INFORMACIÓN Y AUDITORÍA INFORMÁTICA**

Sexta Versión, Gestión 2023-2025

*[ Inserte aquí el logo UMSA: alto 8 cm × ancho 3.5 cm, colores aprobados por la Resolución ]*

**PRE-DEFENSA DE TESIS**

**“METODOLOGÍA HONEYPOT PARA LA GESTIÓN DE INCIDENTES EN SERVICIOS FISCALES CONFORME A NORMAS INTERNACIONALES”**

**POR: LIC. FERNANDO MENDOZA ESCOBAR**

**TUTOR: MSC. ELIZABETH PATRICIA POMMIER GALLO**

La Paz – Bolivia

Octubre, 2026

# Dedicatoria

*[Escriba su dedicatoria. Puede ser breve y personal. Ej.: A mi familia, por su apoyo incondicional durante este proceso de formación.]*

# Agradecimientos

*[Agradezca a quienes contribuyeron a su investigación: tutor/a, docentes del Postgrado en Informática, colegas, instituciones y familia.]*

# Resumen

*[El resumen debe tener entre 150 y 250 palabras. Incluya: (a) el problema investigado, (b) la metodología empleada (propositiva o demostrativa), (c) los hallazgos o resultados principales y (d) las conclusiones. No incluya citas en el resumen.]*

**Palabras clave:** *[palabra1, palabra2, palabra3, palabra4, palabra5]*

# Índice

[Dedicatoria ii](#_Toc240296729)

[Agradecimientos iii](#_Toc240296730)

[Resumen iv](#_Toc240296731)

[Índice v](#_Toc240296732)

[Índice de Tablas, Cuadros y Gráficos ix](#_Toc240296733)

[Introducción 1](#_Toc240296734)

[Capítulo I: Aspectos Generales 2](#_Toc240296735)

[1.1 Antecedentes 2](#_Toc240296736)

[1.2 Planteamiento del Problema 3](#_Toc240296737)

[1.2.1 Formulación del Problema de Investigación 4](#_Toc240296738)

[1.3 Objetivo General y Específicos de la Investigación 4](#_Toc240296739)

[1.3.1 Objetivo General 4](#_Toc240296740)

[1.3.2 Objetivos Específicos 4](#_Toc240296741)

[1.4 Resultados de la Investigación 4](#_Toc240296742)

[1.5 Planteamiento de la Hipótesis 5](#_Toc240296743)

[1.6 Operacionalización de Variables 6](#_Toc240296744)

[Capítulo II: Marco Teórico 10](#_Toc240296745)

[2.1 Marco Conceptual 10](#_Toc240296746)

[2.1.1 Detección y gestión de eventos de seguridad 10](#_Toc240296747)

[2.1.1.1 Evento e incidente de seguridad 10](#_Toc240296748)

[2.1.1.2 Ciclo de vida del incidente 11](#_Toc240296749)

[2.1.1.3 Indicadores MTTD y MTTR 12](#_Toc240296750)

[2.1.1.4 Evidencia forense y cadena de custodia 13](#_Toc240296751)

[2.1.2 El servicio fiscal digital como sector de aplicación 13](#_Toc240296752)

[2.1.2.1 Definición de servicio fiscal digital 14](#_Toc240296753)

[2.1.2.2 Tributaria 3.0 14](#_Toc240296754)

[2.1.2.3 Modelo de Madurez de la Transformación Digital 15](#_Toc240296755)

[2.1.2.4 Contexto institucional boliviano 16](#_Toc240296756)

[2.1.2.5 Índice de madurez en ciberseguridad fiscal 17](#_Toc240296757)

[2.1.3 Conceptos operativos de detección 18](#_Toc240296758)

[2.1.3.1 Marco MITRE ATT&CK 18](#_Toc240296759)

[2.1.3.2 Ciberdecepción 19](#_Toc240296760)

[2.1.3.3 Honeypots 20](#_Toc240296761)

[2.1.3.4 Honeytokens, honeynets y sensores de engaño 21](#_Toc240296762)

[2.1.3.5 Detección, evidencia y mejora continua 22](#_Toc240296763)

[2.2 Marco Referencial 22](#_Toc240296764)

[2.2.1 Teoría general de riesgo y resiliencia en ciberseguridad 23](#_Toc240296765)

[2.2.1.1 Origen y fundamento de la teoría 23](#_Toc240296766)

[2.2.1.2 Ciclo de gestión del riesgo 24](#_Toc240296767)

[2.2.1.3 Capacidades de la resiliencia organizacional 25](#_Toc240296768)

[2.2.1.4 Articulación riesgo–resiliencia 26](#_Toc240296769)

[2.2.1.5 Criterios de evaluación teórica 26](#_Toc240296770)

[2.2.2 Teoría sustantiva de modelos de madurez en ciberseguridad tributaria 28](#_Toc240296771)

[2.2.2.1 Fundamento de los modelos de madurez 28](#_Toc240296772)

[2.3 Marco Legal 29](#_Toc240296773)

[Capítulo III: Metodología de la Investigación 30](#_Toc240296774)

[3.1 Métodos de Investigación 30](#_Toc240296775)

[3.2 Tipo de Investigación 31](#_Toc240296776)

[3.3 Universo o Población de Estudio 33](#_Toc240296777)

[3.3.1 Determinación y Elección de la Muestra 34](#_Toc240296778)

[3.4 Sujetos Vinculados a la Población 36](#_Toc240296779)

[3.5 Fuentes y Diseño de los Instrumentos de Relevamiento de Información 37](#_Toc240296780)

[3.5.1 Fuentes de la Investigación 37](#_Toc240296781)

[3.5.2 Diseño de los Instrumentos de Relevamiento de Información 40](#_Toc240296782)

[3.5.2.1 Descripción del Instrumento de Diagnóstico 41](#_Toc240296783)

[3.5.2.2 Validez del Instrumento 48](#_Toc240296784)

[3.5.2.3 Confiabilidad del Instrumento 56](#_Toc240296785)

[3.6 Procesamiento y Análisis de la Información 63](#_Toc240296786)

[Capítulo IV: Marco Práctico 64](#_Toc240296787)

[4.1 Análisis de la situación actual 64](#_Toc240296788)

[4.1.1 Análisis de la normativa 64](#_Toc240296789)

[4.1.1.1 Criterio de selección de las normas 65](#_Toc240296790)

[4.1.1.2 Normas de gestión de incidentes 66](#_Toc240296791)

[4.1.1.3 Norma marco de seguridad de la información 68](#_Toc240296792)

[4.1.1.4 Normas de evidencia digital y forense 69](#_Toc240296793)

[4.1.1.5 Norma de gestión de riesgos 70](#_Toc240296794)

[4.1.1.6 Marco de comportamiento adversario 70](#_Toc240296795)

[4.1.1.7 Benchmarks operativos y modelos de madurez 71](#_Toc240296796)

[4.1.2 Aplicación del instrumento 74](#_Toc240296797)

[4.1.2.1 Aplicación a la muestra de diagnóstico 75](#_Toc240296798)

[4.1.2.2 Confiabilidad del instrumento 76](#_Toc240296799)

[4.1.2.3 Resultados por instrumento 77](#_Toc240296800)

[4.1.2.4 Resultados por grupo temático 80](#_Toc240296801)

[4.1.2.5 Resultado global de madurez 82](#_Toc240296802)

[4.1.3 Diagnóstico situacional 83](#_Toc240296803)

[4.1.3.1 Brechas en gestión de incidentes 84](#_Toc240296804)

[4.1.3.2 Brechas en evidencias y respaldo 85](#_Toc240296805)

[4.1.3.3 Brechas en controles técnicos 86](#_Toc240296806)

[4.1.3.4 Brechas en gestión organizacional y mejora 87](#_Toc240296807)

[4.1.3.5 Caracterización del estado actual 88](#_Toc240296808)

[4.1.3.6 Matriz de trazabilidad 90](#_Toc240296809)

[4.2 Diseño de la metodología de honeypot para la gestión de incidentes en los servicios fiscales 93](#_Toc240296810)

[4.2.1 Fundamentación del diseño metodológico 93](#_Toc240296811)

[4.2.1.1 Principios de diseño de la metodología Honeypot 94](#_Toc240296812)

[4.2.1.2 Atención integral de los hallazgos del diagnóstico 98](#_Toc240296813)

[4.2.1.3 Decisiones de diseño asumidas por la metodología Honeypot 105](#_Toc240296814)

[4.2.2 Arquitectura general de la metodología 107](#_Toc240296815)

[4.2.2.1 Estructura secuencial de las cinco fases y sus bucles de retroalimentación 109](#_Toc240296816)

[4.2.2.2 Planos transversales de la metodología y categorías funcionales de tecnología 110](#_Toc240296817)

[4.2.2.3 Trazabilidad metodológica de las cinco fases 113](#_Toc240296818)

[4.2.2.4 Prerrequisitos de la organización y transferibilidad de la metodología 115](#_Toc240296819)

[4.2.2.5 Justificación metodológica de las cinco actividades por fase 117](#_Toc240296820)

[4.2.3 Fase 1. Diseño del señuelo 122](#_Toc240296821)

[4.2.4 Fase 2. Despliegue aislado 128](#_Toc240296822)

[4.2.5 Fase 3. Captura, enriquecimiento y custodia 132](#_Toc240296823)

[4.2.6 Fase 4. Correlación con gestión de incidentes 137](#_Toc240296824)

[4.2.7 Fase 5. Medición de impacto y lecciones aprendidas 142](#_Toc240296825)

[4.3 Implementación de la metodología de honeypot para la gestión de incidentes 148](#_Toc240296826)

[4.3.1 Propósito, alcance y línea base 150](#_Toc240296827)

[4.3.2 Entorno controlado de implementación 151](#_Toc240296828)

[4.3.3 Plataforma tecnológica del prototipo 154](#_Toc240296829)

[Capítulo V: Conclusiones y Recomendaciones de la Investigación 159](#_Toc240296830)

[5.1 Conclusiones 171](#_Toc240296831)

[5.2 Recomendaciones 171](#_Toc240296832)

[Anexos 173](#_Toc240296833)

[Anexo A: [Nombre del Primer Anexo] 173](#_Toc240296834)

[Anexo B: [Nombre del Segundo Anexo] 173](#_Toc240296835)

[Glosario 174](#_Toc240296836)

[Apéndice 175](#_Toc240296837)

[Apéndice A: Instrumento de Recolección de Datos 175](#_Toc240296838)

[Apéndice B: Consentimiento Informado 175](#_Toc240296839)

[Bibliografía 176](#_Toc240296840)

# Índice de Tablas, Cuadros y Gráficos

*[Inserte aquí la lista de tablas, cuadros y figuras. En Word: Referencias → Insertar tabla de ilustraciones.]*

Tabla 1 *Descripción de la tabla ..............................* xx

Figura 1 *Descripción de la figura .............................* xx

# Introducción

*[Presente el tema general de la investigación, su relevancia en el ámbito de la informática/sistemas de información, y la estructura del documento. Extensión sugerida: 2–4 páginas.]*

Escriba aquí el primer párrafo de la introducción. Contextualice el problema desde lo general hasta llegar al tema específico de su investigación.

Indique brevemente cómo está organizado el documento: el Capítulo I presenta los aspectos generales; el Capítulo II desarrolla el marco teórico; el Capítulo III describe la metodología; el Capítulo IV expone el marco práctico; y el Capítulo V contiene las conclusiones y recomendaciones.

# Capítulo I: Aspectos Generales

## 1.1 Antecedentes

Es fundamental indagar investigaciones previas que han abordado la relevancia de los honeypots como herramienta de seguridad, así como la forma en que estos mecanismos han sido aplicados en distintos contextos para mejorar la gestión de incidentes. Se han encontrado tesis y estudios que se centran en el análisis de la efectividad de los honeypots, la integración de marcos normativos y su aporte a la detección temprana de amenazas en entornos críticos, entre ellos se destaca el siguiente:

* **Autor:** Oscar Rehnbäck
* **Título:** A case study of unauthorized login attempts against honeypots via remote desktop.
* **Publicación:** 2023.
* **Institución:** Luleå University of Technology.
* **Resumen:** Analiza más de 120 000 intentos de acceso RDP contra tres honeypots expuestos durante 37 días. Evalúa el bloqueo de cuentas y la obfuscación de puertos como controles, concluyendo que las medidas tuvieron impacto limitado en la disponibilidad, pero demostraron el alto valor de los honeypots para monitorear y gestionar incidentes de fuerza bruta en servicios expuestos.
* **Autor:** Javier R. Franco
* **Título:** Honeypot‑based Security Enhancements for Information Systems.
* **Publicación:** 2022.
* **Institución:** Florida International University.
* **Resumen:** Presenta S‑Pot, un framework de honeypots empresariales e IoT orquestados con SDN y aprendizaje automático (97 % de precisión en detección).
* **Autor:** Enea Gizzarelli
* **Publicación:** 2024
* **Título:** Honeypot and Generative AI.
* **Institución:** Politecnico di Torino University.
* **Resumen:** Propone SYNAPSE, un honeypot dinámico que integra IA generativa para interactuar con atacantes y mapea automáticamente sus registros al marco MITRE ATT&CK. Demuestra mejoras en la recolección de inteligencia y capacidad adaptativa frente a ataques automatizados, alineándose con requisitos de respuesta rápida de normas internacionales.

Los estudios revelan una tendencia a evolucionar el honeypot desde un sensor pasivo hacia plataformas inteligentes que incorporan aprendizaje automático, IA generativa y principios Zero-Trust. Convergen en la utilidad de la telemetría honeypot para enriquecer la detección y respuesta a incidentes bajo marcos como ISO 27035 y NIST SP 800-61. Sin embargo, existe una brecha la falta de metodologías específicas para servicios fiscales, donde confluyen requisitos regulatorios y alta sensibilidad de datos. Además, pocos trabajos formulan indicadores normativos que faciliten la adopción institucional. La presente investigación aborda estas lagunas al proponer una metodología honeypot adaptada al contexto fiscal, con KPIs alineados a estándares y regulaciones nacionales, fortaleciendo así la gestión integral de incidentes en dichos servicios.

## 1.2 Planteamiento del Problema

Pese a los avances en controles preventivos, las plataformas fiscales digitales continúan enfrentando una ventana de exposición elevada, donde los intentos de intrusión y reconocimiento persisten, la detección temprana resulta limitada y la contención de incidentes no siempre dispone de evidencias completas para sustentar decisiones técnicas y legales. Esta situación dificulta cumplir integralmente el ciclo de gestión de incidentes establecido por ISO/IEC 27035 detección, notificación, evaluación, respuesta, recuperación y lecciones aprendidas y tensiona los requisitos del SGSI (ISO/IEC 27001), especialmente en lo relativo a monitoreo, mejora continua y tratamiento del riesgo.

El problema central que aborda esta investigación es, por tanto, la insuficiente capacidad de detección y respuesta temprana, junto con la incompletitud de evidencias forenses en incidentes que afectan a servicios fiscales en línea. Se carece de una metodología sistemática para diseñar, desplegar, operar e integrar honeypots de interacción media dentro del proceso institucional de gestión de incidentes, alineada a estándares y medible mediante indicadores de desempeño. En consecuencia, se dificulta reducir el MTTD/MTTR, elevar la calidad de la trazabilidad técnica y fortalecer la resiliencia de las plataformas.

### 1.2.1 Formulación del Problema de Investigación

¿Cómo se puede reducir la gestión de incidentes de los servicios fiscales?

## 1.3 Objetivo General y Específicos de la Investigación

### 1.3.1 Objetivo General

Desarrollar una metodología de honeypot con normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK para mejorar la gestión de incidentes en los servicios fiscales.

### 1.3.2 Objetivos Específicos

1. Analizar la situación actual de la gestión de incidentes en los servicios fiscales y su relación con las normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK, identificando vulnerabilidades y tiempos promedio de detección.
2. Diseñar una metodología de honeypot orientada a mejorar la detección temprana y la recolección de evidencia en la gestión de incidentes de los servicios fiscales
3. Implementar la metodología de honeypot en un entorno controlado para su aplicación en la gestión de incidentes.
4. Validar la eficacia de la metodología propuesta mediante la evaluación de su impacto en la reducción del tiempo promedio de detección de incidentes.

## 1.4 Resultados de la Investigación

*[Describa los resultados esperados del trabajo de investigación, es decir, los productos o entregables que se generarán (sistema, modelo, metodología, prototipo, etc.).]*

1. Resultado 1: [Nombre del producto o entregable principal].
2. Resultado 2: [Nombre del segundo producto o entregable].
3. Resultado 3: [Documento, informe o publicación derivada].

## 1.5 Planteamiento de la Hipótesis

Una metodología de honeypot, con las normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK, mejora la gestión de incidentes en los servicios fiscales.

## 1.6 Operacionalización de Variables

A continuación, detallamos la operacionalización de variables dependiente e independiente

**Tabla 1**

*Operacionalización de variable Independiente*

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Variable** | **Tipo de variable** | **Definición** | **Operacionalización** | **Categorización / Dimensiones** | **Indicador** | **Nivel de medición** | **Unidad de medida** |
| Metodología de honeypot, con las normativas ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK. | Independiente | Enfoque estructurado de deception (honeypots de interacción media) integrado al proceso de gestión de incidentes; alineado con el Anexo A de ISO/IEC 27001, ciclo de incidentes de ISO/IEC 27035 y taxonomía MITRE ATT&CK. | Aplicación paso a paso e integración al proceso institucional (preparación, detección, análisis, respuesta y lecciones aprendidas), con trazabilidad a controles y tácticas/técnicas ATT&CK. | Metodología (fases) | Nivel de implementación de fases | Intervalo | % de cumplimiento |
| Alineación normativa | Cobertura de controles ISO/IEC 27001 (A.5.7, A.5.23, A.5.25, A.5.26) | Intervalo | % |
| Alineación normativa | Integración del proceso ISO/IEC 27035 (prep., det., anál., resp., lecc.) | Intervalo | % |
| Alineación normativa | Mapeo de tácticas/técnicas MITRE ATT&CK | Intervalo | % |
| Eficacia de captura | Nº de eventos captados | Razón | Nº de eventos |
| **Naturaleza** | **Índice** | **Valor/meta** | **Instrumento de medición** |
| Continua | IIAM = promedio ponderado (0–100) | Meta: ≥ 85% | Lista de verificación documental, registro de fases cumplidas. |
| Continua | Cobertura 27001 = (controles cubiertos / controles aplicables) × 100 | Meta: ≥ 85% | Matriz de cumplimiento de controles. |
| Continua | Índice 27035 = (requisitos integrados / requisitos definidos) × 100 | Meta: ≥ 80% | Registro de integración de requisitos. |
| Continua | Índice ATT&= (Tácticas mapeadas / relevantes) × 100 | Meta: ≥ 80% | Matriz de mapeo ATT&CK. |
| Discreta | TEMH = Nº eventos por período | Meta: ≥ línea base (+20% al mes 2) | Registro de eventos en honeypot, bitácora de incidentes. |

***Nota.*** *[Descripción breve si es necesario].*

**Tabla 2**

*Operacionalización de variable Dependiente*

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Variable** | **Tipo de variable** | **Definición** | **Operacionalización** | **Categorización / Dimensiones** | **Indicador** | **Nivel de medición** | **Unidad de medida** |
| Gestión de incidentes en los servicios fiscales. | Dependiente | Grado en que el proceso incrementa su capacidad para identificar, analizar, responder y cerrar incidentes con evidencia suficiente y en tiempos óptimos. | Comparación antes/después de aplicar la metodología (detección, análisis, respuesta/contención, recuperación y lecciones aprendidas). | Detección | MTTD (tiempo medio de detección) | Razón | Minutos/horas |
| Detección | Falsos positivos (FP/total detecciones) | Intervalo | % |
| Análisis y evidencia forense | % de evidencia completa por caso | Intervalo | % |
| Respuesta y contención | MTTR (tiempo medio de respuesta) | Razón | Minutos/horas |
| Cumplimiento del proceso / lecciones aprendidas | % de procedimientos cumplidos | Ordinal | Bajo/Medio/Alto (escala jerárquica) |
| Cumplimiento del proceso / lecciones aprendidas | % de casos con lecciones aprendidas cerradas | Intervalo | % |
| **Naturaleza** | **Índice** | **Valor/meta** | **Instrumento de medición** |
| Continua | Subíndice MTTD = 100 × (1 − MTTD\_t / MTTD\_base) | Meta: -30% | Registro de incidentes, métricas SIEM |
| Continua | Subíndice FP = 100 × (1 − FP%) | Meta: FP ≤ 5% | Registro de alertas, reportes de detección |
| Continua | Subíndice Evidencia = % de evidencia completa | Meta: ≥ 90% | Informe de análisis forense, checklist de evidencia |
| Continua | Subíndice MTTR = 100 × (1 − MTTR\_t / MTTR\_base) | Meta: -25% | Registro de tiempos de respuesta, SIEM/SOC |
| Discreta | % de procedimientos cumplidos | Meta: ≥ 90% | Checklist de cumplimiento de procesos |
| Continua | Subíndice Lecciones = % casos cerrados | Meta: ≥ 80% | Actas de cierre, informe de lecciones aprendidas |

***Nota.*** *[Descripción breve si es necesario].*

# Capítulo II: Marco Teórico

*[Fundamente la investigación en la literatura existente. Organice de lo general a lo particular. Extensión sugerida: 15–25 páginas.]*

## 2.1 Marco Conceptual

### 2.1.1 Detección y gestión de eventos de seguridad

Toda metodología orientada a fortalecer la respuesta institucional frente a amenazas digitales descansa sobre un conjunto de conceptos básicos que delimitan qué se considera un evento, cómo se gestiona, con qué indicadores se mide su tratamiento y qué condiciones debe cumplir la evidencia que de él se obtiene. Este apartado precisa esos conceptos, ancla cada uno a su referencia normativa y contrasta los enfoques de los principales organismos rectores en la materia.

#### 2.1.1.1 Evento e incidente de seguridad

La norma ISO/IEC 27035-1 distingue entre evento de seguridad de la información e incidente de seguridad de la información. Un evento es cualquier ocurrencia identificada en un sistema, servicio o red que indica una posible violación de la política de seguridad, una falla de los controles o una situación previamente desconocida con relevancia para la seguridad (ISO/IEC, 2023). Un incidente, en cambio, es uno o varios eventos no deseados o inesperados con probabilidad significativa de comprometer las operaciones del negocio y amenazar la seguridad de la información.

El NIST adopta una conceptualización compatible, aunque con matices propios. La Revisión 3 de NIST SP 800-61 define el evento como cualquier ocurrencia observable en un sistema o red, y el incidente cibernético como un evento, o conjunto de eventos, que pone en riesgo la confidencialidad, integridad o disponibilidad de los activos de información, o que constituye una violación de las políticas vigentes (NIST, 2025). La distinción entre ambas figuras es operativa más que ontológica: separa lo observado de lo que requiere respuesta formal.

La diferencia entre evento e incidente tiene consecuencias prácticas. Toda institución observa y registra miles de eventos diarios; únicamente una fracción reúne los criterios para escalar a incidente y activar los procedimientos formales de respuesta. La precisión con que se filtra entre ambas categorías es, por sí misma, un indicador de madurez del proceso (Liyanage et al., 2024). En el contexto de servicios fiscales digitales, donde los portales tributarios reciben volúmenes elevados de tráfico legítimo y hostil, esta distinción se vuelve crítica para evitar tanto el ruido operativo como la subdetección.

#### 2.1.1.2 Ciclo de vida del incidente

El ciclo de vida del incidente es la secuencia ordenada de fases que estructura su gestión, desde la preparación previa hasta la incorporación de las lecciones aprendidas al sistema institucional. Dos formulaciones de referencia conviven en la literatura actual y conviene contrastarlas.

La norma ISO/IEC 27035-1 organiza el ciclo en cinco fases: planificación y preparación, detección y reporte, evaluación y decisión, respuesta, y lecciones aprendidas (ISO/IEC, 2023). La planificación define políticas, roles, procedimientos y capacidades del CSIRT u oficina de respuesta. La detección y reporte abarca los mecanismos de identificación y la notificación a las instancias responsables. La evaluación clasifica el incidente y determina la prioridad de respuesta. La respuesta concentra la contención, erradicación y recuperación. Las lecciones aprendidas cierran el ciclo y retroalimentan el sistema de gestión.

El NIST, en la Revisión 3 de su SP 800-61, abandonó el modelo lineal de fases que había sostenido durante más de una década y alineó las recomendaciones con las seis funciones del Cybersecurity Framework 2.0: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar (NIST, 2025). El cambio reconoce que las actividades de preparación no se limitan al inicio del ciclo, sino que se desarrollan de manera continua como parte de la gestión del riesgo. Bajo esta lógica, la mejora deja de ser una fase final y se entiende como una actividad transversal que opera durante toda la vida del incidente.

Ambos marcos coinciden en lo esencial: un incidente no se gestiona como un evento aislado, sino como un proceso institucional documentado, trazable y susceptible de mejora continua (Calder & Watkins, 2019; ISO/IEC, 2023). El diseño metodológico de esta tesis articula los dos enfoques: toma de ISO/IEC 27035-1 la nomenclatura de fases y de NIST SP 800-61 Rev. 3 la integración con las funciones del CSF 2.0.

#### 2.1.1.3 Indicadores MTTD y MTTR

Dos indicadores cuantitativos concentran la mayor parte de la literatura operativa sobre eficacia en la gestión de incidentes: el tiempo medio de detección (Mean Time To Detect, MTTD) y el tiempo medio de respuesta (Mean Time To Respond, MTTR). El MTTD mide el lapso transcurrido entre el inicio efectivo del incidente y el momento en que la organización lo identifica. El MTTR mide el lapso entre la identificación y la contención o resolución (NIST, 2025).

Ambos se calculan como promedios estadísticos sobre el conjunto de incidentes registrados en un período definido. Su utilidad reside en que permiten comparar el desempeño antes y después de una intervención, así como cotejar la madurez de distintas organizaciones que adopten una misma referencia de medición. La literatura reciente identifica además derivaciones del MTTR —tales como el tiempo medio de contención (MTTC) y el tiempo medio de recuperación (MTTRec)— que desagregan la fase de respuesta en componentes más finos para diagnósticos detallados (Liyanage et al., 2024).

La importancia operativa de estos indicadores está bien documentada en reportes sectoriales. ENISA (2021) muestra que las organizaciones con menores MTTD y MTTR reducen significativamente el costo agregado de los incidentes, en particular en el sector público, donde el tiempo de exposición incide de manera directa sobre el grado de afectación a los servicios y sobre la confianza ciudadana. La hipótesis de la presente investigación incorpora ambos indicadores como variables dependientes principales, lo que los convierte en piezas operativas y no meramente conceptuales del estudio.

#### 2.1.1.4 Evidencia forense y cadena de custodia

La evidencia digital se define como cualquier información, almacenada o transmitida en forma binaria, susceptible de ser utilizada para reconstruir hechos durante el análisis de un incidente o en el marco de un proceso de investigación administrativa o judicial. La norma ISO/IEC 27037 (ISO/IEC, 2012) establece los lineamientos para su identificación, recolección, adquisición y preservación, y constituye la referencia internacional más utilizada en el campo de la informática forense.

La cadena de custodia es el procedimiento documental que garantiza la trazabilidad de la evidencia desde el momento de su recolección hasta su presentación final. Su propósito es preservar la integridad y autenticidad de los registros, de modo que ninguna alteración —deliberada o accidental— invalide su valor probatorio. Requiere, como mínimo, identificación inequívoca del activo, sellado mediante funciones criptográficas de hash, registro de los responsables que manipulan el material y trazabilidad de las acciones realizadas (Liyanage et al., 2024).

En contextos de administración tributaria, donde los incidentes pueden derivar en procedimientos administrativos sancionatorios o en investigaciones penales, la calidad de la evidencia forense determina la capacidad institucional para sostener decisiones ante auditorías, controles externos o instancias judiciales. La completitud de la evidencia es uno de los indicadores del cuarto objetivo de esta investigación, lo que ancla el concepto a la operación concreta del estudio (NIST, 2025).

### 2.1.2 El servicio fiscal digital como sector de aplicación

Los conceptos precedentes describen la detección y gestión de eventos de seguridad como un fenómeno aplicable a cualquier organización. La presente investigación, sin embargo, se desarrolla en un sector concreto: la administración tributaria digital. Este apartado precisa los conceptos que delimitan ese sector, articulando la visión internacional impulsada por la OCDE y el CIAT con los actores institucionales del contexto boliviano dentro del cual opera el estudio.

#### 2.1.2.1 Definición de servicio fiscal digital

Un servicio fiscal digital es cualquier servicio público de naturaleza tributaria cuya prestación se realiza a través de plataformas tecnológicas, sin requerir necesariamente la presencia física del contribuyente o del personal administrativo. Comprende los portales de declaración y pago, los sistemas de facturación electrónica, las consultas en línea, las notificaciones electrónicas y las interfaces de programación que conectan los sistemas tributarios con los sistemas contables y administrativos de los contribuyentes (OCDE, 2020).

La Organización para la Cooperación y el Desarrollo Económicos, a través de su Foro de Administración Tributaria, conceptualiza los servicios fiscales digitales como el resultado de un proceso de transformación que integra progresivamente las funciones tributarias en los entornos digitales que los contribuyentes utilizan en su vida cotidiana y profesional (OCDE, 2020). Barreix y Bès (2023), desde el Centro Interamericano de Administraciones Tributarias, añaden una mirada complementaria: los consideran la principal vía para reducir simultáneamente los costos de cumplimiento del contribuyente y fortalecer la capacidad de control institucional.

Dos características son determinantes para esta investigación. Por una parte, los servicios fiscales digitales son servicios críticos: su interrupción afecta de manera directa la recaudación nacional y el cumplimiento ciudadano. Por otra, procesan datos altamente sensibles —información tributaria, financiera y personal— que los convierten en objetivo prioritario para actores maliciosos. Ambas condiciones justifican la aplicación de marcos rigurosos de gestión de incidentes y de modelos de madurez en ciberseguridad como los que adopta el presente estudio.

#### 2.1.2.2 Tributaria 3.0

La visión de Administración Tributaria 3.0, formulada por la OCDE en 2020, describe la fase actual de evolución de las administraciones tributarias a nivel mundial. La numeración no es arbitraria: refleja una progresión que parte de la administración tradicional (1.0), centrada en el cumplimiento poscontable y el procesamiento manual; pasa por la administración electrónica (2.0), basada en el reemplazo de procesos presenciales por equivalentes digitales; y llega a una administración integrada (3.0), donde los procesos tributarios se incrustan en los sistemas naturales de los contribuyentes, ya sean financieros, contables o comerciales (OCDE, 2020).

La visión 3.0 implica un cambio cualitativo más que cuantitativo. La administración deja de ser un destino al cual los contribuyentes acuden y se convierte en una función distribuida que opera dentro de los flujos económicos ordinarios. La facturación electrónica obligatoria, los regímenes simplificados con prellenado automático y la fiscalización basada en datos en tiempo real son manifestaciones concretas de esta visión (OCDE, 2020).

Las implicaciones para la ciberseguridad son significativas. Cuando la administración tributaria se integra en los sistemas que los contribuyentes utilizan diariamente, la superficie de exposición se amplía y los vectores de ataque se diversifican. La protección deja de limitarse al perímetro institucional y debe extenderse a los puntos de integración con sistemas externos. Barreix y Bès (2023) advierten que esta expansión exige niveles de madurez en ciberseguridad equivalentes a los de las instituciones financieras, condición que muchas administraciones tributarias de la región todavía no han alcanzado.

#### 2.1.2.3 Modelo de Madurez de la Transformación Digital

El Modelo de Madurez de la Transformación Digital (MMTD), publicado por la OCDE en 2022 como herramienta operativa para implementar la visión de Administración Tributaria 3.0, es un instrumento de autoevaluación que permite a una administración tributaria diagnosticar su nivel actual de digitalización en diferentes dimensiones y trazar un plan de evolución (OCDE, 2022).

El modelo organiza el diagnóstico en seis bloques temáticos: identidad digital, procesos contributivos, datos, capacidades de la administración, soluciones tecnológicas y gobernanza. Para cada bloque define cinco niveles de madurez que describen estadios típicos de evolución, desde una operación emergente y reactiva hasta una operación integrada y proactiva. La herramienta opera mediante un cuestionario estructurado que el equipo de la administración completa de manera colaborativa, y produce un perfil de madurez comparable con el de otras administraciones que hayan aplicado el mismo instrumento (OCDE, 2022).

La pertinencia del MMTD para la presente investigación es doble. En primer lugar, ofrece un referente metodológico maduro para construir el instrumento diagnóstico de esta tesis, en tanto demuestra la viabilidad de aplicar modelos de madurez al sector tributario específicamente. En segundo lugar, su énfasis en las capacidades organizacionales y no en las tecnologías concretas refuerza el enfoque neutral adoptado en el estudio. Liyanage et al. (2024) reconocen al MMTD como uno de los pocos instrumentos sectoriales contemporáneos que integran de manera explícita las dimensiones humana, organizacional, tecnológica y operacional de la transformación digital.

#### 2.1.2.4 Contexto institucional boliviano

Tres actores institucionales delimitan el contexto operativo dentro del cual se desarrolla la investigación: el Servicio de Impuestos Nacionales, el Sistema de Facturación Virtual y el Centro de Gestión de Incidentes Informáticos.

El Servicio de Impuestos Nacionales (SIN) es la administración tributaria del Estado Plurinacional de Bolivia, responsable de la aplicación, gestión y fiscalización de los impuestos nacionales. Para los fines del marco conceptual interesa caracterizarlo como una administración tributaria que ha avanzado en su transición hacia la fase 2.0 de la visión OCDE, con servicios electrónicos consolidados, y que se encuentra en proceso de incorporar elementos propios de la fase 3.0, particularmente en lo que respecta a la facturación electrónica y la interoperabilidad de datos (Barreix & Bès, 2023).

El Sistema de Facturación Virtual (SFV) es la plataforma operativa que soporta el régimen de facturación electrónica obligatoria del SIN (SIN, 2024). Constituye el principal servicio fiscal digital del país, ya que media la totalidad de las operaciones de facturación de los contribuyentes alcanzados por el régimen. Su criticidad operativa es alta: una interrupción del SFV afecta de manera directa la actividad económica diaria, lo que lo convierte en un activo de información de máxima prioridad desde la perspectiva de gestión de incidentes.

El Centro de Gestión de Incidentes Informáticos (CGII), dependiente de la Agencia de Gobierno Electrónico y Tecnologías de Información y Comunicación (AGETIC), opera como Equipo de Respuesta a Incidentes de Seguridad Informática (CSIRT) del sector público boliviano. Sus funciones incluyen la coordinación de la respuesta ante incidentes que afecten a entidades estatales, la emisión de alertas, la articulación con CSIRTs internacionales y la publicación de lineamientos operativos como la Guía SEG-001 (CTIC-AGETIC, 2017). Dentro del marco institucional boliviano, el CGII es el referente nacional al que deben alinearse las metodologías de gestión de incidentes que se desarrollen para el sector público, incluida la que propone la presente investigación.

#### 2.1.2.5 Índice de madurez en ciberseguridad fiscal

El índice de madurez en ciberseguridad fiscal es el constructo que articula los conceptos descritos en los apartados anteriores y los convierte en un indicador medible aplicable a una administración tributaria concreta. Operacionalmente, es un valor compuesto que resume el grado de desarrollo de las capacidades institucionales para gestionar incidentes de seguridad, evaluado en las dimensiones que cubre el modelo de madurez adoptado.

La construcción de un índice de madurez requiere tres elementos: una estructura de dimensiones e indicadores anclada a marcos reconocidos, una escala de niveles con criterios verificables y un procedimiento de cálculo que agregue las observaciones individuales en un valor compuesto (Liyanage et al., 2024). El instrumento diagnóstico desarrollado en esta tesis adopta esa lógica y produce dos índices complementarios: el Índice Institucional de Alineación Metodológica (IIAM), centrado en la conformidad con los marcos internacionales de referencia, y el Índice de Madurez en Gestión de Incidentes (IMGI), centrado en el desempeño operativo medido a través de MTTD, MTTR y completitud de evidencia.

La pertinencia del concepto para la investigación es directa. Los cuatro objetivos específicos del estudio se operacionalizan a través de mediciones del IIAM y del IMGI. El primer objetivo establece la línea base mediante el cálculo inicial de ambos índices; el segundo y tercer objetivos diseñan e implementan una intervención metodológica orientada a elevar sus valores; y el cuarto objetivo valida la eficacia de la intervención mediante la comparación de los índices antes y después de la implementación. El índice de madurez en ciberseguridad fiscal es, en consecuencia, el constructo articulador entre la teoría sustantiva, los objetivos específicos y el instrumento operativo de la investigación.

### 2.1.3 Conceptos operativos de detección

Los apartados anteriores definieron el fenómeno general de detección y gestión de eventos y el sector de aplicación dentro del cual se desarrolla el estudio. Resta precisar los conceptos operativos que estructuran la actividad concreta de detección: el lenguaje compartido para describir el comportamiento adversario, el campo de la ciberdecepción y las técnicas que ese campo agrupa, junto con la articulación final entre detección, evidencia y mejora continua que cierra el marco conceptual.

#### 2.1.3.1 Marco MITRE ATT&CK

El marco MITRE ATT&CK (Adversarial Tactics, Techniques and Common Knowledge) es una base de conocimiento taxonómica desarrollada por la MITRE Corporation que documenta el comportamiento observado de actores adversarios reales en operaciones de ciberataque (MITRE, 2024). Su propósito es ofrecer un vocabulario compartido que permita a los equipos defensivos describir, mapear y comunicar el comportamiento adversario de manera estandarizada y comparable entre organizaciones.

El marco se organiza en matrices que cubren distintos entornos: Enterprise para sistemas corporativos, Mobile para dispositivos móviles e ICS para sistemas de control industrial. Cada matriz se estructura en torno a tácticas (los porqués del adversario, como persistir o exfiltrar), técnicas (los cómos generales) y subtécnicas (variaciones específicas). La versión actual describe más de 200 técnicas y casi 700 subtécnicas en su matriz Enterprise, con actualizaciones publicadas dos veces al año en función de la inteligencia de amenazas recolectada por la comunidad (MITRE, 2024).

La adopción de MITRE ATT&CK por parte de la comunidad de ciberseguridad ha sido amplia y rápida. Estudios recientes lo emplean como referencia para evaluar la cobertura defensiva de una organización, para mapear automáticamente registros de detección y para entrenar modelos de inteligencia artificial orientados al análisis de amenazas (Gizzarelli, 2024; Ozkok et al., 2024). En el contexto de esta investigación, el marco constituye la referencia para operacionalizar la dimensión de capacidades técnicas del modelo de madurez adoptado: una administración tributaria alcanza un nivel mayor de madurez cuando logra detectar, registrar y mapear a la taxonomía ATT&CK una proporción mayor de las tácticas adversarias observadas en su entorno.

#### 2.1.3.2 Ciberdecepción

La ciberdecepción es un campo de la ciberseguridad que engloba el conjunto de técnicas mediante las cuales una organización introduce de manera deliberada información, sistemas o señales engañosas en su entorno para alterar la percepción del adversario y, con ello, detectar su actividad, retrasar su avance o desviar sus recursos hacia objetivos sin valor real (NIST, 2021). Aunque la idea cuenta con antecedentes en la inteligencia militar y la teoría del juego, su sistematización como disciplina académica y operativa en ciberseguridad es relativamente reciente.

La literatura especializada distingue tres propósitos complementarios. El primero es descubrir la presencia del adversario, ya que el contacto con un elemento engañoso indica con alta certeza una intención hostil. El segundo es retrasar o desorientar la operación adversaria, obligándola a desperdiciar tiempo y recursos en objetivos ilegítimos. El tercero es recolectar inteligencia sobre las tácticas, técnicas y herramientas del adversario, con el fin de mejorar la postura defensiva general (NIST, 2021; Segovia-Ferreira et al., 2024).

Conviene aclarar que la ciberdecepción es un campo y no una técnica única. Incluye múltiples mecanismos: honeypots, honeytokens, honeynets, sensores distribuidos y sistemas de engaño basados en aprendizaje automático, entre otros. La selección depende del contexto organizacional, del perfil de amenaza y del nivel de madurez de la institución (Franco, 2022). Esta diversidad es relevante para la investigación, ya que la metodología propuesta toma una técnica específica como punto de aplicación experimental, sin que ello implique que sea la única posible dentro del campo.

#### 2.1.3.3 Honeypots

Un honeypot es un sistema informático cuyo valor reside enteramente en ser sondeado, atacado o comprometido por actores adversarios. A diferencia de los sistemas de producción, no presta servicios reales a usuarios legítimos: toda interacción con un honeypot es, por definición, sospechosa o maliciosa, lo que reduce drásticamente la incidencia de falsos positivos en la detección (Franco, 2022).

La literatura clasifica los honeypots según su nivel de interacción con el adversario. Los honeypots de baja interacción emulan servicios y respuestas básicas; son sencillos de operar y presentan bajo riesgo, pero recolectan información limitada. Los honeypots de alta interacción ofrecen sistemas reales o completamente emulados con los que el adversario interactúa de manera natural, lo que permite obtener inteligencia de amenazas detallada a costa de mayor complejidad operativa y mayor exposición a riesgos secundarios. Los honeypots de interacción media constituyen un punto intermedio que combina la riqueza informativa de los anteriores con una operación más manejable, y son el tipo más utilizado en estudios académicos recientes (Franco, 2022; Gizzarelli, 2024; Rehnbäck, 2023).

Como cualquier técnica de detección, los honeypots presentan limitaciones y riesgos que la literatura ha documentado con detenimiento. Un honeypot mal aislado puede convertirse en plataforma de ataque secundario; uno demasiado obvio pierde su valor de detección porque el adversario lo evita; y uno que captura datos personales puede generar consideraciones legales y éticas (Liyanage et al., 2024). Su valor real, por tanto, no reside en el despliegue aislado de la técnica, sino en su integración con el resto del proceso de gestión de incidentes y con los marcos normativos que rigen la institución. Esa integración es uno de los aportes que la presente investigación propone para el sector fiscal.

#### 2.1.3.4 Honeytokens, honeynets y sensores de engaño

Junto a los honeypots, la ciberdecepción dispone de otras tres categorías de mecanismos que conviene precisar para completar el panorama operativo.

Un honeytoken es un artefacto digital cuya activación o uso revela inequívocamente la presencia de un adversario, sin necesidad de desplegar un sistema señuelo completo. Puede tratarse de credenciales falsas insertadas en un repositorio, registros de base de datos diseñados para no ser consultados nunca por usuarios legítimos, archivos con nombres atractivos pero sin contenido sensible o claves de API monitoreadas que disparan alertas al ser utilizadas (NIST, 2021). Su valor reside en la economía: requieren bajísimos recursos de implementación y, sin embargo, ofrecen una señal de alta calidad cuando se activan.

Una honeynet es una red de honeypots interconectados que simula un entorno organizacional más complejo. Permite observar el comportamiento adversario en movimientos laterales, escalamientos de privilegios y persistencia, no solo en accesos iniciales (Franco, 2022). Las honeynets contemporáneas integran frecuentemente capacidades de orquestación dinámica que les permiten reconfigurarse en función del comportamiento observado, lo que aumenta el realismo de la simulación y la calidad de la inteligencia recolectada (Gizzarelli, 2024).

Los sensores de engaño constituyen la generación más reciente de la familia. Son componentes distribuidos a través de la infraestructura organizacional que combinan señuelos pasivos con instrumentación activa de monitoreo para producir detección distribuida y temprana (Segovia-Ferreira et al., 2024). A diferencia de los honeypots tradicionales, los sensores no requieren la existencia de un sistema señuelo dedicado: incrustan la lógica de engaño en activos productivos para detectar comportamientos anómalos sin generar una infraestructura adicional. Su uso es aún incipiente en el sector público latinoamericano, pero la literatura los identifica como el horizonte natural de la ciberdecepción aplicada (Liyanage et al., 2024).

#### 2.1.3.5 Detección, evidencia y mejora continua

El cierre del marco conceptual articula los conceptos precedentes en una secuencia coherente que será retomada por las teorías presentadas en el marco referencial y por las normas analizadas en el marco legal. La detección de eventos de seguridad, cualquiera que sea la técnica empleada, produce evidencia en forma de registros, alertas, capturas y artefactos digitales. Esa evidencia, debidamente preservada bajo cadena de custodia (ISO/IEC, 2012), permite el análisis posterior del incidente y la toma de decisiones sobre la respuesta. El análisis, a su vez, alimenta la mejora continua del sistema institucional mediante la incorporación de lecciones aprendidas en políticas, procedimientos y capacidades.

Esta secuencia, detección–evidencia–mejora, no es novedosa en sí misma, pero adquiere relevancia cuando se la interpreta como la operacionalización concreta de las capacidades de un sistema socio-técnico resiliente. Esa lectura corresponde al marco referencial que se presenta en el siguiente apartado del capítulo, donde la teoría general fundamenta el porqué y la teoría sustantiva ofrece los modelos que permiten medirla.

La metodología propuesta en la presente tesis se construye sobre esa articulación: estructura un proceso institucional en el cual la detección, la evidencia y la mejora continua se integran en un ciclo trazable, auditable y susceptible de evaluación mediante los índices de madurez definidos en el apartado anterior. Con esto, el marco conceptual queda completo y prepara el terreno para la fundamentación teórica que sigue.

## 2.2 Marco Referencial

El marco referencial fundamenta teóricamente los conceptos definidos en el apartado anterior. Se organiza en tres bloques articulados: una teoría general que explica el fenómeno desde una perspectiva amplia, una teoría sustantiva que baja el nivel de abstracción al sector específico estudiado y un conjunto de antecedentes empíricos que sitúan la investigación en la conversación académica reciente. La articulación entre los tres bloques sustenta la elección metodológica y la formulación de la hipótesis de la tesis.

### 2.2.1 Teoría general de riesgo y resiliencia en ciberseguridad

Los conceptos de detección, gestión, evidencia y mejora continua precisados en el marco conceptual no se sostienen por sí solos: requieren un fundamento teórico que explique por qué funcionan y bajo qué condiciones. La presente investigación adopta como teoría general la articulación entre la gestión del riesgo de seguridad de la información, formalizada en estándares como ISO/IEC 27005 (ISO/IEC, 2022) y el Cybersecurity Framework 2.0 del NIST (2024), y la ingeniería de resiliencia organizacional, formulada originalmente por Hollnagel (2011) y desarrollada en años recientes por Patriarca et al. (2018) y Linkov y Kott (2019). La elección de esta articulación responde al requisito de neutralidad tecnológica del estudio, dado que ninguno de sus enunciados presupone una técnica concreta de detección o respuesta.

#### 2.2.1.1 Origen y fundamento de la teoría

En las últimas dos décadas, la gestión del riesgo en seguridad de la información se ha consolidado como un proceso sistemático a través de un cuerpo normativo internacional que le dio forma operativa (ISO/IEC, 2022; NIST, 2024). ISO/IEC 27005 la define como un ciclo continuo de identificación, análisis, evaluación y tratamiento de las amenazas que afectan la confidencialidad, integridad y disponibilidad de los activos. El NIST adoptó una lógica equivalente en la versión 2.0 de su Cybersecurity Framework, que incorpora la función Gobernar junto a Identificar, Proteger, Detectar, Responder y Recuperar (NIST, 2024). Con esa adición, el marco coloca explícitamente la gobernanza del riesgo cibernético en el mismo nivel que las funciones operativas.

La segunda raíz teórica nació como crítica al enfoque tradicional, que apostaba todo a la prevención de fallos. Hollnagel (2011) sostuvo que los sistemas socio-técnicos no se vuelven seguros simplemente evitando errores: necesitan absorber perturbaciones, adaptarse y aprender. El foco se desplazó así desde el control de eventos puntuales hacia el desempeño del sistema a lo largo del tiempo. Investigaciones posteriores llevaron la propuesta al terreno cibernético. Patriarca et al. (2018) sistematizaron el estado del arte y refinaron el modelo de las cuatro capacidades; Linkov y Kott (2019) formalizaron la resiliencia cibernética como propiedad de sistemas y redes, complementaria a la gestión del riesgo; y Segovia-Ferreira et al. (2024) ofrecieron una revisión exhaustiva del campo aplicado a sistemas ciberfísicos.

De la integración de ambas tradiciones resulta un marco analítico suficiente para abordar la detección y gestión de eventos de seguridad. La gestión del riesgo aporta el rigor para anticipar amenazas y priorizar recursos; la resiliencia explica cómo las instituciones sostienen sus funciones críticas cuando los controles preventivos fallan (ENISA, 2021; NIST, 2024).

#### 2.2.1.2 Ciclo de gestión del riesgo

El ciclo de gestión del riesgo organiza la actividad analítica y la toma de decisiones en una secuencia de fases articuladas. ISO/IEC 27005 fija seis: establecimiento del contexto, identificación de riesgos, análisis, evaluación, tratamiento y monitoreo, todas envueltas por un proceso transversal de comunicación con las partes interesadas (ISO/IEC, 2022). La edición vigente sumó la figura del propietario del riesgo, responsable de aprobar el plan de tratamiento y asumir el riesgo residual; con eso, la norma reforzó la rendición de cuentas. La primera fase delimita el alcance, los criterios de aceptación y el marco regulatorio. Luego, la identificación reconoce activos, amenazas y vulnerabilidades; el análisis estima probabilidad y consecuencia; y la evaluación las contrasta con los criterios definidos para priorizar las opciones de tratamiento, que se reducen a cuatro: mitigar, transferir, aceptar o evitar.

El Cybersecurity Framework 2.0 del NIST plantea una estructura compatible con ISO, aunque organizada en seis funciones de alto nivel: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar (NIST, 2024). Gobernar concentra la gestión del riesgo, las políticas y la supervisión; las otras cinco distribuyen la operación. Calder y Watkins (2019) advierten que la lógica de fondo es la misma en ambos marcos: el riesgo no se elimina, se administra hasta reducirlo a un nivel residual tolerable para la institución.

En la práctica, el ciclo se alimenta de evidencia empírica para recalibrar las estimaciones. Cuanto más nítido es el perfil de las tácticas y técnicas adversarias observadas en el entorno, más ajustadas resultan las decisiones de tratamiento (ENISA, 2021; ISO/IEC, 2022). Esa retroalimentación enlaza el ciclo del riesgo con la dimensión de resiliencia que se aborda enseguida.

#### 2.2.1.3 Capacidades de la resiliencia organizacional

La resiliencia organizacional, dentro del marco de la ingeniería de resiliencia, designa la capacidad propia de un sistema socio-técnico para ajustar su funcionamiento antes, durante y después de una perturbación, sosteniendo las operaciones críticas tanto en condiciones previsibles como en las que no lo son (Hollnagel, 2011; Patriarca et al., 2018). No es un atributo dado: se construye en el tiempo, deliberadamente, a partir de capacidades específicas que conviven con los controles preventivos y no los reemplazan (Linkov & Kott, 2019).

La literatura coincide en cuatro capacidades esenciales, sistematizadas inicialmente por Hollnagel (2011) y refinadas por Patriarca et al. (2018). Anticipar consiste en prever amenazas, oportunidades y cambios futuros, junto con sus posibles consecuencias para el sistema. Monitorear es observar de manera continua las condiciones internas y externas pertinentes para identificar variaciones que afecten las operaciones críticas. Responder requiere actuar con flexibilidad y oportunidad frente a eventos esperados o emergentes, ya sea con opciones preparadas de antemano o improvisando cuando la situación lo exige. Aprender, por último, supone incorporar la experiencia, sobre todo la de incidentes pasados, para fortalecer las tres capacidades anteriores.

En el dominio cibernético, estas capacidades han sido formalizadas por instituciones de referencia. La guía *Systems Security Engineering: Cyber Resiliency Considerations* del NIST (2021) las articula con la ingeniería de sistemas seguros. La norma ISO 22301 (ISO, 2019) las traduce en requisitos para la continuidad del negocio. Y Segovia-Ferreira et al. (2024) ofrecen un mapeo actualizado de su aplicación a infraestructuras críticas. La resiliencia se mide, entonces, no por la ausencia de incidentes sino por la velocidad con la que la organización detecta, contiene, restablece y aprende cuando estos ocurren.

#### 2.2.1.4 Articulación riesgo–resiliencia

Riesgo y resiliencia, examinados conjuntamente, ofrecen una capacidad explicativa mayor que la que tiene cada uno por separado (Linkov & Kott, 2019; Patriarca et al., 2018). El primero opera con una lógica anticipatoria y probabilística, dirigida a reducir la exposición antes de que las amenazas se materialicen. La segunda parte del supuesto contrario: los incidentes ocurrirán, y la pregunta relevante es cómo seguir operando cuando lo hagan (ISO/IEC, 2022). No son perspectivas excluyentes, sino complementarias: la gestión del riesgo señala dónde conviene invertir en capacidades de resiliencia, y la resiliencia, a su vez, aporta evidencia empírica que mantiene vivo el análisis del riesgo (Patriarca et al., 2018).

La complementariedad se ve con claridad en los sistemas socio-técnicos de información, donde personas, procesos y tecnologías interactúan bajo presión adversa. Las estimaciones de probabilidad y consecuencia se nutren de los eventos observados en operación; a su vez, la respuesta gana eficacia cuanto mejor se conoce el perfil de riesgo del entorno (NIST, 2024; Segovia-Ferreira et al., 2024). Bajo esta lente, la seguridad de la información no es un estado que se alcanza una vez, sino un proceso continuo de aprendizaje y adaptación.

La utilidad de esta articulación para la presente investigación es directa: el análisis se vuelca sobre las capacidades organizacionales (anticipar, monitorear, responder y aprender) sin atarse a una tecnología en particular. De ahí que cualquier técnica de detección o respuesta deba juzgarse por su aporte a esas capacidades y por su efecto sobre el riesgo residual.

#### 2.2.1.5 Criterios de evaluación teórica

La teoría general adoptada satisface los cinco criterios exigidos para la evaluación de teorías científicas. Describe, explica y predice: la integración riesgo–resiliencia da cuenta de cómo las organizaciones perciben las amenazas, explica por qué ciertos controles reducen la exposición y anticipa las condiciones en las que un sistema logra absorber un incidente sin comprometer sus operaciones críticas (ISO/IEC, 2022; Patriarca et al., 2018). También es lógicamente consistente: el riesgo se administra y la resiliencia se cultiva, y ninguna proposición contradice a la otra. Su perspectiva es amplia, porque sus principios resultan aplicables a organizaciones de cualquier tamaño, sector o nivel de madurez, desde una pyme hasta una administración pública compleja (Calder & Watkins, 2019; NIST, 2024).

La fructificación queda en evidencia cuando uno se pregunta qué capacidades de resiliencia están más débiles en un tipo determinado de organización, qué indicadores capturan mejor la madurez del proceso o cómo se relacionan la calidad de la información disponible y la velocidad de respuesta ante incidentes (Linkov & Kott, 2019; Segovia-Ferreira et al., 2024). La parsimonia, en último lugar, se cumple sin esfuerzo: el modelo se condensa en pocas proposiciones, un ciclo integrado para el riesgo y cuatro capacidades para la resiliencia (Hollnagel, 2011; ISO/IEC, 2022), lo que lo hace manejable sin perder profundidad explicativa.

La estrategia de construcción combina varias teorías aplicables y toma de cada una lo pertinente. De ISO/IEC 27005 y NIST CSF 2.0 se recoge el ciclo de gestión del riesgo y su nomenclatura (ISO/IEC, 2022; NIST, 2024); de la ingeniería de resiliencia, las cuatro capacidades y la mirada temporal sobre el desempeño organizacional (Hollnagel, 2011; Patriarca et al., 2018); y de la literatura reciente en resiliencia cibernética, la operacionalización de esos conceptos en sistemas digitales contemporáneos (Linkov & Kott, 2019; NIST, 2021; Segovia-Ferreira et al., 2024). La integración deja una teoría general suficiente para enmarcar la detección y gestión de eventos de seguridad. Definida así la teoría general, corresponde bajar el nivel de abstracción al campo específico que aborda la investigación, asunto que desarrolla la siguiente subsección.

### 2.2.2 Teoría sustantiva de modelos de madurez en ciberseguridad tributaria

La teoría general adoptada en el apartado anterior describe el fenómeno en un nivel amplio: la integración entre la gestión del riesgo y la resiliencia organizacional explica por qué y cómo las instituciones desarrollan capacidades para detectar y gestionar eventos de seguridad. Esa explicación general, sin embargo, no basta para guiar una intervención en un sector específico. Hace falta una teoría sustantiva que baje el nivel de abstracción y permita medir, comparar y mejorar las capacidades en el campo concreto que aborda la investigación. Esa función la cumplen los modelos de madurez en ciberseguridad aplicados al sector fiscal, una familia de marcos analíticos que traduce las capacidades organizacionales en niveles medibles, comparables y abiertos a la mejora progresiva (Liyanage et al., 2024; NIST, 2024). La elección es coherente con el enfoque del estudio, ya que estos modelos evalúan la calidad institucional de los procesos sin presuponer una tecnología concreta, preservando así la neutralidad metodológica.

#### 2.2.2.1 Fundamento de los modelos de madurez

Los modelos de madurez tienen su origen conceptual en la ingeniería de software, donde Humphrey (1989) y Paulk et al. (1993) plantearon que el desempeño organizacional depende más de la calidad de los procesos institucionales que de la pericia individual. Sobre esa premisa, los modelos definen niveles ascendentes que van desde una operación ad hoc hasta una optimizada y en mejora continua.

El concepto se trasladó con éxito al dominio de la ciberseguridad y se ha consolidado con fuerza en los últimos años. Liyanage et al. (2024) propusieron un marco contemporáneo para medir la madurez de las capacidades organizacionales, que distingue cuatro aspectos esenciales —humano, organizacional, tecnológico y operacional— y los evalúa de forma holística para evitar las brechas típicas de los enfoques fragmentarios. El *Cybersecurity Capability Maturity Model* (C2M2), del Departamento de Energía de Estados Unidos, organiza por dominios y niveles la capacidad de proteger los activos digitales (U.S. Department of Energy, 2022). Y el *Cybersecurity Framework* 2.0 del NIST incorpora cuatro niveles de implementación —parcial, informado por riesgo, repetible y adaptativo— que operan, de hecho, como un modelo de madurez para las funciones de gobernar, identificar, proteger, detectar, responder y recuperar (NIST, 2024).

Tres rasgos comunes en estos marcos resultan determinantes para la investigación. Primero, descomponen el fenómeno en dimensiones o dominios independientes, lo que permite identificar fortalezas y debilidades específicas en vez de emitir juicios globales poco informativos (Liyanage et al., 2024). Segundo, definen niveles discretos y observables que dan un lenguaje compartido para describir el estado actual y el objetivo. Tercero, son explícitamente independientes de la tecnología empleada: evalúan la calidad del proceso, no la herramienta con la que se ejecuta (NIST, 2024; U.S. Department of Energy, 2022).

## 2.3 Marco Legal

*[Incluya las normativas, leyes, decretos y reglamentos bolivianos e internacionales que enmarcan su investigación. El contenido estará en función del tipo y alcances de la investigación. Ejemplos: Ley N.° 164 de Telecomunicaciones (Bolivia), normativas de protección de datos, estándares ISO, etc.]*

Zambrana (2019) desarrolló un sistema de [descripción técnica] utilizando [tecnología/metodología]. Los resultados demostraron [hallazgos relevantes para su investigación].

1. Ley N.° [número]: [Nombre de la ley] — [Artículo(s) relevante(s)].
2. Decreto Supremo N.° [número]: [Descripción] — [Relevancia para la investigación].
3. Normativa / Estándar: [ISO/IEC xxxx — Descripción y aplicación].

# Capítulo III: Metodología de la Investigación

## 3.1 Métodos de Investigación

La investigación adopta el método científico como marco general de actuación y el método deductivo como método principal para orientar el proceso investigativo. El método científico organiza la secuencia de pasos que la investigación recorre de manera sistemática: la observación de los hechos relevantes, el planteamiento del problema, la formulación de la hipótesis, el desarrollo de la experimentación y el análisis de los resultados obtenidos. El método deductivo opera dentro de esa secuencia y se materializa en la derivación de las conclusiones particulares del trabajo a partir de los marcos normativos y conceptuales generales que sustentan el campo de la gestión de incidentes y de la seguridad de la información.

La aplicación de estos métodos al objeto de estudio se estructura en dos fases articuladas. La primera fase, de carácter diagnóstico, observa y caracteriza la situación actual de la gestión de incidentes en la institución bajo estudio mediante la aplicación del Instrumento de Diagnóstico de Madurez en Seguridad de la Información. La segunda fase, de carácter propositivo, despliega de manera controlada una metodología basada en honeypots de interacción media sobre un entorno simulado y registra los efectos generados sobre los indicadores de impacto.

A partir de la observación de la situación actual y de los registros generados por las dos fases, la investigación construye el planteamiento del problema sobre la necesidad de reducir los tiempos de detección y mejorar la gestión de incidentes en servicios fiscales digitales. Sobre esta base se formula la hipótesis del trabajo, según la cual la implementación de una metodología honeypot alineada con las normas internacionales ISO/IEC 27001, ISO/IEC 27035 y el marco MITRE ATT&CK mejora la detección y gestión de incidentes respecto de la situación previa a su aplicación. La experimentación se desarrolla mediante el despliegue controlado de honeypots en laboratorio, la captura de registros de actividad maliciosa y la confrontación de los resultados con las metas de mejora declaradas en la operacionalización de variables del Capítulo I. El análisis se realiza mediante cálculos, tablas, resúmenes e indicadores compuestos (IIAM e IMGI), con el propósito de comprobar o refutar la hipótesis y aportar conclusiones válidas para los objetivos planteados.

## 3.2 Tipo de Investigación

La investigación se define metodológicamente a partir de cinco dimensiones articuladas que en conjunto caracterizan su tipo: el diseño del estudio, el enfoque metodológico, el nivel o alcance, el propósito y la ubicación temporal de los hechos analizados. Cada dimensión se justifica a continuación.

**Diseño**

La investigación adopta un diseño pre-experimental con esquema preprueba-posprueba sobre un mismo grupo. La fase diagnóstica establece una medición inicial de la situación de la gestión de incidentes en la institución bajo estudio, que opera como línea base de los indicadores de impacto. La fase de validación de la metodología honeypot establece una medición posterior sobre el mismo objeto, lo cual permite comparar el impacto generado por la aplicación de la propuesta. El diseño se reconoce como pre-experimental porque implica manipulación de la variable independiente, pero no incorpora grupo de control ni asignación aleatoria de sujetos, condiciones que serían propias de un diseño experimental puro.

La elección de este diseño responde a la naturaleza del objeto de estudio. La metodología honeypot se aplica en un entorno institucional acotado, donde la conformación de un grupo de control equivalente no resulta factible operativamente y la aleatorización de sujetos no es pertinente al tratarse de una unidad institucional única. El esquema preprueba-posprueba permite una comparación válida del efecto generado por la propuesta, dado que las mediciones se realizan sobre el mismo conjunto de procesos y los indicadores de impacto (MTTD, MTTR, completitud de evidencia) se calculan con criterios idénticos en ambos momentos del estudio.

**Enfoque metodológico**

El enfoque de la investigación es mixto con dominio cuantitativo. La dimensión cuantitativa, predominante en el trabajo, se materializa en la recolección, el procesamiento y el análisis de datos objetivos que permiten medir con precisión los fenómenos estudiados. Esta dimensión se expresa en la utilización de indicadores específicos como el tiempo medio de detección (MTTD), el tiempo medio de respuesta (MTTR), el porcentaje de evidencia completa por caso, el número de eventos captados y los índices compuestos IIAM e IMGI. Los indicadores proporcionan métricas verificables y comparables sobre el comportamiento de los ataques simulados y la capacidad de respuesta del sistema analizado.

La dimensión cualitativa, complementaria a la anterior, se incorpora a través de la revisión documental de normas, marcos de referencia y literatura especializada que sustentan el diseño del instrumento de diagnóstico y la metodología honeypot. Esta dimensión interviene en la operacionalización del constructo de madurez, en la validación de contenido del instrumento mediante el anclaje normativo de cada reactivo a estándares internacionales, y en la interpretación cualitativa de los hallazgos diagnósticos. La articulación de ambas dimensiones permite que el trabajo conserve el rigor cuantitativo propio de los estudios de medición de impacto y, simultáneamente, el sustento conceptual y normativo que el objeto de estudio requiere para que sus hallazgos sean defendibles y replicables.

**Nivel o alcance**

La investigación se desarrolla en un nivel descriptivo-correlacional. La dimensión descriptiva caracteriza la situación actual de la gestión de incidentes en la institución bajo estudio, identificando los niveles de madurez observados en cada una de las catorce subdimensiones del proceso evaluado. Esta caracterización aporta el diagnóstico institucional que sustenta el cumplimiento del primer objetivo específico del trabajo.

La dimensión correlacional establece relaciones entre la implementación de la metodología honeypot y la mejora observada en los indicadores de gestión de incidentes. La comparación de los valores obtenidos en la fase de preprueba y en la fase de posprueba permite evaluar la asociación entre la aplicación de la propuesta y los cambios en las métricas de impacto, sin pretender establecer una relación causal estricta que exigiría un diseño experimental puro. La articulación de ambos niveles produce una comprensión integral del fenómeno estudiado, sustentando tanto el diagnóstico de la situación actual como la evaluación del impacto de la propuesta metodológica.

**Propósito**

La investigación es de carácter aplicado. Busca ofrecer una solución práctica y transferible para mejorar la gestión de incidentes en los servicios fiscales, contribuyendo con un modelo replicable y ajustado a estándares internacionales. Su orientación se concreta en directrices aplicables al fortalecimiento de los procesos institucionales, de modo que los resultados obtenidos no se limiten al plano teórico. El estudio se vincula directamente con la resolución de problemáticas reales del entorno organizacional analizado e incorpora lineamientos que pueden integrarse a las actividades de control, monitoreo y respuesta ante incidentes de la institución objeto de estudio.

**Ubicación temporal**

La investigación se ubica temporalmente en dos momentos diferenciados que estructuran su diseño. La fase diagnóstica adopta un corte transversal: el instrumento de diagnóstico de madurez se aplica a los informantes institucionales en un único momento del estudio, proporcionando una caracterización de la situación actual en un punto temporal definido. La fase de validación de la propuesta incorpora un segundo momento temporal, posterior a la aplicación de la metodología honeypot sobre el entorno controlado, lo que permite comparar los indicadores de impacto antes y después de la intervención. La estructura temporal no constituye un seguimiento longitudinal en sentido estricto, dado que no se observa la evolución continua del fenómeno a lo largo de un período prolongado. Se trata de dos cortes transversales sucesivos cuya comparación produce la evidencia del impacto de la metodología propuesta.

## 3.3 Universo o Población de Estudio

El universo de la investigación se compone de dos planos articulados, correspondientes a las dos fases del estudio.

El universo de la fase diagnóstica está constituido por el conjunto de procesos, prácticas y registros institucionales relacionados con la gestión de incidentes y la seguridad de la información en la institución bajo estudio, durante el período de referencia declarado por el instrumento. La unidad de análisis institucional es una entidad del rubro de servicios fiscales digitales del Estado Plurinacional de Bolivia, sobre la cual se aplica el cuestionario de diagnóstico distribuido por roles funcionales.

El universo de la fase de validación está constituido por los eventos de seguridad informática asociados a un portal fiscal digital, generados en un entorno controlado de laboratorio que reproduce las características operativas de un sistema fiscal real. Este universo abarca la totalidad de incidentes generados durante el período experimental, incluyendo intentos de intrusión, patrones de ataque y registros de actividad maliciosa. La elección del entorno simulado se justifica en la necesidad de evaluar la metodología propuesta sin comprometer la infraestructura real de la institución, manteniendo fidelidad con la dinámica de los servicios fiscales digitales bajo un marco seguro y experimental.

### 3.3.1 Determinación y Elección de la Muestra

La determinación de la muestra se realiza de manera diferenciada para cada fase del estudio, conforme a la naturaleza del universo correspondiente.

Para la fase diagnóstica se adopta un muestreo no probabilístico intencional. La muestra está integrada por catorce informantes designados conforme a los roles funcionales declarados en el instrumento, cada uno con responsabilidad y conocimiento directos sobre la subdimensión específica que evalúa. El criterio de selección responde a que las métricas operativas que el instrumento solicita (porcentajes de cobertura, tiempos de respuesta, registros operativos) no son uniformemente accesibles a todos los miembros de la organización, lo cual hace inviable un muestreo aleatorio. El estudio incluyó, asimismo, una muestra piloto de treinta respondentes heterogéneos para el cálculo del Coeficiente Alfa de Cronbach del instrumento, con propósitos psicométricos diferenciados de la aplicación institucional. La descripción detallada del piloto, sus criterios de selección y los resultados obtenidos figuran en el apartado 3.5.2.3.

Para la fase de validación de la propuesta se adopta un muestreo no probabilístico por conveniencia. La muestra corresponde al conjunto de eventos y registros obtenidos en un entorno de laboratorio durante un período definido de pruebas. Se seleccionan los escenarios y campañas de ataque disponibles y factibles de ejecutar en condiciones controladas, lo cual permite evaluar la eficacia de la metodología propuesta sobre un conjunto representativo de situaciones de amenaza documentadas en los marcos de referencia internacionales.

La Tabla [N° por asignar] sintetiza la comparación de los tipos de muestreo evaluados y la justificación de los criterios adoptados.

**Tabla [N° por asignar]**
*Comparación y justificación del tipo de muestreo adoptado*

| **Tipo de muestreo** | **Características principales** | **Aplicabilidad en la investigación** | **Justificación** |
| --- | --- | --- | --- |
| Probabilístico | Cada elemento de la población tiene la misma probabilidad de ser seleccionado. Garantiza representatividad estadística. | Se utiliza en estudios con poblaciones amplias, heterogéneas y accesibles en su totalidad. | No corresponde porque las poblaciones del estudio no son aleatorias, sino conjuntos delimitados de informantes con conocimiento específico (fase diagnóstica) y de escenarios definidos en laboratorio (fase de validación). |
| No probabilístico — Intencional | Selección dirigida por criterios técnicos del investigador. Se privilegia el acceso al dato relevante. | Se aplica cuando la información solicitada requiere informantes con responsabilidad o experticia específica. | Se adopta en la fase diagnóstica porque cada uno de los catorce instrumentos requiere un respondente con responsabilidad y acceso directos sobre la subdimensión evaluada. |
| No probabilístico — Por conveniencia | Selección de casos accesibles y factibles de obtener. Se prioriza la disponibilidad. | Permite focalizarse en escenarios de laboratorio reproducibles y registrables con facilidad. | Se adopta en la fase de validación porque los escenarios de ataque se eligen por su accesibilidad y pertinencia para evaluar la metodología propuesta. |

*Nota.* Elaboración propia, 2026.

## 3.4 Sujetos Vinculados a la Población

*[Identifique los actores clave vinculados a la investigación: usuarios del sistema, expertos consultados, stakeholders, etc. Describa su rol en el estudio.]*

La investigación involucra a un conjunto de sujetos vinculados al objeto de estudio cuya identificación es necesaria para precisar el alcance del trabajo y los procedimientos éticos que rigen su participación. Estos sujetos se agrupan en cuatro categorías diferenciadas por la función que cumplen dentro del proceso investigativo.

La primera categoría corresponde al investigador. La conducción del estudio, el diseño del instrumento, la aplicación institucional del cuestionario y el procesamiento de los datos obtenidos.

La segunda categoría reúne a los catorce informantes institucionales que responden el instrumento de diagnóstico durante la fase de aplicación al objeto de estudio. Estos informantes son funcionarios designados conforme a los roles funcionales descritos en el apartado 3.5.2.1, cada uno con responsabilidad directa sobre la subdimensión que evalúa el instrumento asignado. Su participación se limita a la respuesta del cuestionario y a la entrega de los documentos institucionales de respaldo correspondientes, en condiciones de confidencialidad sobre la identidad individual del respondente y con el compromiso explícito de que los datos recolectados se emplean únicamente para los fines diagnósticos del presente trabajo.

La tercera categoría comprende a los treinta respondentes del piloto de confiabilidad del instrumento. Estos participantes se vincularon al estudio con el propósito específico de aportar la base empírica para el cálculo del Coeficiente Alfa de Cronbach, conforme a lo descrito en el apartado 3.5.2.3. Su participación fue voluntaria, anónima y no requirió la entrega de información institucional específica.

La cuarta categoría involucra a los operadores del entorno experimental durante la fase de validación de la propuesta. Esta función la asume el investigador, con el apoyo técnico necesario para el despliegue del laboratorio, la ejecución de las campañas de ataque controladas y la captura de los registros de actividad maliciosa. El entorno experimental no involucra a terceros ajenos al equipo técnico del estudio.

El tratamiento de los datos recolectados durante el trabajo se rige por los principios de confidencialidad, integridad y uso restringido a los fines declarados. La identidad de los informantes institucionales no se hace pública en ningún producto derivado del estudio. La institución bajo análisis se referencia por su rubro y no por su denominación legal, conforme al criterio de protección de información institucional sensible aplicable a entidades del Estado Plurinacional de Bolivia.

## 3.5 Fuentes y Diseño de los Instrumentos de Relevamiento de Información

### 3.5.1 Fuentes de la Investigación

**Tipología y enfoque general de las fuentes**

La presente investigación se nutre de dos tipos complementarios de fuentes de información, organizadas conforme a la clasificación metodológica estándar entre fuentes primarias y fuentes secundarias. Las fuentes primarias corresponden a los datos originales generados específicamente para los fines del estudio, recolectados a través del instrumento de diagnóstico y de los respaldos documentales que lo acompañan. Las fuentes secundarias agrupan el material previamente publicado que sustenta el marco conceptual, normativo y legal sobre el que se construye el trabajo.

La articulación de ambos tipos de fuentes responde a una lógica metodológica precisa. Las fuentes secundarias proveen el cuerpo doctrinal y normativo que define los conceptos, las prácticas estándar y los criterios de medición empleados en la investigación. Las fuentes primarias proveen la evidencia empírica que permite caracterizar la situación actual del problema en la institución analizada y comparar esa situación con los parámetros documentados por las fuentes secundarias. La distancia entre ambos planos es la que produce el diagnóstico de madurez que la investigación se propone construir.

El diseño del instrumento sobre el que se recolectan las fuentes primarias y los procedimientos de validez y confiabilidad que sustentan su aplicabilidad se desarrollan en los apartados posteriores del capítulo.

**Fuentes primarias**

Las fuentes primarias de la investigación corresponden a los datos originales producidos específicamente para sustentar el diagnóstico institucional perseguido. Estos datos se obtienen mediante tres vías complementarias que, en conjunto, configuran la base empírica del trabajo.

La primera vía corresponde a la aplicación institucional del instrumento de diagnóstico. Los catorce informantes designados por rol funcional, descritos en el apartado 3.5.2.1, responden el cuestionario completo sobre la realidad operativa de la institución bajo estudio. Cada respuesta produce un puntaje cuantitativo entre 0 y 4 sobre el ítem correspondiente. El conjunto de cuarenta y dos respuestas conforma la matriz central de datos sobre la cual se calcula la madurez por instrumento, por grupo y a nivel global de la institución.

Una segunda vía proviene de la aplicación piloto del instrumento sobre treinta respondentes heterogéneos. Esta aplicación, descrita en el apartado 3.5.2.3, se realizó con propósitos psicométricos y no diagnósticos: produce la evidencia empírica que sustenta el Coeficiente Alfa de Cronbach reportado para la confiabilidad del cuestionario. Aun cuando los datos del piloto no integran el diagnóstico institucional, sí integran las fuentes primarias del estudio en cuanto constituyen datos originales recolectados para fines metodológicos definidos.

Los documentos institucionales aportados como respaldo de cada respuesta conforman la tercera vía. Estos documentos incluyen reportes operativos, registros de sistemas de monitoreo, actas de comités, políticas internas, contratos de servicio y cualquier otro artefacto institucional que sustente el dato declarado por el respondente. Los documentos cumplen una función dual. Evidencian la veracidad de cada puntaje asignado al ítem correspondiente y constituyen el material de contraste sobre el cual el investigador valida o cuestiona la respuesta declarada durante la fase de análisis de los resultados.

La conjunción de estas tres vías garantiza que cada afirmación diagnóstica del trabajo pueda rastrearse a un dato original recolectado, a una propiedad psicométrica acreditada o a un documento institucional verificable. Esa trazabilidad de las fuentes primarias hasta su origen empírico es la que sostiene la legitimidad del diagnóstico que la investigación se propone construir.

**Fuentes secundarias**

Las fuentes secundarias de la investigación corresponden al material previamente publicado que sustenta el marco conceptual, normativo y legal sobre el que se construye el trabajo. Se agrupan en tres categorías diferenciadas por la naturaleza del aporte que cada una realiza al estudio.

La primera categoría comprende los estándares internacionales sobre gestión de incidentes y seguridad de la información que operan como referencia normativa del instrumento de diagnóstico. Esta categoría incluye la familia ISO/IEC (27001:2022, 27005, 27035 partes 1, 2 y 4, 27037, 27041, 27042 y 27050), las publicaciones del National Institute of Standards and Technology (NIST SP 800-61 y NIST SP 800-92), los benchmarks operativos publicados en el SANS SOC Survey, los niveles de servicio estándar del marco ITIL y los modelos de madurez documentados en CMMI y COBIT. El detalle del anclaje de cada reactivo del instrumento a la cláusula o sección específica de estos estándares figura en el apartado 3.5.2.2 y en el Anexo correspondiente.

Una segunda categoría reúne la literatura académica revisada sobre los campos disciplinares en los que se inscribe la investigación. Esta categoría agrupa publicaciones especializadas en ciberseguridad aplicada a entidades públicas, gestión de incidentes de seguridad de la información, modelos de madurez en seguridad y administración tributaria digital. El conjunto bibliográfico revisado se sistematiza en el Capítulo II del presente trabajo y se referencia íntegramente en la sección de Referencias.

El marco legal nacional aplicable al objeto de estudio conforma la tercera categoría. Esta categoría incluye la Ley N° 164 de 2011 (Ley General de Telecomunicaciones, Tecnologías de Información y Comunicación), el Decreto Supremo N° 1793 de 2013 (reglamentario de la Ley N° 164), el Decreto Supremo N° 2514 de 2015 (que crea la Agencia de Gobierno Electrónico y Tecnologías de Información y Comunicación y el Centro de Gestión de Incidentes Informáticos), y la Ley N° 2492 de 2003 (Código Tributario Boliviano). El detalle del análisis legal y de las atribuciones que cada norma confiere a la institución bajo estudio se desarrolla en el apartado 2.3 del Marco Teórico.

Las tres categorías de fuentes secundarias cumplen funciones distintas pero articuladas. Los estándares internacionales definen las prácticas de referencia y los criterios cuantitativos contra los que se mide la situación institucional. La literatura académica sustenta los marcos conceptuales empleados en la operacionalización de las variables y en la interpretación de los hallazgos. El marco legal nacional delimita las obligaciones y atribuciones de la institución bajo estudio. Su aporte complementa, en el plano normativo doméstico, el sustento técnico de los estándares internacionales. La articulación de las tres categorías produce el marco de referencia completo sobre el cual la investigación construye su análisis.

### 3.5.2 Diseño de los Instrumentos de Relevamiento de Información

El diseño del instrumento principal de relevamiento de información se documenta en tres componentes articulados. La descripción técnica define la estructura del cuestionario, su sistema de medición, su aplicación por roles funcionales y las limitaciones reconocidas de su construcción. La validez de contenido acredita que el conjunto de reactivos cubre íntegramente el constructo medido y se sustenta en estándares internacionales documentados. La confiabilidad, calculada mediante el Coeficiente Alfa de Cronbach sobre el piloto, acredita la consistencia interna de los reactivos al ser respondidos por una muestra heterogénea de informantes. Ningún instrumento puede considerarse metodológicamente operativo sin la triangulación entre su descripción técnica, la validez de su contenido y la confiabilidad de su medición.

#### 3.5.2.1 Descripción del Instrumento de Diagnóstico

**Naturaleza y enfoque del instrumento**

El instrumento de relevamiento de información empleado en esta investigación es un cuestionario estructurado de autoinforme con respaldo documental. Se diseñó como índice de madurez para diagnosticar la situación actual de la gestión de incidentes y de la seguridad de la información en el escenario institucional bajo estudio. La denominación adoptada para el documento es Instrumento de Diagnóstico de Madurez en Seguridad de la Información, en versión neutral. Esa neutralidad significa que la redacción del cuestionario no contiene referencias específicas a la institución analizada ni a la solución tecnológica que esta tesis propone; el instrumento puede aplicarse, en consecuencia, a cualquier entidad del rubro de servicios fiscales digitales sin sesgo hacia un resultado predeterminado.

La elección de un cuestionario estructurado responde a la coherencia metodológica del trabajo. El enfoque cuantitativo declarado en el apartado 3.1 exige instrumentos que produzcan mediciones numéricas comparables. Sobre el alcance descriptivo declarado en el apartado 3.2 recae la obligación de caracterizar la situación actual del problema sin manipular variables. El objetivo específico que esta sección operacionaliza apunta a diagnosticar el estado de madurez institucional al momento del estudio. Un cuestionario de selección única con escala ordinal cumple las tres condiciones de manera directa: produce datos cuantificables, no manipula variables y permite caracterizar el estado actual de cada dimensión evaluada.

La modalidad de autoinforme se complementa con un mecanismo de respaldo documental que opera como contrapeso al sesgo conocido de este tipo de instrumentos. Cada respondente debe sustentar la respuesta seleccionada en la fuente del dato (reporte, registro o sistema institucional) a través de una columna específica del cuestionario. La sustentación se refuerza con la entrega obligatoria de al menos un documento de respaldo por cada uno de los catorce instrumentos que componen el cuestionario. Esta combinación reduce el margen de respuesta no comprobable y produce evidencia trazable para cada puntaje reportado.

**Estructura del instrumento y trazabilidad con el objetivo**

La estructura del instrumento materializa la operacionalización de la variable central de la investigación: la madurez en seguridad de la información orientada a la gestión de incidentes. Esa operacionalización se despliega en una arquitectura jerárquica de tres niveles. Los cuatro grupos del cuestionario funcionan como las dimensiones de la variable. Cada grupo se descompone en instrumentos funcionales que representan sus subdimensiones, sumando catorce en total. Dentro de cada instrumento, los ítems individuales actúan como indicadores cuantitativos que permiten calcular la madurez observada en cada subdimensión; el cuestionario completo contiene cuarenta y dos.

La distribución de instrumentos e ítems por grupo ya fue presentada en el apartado 3.5.2.2 (Tabla [N° por asignar]), donde se muestra que la variable queda cubierta por trece reactivos del grupo de gestión de incidentes, ocho del grupo de evidencias y respaldo, doce del grupo de controles técnicos y nueve del grupo de gestión organizacional. Cada uno de esos reactivos mide un indicador concreto a través de una fórmula cuantitativa única. Ningún ítem queda sin métrica observable, y ninguna métrica queda sin un reactivo que la registre.

La trazabilidad entre la estructura del instrumento y el Objetivo Específico 1 de la investigación se hace explícita al examinar la contribución diagnóstica de cada grupo. El Objetivo Específico 1 consiste en diagnosticar la situación actual de la gestión de incidentes y de la madurez en seguridad de la información en la institución bajo estudio. Cada grupo aporta una pieza específica de ese diagnóstico. La Tabla [N° por asignar] presenta esa trazabilidad en términos operativos.

**Tabla [N° por asignar]**
*Trazabilidad entre la estructura del instrumento y el Objetivo Específico 1*

| **Grupo (dimensión)** | **Subdimensiones (instrumentos)** | **Contribución al Objetivo Específico 1** |
| --- | --- | --- |
| G1 — Gestión de incidentes | Instrumentos 1 a 4 | Mide el núcleo del objeto de estudio: ciclo completo de detección, clasificación, respuesta y lecciones aprendidas |
| G2 — Evidencias y respaldo | Instrumentos 5 a 7 | Sustenta la dimensión forense del proceso: integridad, custodia y recuperabilidad de las evidencias generadas durante el ciclo de incidentes |
| G3 — Seguridad y controles técnicos | Instrumentos 8 a 11 | Aporta el contexto preventivo: superficie de ataque institucional que incide sobre la frecuencia y la gravedad de los incidentes |
| G4 — Gestión organizacional y mejora | Instrumentos 12 a 14 | Captura la capacidad organizacional (gestión de riesgos, capacitación y mejora continua) que sostiene la operación del proceso |

*Nota.* La descripción detallada de cada uno de los catorce instrumentos, con sus roles funcionales asignados y sus normas de referencia, figura en el Anexo [N° por asignar].

El conjunto de las cuatro dimensiones cubre el constructo medido sin fugas ni redundancias. El Grupo 1 atiende la respuesta operativa al incidente cuando ya ocurrió. El Grupo 2 se ocupa de las evidencias que ese incidente genera y que sostienen su trazabilidad posterior. Los Grupos 3 y 4 cubren un terreno previo: las condiciones que determinan cuántos incidentes ocurren y con qué gravedad. La medición conjunta de las cuatro dimensiones permite diagnosticar el estado de madurez institucional como un sistema, y no como una suma de partes aisladas. Por esa propiedad el instrumento responde, en su totalidad, al Objetivo Específico 1 de la investigación.

**Sistema de medición y calificación**

El sistema de medición del instrumento opera sobre una escala ordinal descendente de cinco puntos aplicada de manera homogénea a los 42 reactivos. Cada ítem ofrece cinco opciones de respuesta cuantificadas, asignándose 4 puntos a la opción que representa el mayor nivel de cumplimiento de la métrica evaluada y 0 puntos a la que representa el menor nivel o la ausencia comprobada de la métrica. Entre ambos extremos se ubican los valores 3, 2 y 1, que reproducen niveles intermedios de cumplimiento documentados. La modalidad de respuesta es de selección única. Cada respondente elige exactamente una opción por ítem, sin combinaciones múltiples ni promedios entre rangos.

El período de referencia de la medición varía según la naturaleza del indicador. Por defecto, cada ítem evalúa el cumplimiento sobre los últimos noventa días anteriores al momento de la respuesta. Algunos reactivos se evalúan sobre períodos distintos cuando la métrica lo requiere: treinta días para indicadores operativos de alta frecuencia, tres meses para procesos de revisión técnica, seis meses para indicadores de custodia y respaldo y doce meses para evaluaciones de cobertura organizacional. El período aplicable está declarado dentro de cada ítem del cuestionario y no queda librado a la interpretación del respondente.

El cálculo del puntaje a nivel de instrumento se obtiene por suma directa de los puntos asignados a cada uno de sus ítems. El puntaje máximo de cada instrumento depende del número de reactivos que lo componen. La distribución es desigual: el Instrumento 1 alcanza un máximo de 16 puntos (cuatro ítems), el Instrumento 7 alcanza 8 puntos (dos ítems), y los doce instrumentos restantes alcanzan 12 puntos cada uno (tres ítems). El porcentaje de cumplimiento del instrumento se calcula como el cociente entre el puntaje obtenido y el puntaje máximo posible, multiplicado por cien. Esa transformación expresa el resultado de cada instrumento en una escala porcentual común de 0 a 100, lo cual permite comparar instrumentos con distinto número de ítems y referir todos los resultados al sistema unificado de niveles de madurez.

El porcentaje de cumplimiento se traduce en un nivel de madurez. La escala adoptada distingue cuatro categorías ordenadas. La Tabla [N° por asignar] presenta los cortes y la denominación de cada nivel.

**Tabla [N° por asignar]**
*Niveles de madurez según porcentaje de cumplimiento del instrumento*

| **Nivel de madurez** | **Rango de porcentaje de cumplimiento** |
| --- | --- |
| Inicial | 0 % ≤ % < 26 % |
| Básico | 26 % ≤ % < 51 % |
| Gestionado | 51 % ≤ % < 76 % |
| Optimizado | 76 % ≤ % ≤ 100 % |

*Nota.* La denominación de los cuatro niveles reproduce el patrón estándar de los modelos de madurez documentados en CMMI y COBIT, según se justifica en el apartado 3.5.2.2.

La agregación de resultados al nivel de grupo y al nivel global del instrumento se realiza por promedio aritmético. La madurez por grupo se calcula como el promedio del porcentaje de cumplimiento de los instrumentos que conforman el grupo. Para el nivel global del instrumento se aplica el mismo principio sobre los catorce porcentajes de instrumento, sin distinción de grupo. Esta agregación adopta una ponderación igualitaria entre instrumentos: cada instrumento contribuye con el mismo peso al resultado de su grupo, y cada grupo contribuye con el mismo peso al resultado global, independientemente del número de ítems que cada instrumento agrupe. La opción de aplicar pesos diferenciados se evaluó y se descartó. La asignación de pesos diferenciados requeriría un marco de criterios externos que la presente investigación no se propone establecer. La ponderación igualitaria funciona como criterio neutral y reproducible, alineado con la modalidad estándar de los índices de madurez documentados en la literatura del campo.

**Aplicación por roles funcionales**

La aplicación del instrumento se realiza por distribución funcional. Cada uno de los catorce instrumentos que componen el cuestionario se asigna al rol institucional con visibilidad directa sobre la subdimensión que mide. Esta decisión metodológica responde a la naturaleza del constructo. Las métricas que el instrumento solicita (porcentajes de cobertura, tiempos de respuesta, registros operativos) no son uniformemente accesibles a todos los miembros de la organización. Cada rol funcional gestiona una porción específica de la operación, dispone de la documentación correspondiente y posee la perspectiva necesaria para responder con propiedad sobre su dominio. La distribución por rol garantiza que cada respuesta provenga de la fuente institucional con conocimiento directo del indicador evaluado.

La Tabla [N° por asignar] presenta la correspondencia entre cada instrumento y el rol funcional al que se asigna.

**Tabla [N° por asignar]**
*Asignación de instrumentos a roles funcionales para la aplicación institucional*

| **Grupo** | **Instr.** | **Subdimensión** | **Rol funcional asignado** |
| --- | --- | --- | --- |
| G1 | 1 | Detección y registro de eventos | Encargado de monitoreo |
| G1 | 2 | Clasificación y evidencia de incidentes | Analista de incidentes |
| G1 | 3 | Respuesta y tiempos de atención | Líder de respuesta |
| G1 | 4 | Lecciones aprendidas y mejora | Coordinador de mejora |
| G2 | 5 | Integridad y custodia de evidencias | Encargado de evidencias |
| G2 | 6 | Respaldos y restauración de evidencias | Soporte técnico |
| G2 | 7 | Retención y acceso a evidencias | Administrador de repositorios |
| G3 | 8 | Accesos y mínimos privilegios | Responsable de infraestructura |
| G3 | 9 | Desarrollo seguro y validaciones | Responsable de desarrollo |
| G3 | 10 | Gestión de vulnerabilidades | Responsable de seguridad técnica |
| G3 | 11 | Integridad y trazabilidad de registros | Administrador de registros |
| G4 | 12 | Gestión de riesgos | Responsable de seguridad de la información |
| G4 | 13 | Capacitación y cobertura | Tecnologías de la Información |
| G4 | 14 | Métricas y mejora continua | Jefatura de seguridad |

*Nota.* Cuando la institución no cuente con la denominación exacta del rol, el instrumento debe ser respondido por la persona que desempeñe la función equivalente, registrándose el cargo formal en la columna de identificación del cuestionario.

El criterio de selección de los informantes es no probabilístico intencional. Cada uno de los catorce instrumentos requiere un respondente con responsabilidad y conocimiento directos sobre la subdimensión evaluada. Un muestreo aleatorio entre el conjunto de funcionarios de la institución produciría informantes sin acceso a la información solicitada o sin capacidad de sustentar documentalmente sus respuestas. Los criterios de inclusión adoptados exigen que cada informante ocupe el rol designado en la Tabla anterior o desempeñe una función institucional equivalente, y que disponga de los registros operativos necesarios para sustentar las respuestas conforme al mecanismo de respaldo documental descrito previamente.

**Control de sesgos y respaldo documental**

Los instrumentos de autoinforme conllevan un riesgo conocido en la literatura metodológica. El respondente puede seleccionar la opción que mejor preserva la imagen institucional o personal en lugar de la opción que mejor describe la realidad operativa medida. Para reducir ese riesgo a niveles defendibles en el presente trabajo, el instrumento incorpora tres mecanismos de control que operan en planos complementarios.

El primer mecanismo es la exigencia de justificación documental dentro del propio reactivo. Cada ítem incluye una columna específica donde el respondente debe registrar la fuente del dato que sustenta la opción seleccionada. La fuente declarada puede ser un reporte, un registro institucional, una salida de un sistema de monitoreo o cualquier otro respaldo verificable. La columna no afecta el puntaje numérico que se asigna al ítem. Sí permite al investigador rastrear el origen de cada respuesta y descartar aquellas cuya fuente declarada no resulte coherente con la métrica evaluada.

Una segunda capa de control proviene del respaldo documental obligatorio por instrumento. Cada conjunto de tres o cuatro ítems pertenecientes a un mismo instrumento debe acompañarse de al menos un documento institucional que evidencie el dato reportado. Esta obligación impide que las respuestas permanezcan en el plano declarativo. El investigador puede examinar el documento, contrastarlo con la opción seleccionada y referenciarlo durante la fase de análisis de resultados. La combinación de justificación por ítem y respaldo por instrumento construye una doble capa de evidencia documental sobre la totalidad de las respuestas obtenidas.

El tercer mecanismo opera en un plano distinto y complementa a los dos anteriores. La validez de contenido del instrumento, sustentada en la tabla de especificaciones normativas descrita en el apartado 3.5.2.2, asegura que ningún reactivo es producto de la apreciación subjetiva del investigador y reduce el sesgo de diseño. La confiabilidad del instrumento, acreditada por el Coeficiente Alfa de Cronbach en el apartado 3.5.2.3, asegura que los ítems se comportan de manera consistente al ser respondidos por una muestra heterogénea de informantes. Esta consistencia permite descartar que el cuestionario produzca lecturas erráticas por defectos de redacción o de escala.

#### 3.5.2.2 Validez del Instrumento

**Concepto de validez adoptado**

La validez de un instrumento de medición se entiende, en el presente trabajo, como la propiedad que sostiene que el cuestionario efectivamente mide la variable que dice medir y no otra. La validez es distinta de la confiabilidad: una se ocupa del qué se mide, la otra del con qué estabilidad se mide. Un instrumento puede ser muy confiable sin ser válido (si mide consistentemente algo distinto de lo que pretende) y puede tener cierta validez aparente sin alcanzar consistencia suficiente. Por ese motivo, ambas evidencias se reportan en este capítulo como condiciones complementarias y mutuamente necesarias para acreditar la calidad métrica del Instrumento de Diagnóstico de Madurez en Seguridad de la Información.

La literatura metodológica distingue tres modalidades clásicas de validez: validez de contenido, validez de criterio y validez de constructo. La validez de criterio compara los resultados del instrumento con una medida externa de referencia y se justifica en estudios de carácter predictivo. La validez de constructo verifica que el instrumento opere conforme a la teoría que sustenta la variable latente, y se aborda habitualmente con análisis factoriales sobre muestras de tamaño considerable. La validez de contenido evalúa que el conjunto de reactivos del instrumento cubra de manera representativa el dominio teórico y normativo de la variable medida, sin excluir aspectos relevantes ni introducir reactivos ajenos al constructo.

Para esta investigación la modalidad relevante es la validez de contenido. La justificación de esa elección descansa en tres argumentos. El instrumento es de carácter diagnóstico y no predictivo, lo cual deja fuera de propósito a la validez de criterio. La variable latente, definida como el nivel de madurez en gestión de incidentes, está operacionalmente delimitada por los estándares internacionales que la disciplinan (ISO/IEC 27001:2022, ISO/IEC 27005, ISO/IEC 27035 y las normas conexas de la familia forense ISO/IEC), de modo que la validez de constructo queda en gran medida sostenida desde el propio anclaje normativo del instrumento sin requerir análisis factoriales adicionales. La pregunta metodológicamente decisiva para un cuestionario de diagnóstico institucional es, en cambio, si sus 42 reactivos cubren íntegra y proporcionadamente el dominio del proceso de gestión de incidentes, asunto que solo la validez de contenido permite responder de manera directa.

**Estrategia de validación adoptada**

La validación del instrumento aplicado en esta investigación se sustenta en dos evidencias complementarias. La validez de contenido del cuestionario queda documentada en una tabla de especificaciones normativas que vincula explícitamente cada uno de los 42 reactivos con su dimensión, su indicador cuantitativo y un estándar internacional que respalda su formulación. La confiabilidad se acredita por separado, mediante el Coeficiente Alfa de Cronbach calculado sobre la aplicación efectiva del instrumento a 30 respondentes durante la fase piloto. Articuladas, ambas evidencias configuran una arquitectura de validación bipartita. Cada propiedad psicométrica del instrumento se sustenta en su propio procedimiento, sin depender del juicio subjetivo del investigador ni de un panel externo de expertos. El presente apartado describe la primera evidencia; la segunda se desarrolla en el apartado 3.5.2.3.

Para acreditar la validez de contenido se consideraron tres alternativas metodológicas durante la fase de diseño del instrumento. La primera proponía someterlo a juicio de expertos cuantificado mediante el coeficiente V de Aiken. La segunda planteaba sostener la validez exclusivamente con el Alfa de Cronbach. Una tercera vía proponía construir una tabla de especificaciones que vinculara cada reactivo con la dimensión que mide y con un estándar internacional que lo respalde, sin recurrir a expertos externos. Esa tercera vía es la que finalmente se adoptó.

Las dos primeras alternativas se descartaron por razones precisas. El recurso al juicio de expertos introducía limitaciones. La conformación de un panel especializado requiere tiempos y costos que no se ajustan a las condiciones operativas del presente estudio, y la justificación formal de las credenciales del panel demanda procedimientos de tipo Delphi cuya aplicación excede el alcance del trabajo. Apoyarse exclusivamente en el Alfa de Cronbach resulta igualmente insuficiente. El coeficiente acredita confiabilidad, no validez de contenido. No alcanza, en consecuencia, para sostener que los reactivos cubren adecuadamente el dominio teórico y normativo de la variable medida. El Alfa de Cronbach se conserva, sí, como segunda evidencia del blindaje bipartito anunciado al inicio del apartado, pero no como soporte único de la validez del instrumento.

La estrategia adoptada se materializa en un único instrumento documental: la tabla de especificaciones normativas del cuestionario. Esa tabla vincula cada uno de los 42 ítems con dos atributos críticos. Uno es la estructura interna del constructo, expresada como la cadena grupo → instrumento → indicador a la que cada reactivo se adscribe. Este componente demuestra que el conjunto de ítems cubre íntegramente las dimensiones del proceso de gestión de incidentes sin omitir aspectos relevantes ni introducir redundancias entre reactivos. El otro atributo es el respaldo normativo externo de cada reactivo, expresado como la cláusula o sección de un estándar internacional documentado que justifica la pertinencia y la formulación del ítem. Este componente garantiza que el contenido del instrumento no proviene de la apreciación subjetiva del investigador, sino de definiciones operativas avaladas por la literatura normativa internacional del campo. La articulación de ambos atributos en un solo documento permite que la validez de contenido se verifique de manera trazable, ítem por ítem, sin necesidad de paneles externos ni de análisis factoriales adicionales.

La elección de esta estrategia responde a la naturaleza misma del instrumento. Se trata de un índice de madurez compuesto por subdimensiones heterogéneas y aplicado a un objeto institucional acotado. En ese escenario, la verificación documental de la cobertura del constructo y del respaldo normativo de cada ítem, sumada a la consistencia interna empíricamente demostrada sobre 30 respondentes, produce el respaldo metodológico más sólido y operativamente accesible. Ninguna de las dos evidencias depende del criterio del investigador ni de la calidad de un panel externo. Ambas se sustentan en evidencia verificable: documental en un caso, empírica en el otro. Esa es la propiedad que sostiene la validación bipartita del instrumento aplicado en este trabajo.

**Tabla de especificaciones del instrumento**

La tabla de especificaciones normativas del cuestionario es el documento sobre el que se sostiene la validez de contenido del instrumento. Su contenido vincula cada uno de los 42 reactivos con cuatro atributos descriptivos: el grupo temático al que pertenece, el instrumento al que se adscribe, el indicador cuantitativo con el que mide la dimensión correspondiente y el estándar internacional de referencia que respalda su formulación. Por su extensión, la tabla completa se incluye como Anexo [N° por asignar]. Este apartado se ocupa de su lectura estructural; el siguiente, de su lectura normativa.

La estructura del cuestionario se organiza en tres niveles jerárquicos. En el nivel superior se ubican los cuatro grupos temáticos que componen la variable medida. Cada grupo se descompone en un conjunto de instrumentos funcionales que cubren dominios específicos del proceso bajo evaluación. Esos instrumentos, a su vez, agrupan los reactivos individuales que materializan la medición cuantitativa. La distribución general de esta arquitectura se sintetiza en la siguiente tabla.

**Tabla [N° por asignar]**
Distribución de instrumentos e ítems por grupo temático del cuestionario

| **Grupo** | **Denominación del grupo** | **Instrumentos** | **Ítems** |
| --- | --- | --- | --- |
| G1 | Gestión de incidentes | 4 | 13 |
| G2 | Evidencias y respaldo | 3 | 8 |
| G3 | Seguridad y controles técnicos | 4 | 12 |
| G4 | Gestión organizacional y mejora | 3 | 9 |
| **—** | **Total** | **14** | **42** |

*Nota.* La distribución detallada ítem por ítem, con la denominación de cada instrumento, el indicador asociado y la referencia normativa, figura en el Anexo [N° por asignar].

La construcción de la tabla siguió un procedimiento descendente. Se partió de la variable latente del estudio (el nivel de madurez en la gestión de incidentes de servicios fiscales digitales) y se derivaron los grupos temáticos a partir de la literatura normativa internacional sobre el dominio. Cada grupo se descompuso luego en los instrumentos funcionales que cubren las fases operativas del proceso de respuesta a incidentes (detección, clasificación, respuesta, lecciones aprendidas) y los dominios contextuales de seguridad preventiva y gobernanza institucional que inciden sobre la frecuencia y la gravedad de los incidentes. Para cada instrumento se redactaron entre dos y cuatro reactivos cuantitativos, asegurando que cada ítem midiera una característica observable mediante una métrica documentada en su columna correspondiente, y no mediante términos genéricos sujetos a la interpretación del respondente.

La lectura estructural de la tabla aporta una evidencia central a la validez de contenido: la cobertura íntegra del constructo. Al recorrer la columna de instrumentos se verifica que el cuestionario abarca las dimensiones centrales del proceso de gestión de incidentes (detección, registro, clasificación, respuesta y lecciones aprendidas) sin omitir fases relevantes. Incorpora además los dominios contextuales que el constructo requiere para una medición integral en el escenario institucional analizado. La columna del indicador refuerza este resultado. Muestra que cada ítem mide una característica observable y cuantificable, expresada como una fórmula concreta, lo que reduce el margen de interpretación subjetiva.

**Anclaje normativo de los reactivos**

La lectura normativa de la tabla de especificaciones se centra en la columna que vincula cada reactivo con un estándar internacional documentado. Esta lectura aporta la evidencia que sostiene la validez externa del contenido del instrumento. Ningún ítem es producto de la apreciación personal del investigador. Cada reactivo deriva su pertinencia y su formulación de una cláusula o sección concreta de una norma de referencia, de modo que el contenido del cuestionario puede rastrearse íntegramente hasta su fuente normativa.

El anclaje normativo opera en dos capas independientes que se refuerzan mutuamente. La primera capa vincula cada uno de los 42 reactivos con uno o más estándares de la familia ISO/IEC. La segunda capa vincula los rangos cuantitativos de calificación, esto es, los cortes que delimitan los niveles de madurez de 0 a 4, con benchmarks operativos documentados en la literatura del campo.

La primera capa, correspondiente al anclaje ítem-norma, se documenta en la columna "Norma de referencia" de la tabla de especificaciones. La estructura del anclaje refleja la lógica del constructo medido. Los grupos vinculados al proceso de gestión de incidentes y al manejo de evidencias se anclan principalmente a la familia ISO/IEC 27035 (partes 1, 2 y 4) y a la familia forense ISO/IEC 27037, 27041, 27042 y 27050. En los grupos vinculados a controles técnicos de seguridad, el anclaje se desplaza a controles específicos del estándar ISO/IEC 27001:2022 (controles A.5.17, A.5.30, A.6.3, A.8.15, A.8.16, A.8.23 y A.10.1). Para el grupo de gestión organizacional y de gestión de riesgos, el anclaje recae en ISO/IEC 27005 y en los controles A.6.3 y A.10.1 de ISO/IEC 27001:2022. La Tabla [N° por asignar] sintetiza esta distribución por grupo temático.

**Tabla [N° por asignar]**
Anclaje normativo de los reactivos por grupo temático (capa ítem-norma)

| **Grupo** | **Estándares ISO/IEC de referencia** |
| --- | --- |
| G1 — Gestión de incidentes | ISO/IEC 27035-1, 27035-2 y 27035-4; ISO/IEC 27001:2022 (A.5.30, A.8.15, A.8.16) |
| G2 — Evidencias y respaldo | ISO/IEC 27037, 27041, 27042 y 27050; ISO/IEC 27001:2022 (A.5.30, A.8.15, A.8.16) |
| G3 — Seguridad y controles técnicos | ISO/IEC 27001:2022 (A.5.17, A.8.16, A.8.23) |
| G4 — Gestión organizacional y mejora | ISO/IEC 27005; ISO/IEC 27001:2022 (A.6.3, A.10.1); ISO/IEC 27035-4 |

*Nota.* La referencia específica de cada uno de los 42 ítems al control o cláusula correspondiente figura en el Anexo [N° por asignar].

La calibración cuantitativa de los rangos constituye la segunda capa del anclaje, declarada en la ficha técnica del instrumento. Esta capa establece que los cortes que separan los cinco niveles ordinales de calificación (de 0 a 4) no son arbitrarios ni reflejan apreciaciones del investigador, sino que derivan de fuentes documentadas para cada tipo de métrica. Los porcentajes de completitud y cobertura se calibran contra las recomendaciones de NIST SP 800-92 sobre gestión de registros y el control A.8.15 de ISO/IEC 27001:2022. Para los tiempos de detección, registro y respuesta, la referencia operativa es NIST SP 800-61 sobre manejo de incidentes, complementada por los benchmarks publicados en el SANS SOC Survey. La disponibilidad de servicios se evalúa contra los niveles SLA estándar del marco ITIL para la gestión de servicios de TI. La propia escala ordinal de cinco niveles, que estructura el sistema de calificación del instrumento, reproduce el patrón de los modelos de madurez documentados en CMMI y COBIT, coherente con la secuencia Inicial, Básico, Gestionado y Optimizado. La Tabla [N° por asignar] sintetiza esta segunda capa.

**Tabla [N por asignar]**

Calibración normativa de los rangos cuantitativos del instrumento (capa rango-benchmark)

| **Tipo de métrica calibrada** | **Fuente normativa de referencia** |
| --- | --- |
| Porcentajes de completitud y cobertura | NIST SP 800-92; ISO/IEC 27001:2022 (A.8.15) |
| Tiempos de detección, registro y respuesta | NIST SP 800-61; SANS SOC Survey |
| Disponibilidad de servicios | Niveles SLA estándar conforme a ITIL |
| Escala ordinal de cinco niveles (4 a 0) | Modelos de madurez CMMI y COBIT |

*Nota.* La declaración íntegra de las fuentes de calibración figura en la ficha técnica del Instrumento de Diagnóstico de Madurez (Anexo [N° por asignar]).

La combinación de ambas capas configura una arquitectura de anclaje normativo de alcance completo. Ningún componente del instrumento, ni los reactivos ni los rangos que estructuran sus opciones de respuesta, queda librado al criterio. La pertinencia de cada ítem se sostiene en una norma internacional, y la calibración cuantitativa de sus opciones de respuesta se sostiene en un benchmark operativo documentado. Esa propiedad permite afirmar que la validez de contenido del instrumento no se construye desde adentro del trabajo, sino que se importa desde el cuerpo normativo del campo de la seguridad de la información y de la gestión de servicios de TI.

**Síntesis y declaración de validez del instrumento**

Los apartados precedentes documentan, desde dos ángulos distintos pero convergentes, la validez de contenido del Instrumento de Diagnóstico de Madurez en Seguridad de la Información. La lectura estructural de la tabla de especificaciones demuestra que el cuestionario cubre íntegramente las dimensiones del proceso de gestión de incidentes, distribuidas en cuatro grupos temáticos, catorce instrumentos funcionales y cuarenta y dos reactivos cuantitativos, sin omisiones ni redundancias relevantes. La lectura normativa de la misma tabla, complementada con la ficha técnica del instrumento, demuestra que tanto la formulación de los ítems como la calibración de sus rangos de calificación se sustentan en estándares internacionales documentados de la familia ISO/IEC, NIST, SANS, ITIL, CMMI y COBIT.

Esta evidencia de validez de contenido se articula con la evidencia de confiabilidad acreditada en el apartado 3.5.2.3, donde el Coeficiente Alfa de Cronbach calculado sobre la aplicación efectiva del instrumento a 30 respondentes arrojó un valor de 0,869, ubicado en el rango Bueno de la escala convencional de interpretación. Ambas evidencias configuran la arquitectura de validación bipartita anunciada al inicio del presente apartado. Cada propiedad psicométrica del instrumento se sustenta en su propio procedimiento específico y verificable. La validez de contenido se respalda documentalmente en la tabla de especificaciones normativas; la confiabilidad se respalda empíricamente en el cálculo del coeficiente sobre datos reales del piloto.

En consecuencia, el Instrumento de Diagnóstico de Madurez en Seguridad de la Información se declara validado para su aplicación en la fase diagnóstica de la presente investigación. La validez de su contenido y la consistencia interna de sus reactivos quedan documentadas mediante procedimientos verificables, trazables a sus respectivas fuentes. Ningún componente del instrumento depende del juicio subjetivo. Esa propiedad sostiene su aplicabilidad en el escenario institucional bajo estudio y autoriza el uso de sus resultados como base diagnóstica del nivel de madurez en la gestión de incidentes de servicios fiscales digitales.

#### 3.5.2.3 Confiabilidad del Instrumento

**Concepto y elección del coeficiente**

La confiabilidad del instrumento se entiende como la propiedad que asegura que sus ítems midan de manera coherente y estable la variable a la que están asignados. Esto es, como consistencia interna del conjunto de reactivos. La cualidad es estadística y distinta de la validez de contenido: una mide qué tan establemente responde el instrumento cuando se aplica, la otra mide qué tan bien representa el dominio teórico de la variable.

El Instrumento de Diagnóstico de Madurez en Seguridad de la Información está integrado por k = 42 ítems, organizados en cuatro grupos y catorce instrumentos, calificados sobre una escala ordinal de cinco puntos (0 a 4) que traduce niveles de madurez. Para una construcción de estas características corresponde el Coeficiente Alfa de Cronbach, que es el estadístico aceptado para instrumentos de autoinforme con escalas politómicas ordenadas tipo Likert. Su uso aquí se justifica por tres razones operativas. El coeficiente acepta una sola aplicación del cuestionario, condición indispensable en una entidad pública de servicios fiscales donde no resulta factible repetir la medición en momentos diferenciados. La escala 0–4 satisface el supuesto métrico que el estadístico requiere. Y su difusión en investigaciones sobre madurez en ciberseguridad y gestión de incidentes facilita la comparabilidad de resultados con estudios afines del campo.

El Alfa de Cronbach mide confiabilidad, no validez. La validez de contenido del instrumento se sustenta en una tabla de especificaciones que vincula cada ítem con su variable, dimensión e indicador, reforzada por el anclaje normativo de cada reactivo a la familia de estándares ISO/IEC (27001:2022, 27005, 27035, 27037, 27041, 27042 y 27050). El procedimiento se desarrolla en el apartado 3.5.2.2. El Alfa de Cronbach se reporta entonces como evidencia complementaria de consistencia interna, no como sustituto de la validación de contenido. La distinción es metodológicamente relevante porque el instrumento se concibe como un índice de madurez con subdimensiones heterogéneas, característica que más adelante obliga a matizar el alcance del coeficiente global y a reconocer sus limitaciones específicas.

**Fórmula y parámetros de cálculo**

El cálculo del Coeficiente Alfa de Cronbach se realiza mediante la expresión

α = ( k / (k − 1) ) · ( 1 − Σ s²ᵢ / s²ₜ )

donde *k* es el número de ítems del instrumento, Σ s²ᵢ corresponde a la suma de las varianzas individuales de los *k* ítems y s²ₜ representa la varianza del puntaje total obtenido por cada respondente en el cuestionario completo. La lógica del estadístico es directa: cuanto mayor sea la consistencia con que los ítems se comportan en una misma dirección, menor será la suma de varianzas individuales respecto de la varianza del total, y mayor será el valor de α. El coeficiente queda acotado teóricamente entre 0 y 1; valores próximos al límite inferior suelen indicar respuestas erráticas o ítems mal redactados, mientras que valores muy próximos a 1 pueden señalar redundancia entre reactivos.

Para esta investigación se fijaron los siguientes parámetros de cálculo. El número de ítems es k = 42, correspondiente a la totalidad del Instrumento de Diagnóstico de Madurez en Seguridad de la Información aplicado en la fase piloto. Las varianzas se calcularon con el criterio muestral, dividiendo entre n − 1, donde n representa el número de respondentes válidos del piloto. La elección del denominador n − 1 obedece al carácter inferencial del piloto. La muestra de respondentes no agota la población de potenciales informantes y se asume como una observación a partir de la cual se estima la varianza poblacional. El criterio se mantuvo de manera homogénea tanto en el cálculo de las varianzas individuales por ítem como en la varianza del puntaje total, condición necesaria para que los términos del cociente sean comparables y el coeficiente resulte interpretable.

El procedimiento aritmético se ejecutó sobre la matriz de respuestas n × k construida durante la fase piloto, donde n indica el número de respondentes y k = 42 el número de columnas correspondientes a los ítems del instrumento. Cada celda contiene el valor 0, 1, 2, 3 o 4 asignado por el respondente al ítem respectivo, traducido directamente de la escala ordinal del cuestionario. El detalle de la matriz, las varianzas calculadas por ítem y el valor final del coeficiente se presentan más adelante en este mismo apartado y se respaldan documentalmente en el anexo correspondiente.

**Diseño y aplicación del piloto**

El piloto de confiabilidad se diseñó como una aplicación única del Instrumento de Diagnóstico de Madurez en Seguridad de la Información sobre una muestra no probabilística intencional. La elección de este tipo de muestreo responde al propósito del piloto. No se busca representar a una población general, sino verificar que los reactivos del instrumento sean comprendidos y respondidos de manera consistente por perfiles vinculados al objeto de estudio. Los criterios de inclusión exigieron que cada participante contara con experiencia laboral o académica en al menos una de tres áreas: gestión y operación de servicios fiscales digitales, seguridad de la información y gestión de incidentes, o desarrollo y administración de infraestructura informática. El tamaño definido para el piloto fue de n = 30 respondentes válidos, número considerado suficiente para una estimación inicial del Coeficiente Alfa de Cronbach en instrumentos de escala ordinal con k = 42 ítems.

La muestra integró tres perfiles funcionales complementarios. El primer perfil correspondió a personal institucional vinculado a servicios fiscales digitales, conformado por funcionarios del Servicio de Impuestos Nacionales (SIN) y profesionales de la empresa Libélula SRL, entidad tecnológica homologada por el SIN. Un segundo grupo reunió a profesionales del área de informática con experiencia activa en las funciones de desarrollo de software, seguridad de la información, administración de redes y soporte técnico. El tercer perfil incorporó a docentes del área de informática vinculados a la formación universitaria y de posgrado en seguridad y auditoría. La inclusión deliberada de perfiles heterogéneos persiguió un objetivo metodológico preciso. Si el instrumento solo se hubiera aplicado a un único perfil funcional, la consistencia interna observada habría reflejado las particularidades de ese subgrupo, sin evidenciar si los reactivos resultaban igualmente comprensibles para lectores con marcos de referencia distintos.

La aplicación del piloto se ejecutó entre los meses de mayo y junio de 2026 mediante un formulario digital autoadministrado, implementado en la plataforma Google Forms. Cada participante recibió por correo electrónico una invitación con el enlace al formulario, el propósito del estudio, las instrucciones de respuesta, la explicación de la escala 0–4 y la garantía de anonimato de los datos individuales. El formulario reprodujo la totalidad de los 42 ítems del instrumento sin alteraciones de redacción ni de orden respecto de la versión final aprobada. Las respuestas se exportaron en formato tabular, se depuraron eliminando registros incompletos y se trasladaron a la matriz n × k definida previamente para el cálculo del coeficiente. El formulario aplicado y la matriz de respuestas depuradas se incluyen en el anexo correspondiente.

**Criterios de interpretación**

La interpretación del Coeficiente Alfa de Cronbach se efectuó conforme a la escala convencional propuesta por George y Mallery (2003), ampliamente adoptada en la investigación con instrumentos de medición en ciencias sociales, administrativas y aplicadas a tecnologías de información. La escala distingue cinco rangos de calidad para el coeficiente, presentados en la Tabla [X].

**Tabla [X]**

Escala de interpretación del Coeficiente Alfa de Cronbach

| **Rango del coeficiente α** | **Calidad de la consistencia interna** |
| --- | --- |
| α ≥ 0,90 | Excelente |
| 0,80 ≤ α < 0,90 | Bueno |
| 0,70 ≤ α < 0,80 | Aceptable |
| 0,60 ≤ α < 0,70 | Cuestionable |
| α < 0,60 | Inaceptable |

*Nota.* Adaptado de George y Mallery (2003).

Para los propósitos de esta investigación se declaró como umbral mínimo de aceptación el valor de α ≥ 0,70, correspondiente al límite inferior del rango Aceptable. La elección de este corte responde a tres consideraciones convergentes. Es el umbral más extendido en la literatura metodológica sobre instrumentos psicométricos aplicados a las ciencias administrativas y a la investigación en seguridad de la información, lo cual facilita la comparabilidad del presente estudio con investigaciones afines del campo. Constituye, asimismo, el límite inferior aceptado para considerar que un instrumento exhibe consistencia interna suficiente para ser utilizado en fases diagnósticas o exploratorias como la que sustenta esta tesis. Permite, por último, reconocer como satisfactorios los coeficientes ubicados en rangos superiores, asignando una valoración progresivamente más fuerte a los valores que superan los cortes de 0,80 y 0,90.

En consecuencia, un coeficiente igual o superior a 0,70 se interpretó como evidencia de consistencia interna suficiente para validar la confiabilidad del Instrumento de Diagnóstico de Madurez en Seguridad de la Información. Los coeficientes que superaran el corte de 0,80, ubicándose en el rango Bueno, se considerarían además indicadores de una construcción metodológica sólida del instrumento; los que alcanzaran o superaran 0,90, ubicándose en el rango Excelente, se reportarían como evidencia de una consistencia interna óptima.

**Resultados del cálculo**

El cálculo del Coeficiente Alfa de Cronbach sobre la matriz de respuestas del piloto, ejecutado bajo los parámetros y la fórmula descritos previamente, arrojó un valor de α = 0,869 (0,87 con redondeo a dos decimales). La Tabla [Y] sintetiza los componentes del cálculo y el valor obtenido del coeficiente.

**Tabla [Y]**

Resultado del cálculo del Coeficiente Alfa de Cronbach del Instrumento de Diagnóstico de Madurez

| **Componente del cálculo** | **Valor** |
| --- | --- |
| Número de ítems (k) | 42 |
| Número de respondentes válidos (n) | 30 |
| Suma de varianzas individuales de los ítems (Σ s²ᵢ) | 65,27 |
| Varianza del puntaje total del cuestionario (s²ₜ) | 430,25 |
| Coeficiente Alfa de Cronbach (α) | 0,869 |
| Categoría según escala de interpretación | Bueno |

*Nota.* Cálculo realizado con varianzas muestrales (denominador n − 1). El detalle de la matriz de respuestas y el cómputo celda por celda figuran en el Anexo [Z].

El coeficiente obtenido supera el umbral mínimo declarado de 0,70 por 0,169 puntos, lo que equivale a un 24 % por encima del corte de aceptación. Se ubica en el rango Bueno de la escala convencional de interpretación (0,80 ≤ α < 0,90), próximo al límite inferior del rango Excelente. Esta posición permite afirmar que el conjunto de 42 ítems del instrumento opera de manera coherente en la medición de los niveles de madurez en seguridad de la información, y que ningún reactivo introduce una distorsión que comprometa la lectura conjunta del cuestionario.

A partir de este resultado, el Instrumento de Diagnóstico de Madurez en Seguridad de la Información se consideró confiable en términos de consistencia interna y apto para su aplicación en la fase diagnóstica de la investigación. La confiabilidad evidenciada por el coeficiente se suma a la validez de contenido establecida mediante el procedimiento de validación de contenido descrito en el apartado 3.5.2.2 lo cual configura un instrumento de medición respaldado en sus dos propiedades psicométricas centrales para los fines del presente estudio.

**Alcance y limitaciones de la evidencia**

La evidencia de confiabilidad obtenida en este apartado debe leerse dentro de los límites propios del diseño del piloto. Tres consideraciones matizan el alcance del coeficiente reportado.

El tamaño de la muestra del piloto introduce la primera. El n = 30 respondentes empleado es suficiente para producir una estimación inicial defendible del Alfa de Cronbach, conforme a las recomendaciones operativas habituales para instrumentos de escala ordinal. Aun así, una muestra de ese tamaño produce intervalos de confianza más amplios que los que se obtendrían con muestras mayores, y el valor puntual del coeficiente puede variar levemente si el piloto se replicara con otros 30 respondentes de perfil equivalente. El α = 0,869 reportado se interpretó, en consecuencia, como una estimación robusta para los fines diagnósticos del presente estudio, no como un parámetro poblacional definitivo de la consistencia del instrumento.

La naturaleza del instrumento añade la segunda. El Instrumento de Diagnóstico de Madurez en Seguridad de la Información es un índice compuesto por catorce instrumentos que cubren dominios distintos del proceso de gestión de incidentes: detección, registro, análisis, contención, erradicación, recuperación, lecciones aprendidas y elementos transversales de gobernanza. El Alfa de Cronbach asume, en su formulación estadística, una cierta unidimensionalidad o equivalencia esencial entre los ítems que conforman la escala. Esa condición se cumple parcialmente en este instrumento. Todos los reactivos miden la misma variable latente (el nivel de madurez), pero la abordan desde subdimensiones funcionales heterogéneas. Por ese motivo el coeficiente global se reporta como evidencia agregada de consistencia interna y no como sustento de unidimensionalidad estricta. Si en una fase posterior de la investigación se requiriera disponer de coeficientes por subdimensión, el cálculo es viable; debe advertirse, en ese supuesto, que la estabilidad de cada α parcial disminuye sensiblemente al reducirse el número de ítems involucrados en cada grupo.

La distinción entre confiabilidad y validez plantea la tercera. El Alfa de Cronbach es una evidencia de confiabilidad, no de validez. El coeficiente obtenido demuestra que los reactivos del instrumento se comportan de manera consistente al ser respondidos, pero no demuestra por sí solo que el contenido del instrumento represente adecuadamente la variable que pretende medir. La validez de contenido se sustenta en la tabla de especificaciones del cuestionario y en el anclaje normativo de sus reactivos a estándares internacionales, descritos en el apartado 3.5.2.2. Confiabilidad y validez operan, en consecuencia, como evidencias complementarias y mutuamente necesarias para sostener la calidad métrica del instrumento aplicado en esta investigación.

## 3.6 Procesamiento y Análisis de la Información

*[Explique cómo se procesarán y analizarán los datos recolectados: software utilizado (SPSS, R, Python, Excel…), pruebas estadísticas, criterios de interpretación y herramientas de desarrollo si aplica.]*

# Capítulo IV: Marco Práctico

## 4.1 Análisis de la situación actual

El análisis de la situación actual constituye el punto de partida operativo del marco práctico su función no es descriptiva sino diagnóstica, en tanto se trata de establecer con evidencia verificable en qué estado se encuentra hoy el proceso de gestión de incidentes de seguridad de la información en la institución bajo estudio. Esa caracterización no admite formulación general ni apreciativa, sino que exige una secuencia metodológica que primero fija los criterios de referencia contra los cuales se mide la institución, luego documenta la aplicación del instrumento que produce las mediciones y por último lee los resultados obtenidos a la luz de esos criterios. Cada uno de los tres momentos opera como condición de validez del siguiente, de modo que sin marco normativo no hay parámetro de comparación, sin aplicación rigurosa no hay datos confiables y sin lectura cruzada de datos y normativa no hay diagnóstico, sino apenas enumeración de cifras, el cumplimiento verificable del primer objetivo específico de la investigación se sostiene en esa secuencia y en el cierre de los tres momentos que la componen.

### 4.1.1 Análisis de la normativa

El diagnóstico de un proceso institucional carece de sentido fuera del marco normativo que define qué se espera de ese proceso sin esa referencia previa, cualquier juicio sobre el estado de la gestión se reduce a una apreciación general sobre el funcionamiento observado, lo cual desactiva la posibilidad misma de identificar brechas verificables. El análisis normativo opera, por tanto, como condición lógica del análisis cuantitativo posterior, en la medida en que establece el deber ser del proceso, fija los criterios de cumplimiento contra los cuales se mide la institución y delimita el ámbito de exigibilidad técnica y legal que rige a la entidad evaluada. La selección de las normas que conforman ese marco no es ecléctica, sino que responde a un conjunto de criterios operativos y a una arquitectura argumentada que distribuye el cuerpo normativo en cinco frentes complementarios, cada uno con pertinencia individual y con función específica dentro del marco completo.

#### 4.1.1.1 Criterio de selección de las normas

El cuerpo normativo que sostiene este análisis no se elige por suma sino por necesidad. Cada norma incorporada cubre una porción específica del objeto de estudio que las demás no cubren, y todas, en conjunto, configuran el marco de referencia contra el cual se mide la situación actual de la institución. La gestión de incidentes en un servicio fiscal digital es un proceso compuesto que detecta, registra, clasifica, contiene, evidencia, aprende y previene. Ningún estándar resuelve por sí solo esa cadena, y por eso la selección se articula en bloques complementarios.

Cinco criterios operativos guían la inclusión. El primero es la pertinencia directa al objeto una norma forma parte del marco si sus cláusulas se traducen en métricas verificables sobre el proceso institucional evaluado. El segundo es la autoridad de la fuente emisora, ya sea ISO/IEC, NIST, MITRE o un organismo regulatorio nacional reconocido. El tercero es la vigencia. Se trabaja con la edición vigente de cada estándar al momento del estudio, lo que en el caso de ISO/IEC 27001 implica la versión 2022 y, en el de NIST SP 800-61, la Revisión 3 publicada en 2025. El cuarto criterio es la disponibilidad pública o institucional del documento, condición indispensable para que cualquier auditoría posterior reproduzca el ejercicio diagnóstico. El quinto es la compatibilidad entre marcos: las normas seleccionadas se complementan sin contradecirse, lo cual permite combinarlas en un solo instrumento de medición sin generar reglas de cumplimiento en pugna.

Sobre esa base, el marco normativo se organiza en cuatro frentes un frente técnico-operativo cubierto por la familia ISO/IEC 27000 y por NIST SP 800-61, que define qué hacer durante el ciclo completo del incidente. Un frente forense, integrado por las normas ISO/IEC 27037, 27041, 27042 y 27050, que regula cómo se preserva la evidencia que ese ciclo produce. Un frente analítico, aportado por MITRE ATT&CK, que ofrece la taxonomía para describir el comportamiento adversario observado. Y un frente de benchmarks operativos NIST SP 800-92, SANS SOC Survey, ITIL, CMMI y COBIT que calibra cuantitativamente los rangos de cumplimiento del instrumento. A los cuatro se suma el marco legal nacional, que delimita las obligaciones de la institución bajo estudio dentro del ordenamiento jurídico boliviano.

**Figura 1**
*Arquitectura del marco normativo del análisis de la situación actual*

![](data:image/png;base64...)

Nota. ISO/IEC 27001:2022 opera como norma sombrilla y los cuatro frentes se complementan sin contradecirse. Elaboración propia, 2026.

La consecuencia metodológica es directa. Cada uno de los 42 reactivos del instrumento se ancla a una cláusula, control o sección concreta de alguna de estas fuentes. Ningún ítem mide por intuición. El criterio de cumplimiento que se evaluará en los apartados siguientes proviene del propio marco normativo y no de criterios definidos de manera arbitraria.

#### 4.1.1.2 Normas de gestión de incidentes

El núcleo del marco lo conforman las normas que rigen el proceso completo de gestión de incidentes de seguridad de la información, entre ellas la ISO/IEC 27035 en sus partes 1, 2 y 4, y la Revisión 3 de NIST SP 800-61. La elección de ambas referencias en paralelo no es redundancia sino complemento.

ISO/IEC 27035-1 aporta la estructura conceptual y el ciclo de cinco fases (planificación, detección y reporte, evaluación y decisión, respuesta, lecciones aprendidas) que organiza la actividad institucional desde la preparación hasta la mejora continua (ISO/IEC, 2023). Esa estructura es la que el instrumento adopta como columna vertebral del Grupo 1, donde los Instrumentos 1 a 4 evalúan, respectivamente, detección, clasificación, respuesta y lecciones aprendidas. ISO/IEC 27035-2 desarrolla los lineamientos operativos para la planificación y preparación del proceso, lo cual fundamenta los reactivos relativos a procedimientos formales, tiempos objetivo y criterios de escalamiento. ISO/IEC 27035-4, por su parte, regula la coordinación entre equipos de respuesta y constituye la base para evaluar la integración del proceso con instancias externas como el Centro de Gestión de Incidentes Informáticos.

NIST SP 800-61 Rev. 3 complementa la lectura ISO con la integración explícita al Cybersecurity Framework 2.0. La revisión publicada en 2025 abandona el modelo lineal de fases y alinea la guía con las funciones Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar (NIST, 2025). Esa lectura funcional sostiene el anclaje de los indicadores cuantitativos del instrumento, en particular los tiempos de detección y respuesta, cuya operacionalización se beneficia de la articulación NIST por la profusión de benchmarks publicados sobre cada función.

La pertinencia conjunta de ambos cuerpos normativos descansa en una propiedad práctica. Una institución pública boliviana del sector fiscal opera en un ecosistema donde la familia ISO/IEC es la referencia formal para auditorías de seguridad de la información, en tanto NIST es la referencia técnica más empleada en la literatura operativa y en los reportes sectoriales que documentan tiempos, métricas y prácticas, excluir una de las dos dejaría al diagnóstico incompleto del lado normativo o del lado operativo.

El criterio de cumplimiento que estas normas fijan para el análisis posterior se expresa en cuatro condiciones evaluables, que comprenden la existencia formal del proceso documentado en cada fase del ciclo, la trazabilidad de cada incidente desde la detección hasta el cierre, la medición sistemática de los tiempos de cada fase y la incorporación verificable de lecciones aprendidas al sistema institucional. Las cuatro se traducen en métricas concretas en los Instrumentos 1 a 4 y en sus reactivos asociados, según se detalla en la tabla de especificaciones (Anexo).

#### 4.1.1.3 Norma marco de seguridad de la información

ISO/IEC 27001:2022 opera como norma sombrilla del marco. Su pertinencia al objeto no descansa en su rol de estándar genérico de gestión de seguridad de la información sino en un hecho concreto, siete de sus controles del Anexo A definen condiciones específicas que el proceso de gestión de incidentes debe satisfacer para considerarse maduro. Esos siete controles son los seleccionados para anclar los reactivos del instrumento.

El control A.5.17 (gestión de la información de autenticación) sostiene los reactivos del Instrumento 8 sobre accesos y mínimos privilegios. El control A.5.30 (preparación TIC para la continuidad del negocio) aporta el criterio sobre los procedimientos formales de respuesta evaluados por el Instrumento 3 y por algunos reactivos del Grupo 2. El control A.6.3 (concientización, educación y capacitación en seguridad de la información) ancla el Instrumento 13 sobre cobertura de capacitación del personal. Los controles A.8.15 (registro de eventos) y A.8.16 (actividades de monitorización) sostienen los reactivos del Instrumento 1 sobre detección y registro y del Instrumento 11 sobre integridad de los registros. El control A.8.23 (filtrado web) y otros controles de la sección A.8 dan respaldo al Instrumento 10 sobre gestión de vulnerabilidades. El control A.10.1 (políticas de uso aceptable) cubre el Instrumento 12 sobre gestión de riesgos.

La razón de adoptar la versión 2022 y no una anterior es operativa. La revisión más reciente reorganiza los controles del Anexo A en cuatro temas (organizacional, personas, físico y tecnológico) y ajusta la nomenclatura a la realidad operativa actual de las organizaciones (ISO/IEC, 2022). Trabajar con la versión vigente garantiza que cualquier auditoría que la institución realice tras la implementación de la propuesta encontrará una correspondencia directa entre lo evaluado en el diagnóstico y lo exigido por la norma en uso.

El criterio de cumplimiento que ISO/IEC 27001:2022 fija para el análisis se traduce en evidencia documental y operativa de cada uno de los siete controles activos en la institución bajo estudio. La existencia formal del control no es suficiente el diagnóstico evaluará su grado de implementación efectiva a través de las métricas cuantitativas que cada reactivo del instrumento define.

#### 4.1.1.4 Normas de evidencia digital y forense

Las normas ISO/IEC 27037, 27041, 27042 y 27050 integran el segundo eje del marco. La gestión de un incidente no termina cuando este se contiene, sino que produce evidencia digital cuya preservación, análisis y custodia condiciona el valor probatorio de cualquier procedimiento posterior. En una institución del sector fiscal, donde los incidentes pueden derivar en investigaciones administrativas o procesos penales, el rigor sobre el manejo de la evidencia deja de ser un asunto técnico para convertirse en una condición de defensa institucional.

ISO/IEC 27037 establece los lineamientos para la identificación, recolección, adquisición y preservación de la evidencia digital, y constituye la referencia internacional más utilizada en el campo (ISO/IEC, 2012). Su contenido ancla los reactivos del Instrumento 5 sobre integridad y custodia. ISO/IEC 27041 regula los métodos analíticos aplicables al material recolectado y sustenta los reactivos del Instrumento 6 sobre respaldos y restauración. ISO/IEC 27042 cubre la interpretación de la evidencia digital y aporta criterios al Instrumento 7 sobre retención y acceso a los repositorios. ISO/IEC 27050, finalmente, regula los procesos de descubrimiento electrónico y completa el ciclo evaluado por el Grupo 2 del instrumento.

La adopción del bloque forense en conjunto, y no de una sola norma, responde a la naturaleza del proceso evaluado. La evidencia recorre un trayecto que va desde la captura inicial hasta el archivo prolongado, pasando por el análisis, la cadena de custodia y la disponibilidad para auditorías. Cada norma cubre un tramo. Tomar solo una dejaría brechas en el diagnóstico, lo cual comprometería la lectura del Grupo 2 sobre la solidez forense del proceso institucional.

El criterio de cumplimiento que estas normas fijan se expresa en cuatro propiedades verificables sobre la evidencia digital generada por los incidentes registrados, las cuales comprenden la integridad mediante funciones de hash, trazabilidad de la cadena de custodia, retención durante el período declarado por la política institucional y disponibilidad efectiva en los repositorios para su consulta o entrega.

#### 4.1.1.5 Norma de gestión de riesgos

ISO/IEC 27005 cierra el bloque ISO con la dimensión preventiva del marco. La gestión de incidentes no opera en el vacío, sino que opera sobre un mapa de riesgos previamente identificado y priorizado. Cuanto mejor sea ese mapa, más eficiente resulta la asignación de recursos al monitoreo, la detección y la respuesta. Cuanto más débil, más reactivo y costoso se vuelve el proceso completo.

La pertinencia de la norma al objeto descansa en una condición específica. ISO/IEC 27005 define el ciclo continuo de identificación, análisis, evaluación y tratamiento de las amenazas que afectan los activos de información, junto con la figura del propietario del riesgo introducida en la edición vigente (ISO/IEC, 2022). Esa figura es la que sostiene la rendición de cuentas institucional sobre el riesgo residual, y su existencia operativa en la institución bajo estudio es uno de los reactivos del Instrumento 12.

El bloque que esta norma respalda en el instrumento es el Grupo 4. Los reactivos del Instrumento 12 evalúan si el ciclo de gestión de riesgos se ejecuta de manera periódica, si los riesgos identificados se traducen en planes de tratamiento y si los responsables formales aprueban el riesgo residual. La lectura conjunta de estos reactivos permite distinguir entre instituciones que mantienen una gestión de riesgos viva y aquellas en las que el ciclo existe solo en el papel.

El criterio de cumplimiento que la norma fija se traduce en la existencia de evaluaciones de riesgo actualizadas, en la trazabilidad entre riesgos identificados y controles aplicados, y en la designación formal de propietarios de riesgo con capacidad efectiva de decisión sobre el plan de tratamiento.

#### 4.1.1.6 Marco de comportamiento adversario

MITRE ATT&CK incorpora al marco la dimensión del adversario. Ninguna de las normas ISO ni de las guías NIST referidas hasta aquí describe el comportamiento concreto de los actores hostiles que la institución debe detectar. Esa descripción la aporta MITRE en forma de taxonomía de tácticas, técnicas y subtécnicas observadas en operaciones reales (MITRE, 2024).

Su pertinencia al objeto se sostiene en una propiedad operativa que ningún otro estándar reemplaza. ATT&CK permite mapear los registros de detección y los expedientes de incidentes contra un vocabulario común y comparable entre organizaciones. Esa propiedad es la que el Instrumento 2 evalúa cuando mide la proporción de alertas con categoría de ataque asignada, y la que sostendrá el diseño de la metodología propuesta cuando se aborde la integración entre los honeypots y el sistema de gestión de incidentes.

La elección de la matriz Enterprise, y no de las matrices Mobile o ICS, responde a la naturaleza del entorno evaluado. Un portal fiscal digital opera sobre infraestructura corporativa estándar servidores web, bases de datos, sistemas de identidad, redes de oficina y no sobre dispositivos móviles ni sistemas de control industrial. La matriz Enterprise describe más de doscientas técnicas y cerca de setecientas subtécnicas pertinentes a ese entorno, con actualizaciones semestrales que la mantienen en línea con la inteligencia de amenazas vigente (MITRE, 2024).

El criterio de cumplimiento que el marco ATT&CK fija para el análisis se expresa en la capacidad institucional de describir un incidente registrado en términos de las tácticas y técnicas observadas, y en la cobertura defensiva que la institución puede demostrar sobre el conjunto de técnicas relevantes a su perfil de amenaza. Esa cobertura se mide indirectamente a través de los reactivos del Instrumento 2 y, en una dimensión más amplia, mediante la integración con los reactivos de detección del Instrumento 1.

#### 4.1.1.7 Benchmarks operativos y modelos de madurez

Las normas y los marcos discutidos hasta aquí dicen qué hacer y cómo describirlo. No dicen, sin embargo, cuándo un valor numérico es suficiente. Un porcentaje de cobertura del 70 % puede ser excelente para un tipo de métrica y deficiente para otro, según la práctica documentada en cada sector. Esa calibración cuantitativa la aportan los benchmarks operativos y los modelos de madurez incorporados al marco, los cuales comprenden NIST SP 800-92, SANS SOC Survey, ITIL, CMMI y COBIT.

NIST SP 800-92 cubre la gestión de registros de seguridad y aporta los rangos de referencia para los reactivos que miden completitud y cobertura de logs, particularmente los del Instrumento 1 y del Instrumento 11. SANS SOC Survey, en sus ediciones recientes, publica datos operativos sobre tiempos de detección, respuesta y resolución observados en operaciones de seguridad reales, lo cual permite calibrar los rangos de los reactivos cronométricos del Instrumento 3. ITIL aporta los niveles estándar de SLA para servicios de TI (99,9 %, 99 %, 95 %), cuya adopción facilita la lectura de los reactivos sobre disponibilidad de los sistemas de monitoreo y respuesta.

CMMI y COBIT sostienen la propia escala ordinal de cinco niveles del instrumento. La secuencia Inicial, Básico, Gestionado y Optimizado adoptada para clasificar los resultados de cada instrumento reproduce el patrón estándar documentado en ambos modelos. La correspondencia no es decorativa. Garantiza que la lectura de los resultados del diagnóstico se pueda comparar con la de cualquier otro estudio del campo que adopte la misma referencia, y que las recomendaciones derivadas se enmarquen en lenguaje operativo reconocido por la comunidad de auditoría de TI.

El criterio de cumplimiento que este bloque fija para el análisis es cuantitativo y unificado. Cada reactivo del instrumento traduce un valor observado en un nivel de madurez sobre la escala de cinco puntos, y cada nivel se interpreta contra el rango documentado por el benchmark correspondiente. Ningún resultado depende del criterio del investigador: la calibración está externalizada.

**Tabla X**

*Matriz de selección normativa*

| **Norma / fuente** | **Frente** | **Ancla en el instrumento** | **Criterio de cumplimiento evaluable** | **Versión y justificación** |
| --- | --- | --- | --- | --- |
| ISO/IEC 27035-1, -2, -4 | Técnico-operativo | G1 (Instr. 1–4) | Ciclo de cinco fases documentado; registro y clasificación de incidentes; revisión post-incidente | Edición vigente; aporta la estructura del ciclo de gestión de incidentes |
| NIST SP 800-61 Rev. 3 | Técnico-operativo | G1 (Instr. 1–4) | Tiempos de detección, registro y respuesta; integración a las funciones del CSF 2.0 | Rev. 3 (2025); alinea el ciclo al Cybersecurity Framework 2.0 |
| ISO/IEC 27001:2022 | Norma sombrilla | G3 + controles transversales a G1, G2 y G4 (A.5.17, A.5.30, A.6.3, A.8.15, A.8.16, A.8.23, A.10.1) | Evidencia documental y operativa de cada control del Anexo A evaluado | Versión 2022; reorganiza el Anexo A en cuatro temas y opera como SGSI de referencia |
| ISO/IEC 27037, 27041, 27042, 27050 | Forense | G2 (Instr. 5–7) | Identificación, adquisición, preservación, análisis y trazabilidad de la evidencia digital | Edición vigente; cubren el ciclo completo de la evidencia |
| ISO/IEC 27005 | Técnico-operativo (preventivo) | G4 (Instr. 12) | Evaluaciones de riesgo actualizadas y trazabilidad riesgo → control | Edición vigente; aporta el ciclo de gestión de riesgos |
| MITRE ATT&CK (Enterprise) | Analítico | Transversal a la detección | Capacidad de describir un incidente en tácticas y técnicas de la matriz | Matriz Enterprise por la naturaleza del entorno (portal/servidores), no Mobile ni ICS |
| NIST SP 800-92 | Benchmarks | Calibra reactivos de completitud y cobertura de registros | Rangos de referencia para completitud y cobertura de logs | Aporta los rangos cuantitativos de la gestión de registros |
| SANS SOC Survey · ITIL · CMMI · COBIT | Benchmarks | Calibra rangos y la escala ordinal de cinco niveles | Tiempos de referencia (SANS), SLA (ITIL), escala de madurez (CMMI/COBIT) | Sostienen la calibración cuantitativa y la escala de madurez del instrumento |

*Nota.* Elaboración propia, 2026, a partir del marco normativo descrito en los apartados 4.1.1.2 a 4.1.1.7.

### 4.1.2 Aplicación del instrumento

El paso del marco normativo al diagnóstico institucional exige un puente operativo, conformado por el instrumento de medición y su aplicación a la muestra del objeto de estudio, ningún diagnóstico riguroso puede sostenerse sobre apreciaciones generales del proceso requiere, por el contrario, una operación de captura sistemática de información, ejecutada con un instrumento confiable y aplicada al personal con visibilidad directa sobre los procedimientos evaluados, la validez del análisis cuantitativo depende, en consecuencia, de tres condiciones acumulativas. La primera es que la aplicación haya alcanzado al universo del personal vinculado al área evaluada, y no a una muestra heterogénea ajena al objeto. La segunda es que la confiabilidad del instrumento se sustente en una medición psicométrica estándar sobre la matriz de respuestas obtenida. La tercera es que los resultados se reporten sobre el conjunto completo de respondentes y no sobre subconjuntos seleccionados ex post, el cumplimiento de las tres condiciones convierte los porcentajes resultantes en evidencia diagnóstica utilizable y no en una serie de cifras descontextualizadas.

#### 4.1.2.1 Aplicación a la muestra de diagnóstico

La aplicación del Instrumento de Diagnóstico de Madurez en Seguridad de la Información se ejecuta entre los meses de mayo y junio de 2026 sobre la totalidad del personal vinculado al área de gestión de incidentes y seguridad de la información de la institución bajo estudio. La muestra resultante reúne a treinta respondentes válidos, distribuidos sobre los catorce roles funcionales definidos por el instrumento. Cada rol fue cubierto por dos o más respondentes en función de la dotación real del área, condición que permite contrastar las respuestas obtenidas para cada subdimensión y reduce el peso de la apreciación individual sobre el dato reportado.

El criterio de inclusión exigió pertenencia funcional al área evaluada. La aplicación quedó limitada a funcionarios con responsabilidad operativa o gerencial directa sobre alguna de las catorce subdimensiones que el instrumento mide: detección y monitoreo, clasificación de incidentes, respuesta operativa, lecciones aprendidas, custodia de evidencias, respaldos, retención documental, accesos y privilegios, desarrollo seguro, gestión de vulnerabilidades, trazabilidad de registros, gestión de riesgos, capacitación y métricas. El personal de áreas administrativas no vinculadas a la gestión técnica o gerencial de incidentes quedó fuera de la muestra. La depuración se sostiene en la regla metodológica del estudio: la situación actual de la gestión de incidentes solo puede caracterizarse a partir de los informantes con acceso directo a los registros operativos del proceso.

La modalidad es de autoinforme estructurado mediante formulario digital, reproduciendo sin alteraciones el instrumento de diagnóstico en su forma definitiva. Cada respondente selecciona una opción por reactivo sobre la escala ordinal de cinco puntos definida en la ficha técnica, registrada en la columna de justificación la fuente del dato consultada y entrega al menos un documento institucional de respaldo por cada uno de los catorce instrumentos. La doble capa de justificación por ítem y por instrumento permitió contrastar el puntaje declarado con la fuente operativa que lo sustenta, según el procedimiento previsto en el marco metodológico.

La matriz resultante de respuestas tiene dimensión 30 × 42, con cada celda conteniendo un valor entero del rango cero a cuatro. Sobre esa matriz se calculan las propiedades psicométricas del instrumento y las medidas de madurez que se presentan en los apartados siguientes.

#### 4.1.2.2 Confiabilidad del instrumento

El cálculo del Coeficiente Alfa de Cronbach sobre la matriz de respuestas arroja un valor de α = 0,869, ubicado en el rango Bueno (0,80 ≤ α < 0,90) de la escala convencional propuesta por George y Mallery (2003). La Tabla 1 sintetiza los componentes del cálculo.

**Tabla 1**

*Componentes del cálculo del Coeficiente Alfa de Cronbach sobre la muestra de diagnóstico*

| **Componente** | **Valor** |
| --- | --- |
| Número de ítems (k) | 42 |
| Número de respondentes válidos (n) | 30 |
| Suma de varianzas individuales de los ítems (Σ s²ᵢ) | 65,27 |
| Varianza del puntaje total (s²ₜ) | 430,25 |
| Coeficiente Alfa de Cronbach (α) | 0,869 |
| Categoría según escala de interpretación | Bueno |

*Nota.* Cálculo realizado sobre los 30 respondentes válidos de la muestra de diagnóstico, con varianzas muestrales (denominador n − 1). Elaboración propia, 2026.

El coeficiente obtenido supera por 0,169 puntos el umbral mínimo de aceptación declarado en el marco metodológico (α ≥ 0,70), lo cual equivale a un margen del 24 % sobre el corte. Su posición dentro del rango Bueno, próxima al límite inferior del rango Excelente, autoriza dos lecturas. Demuestra, en lo psicométrico, que los cuarenta y dos reactivos del instrumento operan de manera consistente al ser respondidos por la totalidad del personal del área. Y habilita, en lo operativo, el uso de los puntajes agregados por instrumento, por grupo y a nivel global como medidas confiables del nivel de madurez observado.

La estabilidad del comportamiento de los reactivos sobre la muestra de treinta respondentes despeja la sospecha que podría plantearse sobre un cuestionario extenso aplicado a un área acotada. Ningún ítem introduce distorsión apreciable en el conjunto, y ninguna subdimensión arrastra respuestas erráticas que comprometieran la lectura agregada. Sobre esa base, los resultados cuantitativos que siguen pueden interpretarse como mediciones válidas del estado del proceso institucional al momento del diagnóstico.

#### 4.1.2.3 Resultados por instrumento

El cálculo del porcentaje de cumplimiento se ejecuta instrumento por instrumento, conforme al procedimiento declarado en el marco metodológico, consiste en calcular el puntaje obtenido sobre puntaje máximo, multiplicado por cien, calculado individualmente por cada respondente y promediado luego sobre los treinta. La Tabla 2 reúne los resultados.

**Tabla 2**

*Porcentaje de cumplimiento y nivel de madurez por instrumento (n = 30)*

| **Grupo** | **Instr.** | **Subdimensión** | **Ítems** | **% cumplimiento** | **Nivel** |
| --- | --- | --- | --- | --- | --- |
| G1 | 1 | Detección y registro de eventos | 4 | 48,54 | Básico |
| G1 | 2 | Clasificación y evidencia de incidentes | 3 | 56,94 | Gestionado |
| G1 | 3 | Respuesta y tiempos de atención | 3 | 58,06 | Gestionado |
| G1 | 4 | Lecciones aprendidas y mejora | 3 | 49,17 | Básico |
| G2 | 5 | Integridad y custodia de evidencias | 3 | 57,22 | Gestionado |
| G2 | 6 | Respaldos y restauración de evidencias | 3 | 58,33 | Gestionado |
| G2 | 7 | Retención y acceso a evidencias | 2 | 47,92 | Básico |
| G3 | 8 | Accesos y mínimos privilegios | 3 | 49,72 | Básico |
| G3 | 9 | Desarrollo seguro y validaciones | 3 | 53,06 | Gestionado |
| G3 | 10 | Gestión de vulnerabilidades | 3 | 50,56 | Básico |
| G3 | 11 | Integridad y trazabilidad de registros | 3 | 52,78 | Gestionado |
| G4 | 12 | Gestión de riesgos | 3 | 53,89 | Gestionado |
| G4 | 13 | Capacitación y cobertura | 3 | 47,78 | Básico |
| G4 | 14 | Métricas y mejora continua | 3 | 53,89 | Gestionado |

*Nota.* Cálculo del porcentaje sobre el promedio de los puntajes individuales de los 30 respondentes para cada instrumento. Niveles de madurez según los cortes definidos en la ficha técnica del instrumento: Inicial 0–25 %, Básico 26–50 %, Gestionado 51–75 %, Optimizado 76–100 %. Elaboración propia, 2026.

La lectura de la tabla revela una distribución concentrada en una franja estrecha. Ningún instrumento alcanza el nivel Optimizado y ninguno descende al nivel Inicial. Los catorce valores oscilan entre 47,78 % y 58,33 %, lo cual sitúa al proceso completo dentro del corredor que separa el final del nivel Básico del comienzo del nivel Gestionado. Esa estrechez del rango es, por sí misma, una característica del diagnóstico. Las instituciones no presentan dominios donde la madurez se haya consolidado claramente ni dominios donde la operación esté ausente, sino un patrón sostenido de cumplimiento parcial.

Seis instrumentos quedan en nivel Básico, entre ellos detección y registro, lecciones aprendidas, retención y acceso a evidencias, accesos y mínimos privilegios, gestión de vulnerabilidades y capacitación. Ocho instrumentos alcanzan nivel Gestionado, todos en el tercio inferior del rango (entre 51 % y 60 %). El valor más alto del conjunto corresponde al Instrumento 6 sobre respaldos y restauración de evidencias (58,33 %), y el más bajo al Instrumento 13 sobre capacitación y cobertura (47,78 %). La distancia entre ambos extremos es de apenas 10,55 puntos porcentuales, lo cual confirma que el diagnóstico no obedece a una asimetría entre dominios sino a una madurez uniformemente intermedia.

**Figura 1.**

*Porcentaje de cumplimiento por instrumento (n = 30)*

![](data:image/png;base64...)

*Nota.* Los instrumentos se presentan ordenados de menor a mayor porcentaje de cumplimiento. Las líneas verticales delimitan los puntos de corte correspondientes a los niveles de madurez establecidos para el análisis. Elaboración propia (2026).

#### 4.1.2.4 Resultados por grupo temático

La agregación al nivel de grupo se calcula como promedio simple de los porcentajes de los instrumentos que conforman cada bloque, según la ponderación igualitaria establecida en el marco metodológico. La Tabla 3 sintetiza los cuatro resultados, la consolidación por grupos facilita una lectura integrada del comportamiento de las dimensiones evaluadas, sin alterar la información proporcionada por cada instrumento individual. Este nivel de agregación permite identificar de manera comparativa los bloques con mayor y menor grado de cumplimiento, proporcionando una visión global del estado del proceso evaluado y orientando la posterior interpretación de las brechas que deberán ser atendidas mediante la propuesta metodológica.

**Tabla 3**

*Porcentaje de cumplimiento y nivel de madurez por grupo temático*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupo** | **Denominación** | **Instrumentos** | **% cumplimiento** | **Nivel** |
| G1 | Gestión de incidentes | 1, 2, 3, 4 | 53,18 | Gestionado |
| G2 | Evidencias y respaldo | 5, 6, 7 | 54,49 | Gestionado |
| G3 | Seguridad y controles técnicos | 8, 9, 10, 11 | 51,53 | Gestionado |
| G4 | Gestión organizacional y mejora | 12, 13, 14 | 51,85 | Gestionado |

*Nota.* Los porcentajes de cumplimiento por grupo corresponden al promedio aritmético simple de los resultados obtenidos en los instrumentos que integran cada categoría de análisis. Elaboración propia (2026).

**Figura 2.**

*Madurez por grupo temático frente al umbral del nivel Gestionado*

![](data:image/png;base64...)

*Nota.* Valores expresados como promedio simple de los instrumentos de cada grupo. La línea discontinua representa el umbral del nivel Gestionado (51%). Elaboración propia, 2026.

Los cuatro grupos quedan clasificados en el nivel Gestionado, todos dentro de los primeros cinco puntos porcentuales de su rango. La diferencia entre el grupo mejor evaluado y el peor evaluado es de apenas 2,96 puntos, separación que confirma a nivel agregado la homogeneidad ya observada al nivel de instrumento.

El grupo de Evidencias y respaldo encabeza la medición con 54,49 %, sostenido por la calidad relativa de la integridad de las custodias (57,22 %) y de los respaldos (58,33 %), aunque debilitado por la retención y el acceso a las evidencias archivadas (47,92 %). El grupo de Gestión de incidentes alcanza 53,18 %, tirado hacia arriba por los tiempos de respuesta y la clasificación, y hacia abajo por la detección inicial y por las lecciones aprendidas. El grupo de Gestión organizacional y mejora obtiene 51,85 %, con un patrón similar. Una gestión de riesgos y un sistema de métricas razonablemente activos contrastan con una cobertura de capacitación insuficiente. El grupo de Seguridad y controles técnicos queda al borde inferior del rango Gestionado con 51,53 %, lo cual lo convierte en el bloque más cercano a una degradación al nivel Básico si alguno de sus instrumentos perdiera puntos.

La proximidad entre los cuatro valores tiene implicación analítica. El proceso institucional no exhibe un dominio claramente fuerte que sostenga a los demás ni un dominio claramente débil que tire del conjunto hacia abajo. Funciona, más bien, como un sistema donde cada componente opera al mismo ritmo que los restantes, sin compensaciones internas. En términos de teoría de la resiliencia, esa propiedad describe un proceso sin redundancias funcionales, si una dimensión cae, no hay otra con margen suficiente para absorber el impacto.

#### 4.1.2.5 Resultado global de madurez

El cálculo de la madurez global del proceso institucional se ejecuta como promedio simple de los catorce porcentajes de los instrumentos, conforme a la ponderación igualitaria declarada en el marco metodológico. El resultado obtenido es de 52,70 %, ubicado en el nivel Gestionado según los cortes de la ficha técnica del instrumento.

**Figura 3.**

*Posición de la madurez global del proceso institucional*

![](data:image/png;base64...)

*Nota.* La madurez global (52,70%) se ubica 1,70 puntos por encima del umbral inferior del nivel Gestionado. Elaboración propia, 2026.

La posición de ese valor dentro del rango Gestionado merece dos lecturas. La primera es estadística. El 52,70 % se localiza apenas 1,70 puntos por encima del corte que separa el nivel Gestionado del nivel Básico, lo cual sitúa al proceso institucional en el extremo inferior del rango. La segunda lectura es operativa. Una variación negativa de magnitud equivalente a la observada entre el mejor y el peor instrumento (10,55 puntos) sería suficiente, en términos teóricos, para degradar el nivel global al rango Básico si afectara a los componentes que actualmente sostienen el promedio. La estabilidad del nivel Gestionado, en consecuencia, depende del mantenimiento sostenido de los ocho instrumentos que hoy están sobre el umbral.

El resultado global admite una interpretación constructiva en términos del diseño de la propuesta. Un proceso clasificado en Gestionado al borde inferior cuenta con bases operativas suficientes para sostener una intervención metodológica orientada a elevarlo, condición que no se cumpliría en un proceso clasificado como Inicial. Existen procedimientos documentados, registros sistemáticos y prácticas observables sobre los cuales la propuesta puede operar. Existen, al mismo tiempo, brechas verificables y dispersas que justifican la intervención. Esa combinación madurez suficiente para sostener una propuesta y brechas suficientes para necesitarla configura el escenario diagnóstico sobre el cual se construyen los apartados siguientes.

La caracterización detallada del estado actual, expresada como distancias verificables entre la práctica observada y los criterios normativos fijados en el apartado 4.1.1, se desarrolla en el apartado 4.1.3 que sigue.

### 4.1.3 Diagnóstico situacional

El diagnóstico situacional no se reduce a la enumeración de los porcentajes obtenidos por cada instrumento es la operación analítica que cruza esos porcentajes con los criterios normativos fijados en el primer momento del análisis y produce, como resultado, un conjunto de brechas verificables expresadas como distancias entre la práctica observada y el estándar exigido. La diferencia metodológica entre un reporte de resultados y un diagnóstico se localiza precisamente en ese cruce. Un reporte presenta datos; un diagnóstico identifica problemas. La construcción del diagnóstico se ejecuta grupo por grupo, dado que cada bloque temático del instrumento responde a un cuerpo normativo distinto y exige, en consecuencia, una lectura propia la integración de los cuatro bloques produce una caracterización única del estado actual del proceso institucional.

#### 4.1.3.1 Brechas en gestión de incidentes

El Grupo 1 alcanza un porcentaje de cumplimiento del 53,18 %, ubicándose en el nivel Gestionado. La lectura agregada, sin embargo, esconde un patrón que solo aparece al examinar los cuatro instrumentos por separado. Dos de ellos el primero y el último del ciclo de gestión quedaron en nivel Básico, mientras que los dos del medio se sostienen en Gestionado. La cadena de respuesta funciona en su núcleo y pierde tracción en sus extremos.

La brecha más visible se localiza en la detección y el registro de eventos. El Instrumento 1 obtiene 48,54 %, valor inferior en 2,46 puntos al corte que separa el nivel Básico del Gestionado. ISO/IEC 27035-1 exige que toda institución mantenga capacidades sostenidas de identificación y reporte de eventos como condición de entrada al ciclo de gestión (ISO/IEC, 2023), y el control A.8.15 de ISO/IEC 27001:2022 establece sobre el registro de eventos un criterio cuantitativo de completitud que el reactivo correspondiente operacionaliza, la distancia observada se manifiesta en tres frentes. La proporción de eventos con todos los campos mínimos registrados queda por debajo del rango esperado para una operación gestionada, los tiempos entre la generación del evento y su registro en el sistema central de monitoreo superan el umbral operativo de referencia, y la disponibilidad del sistema de detección no alcanza el nivel de SLA estándar definido por ITIL para servicios críticos.

La segunda brecha del grupo aparece en el cierre del ciclo. El Instrumento 4 sobre lecciones aprendidas y mejora obtiene 49,17 %, también en nivel Básico. ISO/IEC 27035-1 e ISO/IEC 27035-4 sitúan la fase de lecciones aprendidas como el mecanismo institucional que retroalimenta el sistema de gestión a partir de la experiencia acumulada (ISO/IEC, 2023). La brecha observada indica que los incidentes registrados no se traducen consistentemente en revisiones formales ni en actualizaciones documentadas del proceso. La consecuencia operativa de esta deficiencia se acumula en el tiempo, la institución repite patrones de respuesta sobre incidentes que ya enfrenta antes, lo cual erosiona la curva de aprendizaje esperada en un proceso gestionado.

El contraste con los Instrumentos 2 y 3 vuelve más nítido el patrón. La clasificación y la evidencia de incidentes alcanzan 56,94 %, y la respuesta y los tiempos de atención llegan a 58,06 %, ambos dentro del nivel Gestionado. Una vez que un incidente entra al ciclo, la institución lo clasifica con razonable consistencia y le aplica una respuesta operativamente válida. El problema no está en cómo se atiende el incidente identificado, sino en cuántos eventos quedan fuera del registro inicial y en qué tan poco regresa la experiencia al sistema después del cierre.

#### 4.1.3.2 Brechas en evidencias y respaldo

El Grupo 2 obtiene el porcentaje más alto del diagnóstico (54,49 %), aunque ese liderazgo no implica ausencia de brechas. La distribución entre los tres instrumentos del bloque revela una asimetría clara entre el manejo de la evidencia en el corto plazo y su gestión en el archivo prolongado.

Los Instrumentos 5 y 6 alcanzan los porcentajes más altos del diagnóstico completo, con 57,22 % para integridad y custodia, y 58,33 % para respaldos y restauración. ISO/IEC 27037 establece los lineamientos para la identificación, recolección y preservación de la evidencia digital (ISO/IEC, 2012), y ISO/IEC 27041 regula los métodos analíticos aplicables a esa evidencia. El cumplimiento observado en ambos instrumentos indica que la institución, una vez que ha capturado evidencia asociada a un incidente, la preserva con funciones criptográficas de hash, mantiene una cadena de custodia funcional y dispone de mecanismos de respaldo que permiten su restauración dentro de los tiempos esperables.

La brecha se localiza en el tramo posterior del ciclo de la evidencia. El Instrumento 7 sobre retención y acceso a evidencias queda en 47,92 %, valor que constituye el segundo más bajo del diagnóstico completo y lo sitúa en nivel Básico. ISO/IEC 27042 e ISO/IEC 27050 regulan, respectivamente, la interpretación de la evidencia digital y los procesos de descubrimiento electrónico que sostienen su disponibilidad para auditorías o procedimientos posteriores. La distancia observada se traduce en dos manifestaciones operativas los períodos de retención efectiva de las evidencias archivadas quedan por debajo de los plazos exigidos por la política institucional, y los procedimientos de consulta y entrega de evidencia para auditorías internas o requerimientos externos operan sin la trazabilidad ni la oportunidad esperadas en un proceso gestionado.

El patrón del grupo resulta consistente. La evidencia generada en el momento del incidente se trata con rigor; la evidencia archivada para uso futuro no recibe el mismo cuidado. La diferencia tiene una implicación operativa precisa: la institución estaría en condiciones de responder a una auditoría sobre incidentes recientes con material probatorio sólido, pero su capacidad de respuesta sobre incidentes históricos los más probables de generar requerimientos legales prolongados se ve comprometida por la debilidad del archivo y del acceso.

#### 4.1.3.3 Brechas en controles técnicos

El Grupo 3 obtiene el menor porcentaje de los cuatro grupos del diagnóstico, con 51,53 %, valor que lo deja apenas 0,53 puntos por encima del corte que separa el nivel Gestionado del Básico. Esa proximidad lo convierte en el bloque más expuesto a degradación si algún instrumento perdiera puntos en mediciones futuras.

La brecha más severa del grupo aparece en los Instrumentos 8 y 10, ambos en nivel Básico. El Instrumento 8 sobre accesos y mínimos privilegios obtiene 49,72 %, valor que se ancla al control A.5.17 de ISO/IEC 27001:2022 sobre gestión de la información de autenticación (ISO/IEC, 2022). La distancia observada indica que las prácticas de asignación, revisión y revocación de credenciales no operan con la sistematicidad exigida por la norma. La consecuencia técnica es directa la superficie de exposición de la institución incorpora vectores prevenibles que la familia ATT&CK clasifica como acceso inicial y persistencia, vectores cuya cobertura defensiva depende precisamente de la fortaleza del control de accesos.

El Instrumento 10 sobre gestión de vulnerabilidades queda en 50,56 %, apenas 0,44 puntos por encima del corte del nivel Básico. El control A.8.23 de ISO/IEC 27001:2022 establece criterios sobre el filtrado y el manejo de vulnerabilidades técnicas (ISO/IEC, 2022). La brecha observada se manifiesta en la periodicidad de los escaneos, en la velocidad de remediación de las vulnerabilidades identificadas y en la cobertura de los activos incluidos en el ciclo de evaluación. La conjunción con la brecha del Instrumento 8 produce un efecto compuesto, una superficie de ataque parcialmente cubierta multiplica la probabilidad de que un evento adversario alcance los activos institucionales antes de que el sistema de detección lo capture.

Los Instrumentos 9 y 11 se sostienen en nivel Gestionado por márgenes estrechos. El Instrumento 9 sobre desarrollo seguro y validaciones alcanza 53,06 %, y el Instrumento 11 sobre integridad y trazabilidad de registros llega a 52,78 %. Ambos valores indican que los procesos preventivos del lado del desarrollo y del lado de la trazabilidad de logs funcionan, pero no con la holgura suficiente para compensar las dos brechas anteriores. El grupo opera, en consecuencia, sin redundancia funcional entre sus instrumentos. La debilidad de uno no encuentra refuerzo en el otro.

#### 4.1.3.4 Brechas en gestión organizacional y mejora

El Grupo 4 alcanza 51,85 % de cumplimiento, valor que lo sitúa en el nivel Gestionado al borde inferior del rango. La distribución entre sus tres instrumentos contiene la brecha más severa del diagnóstico completo.

El Instrumento 13 sobre capacitación y cobertura del personal obtiene 47,78 %, el porcentaje más bajo de los catorce instrumentos del cuestionario y la única medición que se aleja en más de tres puntos del corte del nivel Gestionado. El control A.6.3 de ISO/IEC 27001:2022 exige programas formales y verificables de concientización, educación y capacitación en seguridad de la información para todo el personal con acceso a activos de información (ISO/IEC, 2022). La distancia observada indica que la cobertura de capacitación no alcanza al conjunto del personal con responsabilidad operativa sobre el proceso, que la periodicidad de los programas no se sostiene con la regularidad exigida y que la evaluación del aprendizaje, cuando existe, opera sin trazabilidad documental sistemática.

El peso operativo de esta brecha se amplifica al cruzarla con los hallazgos de los otros grupos. La debilidad en detección observada en el Grupo 1 se ve agravada por una capacitación insuficiente del personal responsable del monitoreo. La debilidad en gestión de vulnerabilidades del Grupo 3 se profundiza con una capacitación deficiente del personal técnico que debe identificar, priorizar y remediar las vulnerabilidades detectadas. La capacitación, como dimensión transversal, opera como el cuello de botella organizacional que limita la madurez efectiva de varios procesos técnicos del diagnóstico.

Los Instrumentos 12 y 14 se sostienen ambos en 53,89 %, en el tercio inferior del nivel Gestionado. El Instrumento 12 sobre gestión de riesgos se ancla en ISO/IEC 27005 y en el control A.10.1 de ISO/IEC 27001:2022, y su resultado indica que el ciclo de identificación, análisis y tratamiento de riesgos opera de manera periódica aunque sin la robustez suficiente para clasificarlo como un proceso consolidado. El Instrumento 14 sobre métricas y mejora continua se ancla en ISO/IEC 27035-4 y en las prácticas ITIL, y refleja un sistema de indicadores activo pero sin el grado de institucionalización que sostendría una mejora medible en el tiempo.

**Figura 4.**

*Mapa de calor de brechas por instrumento y grupo temático*

*![](data:image/png;base64...)*

*Nota.* Color según nivel de madurez alcanzado por cada instrumento los instrumentos en nivel Básico (ámbar) señalan las brechas que atenderá la propuesta. Elaboración propia, 2026.

#### 4.1.3.5 Caracterización del estado actual

La lectura conjunta de los cuatro grupos permite caracterizar el estado actual del proceso institucional como un sistema de madurez intermedia con cumplimiento parcial sostenido, sin dominios consolidados ni dominios colapsados. El diagnóstico no encuentra fortalezas claras que compensen debilidades específicas, ni encuentra debilidades agudas que demanden intervención exclusiva sobre un dominio aislado. Encuentra, en cambio, un patrón uniformemente intermedio donde la madurez funcional convive con seis brechas concretas distribuidas en los cuatro grupos.

El flujo operativo del proceso reproduce ese patrón en su recorrido temporal. Un incidente que ingresa al ciclo lo hace bajo condiciones de detección inicial parcialmente cubiertas: una fracción significativa de los eventos relevantes queda fuera del registro sistemático antes de poder ser clasificada. Los que sí ingresan reciben una clasificación razonablemente consistente y una respuesta operativa dentro de los tiempos objetivos definidos, lo cual indica que el núcleo del ciclo funciona. La evidencia generada durante la respuesta se preserva con rigor en el corto plazo. El problema empieza después del cierre, la retención prolongada de la evidencia, el acceso para auditorías futuras y la incorporación de lecciones aprendidas al sistema institucional operan por debajo del estándar gestionado, lo cual rompe la cadena de mejora continua que el marco normativo presupone como condición de un proceso maduro.

**Figura 6**
*Flujo operativo del incidente y localización de las brechas*

![](data:image/png;base64...)

*Nota.* Las fases en color funcional operan en nivel Gestionado; las fases y dimensiones en color brecha operan en nivel Básico. La cadena de mejora continua aparece interrumpida por las brechas del cierre. Elaboración propia, 2026.

Las dimensiones preventivas y de gobierno reproducen el mismo patrón con un acento propio. Los controles técnicos preventivos accesos y vulnerabilidades, principalmente operan con cumplimiento insuficiente para reducir la superficie de exposición que llega al sistema de detección, lo cual incrementa la carga sobre un ciclo de gestión que ya muestra debilidades en su fase inicial. La gestión organizacional sostiene un ciclo de riesgos y un sistema de métricas activos, pero los acompaña con una cobertura de capacitación que no alcanza al personal responsable de operar los procesos técnicos diagnosticados. La capacitación funciona como dimensión transversal y, en consecuencia, su debilidad amplifica las brechas observadas en los otros grupos.

La caracterización admite una expresión sintética. El sistema institucional gestiona los incidentes que detecta, conserva la evidencia que captura y mantiene un marco organizacional funcional, pero pierde eventos en la entrada, pierde evidencia en el archivo, pierde aprendizaje en el cierre y pierde cobertura preventiva por debilidad de los controles técnicos. La intervención metodológica que se diseñe en el apartado siguiente deberá actuar sobre las seis brechas identificadas, no como problemas independientes, sino como expresiones de un mismo patrón institucional de madurez intermedia.

#### 4.1.3.6 Matriz de trazabilidad

El cierre operativo del primer objetivo específico exige establecer la trazabilidad explícita entre la dimensión evaluada, el instrumento aplicado, el resultado cuantitativo obtenido, el criterio normativo de referencia y la debilidad concreta que la propuesta deberá atender. La Tabla 4 sintetiza esa trazabilidad para las seis brechas en nivel Básico identificadas en el diagnóstico.

**Tabla 4**

*Matriz de trazabilidad*

| **Grupo** | **Instr.** | **Subdimensión evaluada** | **% cumplimiento** | **Criterio normativo de referencia** | **Debilidad concreta para la propuesta** |
| --- | --- | --- | --- | --- | --- |
| G1 | 1 | Detección y registro de eventos | 48,54 | ISO/IEC 27035-1; ISO/IEC 27001:2022 A.8.15, A.8.16 | Eventos sin registro completo; demoras de registro central; disponibilidad del monitoreo bajo SLA |
| G1 | 4 | Lecciones aprendidas y mejora | 49,17 | ISO/IEC 27035-1; ISO/IEC 27035-4 | Revisiones post-incidente no sistemáticas; lecciones sin incorporación documentada al proceso |
| G2 | 7 | Retención y acceso a evidencias | 47,92 | ISO/IEC 27042; ISO/IEC 27050 | Retención efectiva bajo política; acceso a evidencia histórica sin trazabilidad ni oportunidad |
| G3 | 8 | Accesos y mínimos privilegios | 49,72 | ISO/IEC 27001:2022 A.5.17 | Asignación, revisión y revocación de credenciales sin sistematicidad exigible |
| G3 | 10 | Gestión de vulnerabilidades | 50,56 | ISO/IEC 27001:2022 A.8.23 | Periodicidad de escaneos, velocidad de remediación y cobertura de activos por debajo del estándar |
| G4 | 13 | Capacitación y cobertura | 47,78 | ISO/IEC 27001:2022 A.6.3 | Cobertura, periodicidad y trazabilidad de capacitación insuficientes en el personal operativo |

*Nota.* Resultados expresados como promedio simple de los puntajes individuales de los 30 respondentes para cada instrumento. Criterios normativos según el marco fijado en el apartado 4.1.1. Elaboración propia, 2026.

La matriz documenta el cumplimiento del primer objetivo específico de la investigación en términos verificables. Cada brecha registrada se sostiene en un porcentaje calculado sobre datos reales, se ancla a un criterio normativo documentado y se traduce en una debilidad concreta que admite intervención metodológica. Los ocho instrumentos restantes, ubicados en nivel Gestionado, configuran las bases operativas sobre las que la intervención podrá apoyarse sin necesidad de reconstruir el proceso completo.

El estado de cumplimiento del Objetivo Específico 1 queda, en consecuencia, establecido. La situación actual de la gestión de incidentes en la institución bajo estudio se diagnostica con el instrumento confiable (α = 0,869), aplicación válida sobre el personal del área (n = 30, 14 roles funcionales) y resultado expresado como nivel global de madurez (52,70 %, Gestionado al borde inferior). Las seis debilidades concretas listadas en la Tabla 4 configuran el conjunto de insumos diagnósticos sobre los cuales se construye, en el apartado siguiente, el diseño de la metodología propuesta.

## 4.2 Diseño de la metodología de honeypot para la gestión de incidentes en los servicios fiscales

La metodología de honeypot que se diseña para atender las carencias detectadas en el diagnóstico previo tiene alcance específico en la gestión de incidentes en servicios fiscales y se articula sobre el marco de referencia que integran las normas internacionales reconocidas.

La estructura de cuatro componentes que adopta esta sección se desprende de la propia lógica del diseño metodológico, en la que cada componente responde a una pregunta operativa distinta sobre el procedimiento documentado. La primera pregunta es por qué la metodología se diseña de la forma propuesta y la respuesta se condensa en la sección 4.2.1 con los principios, la articulación con el diagnóstico previo y las decisiones operativas que sostienen toda la propuesta. La segunda pregunta es cómo se organiza la metodología en su conjunto y la respuesta se condensa en la sección 4.2.2 con la arquitectura general, las cinco fases, los tres bucles de retroalimentación y los tres planos transversales. La tercera pregunta es cómo opera cada fase en detalle y la respuesta se condensa en la sección 4.2.3 a la 4.2.7 con la entrada, las actividades, la salida, la trazabilidad y los errores comunes de cada fase. La cuarta pregunta es cómo se cierra la propuesta y se conecta con el resto de la investigación y la respuesta se condensa en la sección 4.2.8 con la integración de las cinco fases, la cobertura integral de las brechas del diagnóstico y la transición documentada hacia el tercer y cuarto objetivo específico.

### 4.2.1 Fundamentación del diseño metodológico

La fundamentación del diseño metodológico se articula en tres componentes sobre las bases conceptual, empírica y operativa de la propuesta, distintos de los cuatro componentes de la sección 4.2. El primero expone los principios conceptuales que guían el diseño (4.2.1.1), con énfasis en la separación entre procedimiento y ejecución, junto con la mejora continua iterativa. El segundo desarrolla la base empírica al conectar la metodología con las carencias del diagnóstico (4.2.1.2), mediante una tabla que muestra la correspondencia de cada elemento con las brechas correspondientes. El tercero detalla la base operativa con las decisiones que adopta la metodología para su implementación (4.2.1.3), entre ellas el entorno controlado como condición de validez interna que asegura la trazabilidad.

#### 4.2.1.1 Principios de diseño de la metodología Honeypot

Los cinco principios de diseño que se desarrollan en esta sección son las decisiones de segundo orden que gobiernan las decisiones operativas de las cinco fases de 4.2.2, y se exponen antes del detalle operativo porque toda decisión de las fases debe ser coherente con los principios que las rigen. Adoptamos cinco principios en que la metodología requiere cinco dimensiones de gobierno (estructural, normativa, metodológica, de alcance, y temporal), y la cifra de cinco dimana de que cada dimensión requiere un principio que la gobierne y un riesgo que mitigue. La Figura 1 muestra los cinco principios como sistema unificado con su dimensión, su riesgo mitigado y su anclaje en las decisiones de diseño de 4.2.1.3.

* **El primer principio** establece la separación entre el procedimiento documentado, la ejecución materializada y corresponde a la dimensión estructural. Adoptamos la separación en que sin ella la metodología queda atada a productos concretos de un fabricante y se justifica porque el procedimiento debe ser transferible mientras la ejecución depende del contexto tecnológico de cada organización. La separación dimana de la decisión D2 de 4.2.1.3 y se aplica mediante la documentación de las catorce funciones.
* **El segundo principio** adopta la referencia internacional como guía y corresponde a la dimensión normativa, adoptamos la referencia internacional en que sin ella la metodología carece de anclaje en estándares reconocidos y se justifica porque la auditoría externa y la comparación entre organizaciones requieren normas comunes. La metodología se ancla en ISO/IEC 27035-1:2023 para el ciclo de gestión de incidentes, en NIST SP 800-61 Rev. 3 para la respuesta institucional, en MITRE ATT&CK para el lenguaje de tácticas y técnicas, en ISO/IEC 27037:2012 para la preservación de evidencia digital, junto con ISO/IEC 27001:2022 para los controles institucionales.
* **El tercer principio** exige la trazabilidad explícita de tres anclas en cada decisión, y corresponde a la dimensión metodológica. Adoptamos tres anclas en que la trazabilidad exige tres elementos mínimos para ser auditable sin consultar al autor y se justifica porque cada decisión debe llevar anclaje a la carencia diagnosticada, la norma internacional, junto con el índice medible. La trazabilidad dimana de la decisión D3 de 4.2.1.3, y se aplica en la Tabla 1 de 4.2.1.2 sobre las seis brechas del diagnóstico.
* **El cuarto principio** asume la cobertura quirúrgica de las brechas que la herramienta puede reducir y corresponde a la dimensión de alcance, adoptamos la cobertura quirúrgica en que sin ella la metodología pretende atender carencias que el honeypot no puede reducir con resultados verificables y se justifica porque el alcance debe acotarse a lo verificable. La metodología se concentra en las tres brechas del diagnóstico que la herramienta puede reducir (detección de incidentes, lecciones aprendidas, preservación de evidencia), y deriva las tres brechas restantes a un plan institucional paralelo descrito en 4.2.1.2.
* **El quinto principio** articula la mejora continua iterativa mediante tres bucles con latencia diferenciada, y corresponde a la dimensión temporal, adoptamos tres bucles en que la captura, la correlación y la medición operan en escalas temporales distintas y se justifica porque cada escala requiere su propio mecanismo de retorno. El bucle táctico opera en horas, el bucle operacional opera en semanas, junto con el bucle estratégico que opera en meses, y los tres bucles se ilustran en la Figura 2.

*Figura 1* *Cinco principios de diseño como sistema unificado*

![](data:image/jpeg;base64...)

Nota. La Figura 1 muestra los cinco principios de diseño de la metodología Honeypot como sistema unificado, donde cada principio gobierna una dimensión específica del procedimiento y mitiga un riesgo particular diagnosticado en el OE1. La disposición de los principios en el plano superior, asociados a su dimensión metodológica en el plano medio y al riesgo mitigado en el plano inferior, materializa visualmente la correspondencia uno a uno que articula toda la arquitectura de la propuesta, de modo que ningún riesgo queda sin gobernanza ni ningún principio opera sin anclaje normativo. Esta correspondencia resulta decisiva durante la fase de auditoría, pues permite que un evaluador externo rastree de inmediato el origen de cada decisión metodológica hasta la norma internacional que la respalda, sea ISO 27035, NIST SP 800-61 Rev. 3, MITRE ATT&CK o ISO 27037, y hasta el indicador medible IMGI o IIAM que cuantifica su efecto sobre la gestión. Los íconos representan visualmente la esencia operativa de cada principio: divisor para la separación procedimiento-ejecución entre el OE2 y el OE3, globo para la referencia internacional que ancla cada fase, puntos conectados para la trazabilidad entre carencia diagnosticada, fase, norma e índice, y diana para la cobertura quirúrgica de los focos de fallo identificados. El ciclo, por su parte, representa la mejora continua iterativa habilitada por las retroalimentaciones explícitas F3→F2, F4→F1 y F5→F1, y cierra la lógica circular del sistema. La lectura vertical de la figura, columna por columna, comunica el gobierno individual de cada riesgo, mientras que la lectura horizontal, fila por fila, revela la coherencia sistémica del conjunto y la interdependencia entre los cinco principios. Esta doble lectura refuerza la idea de que la metodología opera como un sistema de gobierno del riesgo, y no como un catálogo acumulativo de buenas prácticas, lo cual preserva la coherencia interna entre las cinco fases del ciclo de vida del incidente y facilita la transferibilidad del esquema a otras organizaciones con riesgos análogos. En consecuencia, la figura funciona como una guía de navegación para el lector que recorre el resto del capítulo, pues cada principio remite a las subsecciones de §4.2.2 en las que se desarrollan las fases F1 a F5 y sus criterios de cumplimiento verificable. P = principio. Fuente: elaboración propia con base en las decisiones de diseño de §4.2.1.3.

*Figura 2 Tres bucles de retroalimentación con latencia diferenciada*

![](data:image/jpeg;base64...)

*Nota.* La Figura 2 muestra los tres bucles de retroalimentación que articulan la mejora continua iterativa, donde cada bucle opera en una escala temporal distinta: el bucle corto en horas ajusta la configuración del honeypot cuando la captura no produce los eventos esperados, el bucle medio en semanas incorpora al diseño las tácticas, técnicas y procedimientos nuevos que aparecen en la correlación, junto con el bucle largo en meses que aplica las lecciones aprendidas al rediseño estructural. La anchura creciente de las zonas refleja la magnitud relativa de cada escala temporal. F1 = diseño del señuelo. F2 = despliegue aislado. F3 = captura. F4 = correlación. F5 = medición. TTP = tácticas, técnicas y procedimientos. Fuente: elaboración propia.

Los cinco principios formalizan las decisiones de diseño D1 a D4 de §4.2.1.3, donde el principio uno cubre D2, el principio dos es transversal, el principio tres cubre D3, el principio cuatro cubre D1, junto con el principio cinco que cubre D4, y su aplicación operativa se desarrolla en §4.2.2 con las cinco fases, los tres planos, las catorce categorías, y la trazabilidad correspondiente.

#### 4.2.1.2 Atención integral de los hallazgos del diagnóstico

La atención integral de los hallazgos del diagnóstico articula la conexión entre el primer objetivo específico y la metodología y para ello presentamos la trazabilidad normativa de las seis brechas, la separación entre las brechas atendidas y las derivadas, y la justificación de las cifras de cada vía. Justificamos los tres elementos en que toda atención integral de hallazgos requiere una trazabilidad explícita con anclaje normativo, una separación clara entre lo atendido y lo derivado, junto con una justificación de las cifras que conecte cada brecha con la vía de atención que le corresponde. Necesitamos esta sección porque sin la atención integral las carencias del primer objetivo específico quedan sin anclaje normativo ni índice medible y la metodología pierde su conexión con la cadena causal entre los cuatro objetivos de la investigación.

En la Tabla 1 ordenamos la trazabilidad normativa de las seis brechas del primer objetivo específico con sus tres anclas, en aplicación del tercer principio de la metodología expuesto en 4.2.1.1, y desglosamos las seis brechas en seis filas con el identificador del instrumento, la carencia diagnosticada, la norma internacional que la respalda, y el índice medible que la metodología mejora o produce. Las seis brechas corresponden a los seis instrumentos con nivel Básico del primer objetivo específico, los cuales proceden del cuestionario de catorce ítems distribuidos en cuatro grupos según la estructura organizacional de la gestión de incidentes. Definimos el nivel Básico como el rango inferior de la escala de madurez y los instrumentos que no superan el 51% de cumplimiento se clasifican en este nivel. La cifra de tres columnas dimana del tercer principio de la metodología, el cual prescribe que toda decisión de diseño debe llevar anclaje explícito a la carencia diagnosticada, a la norma internacional que la respalda, y al índice medible que la metodología mejora o produce. Las normas internacionales proceden de los tres planos transversales expuestos en 4.2.1.1, y en particular adoptamos ISO/IEC 27035-1:2023 e ISO/IEC 27037:2012 desde el plano normativo para las carencias atendidas por la metodología, mientras que adoptamos ISO/IEC 27001:2022 desde el plano institucional para las carencias derivadas al plan.

***Tabla 1*** *Trazabilidad de las seis brechas del diagnóstico con sus tres anclas*

|  |  |  |  |
| --- | --- | --- | --- |
| **#** | **Brecha diagnosticada** | **Norma internacional** | **Índice medible** |
| 1 | G1 Inst. 1 — Detección de incidentes | ISO/IEC 27035-1:2023 (detección) | MTTD |
| 2 | G1 Inst. 4 — Lecciones aprendidas | ISO/IEC 27035-1:2023 (lecciones) | IIAM |
| 3 | G2 Inst. 7 — Preservación de evidencia | ISO/IEC 27037:2012 | Wilcoxon pareada |
| 4 | G3 Inst. 8 — Controles de acceso | ISO/IEC 27001:2022 (A.5.17 + A.8.16) | Derivada al plan |
| 5 | G3 Inst. 10 — Gestión de vulnerabilidades | ISO/IEC 27001:2022 (A.8.23) | Derivada al plan |
| 6 | G4 Inst. 13 — Concienciación y capacitación | ISO/IEC 27001:2022 (A.6.3) | Derivada al plan |

*Nota.* La Tabla 1 muestra las seis brechas del diagnóstico con su triple anclaje: la carencia diagnosticada en el primer objetivo específico, la norma internacional que la respalda, y el índice medible que la metodología mejora o produce. Las tres primeras brechas son atendidas por la metodología Honeypot, mientras que las tres últimas se derivan al plan institucional paralelo. Las normas proceden de los tres planos transversales de §4.2.1.1: el plano normativo para las tres primeras, el plano institucional para las tres últimas. MTTD = tiempo medio de detección. IIAM = índice de impacto del aprendizaje y la mejora. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. Fuente: elaboración propia con base en los resultados del primer objetivo específico.

Asignamos las seis carencias del primer objetivo específico a dos vías de atención, y la cifra de dos vías dimana de que la metodología y el plan institucional son los dos únicos mecanismos disponibles para atender las brechas, dado que la metodología aporta datos verificables sobre tres de las seis y el plan institucional aporta los controles de gestión sobre las otras tres. Atendemos tres brechas con la metodología Honeypot, y derivamos las otras tres al plan institucional paralelo, de modo que la metodología se concentra en las carencias que puede reducir con resultados verificables mientras que el plan institucional absorbe las carencias que requieren intervenciones organizacionales. La cifra de tres brechas atendidas por la metodología dimana de que solo tres de las seis brechas Básico admiten una reducción verificable mediante un honeypot con un indicador cuantificable, mientras que las otras tres requieren intervenciones organizacionales que escapan al alcance del honeypot.

Las tres brechas atendidas por la metodología son la detección de incidentes, las lecciones aprendidas y la preservación de evidencia, y las asignamos respectivamente a la fase tres de captura, la fase cinco de medición y la fase tres de custodia. Las tres fases mencionadas forman parte de las cinco fases secuenciales expuestas en §4.2.1.1, y la asignación de cada brecha a su fase dimana de que cada fase produce los datos verificables que alimentan el índice correspondiente. La captura de eventos genera el tiempo medio de detección, la medición del impacto genera el índice de impacto del aprendizaje y la mejora, y la custodia de evidencia genera los datos para la prueba de Wilcoxon pareada. Los tres índices cubren una dimensión distinta del impacto, a saber, el MTTD mide la velocidad de identificación de eventos, el IIAM evalúa el aprendizaje organizacional mediante la comparación de indicadores antes y después de la implementación, y la prueba de Wilcoxon pareada valida estadísticamente la hipótesis nula de igualdad entre el estado inicial y el estado posterior. La asignación de cada brecha a la metodología dimana de que el honeypot genera datos verificables para cada una de las tres, de modo que la metodología demuestra con datos cuantitativos la reducción correspondiente.

Asignamos las tres carencias restantes del primer objetivo específico a un plan institucional paralelo, y la derivación al plan dimana de que estas tres brechas requieren intervenciones organizacionales que el honeypot no puede realizar, de modo que la metodología las declara fuera de su alcance y las asigna a un plan complementario. Asignamos la brecha de controles de acceso a los controles A.5.17 y A.8.16 de ISO/IEC 27001:2022, la brecha de gestión de vulnerabilidades al control A.8.23 de ISO/IEC 27001:2022, y la brecha de capacitación al control A.6.3 de ISO/IEC 27001:2022. La asignación de cada control dimana de que los controles A.5.17 y A.8.16 cubren el ciclo de gestión de identidades y accesos (autenticación, autorización, monitoreo), el control A.8.23 define el ciclo de gestión de vulnerabilidades técnicas (identificación, evaluación, remediación), y el control A.6.3 regula los programas formativos de concienciación y capacitación. Definimos los tres índices de medición respectivos como la auditoría de gestión de identidades, el ciclo de gestión de parches, y la tasa de aprobación de los programas formativos, y cada índice mide el aspecto específico de la brecha correspondiente. La auditoría mide la eficacia de los controles de acceso, el ciclo de parches mide la velocidad de remediación de vulnerabilidades, y la tasa de aprobación mide la eficacia de la capacitación. Justificamos la distinción entre procesos organizacionales e infraestructura técnica en que los primeros requieren intervención humana y gestión administrativa, mientras que los segundos son sistemas automatizados que el honeypot puede monitorear y verificar directamente. La cifra de tres brechas derivadas dimana de que las tres brechas restantes del diagnóstico Básico corresponden a controles de la norma ISO/IEC 27001:2022 que requieren gestión institucional, y a las que el honeypot no puede aportar datos verificables porque su implementación depende de procesos organizacionales y no de infraestructura técnica.

En la Figura 1 mostramos la separación entre las dos vías de atención, con las tres brechas superiores asignadas a la metodología y las tres brechas inferiores asignadas al plan institucional.

Asignamos las seis carencias del primer objetivo específico a dos vías de atención, y la cifra de dos vías dimana de que la metodología y el plan institucional son los dos únicos mecanismos disponibles para atender las brechas, dado que la metodología aporta datos verificables sobre tres de las seis y el plan institucional aporta los controles de gestión sobre las otras tres. Atendemos tres brechas con la metodología Honeypot y derivamos las otras tres al plan institucional paralelo, de modo que la metodología se concentra en las carencias que puede reducir con resultados verificables mientras que el plan institucional absorbe las carencias que requieren intervenciones organizacionales. La cifra de tres brechas atendidas por la metodología dimana de que solo tres de las seis brechas Básico admiten una reducción verificable mediante un honeypot con un indicador cuantificable, mientras que las otras tres requieren intervenciones organizacionales.

Las tres brechas atendidas por la metodología son la detección de incidentes, las lecciones aprendidas y la preservación de evidencia, y las asignamos respectivamente a la fase tres de captura, la fase cinco de medición y la fase tres de custodia. Las tres fases mencionadas forman parte de las cinco fases secuenciales expuestas en 4.2.1.1, y la asignación de cada brecha a su fase dimana de que cada fase produce los datos verificables que alimentan el índice correspondiente. La captura de eventos genera el tiempo medio de detección, la medición del impacto genera el índice de impacto del aprendizaje y la mejora y la custodia de evidencia genera los datos para la prueba de Wilcoxon pareada. Los tres índices cubren una dimensión distinta del impacto, a saber, el MTTD mide la velocidad de identificación de eventos, el IIAM evalúa el aprendizaje organizacional mediante la comparación de indicadores antes y después de la implementación y la prueba de Wilcoxon pareada valida estadísticamente la hipótesis nula de igualdad entre el estado inicial y el estado posterior. La asignación de cada brecha a la metodología dimana de que el honeypot genera datos verificables para cada una de las tres, de modo que la metodología demuestra con datos cuantitativos la reducción correspondiente.

Asignamos las tres carencias restantes del primer objetivo específico a un plan institucional paralelo, y la derivación al plan dimana de que estas tres brechas requieren intervenciones organizacionales que el honeypot no puede realizar, de modo que la metodología las declara fuera de su alcance y las asigna a un plan complementario. Asignamos la brecha de controles de acceso a los controles A.5.17 y A.8.16 de ISO/IEC 27001:2022, la brecha de gestión de vulnerabilidades al control A.8.23 de ISO/IEC 27001:2022, y la brecha de capacitación al control A.6.3 de ISO/IEC 27001:2022. La asignación de cada control dimana de que los controles A.5.17 y A.8.16 cubren el ciclo de gestión de identidades y accesos (autenticación, autorización, monitoreo), el control A.8.23 define el ciclo de gestión de vulnerabilidades técnicas (identificación, evaluación, remediación), y el control A.6.3 regula los programas formativos de concienciación y capacitación. Definimos los tres índices de medición respectivos como la auditoría de gestión de identidades, el ciclo de gestión de parches, la tasa de aprobación de los programas formativos y cada índice mide el aspecto específico de la brecha correspondiente. La auditoría mide la eficacia de los controles de acceso, el ciclo de parches mide la velocidad de remediación de vulnerabilidades y la tasa de aprobación mide la eficacia de la capacitación. Justificamos la distinción entre procesos organizacionales e infraestructura técnica en que los primeros requieren intervención humana y gestión administrativa, mientras que los segundos son sistemas automatizados que el honeypot puede monitorear y verificar directamente. La cifra de tres brechas derivadas dimana de que las tres brechas restantes del diagnóstico Básico corresponden a controles de la norma ISO/IEC 27001:2022 que requieren gestión institucional y a las que el honeypot no puede aportar datos verificables porque su implementación depende de procesos organizacionales y no de infraestructura técnica.

En la Figura 1 mostramos la separación entre las dos vías de atención, con las tres brechas superiores asignadas a la metodología y las tres brechas inferiores asignadas al plan institucional.

*Figura 1* *Diagrama de atención de las seis brechas del diagnóstico*

*![](data:image/jpeg;base64...)*

*Nota.* La Figura 1 muestra cómo las seis brechas del diagnóstico se enrutan a dos vías de atención. Las tres brechas superiores (G1 Inst. 1 detección, G1 Inst. 4 lecciones, G2 Inst. 7 evidencia) se atienden con la metodología Honeypot y se miden con el tiempo medio de detección, el índice de impacto del aprendizaje y la mejora, y la prueba no paramétrica de Wilcoxon pareada. Las tres brechas inferiores (G3 Inst. 8 accesos, G3 Inst. 10 vulnerabilidades, G4 Inst. 13 capacitación) se derivan al plan institucional paralelo y se atienden con los controles A.5.17, A.8.23 y A.6.3 de ISO/IEC 27001:2022. MTTD = tiempo medio de detección. IIAM = índice de impacto del aprendizaje y la mejora. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. Fuente: elaboración propia con base en los resultados del primer objetivo específico.

Cerramos la atención integral con la separación entre lo que la metodología atiende y lo que se deriva al plan institucional, de modo que el diseño queda conectado con el primer objetivo específico mediante la Tabla 1 y la Figura 1, y las decisiones de diseño que adopta el método se formalizan en §4.2.1.3.

#### 4.2.1.3 Decisiones de diseño asumidas por la metodología Honeypot

Las decisiones de diseño que adopta la metodología Honeypot son cuatro, y cada una responde a una necesidad específica del método. La cifra de cuatro decisiones dimana de que la metodología requiere un alcance acotado, una separación entre procedimiento y ejecución, una trazabilidad explícita, junto con una mejora continua iterativa.

**D1. Alcance acotado.** Justificamos el alcance acotado de la metodología en que solo tres de las seis brechas del primer objetivo específico admiten una reducción verificable mediante un honeypot, mientras que las otras tres requieren intervenciones organizacionales. La metodología se enfoca en la detección de incidentes, las lecciones aprendidas y la preservación de evidencia, que son las tres brechas atendibles con datos cuantitativos del honeypot. La cifra de tres brechas atendidas por la metodología coincide con la separación entre las dos vías de atención de 4.2.1.2, y se justifica porque el honeypot genera datos verificables solo para procesos automatizados que puede monitorear, de modo que las brechas que dependen de intervención humana quedan fuera del alcance del método.

**D2. Separación procedimiento-ejecución.** Justificamos la separación entre procedimiento y ejecución en que la metodología debe poder documentarse, revisarse y validarse con independencia del stack tecnológico específico que se utilice para ejecutarla. La metodología documenta el procedimiento y la ejecución del procedimiento se materializa con un stack específico. La separación dimana del tercer principio expuesto en 4.2.1.1, y se justifica porque el procedimiento es transferible a otras organizaciones, mientras que la ejecución depende del contexto tecnológico de cada organización.

**D3. Trazabilidad explícita.** Justificamos la trazabilidad explícita en que toda decisión de diseño debe llevar anclaje explícito a la carencia diagnosticada, la norma internacional que la respalda y el índice medible que la metodología mejora o produce. La trazabilidad dimana del tercer principio expuesto en 4.2.1.1, y se aplica en la Tabla 1 de 4.2.1.2 mediante el triple anclaje de las seis brechas. La cifra de tres anclas obedece a que la trazabilidad requiere tres elementos mínimos para ser verificable, a saber, la carencia (qué se atiende), la norma (con qué respaldo), y el índice (cómo se mide).

**D4. Mejora continua iterativa.** Justificamos la mejora continua iterativa en que las amenazas evolucionan, los datos del honeypot deben retroalimentar el diseño y la metodología debe adaptarse a los hallazgos. La mejora continua se implementa mediante tres bucles de retroalimentación. El bucle F3→F2 opera en horas y ajusta la captura con base en los eventos detectados, el bucle F4→F1 opera en semanas y ajusta el diseño del señuelo con base en la correlación con la gestión de incidentes y el bucle F5→F1 opera en meses y ajusta el diseño del señuelo con base en la medición del impacto. La cifra de tres bucles dimana del cuarto principio expuesto en 4.2.1.1, y se justifica porque la captura, la correlación y la medición operan en escalas temporales distintas que requieren ajustes a distintos plazos.

La Figura 2 sintetiza las cuatro decisiones adoptadas, y permite ver de un vistazo cómo el alcance acotado, la separación procedimiento-ejecución, la trazabilidad explícita y la mejora continua iterativa se articulan entre sí para configurar el marco de operación de la metodología.

*Figura 2* *Decisiones de diseño adoptadas por la metodología Honeypot*

![](data:image/png;base64...)

*Nota.* La Figura 2 muestra las cuatro decisiones de diseño adoptadas por la metodología Honeypot en flujo secuencial de izquierda a derecha, desde la decisión D1 (alcance acotado) hasta la decisión D4 (mejora continua iterativa). La flecha curvada que retorna de D4 a D1 representa el bucle de retroalimentación mediante el cual la operación de la metodología alimenta el diseño inicial con las lecciones aprendidas. Los íconos sintetizan la esencia de cada decisión, y la numeración 1-4 indica el orden lógico de adopción, no el orden temporal de implementación. D = decisión. Fuente: elaboración propia con base en los principios de 4.2.1.1

Las cuatro decisiones de diseño adoptadas por la metodología configuran un marco de operación que acotamos a tres brechas atendibles, separamos en procedimiento y ejecución, trazamos con triple anclaje, e iteramos con tres bucles de retroalimentación, de modo que el método queda listo para su despliegue operativo en las cinco fases.

### 4.2.2 Arquitectura general de la metodología

La arquitectura general de la metodología que se desarrolla en esta sección operacionaliza la decisión D3 de 4.2.1.3 sobre la trazabilidad explícita y organiza los elementos que estructuran las cinco fases operativas en cuatro ejes que se desglosan en 4.2.2.1 a 4.2.2.4. Adoptamos cuatro ejes porque las cinco fases necesitan cuatro anclas arquitectónicas (una dimensión secuencial, una dimensión transversal, una dimensión de verificabilidad, junto con una dimensión de portabilidad) y la cifra de cuatro dimana de que ningún eje es absorbible por otro sin perder coherencia. La Figura 1 muestra la composición general de la metodología con la integración de las cinco fases, los tres planos, los tres bucles, las cinco métricas, los cuatro objetivos específicos, y las tres brechas atendidas.

Los cuatro ejes se desarrollan en orden, de modo que el primer eje de 4.2.2.1 fija la secuencia de las cinco fases y los tres bucles de retroalimentación, el segundo eje de 4.2.2.2 declara los tres planos transversales y las catorce categorías funcionales de tecnología, el tercer eje de 4.2.2.3 resume la trazabilidad de tres columnas por fase, junto con el cuarto eje de 4.2.2.4 que establece los prerrequisitos institucionales y las condiciones de transferibilidad. Las cinco fases se articulan sobre los cuatro ejes, donde la primera diseña el señuelo, la segunda lo despliega, la tercera captura y custodia, la cuarta correlaciona con la gestión institucional, junto con la quinta que mide el impacto y recoge las lecciones aprendidas.

*Figura 1* *Composición general de la metodología Honeypot*

![](data:image/jpeg;base64...)

*Nota.* La Figura 1 muestra la composición general de la metodología con la integración de las cinco fases secuenciales (diseño del señuelo, despliegue aislado, captura y custodia, correlación con gestión institucional, medición y lecciones), los tres planos transversales (normativo con ISO/IEC 27035-1:2023, NIST SP 800-61 Rev. 3, MITRE ATT&CK, e ISO/IEC 27037:2012; operativo con hash, sellado temporal, inmutabilidad, roles, y geolocalización; institucional con plan de respuesta a incidentes, reglas del sistema de gestión de información y eventos de seguridad, indicadores de compromiso, orquestación, y comité de seguridad), los tres bucles de retroalimentación con latencia diferenciada (horas, semanas, meses), las cinco métricas (tiempo medio de detección, tiempo medio de respuesta, índice de madurez en gestión de incidentes, índice de impacto del aprendizaje y la mejora, y prueba no paramétrica de Wilcoxon pareada), la cadena causal de los cuatro objetivos específicos, y las tres brechas atendidas por la metodología con sus porcentajes del primer objetivo específico. MTTD = tiempo medio de detección. MTTR = tiempo medio de respuesta. IMGI = índice de madurez en gestión de incidentes. IIAM = índice de impacto del aprendizaje y la mejora. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. NIST = Instituto Nacional de Estándares y Tecnología. MITRE ATT&CK = marco de tácticas, técnicas y procedimientos adversarios. SHA-256 = algoritmo de hash seguro de 256 bits. NTP = protocolo de tiempo de red. WORM = escribir una vez, leer muchas. DEFR = respondedor de evidencia digital. DES = especialista en evidencia digital. IRP = plan de respuesta a incidentes. SIEM = gestión de información y eventos de seguridad. MISP = plataforma de compartición de información de malware. SOAR = orquestación, automatización y respuesta de seguridad. IOC = indicadores de compromiso. TTP = tácticas, técnicas y procedimientos. Fuente: elaboración propia con base en el primer objetivo específico y las decisiones de diseño de 4.2.1.3.

#### 4.2.2.1 Estructura secuencial de las cinco fases y sus bucles de retroalimentación

La estructura secuencial de la metodología Honeypot organiza las cinco fases operativas en orden temporal y articula los tres bucles de retroalimentación que cierran el ciclo de mejora continua. Adoptamos cinco fases en que el método cubre el ciclo completo desde el diseño del señuelo hasta la medición del impacto y adoptamos tres bucles en que la captura, la correlación y la medición operan en escalas temporales distintas. La cifra de cinco fases obedece a que cada fase cubre una etapa del ciclo que no puede omitirse sin perder coherencia, la cifra de tres bucles obedece a que cada escala temporal requiere su propio mecanismo de retorno, de modo que el ajuste no se posterga hasta el cierre del ciclo.

La primera fase diseña el señuelo (F1) con cinco decisiones de diseño (activo, nivel de interacción, contenido, mecanismos de detección, perfil del atacante), la segunda fase lo despliega de forma aislada (F2) con tres niveles de interacción, y la tercera fase captura, enriquece y custodia los eventos generados (F3) que alimentan el MTTD. La cuarta fase correlaciona los eventos con la gestión institucional de incidentes (F4), y produce los datos para la prueba no paramétrica de Wilcoxon pareada, y la quinta fase mide el impacto en el aprendizaje y la mejora organizacional (F5), y produce el IIAM que cierra el ciclo. Cada fase se desarrolla en detalle en 4.2.3 a 4.2.7 con su producto específico, su ancla normativa y su índice de medición, de modo que la estructura secuencial sirve de índice navegable del método.

El primer bucle (F3→F2, táctico, horas) ajusta la configuración del honeypot en la fase 2 con base en los eventos no esperados que detecta la fase 3, y su latencia típica es de horas porque la captura opera de forma continua. El segundo bucle (F4→F1, operacional, semanas) ajusta el perfil del señuelo en la fase 1 con base en las técnicas MITRE ATT&CK observadas en la gestión de incidentes de la fase 4, y su latencia típica es de semanas porque la correlación requiere acumular suficientes casos. El tercer bucle (F5→F1, estratégico, meses) ajusta el diseño del señuelo en la fase 1 con base en las lecciones aprendidas de la medición del impacto de la fase 5, y su latencia típica es de meses porque la medición requiere completar un ciclo completo de despliegue.

Las tres fases de captura, correlación y medición producen los tres índices de impacto (MTTD, IIAM, Wilcoxon pareada) que sustentan la prueba de hipótesis del cuarto objetivo específico y los tres bucles coinciden con los tres bucles del cuarto principio de 4.2.1.1, de modo que la estructura secuencial articula la captura, la correlación y la medición en una cadena continua de mejora.

#### 4.2.2.2 Planos transversales de la metodología y categorías funcionales de tecnología

Los tres planos transversales que se desarrollan en esta sección provienen del triple anclaje de la trazabilidad establecido en 4.2.1.2, donde se decidió que toda decisión del método debe llevar tres anclas (la carencia diagnosticada, la norma internacional y el índice medible). Las catorce categorías funcionales que también se desarrollan en esta sección provienen de las cinco fases de la metodología expuestas en 4.2.2.1, donde se decidió que las cinco fases cubren el ciclo completo desde el diseño del señuelo hasta la medición del impacto. Los planos responden a la pregunta de cómo se valida cada decisión y las categorías responden a la pregunta de qué funciones ejecuta el método. Adoptamos tres planos porque el triple anclaje exige tres tipos de respaldo, y adoptamos catorce categorías porque las cinco fases requieren catorce funciones tecnológicas.

El plano normativo es el primero de los tres y responde a la pregunta de con qué norma internacional se respalda cada decisión, y se compone de ISO/IEC 27035-1:2023 para la gestión de incidentes, NIST SP 800-61 Rev. 3 para el manejo de incidentes de seguridad, MITRE ATT&CK para las tácticas y técnicas adversarias, e ISO/IEC 27037:2012 para la preservación de evidencia digital. El plano institucional es el segundo de los tres y responde a la pregunta de con qué control de la organización se implementa cada decisión y se compone de los controles de ISO/IEC 27001:2022 que la metodología presupone implementados. El plano operativo es el tercero de los tres y responde a la pregunta de con qué métrica se mide cada decisión y se compone del MTTD para la velocidad de detección, del IIAM para el aprendizaje organizacional y de la prueba no paramétrica de Wilcoxon pareada para la validación estadística de la hipótesis nula.

Las catorce categorías funcionales operacionalizan las cinco fases, de modo que cada fase agrupa las funciones que la ejecución materializa con productos específicos. La cifra de catorce categorías dimana de la suma de funciones por fase, donde la fase uno de diseño aporta tres categorías, la fase dos de despliegue aporta dos categorías, la fase tres de captura aporta tres categorías, la fase cuatro de correlación aporta tres categorías, junto con la fase cinco de medición que aporta tres categorías. La distribución 3+2+3+3+3 = 14 obedece a las funciones específicas que cada fase necesita ejecutar, y la Tabla 2 presenta las catorce categorías con su fase de origen, su plano de anclaje, y su función específica.

*Tabla 2* *Catorce categorías funcionales de tecnología con su plano transversal*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **#** | **Fase** | **Categoría funcional** | **Plano** | **Función específica** |
| 1 | F1 | Identificación de activo | Operativo | Identificar el activo que el señuelo debe proteger |
| 2 | F1 | Configuración del señuelo | Normativo | Configurar el perfil del señuelo según ISO/IEC 27035-1:2023 |
| 3 | F1 | Perfil del atacante | Normativo | Mapear el perfil contra técnicas de MITRE ATT&CK |
| 4 | F2 | Aislamiento de red | Institucional | Segmentar el señuelo del tráfico institucional |
| 5 | F2 | Entorno controlado | Operativo | Preparar el entorno de despliegue aislado |
| 6 | F3 | Captura de eventos | Normativo | Registrar los eventos según ISO/IEC 27035-1:2023 |
| 7 | F3 | Enriquecimiento | Operativo | Agregar contexto a los eventos capturados |
| 8 | F3 | Custodia de evidencia | Normativo | Preservar la cadena de custodia según ISO/IEC 27037:2012 |
| 9 | F4 | Normalización | Operativo | Estandarizar el formato de los eventos para correlación |
| 10 | F4 | Correlación con tickets | Institucional | Vincular los eventos con la gestión institucional de incidentes |
| 11 | F4 | Mapeo con ATT&CK | Normativo | Clasificar las técnicas observadas según MITRE ATT&CK |
| 12 | F5 | Cálculo de MTTD | Operativo | Medir el tiempo medio de detección |
| 13 | F5 | Cálculo de IIAM | Operativo | Medir el aprendizaje organizacional |
| 14 | F5 | Reporte de lecciones | Institucional | Documentar las lecciones aprendidas y las mejoras |

*Nota.* La Tabla 2 presenta las catorce categorías funcionales de tecnología que el procedimiento requiere para ejecutar las cinco fases, con su plano de anclaje y su función específica. La distribución 3+2+3+3+3 = 14 por fase obedece a las funciones específicas que cada fase necesita ejecutar y la asignación de cada categoría a un plano obedece al tipo de respaldo que la categoría requiere, de modo que las categorías con respaldo en normas internacionales se asignan al plano normativo, las categorías con respaldo en controles institucionales se asignan al plano institucional, junto con las categorías con respaldo en métricas operativas se asignan al plano operativo. Los productos específicos que ejecutan cada categoría se desarrollan en el tercer objetivo específico, donde las catorce funciones se materializan con veintiún productos del stack. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. NIST = Instituto Nacional de Estándares y Tecnología. MITRE ATT&CK = marco de tácticas, técnicas y procedimientos adversarios. MTTD = tiempo medio de detección. IIAM = índice de impacto del aprendizaje y la mejora. Fuente: elaboración propia con base en las cinco fases de la metodología.

Las catorce categorías funcionales se anclan en los tres planos transversales de modo que cada categoría tiene respaldo verificable, y la Tabla 2 muestra la asignación por fase, plano, y función. Los productos específicos que ejecutan cada categoría se desarrollan en el tercer objetivo específico, y en este las catorce funciones se materializan con veintiún productos del stack tecnológico, de modo que la trazabilidad de cada categoría hacia su producto se cierra en 4.2.3 a 4.2.7.

#### 4.2.2.3 Trazabilidad metodológica de las cinco fases

La trazabilidad metodológica de las cinco fases que se desarrolla en esta sección operacionaliza el principio de trazabilidad explícita formalizado en la decisión D3 de 4.2.1.3, según el cual cada decisión del método debe llevar anclaje a la carencia diagnosticada, la norma internacional, junto con el índice medible. La Tabla 3 presenta las cinco fases con su brecha diagnosticada, su norma internacional y su índice medible, de modo que cada fase queda conectada con el primer objetivo específico y con los tres planos transversales de 4.2.2.2. Adoptamos tres columnas de anclaje porque la trazabilidad exige tres elementos mínimos para ser verificable y adoptamos cinco filas porque cada una de las cinco fases requiere su propio registro de trazabilidad.

Las fases uno y dos son preparatorias porque no atienden brechas directamente, pero son condiciones necesarias para que las fases tres, cuatro y cinco atiendan las tres brechas asignadas a la metodología. La fase uno diseña el señuelo con cinco decisiones y se ancla en ISO/IEC 27035-1:2023 para la gestión de incidentes. La fase dos despliega el señuelo de forma aislada y se ancla en ISO/IEC 27001:2022 para los controles institucionales de acceso. La fase tres capturas y custodia los eventos, atiende las brechas G1 Inst. 1 de detección de incidentes y G2 Inst. 7 de preservación de evidencia, se ancla en ISO/IEC 27035-1:2023 y en ISO/IEC 27037:2012, y produce el MTTD junto con los datos para la prueba de Wilcoxon pareada. La fase cuatro aplica la prueba de Wilcoxon pareada sobre los datos que custodia la fase tres, se ancla en MITRE ATT&CK y en ISO/IEC 27035-1:2023, y produce el resultado de la prueba como índice medible. La fase cinco mide el impacto en el aprendizaje y la mejora, atiende la brecha G1 Inst. 4 de lecciones aprendidas, se ancla en ISO/IEC 27035-1:2023 y en NIST SP 800-61 Rev. 3, y produce el IIAM como índice medible.

*Tabla 3* *Trazabilidad metodológica de las cinco fases con su triple anclaje*

|  |  |  |  |
| --- | --- | --- | --- |
| **Fase** | **Brecha diagnosticada** | **Norma internacional** | **Índice medible** |
| F1 Diseño del señuelo | (preparatoria, no atiende directa) | ISO/IEC 27035-1:2023 | (preparatoria, no produce) |
| F2 Despliegue aislado | (preparatoria, no atiende directa) | ISO/IEC 27001:2022 | (preparatoria, no produce) |
| F3 Captura y custodia | G1 Inst. 1 (detección), G2 Inst. 7 (preservación) | ISO/IEC 27035-1:2023, ISO/IEC 27037:2012 | MTTD, datos para Wilcoxon pareada |
| F4 Correlación institucional | (intermedia, aplica Wilcoxon) | MITRE ATT&CK, ISO/IEC 27035-1:2023 | Wilcoxon pareada (resultado del test) |
| F5 Medición de impacto | G1 Inst. 4 (lecciones aprendidas) | ISO/IEC 27035-1:2023, NIST SP 800-61 Rev. 3 | IIAM |

*Nota.* La Tabla 3 presenta la trazabilidad metodológica de las cinco fases con su triple anclaje a la brecha diagnosticada del primer objetivo específico, la norma internacional del plano normativo de 4.2.2.2, y el índice medible del plano operativo de 4.2.2.2. Las fases uno y dos son preparatorias porque no atienden brechas directamente, pero son condiciones necesarias para que las fases tres, cuatro y cinco atiendan las tres brechas asignadas a la metodología. La fase cuatro es intermedia porque aplica la prueba de Wilcoxon pareada sobre los datos que custodia la fase tres, de modo que el resultado del test se produce en la fase cuatro y los datos se custodian en la fase tres. Los tres índices medibles (MTTD, Wilcoxon pareada, IIAM) son los que validan la hipótesis nula en el cuarto objetivo específico. MTTD = tiempo medio de detección. IIAM = índice de impacto del aprendizaje y la mejora. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. NIST = Instituto Nacional de Estándares y Tecnología. MITRE ATT&CK = marco de tácticas, técnicas y procedimientos adversarios. Fuente: elaboración propia con base en el primer objetivo específico, los tres planos transversales de 4.2.2.2, y la decisión de diseño D3 de 4.2.1.3.

La Tabla 3 muestra la trazabilidad completa de las cinco fases con su triple anclaje, de modo que cada fase queda conectada con el primer objetivo específico, con los tres planos transversales de 4.2.2.2, y con los tres índices que validan la hipótesis nula en el cuarto objetivo específico. Las cinco fases cubren las tres brechas asignadas a la metodología y los tres índices (MTTD, Wilcoxon pareada, IIAM) son los que sustentan la prueba de hipótesis de 4.2.7.

#### 4.2.2.4 Prerrequisitos de la organización y transferibilidad de la metodología

Los prerrequisitos de la organización y la transferibilidad de la metodología que se desarrollan en esta sección provienen de dos decisiones adoptadas en 4.2.1.3: la decisión D2 de separar el procedimiento de la ejecución y la decisión D4 de mejorar continuamente con la operación. Los prerrequisitos operacionalizan las condiciones institucionales que la organización receptora debe cumplir para ejecutar la metodología, y la transferibilidad operacionaliza la portabilidad del procedimiento entre organizaciones. Adoptamos tres categorías de prerrequisitos porque la metodología requiere condiciones de entorno controlado, personal capacitado, procesos institucionales, y la transferibilidad dimana de que la separación entre procedimiento y ejecución permite replicar el método sin modificar el documento.

Los prerrequisitos se organizan en tres categorías que la organización receptora debe cumplir para ejecutar la metodología, la primera categoría es el entorno controlado (aislamiento de red, segmentación de tráfico, recursos de cómputo dedicados), la segunda es el personal capacitado (formación en gestión de incidentes, preservación de evidencia digital), junto con la tercera que son los procesos institucionales (gestión de accesos, gestión de vulnerabilidades, gestión de cambios). La Tabla 4 presenta los prerrequisitos con su categoría, su requisito específico, y su norma fuente.

*Tabla 4* *Prerrequisitos de la organización para ejecutar la metodología*

|  |  |  |
| --- | --- | --- |
| **Categoría** | **Requisito específico** | **Norma fuente** |
| Entorno controlado | Aislamiento de red | ISO/IEC 27001:2022 (A.8.20) |
| Entorno controlado | Segmentación de tráfico | ISO/IEC 27001:2022 (A.8.22) |
| Entorno controlado | Recursos de cómputo dedicados | (requisito operativo) |
| Personal capacitado | Gestión de incidentes | ISO/IEC 27035-1:2023 |
| Personal capacitado | Preservación de evidencia digital | ISO/IEC 27037:2012 |
| Procesos institucionales | Gestión de accesos | ISO/IEC 27001:2022 (A.5.16, A.8.3) |
| Procesos institucionales | Gestión de vulnerabilidades | ISO/IEC 27001:2022 (A.8.8) |
| Procesos institucionales | Gestión de cambios | ISO/IEC 27001:2022 (A.8.32) |

*Nota.* La Tabla 4 presenta los ocho prerrequisitos que la organización receptora debe cumplir para ejecutar la metodología, distribuidos en tres categorías (entorno controlado, personal capacitado, procesos institucionales). Cada prerrequisito se ancla en una norma internacional del plano institucional de 4.2.2.2, y la categoría de entorno controlado se complementa con un requisito operativo de recursos de cómputo dedicados que no tiene anclaje normativo específico. La asignación de los controles de ISO/IEC 27001:2022 sigue la nomenclatura oficial de la norma, donde A.5 se refiere a controles organizacionales y A.8 a controles tecnológicos. ISO/IEC = Organización Internacional de Normalización y Comisión Electrotécnica Internacional. Fuente: elaboración propia con base en ISO/IEC 27001:2022, ISO/IEC 27035-1:2023, e ISO/IEC 27037:2012.

La transferibilidad de la metodología dimana de la decisión D2 de 4.2.1.3, que separa el procedimiento documentado de la ejecución materializada con un stack específico. El procedimiento es portable a otras organizaciones porque no depende de un producto determinado y la ejecución es context-specific porque depende del stack tecnológico y los recursos de cada organización receptora. La separación entre procedimiento y ejecución permite que una organización con entorno controlado, personal capacitado y procesos institucionales pueda adoptar el método sustituyendo el stack de ejecución sin modificar el documento del procedimiento, de modo que el método se replica sin reescribirse.

La Tabla 4 y el argumento de transferibilidad cierran la arquitectura de la metodología en 4.2.2, de modo que la metodología queda con sus cinco fases, sus tres planos transversales, sus catorce categorías, su trazabilidad, sus prerrequisitos y su transferibilidad. La ejecución materializada de los prerrequisitos con productos específicos se desarrolla en el tercer objetivo específico, donde las catorce funciones se materializan con veintiún productos del stack tecnológico y la articulación final de los cuatro bloques de 4.2.2 se desarrolla en 4.2.8.

#### 4.2.2.5 Justificación metodológica de las cinco actividades por fase

La metodología Honeypot estructura cada fase con cinco actividades operativas y esta decisión arquitectónica se sustenta en tres criterios verificables que descartan un número menor o un número mayor de actividades por fase. Las cinco posiciones del ciclo de vida del señuelo requieren un número específico de actividades cada una, de modo que la cantidad de actividades por fase se deriva de la estructura del ciclo y no es arbitraria. Los tres criterios verificables que sustentan esta decisión se documentan en las Tablas 1 a 4 que acompañan esta sección.

**Criterio 1 · Coherencia con el ciclo de vida del señuelo**

El primer criterio que sustenta la decisión de cinco actividades por fase es la coherencia con el ciclo de vida del señuelo, dado que el ciclo se extiende desde el diseño del señuelo hasta el aprendizaje organizacional y las cinco fases de la metodología ocupan cinco posiciones complementarias dentro de ese ciclo. Cada fase ejecuta una posición específica y la agrupación en cinco actividades por fase refleja las cinco etapas operativas que cada posición requiere para cumplir su propósito sin solaparse con las posiciones de las otras fases, lo que confirma que la cadena opera como un sistema y no como una secuencia de tareas aisladas.

*Tabla 1. Posiciones de las cinco fases en el ciclo de vida del señuelo*

|  |  |  |
| --- | --- | --- |
| **Posición en el ciclo** | **Fase** | **Rol dentro de la cadena causal** |
| 1 (diseño) | Fase 1 · Diseño del señuelo | Define qué se engaña, cómo se engaña, y a quién se engaña |
| 2 (preparación) | Fase 2 · Despliegue aislado | Aísla el señuelo en una red separada para evitar contaminación |
| 3 (operación) | Fase 3 · Captura, enriquecimiento y custodia | Registra las acciones del adversario con validez forense |
| 4 (análisis) | Fase 4 · Correlación con gestión de incidentes | Vincula los eventos capturados con el sistema institucional |
| 5 (cierre) | Fase 5 · Medición de impacto y lecciones aprendidas | Cuantifica la efectividad y retroalimenta al siguiente ciclo |

*Nota.* La Tabla 1 muestra que las cinco fases se ubican en posiciones complementarias del ciclo de vida, de modo que ninguna fase duplica el rol de otra y la cadena causal opera como un sistema completo desde el diseño hasta el aprendizaje. La ausencia de cualquiera de las cinco fases dejaría al ciclo sin una de sus posiciones, lo que comprometería la trazabilidad de la cadena.

**Criterio 2 · Trazabilidad normativa verificable**

El segundo criterio que sustenta la decisión de cinco actividades por fase es la trazabilidad normativa verificable, dado que la metodología no se construye sobre supuestos sino sobre referencias internacionales y cada actividad debe respaldarse en al menos una norma para garantizar que la decisión tiene base técnica. La trazabilidad normativa se demuestra en la Tabla 2, en la cual las cinco actividades de la fase piloto aparecen asociadas a la norma que las respalda, con lo cual se verifica que la agrupación en cinco actividades no es arbitraria sino necesaria para cubrir las cláusulas y controles que las normas requieren.

*Tabla 2. Trazabilidad normativa de las cinco actividades de la Fase 1*

|  |  |  |
| --- | --- | --- |
| **Actividad** | **Norma que la respalda** | **Cláusula o control específico** |
| 1. Seleccionar el activo | ISO/IEC 27002:2022 | A.5.9 (inventario de activos) |
| 2. Establecer el nivel de interacción | NIST SP 800-61 Rev. 3 | Sección 3 (preparación) |
| 3. Configurar el contenido | ISO/IEC 27035-1:2023 | Cláusula 5 (preparación) |
| 4. Instrumentar la detección | ISO/IEC 27002:2022 | A.8.16 (actividades de monitoreo) |
| 5. Caracterizar al adversario | MITRE ATT&CK v19.1 | TTPs (Tácticas, Técnicas y Procedimientos) |

*Nota.* La Tabla 2 muestra que las cinco actividades de la fase piloto se respaldan en al menos una norma internacional, la trazabilidad normativa garantiza que la metodología no se construye sobre supuestos sino sobre referencias verificables.

**Criterio 3 · Separación de roles institucionales**

El tercer criterio que sustenta la decisión de cinco actividades por fase es la separación de roles institucionales, dado que la concentración de responsabilidades en una sola persona o área compromete la auditoría organizacional y diluye la trazabilidad de la cadena causal. La separación de roles se demuestra en la Tabla 3, en la cual las cinco actividades de la fase piloto se asignan a cinco roles distintos dentro de la organización, sin solapamiento entre ellos, con lo cual cada actividad tiene un responsable identificable y la auditoría puede verificar la ejecución de cada actividad por separado.

*Tabla 3. Roles institucionales asignados a las cinco actividades de la Fase 1*

|  |  |  |
| --- | --- | --- |
| **Actividad** | **Rol institucional** | **Función dentro de la organización** |
| 1. Seleccionar el activo | Arquitecto de seguridad | Define los servicios críticos que la metodología debe proteger |
| 2. Establecer el nivel de interacción | Ingeniero de seguridad | Configura el balance entre visibilidad y contención del señuelo |
| 3. Configurar el contenido | Administrador del señuelo | Materializa el señuelo según el activo seleccionado |
| 4. Instrumentar la detección | Analista SOC | Activa los mecanismos que registran la interacción del adversario |
| 5. Caracterizar al adversario | Analista de inteligencia | Documenta el perfil del atacante para refinar el señuelo en ciclos futuros |

*Nota.* La Tabla 3 muestra que las cinco actividades de la Fase 1 se asignan a cinco roles distintos dentro de la organización, lo que evita la concentración de responsabilidades y facilita la auditoría. Los mismos cinco patrones de separación de roles se replican en las Fases 2 a 5, con los roles ajustados al propósito de cada fase (administrador de red para la Fase 2, analista forense para la Fase 3, gestor del SGSI para la Fase 4 y gestor de mejora continua para la Fase 5).

**Matriz de verificación cruzada**

La Tabla 4 sintetiza la verificación cruzada de las cinco actividades de la fase piloto contra los cinco criterios que cada actividad debe cumplir, con lo cual se demuestra de manera compacta que las cinco actividades satisfacen simultáneamente los tres criterios presentados.

*Tabla 4. Matriz de verificación cruzada (5 actividades × 5 criterios)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Actividad** | **Norma** | **Brecha OE1** | **Categoría** | **Rol** | **Resultado verificable** |
| 1. Seleccionar el activo | ✓ | ✓ | ✓ | ✓ | Documento de selección del activo prioritario |
| 2. Establecer el nivel de interacción | ✓ | ✓ | ✓ | ✓ | Especificación del nivel de interacción del señuelo |
| 3. Configurar el contenido | ✓ | ✓ | ✓ | ✓ | Especificación del contenido del señuelo |
| 4. Instrumentar la detección | ✓ | ✓ | ✓ | ✓ | Especificación de disparadores de detección |
| 5. Caracterizar al adversario | ✓ | ✓ | ✓ | ✓ | Perfil documentado del adversario tipo |

*Nota.* La Tabla 4 muestra la matriz de verificación cruzada de las cinco actividades de la Fase 1 contra los cinco criterios que cada actividad debe cumplir (norma, brecha del primer objetivo, categoría funcional, rol institucional y resultado verificable). Las cinco actividades cumplen los cinco criterios sin excepción, lo que confirma que la decisión de cinco actividades por fase no es arbitraria sino necesaria.

La decisión de cinco actividades por fase responde a un balance entre suficiencia y eficiencia operativa, dado que cuatro actividades por fase serían insuficientes porque dejarían al menos un rol sin ejecutar, lo que comprometería la trazabilidad normativa y la separación de roles que el primer y el segundo objetivo específico requieren, con lo cual una de las cinco posiciones del ciclo de vida quedaría sin ejecutar. Seis actividades por fase serían redundantes porque duplicarían responsabilidades entre roles, lo que diluiría la separación de roles y aumentaría la complejidad operativa sin agregar valor metodológico. La agrupación en cinco actividades por fase es, por lo tanto, el punto de equilibrio que satisface los tres criterios verificables con la menor complejidad operativa posible.

La consecuencia operativa de estructurar cada fase con cinco actividades es que la metodología Honeypot requiere, como mínimo, un equipo multidisciplinario de cinco roles institucionales para su ejecución completa y que cada rol participa en una sola actividad por fase con responsabilidades claramente delimitadas.

### 4.2.3 Fase 1. Diseño del señuelo

El señuelo es el primer paso de la cadena metodológica, y su función principal es atraer al adversario hacia un servicio que parece real, con el propósito de registrar las técnicas que el adversario utiliza cuando cree que está atacando un sistema productivo de la administración tributaria. La información que el señuelo genera alimenta las fases siguientes de captura, correlación y medición, por lo cual el señuelo resulta indispensable para que la cadena metodológica opere.

La norma ISO/IEC 27035-1:2023 establece que la planificación del señuelo es la base del ciclo de gestión de incidentes y esta Fase 1 traduce esa planificación al contexto de la administración tributaria. La traducción se concreta en la configuración de un servicio tributario falso que atrae al adversario y registra las técnicas que este emplea contra la administración.

Las brechas que justifican esta fase son las que el diagnóstico del primer objetivo específico identifica en la detección y preservación de eventos. Las brechas principales corresponden al Grupo 1 Instrumento 1 (detección) y al Grupo 2 Instrumento 7 (preservación), las cuales requieren un señuelo formalizado para provocar al adversario, registrar sus tácticas, técnicas y procedimientos en un entorno controlado.

Las Fases 4 y 5 envían retroalimentación a esta fase cuando la correlación con la gestión de incidentes identifica ajustes necesarios, o cuando la medición del impacto detecta desviaciones que conviene corregir, con lo cual la planificación del señuelo se actualiza de manera continua a partir de la información operativa que las fases posteriores generan.

Como condiciones previas, esta fase requiere un inventario de activos formalizado por la administración, una evaluación de riesgos vigente y la autorización formal de la alta dirección para operar el señuelo dentro del entorno de la organización. Estas condiciones garantizan que el diseño del señuelo parte de condiciones formales reconocidas por la organización.

*Figura 1 Vista integral de la Fase 1 dentro de la cadena causal de la metodología Honeypot*

![](data:image/png;base64...)

*Nota.* La Figura 1 muestra la vista integral de la Fase 1 con las tres razones que justifican la fase (brechas, normas, condiciones), las cinco actividades con su norma y la brecha que cierran y el entregable con los bucles que recibe. La metodología se diseñó en un entorno controlado, y la ejecución operativa del señuelo corresponde al tercer objetivo específico.

**Actividades de la Fase 1**

1. **Seleccionar el activo a proteger**. ISO/IEC 27001:2022 exige que toda organización cuente con un inventario de activos y el señuelo requiere un activo creíble para provocar al adversario, la actividad selecciona el activo específico que la administración tributaria expone como señuelo, lo que se documenta con la descripción del servicio productivo que el señuelo imita, junto con la justificación de por qué ese activo resulta atractivo para el adversario que opera en el contexto tributario y la evaluación del riesgo que el señuelo implica para los sistemas productivos. La actividad cubre la categoría funcional de inventario de activos del eje institucional y se alinea con el control A.5.9 de ISO/IEC 27001:2022 sobre el inventario de activos, lo que garantiza que el señuelo parte de un activo formalmente reconocido por la organización y que la trazabilidad entre el activo señuelo y los activos productivos de la administración queda establecida desde el inicio.
2. **Establecer el nivel de interacción del señuelo**. La administración tributaria necesita un señuelo que provoque al adversario sin poner en riesgo los sistemas productivos y la decisión se toma entre interacción baja, media, o alta según el riesgo que la administración acepta. La actividad establece el nivel de compromiso del señuelo con el adversario, junto con los servicios expuestos, los protocolos habilitados y los datos simulados, con lo cual la Fase 2 configura el aislamiento y la segmentación de la red según el nivel de interacción definido y la Fase 3 instrumenta la captura de eventos con la profundidad que el nivel requiere. La actividad cubre las categorías funcionales de configuración de red, segmentación de la red y exposición controlada del eje operativo, la decisión del nivel de interacción queda registrada en el documento de arquitectura con la justificación técnica que respalda la elección, lo que permite auditar la decisión posteriormente.
3. **Configurar el contenido del señuelo.** El señuelo debe parecerse a los servicios reales de la administración tributaria para que el adversario lo identifique como objetivo legítimo y la norma ISO/IEC 27035-1:2023 prescribe que el señuelo refleje los servicios productivos. La actividad configura la lista de servicios expuestos al adversario, junto con la apariencia visual, las rutas de navegación y los formularios simulados, con lo cual el señuelo tiene la apariencia creíble que el adversario espera de un servicio tributario real y la brecha del Grupo 1 Instrumento 1 (detección) se cierra porque el señuelo opera como un servicio productivo más dentro del catálogo de servicios. La actividad cubre las categorías funcionales de contenido del señuelo, servicios simulados, datos sintéticos del eje operativo y la definición del contenido opera como insumo directo para la configuración que la Fase 2 realiza en el entorno aislado. La Figura 2 ilustra un ejemplo concreto del tipo de servicio tributario falso que la actividad configura, un portal que simula los servicios tributarios de la administración con el propósito de provocar al adversario y registrar las técnicas que este emplea.

*Figura 2 Ejemplo de señuelo: portal que simula los servicios tributarios de la administración*

![](data:image/jpeg;base64...)

*Nota.* La Figura 2 muestra un ejemplo concreto del servicio tributario falso que la Actividad 3 configura, el portal simula los servicios reales de la administración tributaria, con apariencia visual, rutas de navegación y formularios que el adversario espera encontrar, lo que cierra la brecha del Grupo 1 Instrumento 1 (detección) al hacer que el señuelo opere como un servicio productivo más dentro del catálogo. La metodología se diseñó en un entorno controlado y la ejecución operativa del señuelo corresponde al tercer objetivo específico.

1. **Instrumentar los mecanismos de detección.** El señuelo debe emitir alertas operativas cuando el adversario interactúa con él y la brecha del Grupo 1 Instrumento 1 (detección) requiere que la organización disponga de mecanismos que identifiquen la interacción del adversario. La actividad instrumenta la lista de alertas operativas, junto con los disparadores de cada alerta, los formatos de los eventos y los destinos de las alertas, con lo cual la Fase 3 configura la captura de eventos según los mecanismos definidos y la Fase 4 correlaciona los eventos con la gestión de incidentes según los disparadores que la actividad establece. La actividad cubre las categorías funcionales de alertas operativas, disparadores y formatos de eventos del eje operativo, la definición de los mecanismos de detección se alinea con la directriz de registro de eventos de ISO/IEC 27035-1:2023, lo que garantiza la coherencia entre la detección del señuelo y el ciclo de gestión de incidentes.
2. **Caracterizar el perfil del atacante.** Las técnicas que el señuelo provoca deben mapearse a las tácticas de MITRE ATT&CK v19.1 y la metodología requiere un perfil que cubra las técnicas relevantes para el contexto tributario. La actividad caracteriza el perfil con las tácticas, las técnicas y los identificadores de MITRE ATT&CK que el señuelo provoca, con lo cual se habilita la correlación posterior con la gestión de incidentes y el señuelo atrae al adversario con técnicas específicas que este emplea contra la administración tributaria. La actividad cubre las categorías funcionales de mapeo de tácticas, técnicas y de identificadores de MITRE ATT&CK del eje operativo y la definición del perfil del atacante opera como insumo directo para la correlación que la Fase 4 realiza con el ciclo de gestión de incidentes. La Figura 3 muestra el mapeo concreto de las técnicas que el señuelo provoca a las tácticas de MITRE ATT&CK v19.1.

*Figura 3 Mapeo de las técnicas del señuelo a las tácticas de MITRE ATT&CK v19.1*

![](data:image/jpeg;base64...)

*Nota.* La Figura 3 muestra el mapeo de las técnicas que el señuelo provoca a las tácticas de MITRE ATT&CK v19.1, lo que documenta el perfil del atacante que la Actividad 5 caracteriza. El mapeo cubre las tácticas de reconocimiento, acceso inicial, ejecución, persistencia, escalada de privilegios, evasión de defensas, acceso a credenciales, descubrimiento, movimiento lateral y exfiltración, con los identificadores específicos que la metodología adopta como referencia para el contexto tributario de la administración.

**Cierre, transferencia y retroalimentación con la fase siguiente**

La Fase 1 cierra con un documento de arquitectura del señuelo, que sirve como puente entre el diseño metodológico y el despliegue operativo de la cadena causal de la metodología Honeypot. El documento condensa las cinco actividades de la fase con sus respectivas justificaciones y articula el activo seleccionado, el nivel de interacción, el contenido del señuelo, los mecanismos de detección y el perfil del atacante, de modo que la Fase 2 cuenta con un insumo completo para configurar el aislamiento y la segmentación del entorno donde el señuelo se materializa. El documento incorpora además la especificación de los bucles de retroalimentación que la Fase 4 y la Fase 5 envían a la Fase 1, con lo cual la cadena causal preserva su trazabilidad gracias a la especificación detallada que el documento provee y la metodología Honeypot mantiene su coherencia metodológica a lo largo de las cinco fases.

### 4.2.4 Fase 2. Despliegue aislado

El despliegue aislado constituye el segundo componente operativo de la cadena causal de la metodología Honeypot, dado que coloca el señuelo en una red separada del entorno productivo para provocar al adversario sin exponer los sistemas reales. La separación garantiza que la captura de eventos del señuelo no contamine los sistemas de la administración tributaria y que el adversario no pueda usar el señuelo como pivote hacia los servicios productivos.

La norma ISO/IEC 27035-1:2023 establece que el despliegue controlado del señuelo es la base de la preservación de evidencia digital y esta Fase 2 traduce esa directriz al contexto de la administración tributaria. La traducción se concreta en la configuración de un entorno de red aislado y segmentado donde el señuelo opera bajo condiciones controladas que la organización supervisa.

Las brechas que justifican esta fase son las que el diagnóstico del primer objetivo específico identifica en la preservación y en las vulnerabilidades. Las brechas principales corresponden al Grupo 2 Instrumento 7 (preservación) y al Grupo 3 Instrumento 8 (vulnerabilidades), las cuales requieren un entorno de red aislado donde el señuelo opere sin comprometer la infraestructura productiva de la administración.

La Fase 3 envía retroalimentación a esta fase cuando la captura de eventos identifica configuraciones que conviene ajustar en el despliegue, con lo cual el aislamiento y la segmentación del señuelo se actualizan de manera continua a partir de la inteligencia operativa que la captura genera. Como condiciones previas, esta fase requiere un entorno de red separado del productivo, una topología de segmentación definida y la autorización del administrador de red para desplegar el señuelo dentro del entorno controlado, estas condiciones garantizan que el despliegue parte de una infraestructura formal reconocida por la organización.

*Figura 1 Vista integral de la Fase 2 dentro de la cadena causal de la metodología Honeypot*

![](data:image/png;base64...)

*Nota.* La Figura 1 muestra la vista integral de la Fase 2 con las tres razones que justifican la fase (brechas, normas, condiciones), las cinco actividades con su norma y la brecha que cierran y el entregable con el bucle que recibe. La metodología se diseñó en un entorno controlado y la ejecución operativa del despliegue corresponde al tercer objetivo específico.

**Actividades de la Fase 2**

1. **Aislar la red de producción del señuelo.** ISO/IEC 27002:2022 establece que las redes deben segregarse para reducir la superficie de ataque y el despliegue del señuelo requiere una red aislada que no tenga rutas directas hacia los sistemas productivos. La actividad aísla la red del señuelo mediante la creación de una VLAN separada, la configuración de reglas de firewall que bloquean el tráfico entre el entorno productivo y el señuelo y la desactivación de servicios de descubrimiento automático. La actividad cubre las categorías funcionales de aislamiento de red y configuración de firewall del eje operativo y se alinea con el control A.8.20 de ISO/IEC 27002:2022 sobre la segregación de redes, lo que garantiza que el señuelo opera en un entorno separado que la organización supervisa de forma continua.
2. **Segmentar la red del señuelo.** Una vez aislada la red, el señuelo necesita segmentación interna para que la administración del señuelo no quede expuesta al adversario que interactúa con el servicio tributario falso. La actividad segmenta la red del señuelo en tres zonas (zona de exposición para el servicio falso, zona de gestión para la administración y zona de captura para la instrumentación), y configura reglas que controlan el tráfico entre las zonas según el principio de mínimo privilegio. La actividad cubre las categorías funcionales de segmentación de red y zonas de seguridad del eje operativo y se alinea con el control A.8.22 de ISO/IEC 27002:2022 sobre la segmentación de redes, lo que garantiza que la administración del señuelo queda protegida incluso cuando el adversario compromete el servicio falso.
3. **Desplegar el señuelo en el entorno aislado.** Con la red aislada y segmentada, el señuelo se materializa siguiendo la especificación del documento de arquitectura que la Fase 1 produjo. La actividad despliega el señuelo en la zona de exposición, configura los servicios tributarios falsos según el contenido definido en la Fase 1, y establece los mecanismos de detección según los disparadores que esa misma fase documentó. La actividad cubre las categorías funcionales de despliegue de señuelo y configuración de servicios del eje operativo, la materialización del señuelo opera como insumo directo para la captura que la Fase 3 inicia. La Figura 2 ilustra la arquitectura de red resultante del despliegue, con la red productiva, la red aislada del señuelo y las tres zonas internas que la segmentación establece.

*Figura 2 Arquitectura de red aislada y segmentada para el despliegue del señuelo*

![](data:image/png;base64...)

*Nota.* La Figura 2 muestra la arquitectura de red resultante del despliegue aislado, con la red productiva separada físicamente de la red del señuelo y la red del señuelo dividida en tres zonas (exposición, gestión, captura) que la segmentación controla mediante reglas de firewall interno. La arquitectura garantiza que el adversario que interactúa con el servicio tributario falso no puede acceder a la administración del señuelo ni pivotar hacia los sistemas productivos de la administración tributaria.

1. **Verificar el aislamiento y la segmentación.** Antes de declarar operativo el despliegue, la organización debe comprobar que el aislamiento y la segmentación funcionan según la especificación, la actividad verifica el aislamiento mediante pruebas de penetración que intentan alcanzar la red productiva desde el señuelo, y verifica la segmentación mediante pruebas que intentan acceder a la zona de gestión desde la zona de exposición. La actividad cubre las categorías funcionales de pruebas de penetración y validación de controles del eje soporte y la verificación se documenta con la evidencia que la Fase 4 utiliza para correlacionar los eventos del señuelo con la gestión de incidentes.
2. **Documentar el despliegue.** El despliegue cerrado requiere un documento que registre la arquitectura de red resultante, las reglas de firewall configuradas, las pruebas de verificación realizadas y los procedimientos operativos para la administración del señuelo. La actividad documenta el despliegue con un informe que incluye el diagrama de red, la matriz de reglas, los resultados de las pruebas y los procedimientos de operación, lo que permite a la Fase 3 configurar la captura sobre una base documentada y a la organización auditar el despliegue en cualquier momento posterior. La actividad cubre la categoría funcional de documentación técnica del eje soporte, y la documentación opera como insumo directo para la auditoría y la mejora continua del señuelo.

**Cierre, transferencia y retroalimentación con la fase siguiente**

La Fase 2 cierra con un documento de despliegue aislado, que sirve como puente entre el diseño metodológico y la captura operativa de la cadena causal de la metodología Honeypot. El documento condensa las cinco actividades de la fase con sus respectivas justificaciones y articula el aislamiento, la segmentación, el despliegue del señuelo, la verificación y la documentación, de modo que la Fase 3 cuenta con un insumo completo para configurar la captura de eventos en el entorno donde el señuelo opera. El documento incorpora además la especificación del bucle de retroalimentación que la Fase 3 envía a la Fase 2, con lo cual la cadena causal preserva su trazabilidad gracias a la especificación detallada que el documento provee y la metodología Honeypot mantiene su coherencia metodológica a lo largo de las cinco fases.

### 4.2.5 Fase 3. Captura, enriquecimiento y custodia

La captura de eventos constituye el tercer componente operativo de la cadena causal de la metodología Honeypot, dado que registra las acciones del adversario en el señuelo sin cuyo registro la metodología no puede generar inteligencia operativa. El registro debe capturar las acciones del adversario con el detalle suficiente para que la correlación de la Fase 4 y la medición de la Fase 5 operen sobre datos válidos.

La norma ISO/IEC 27037:2012 establece que la identificación, la recolección y la preservación de la evidencia digital requieren procedimientos documentados que aseguren la integridad y la trazabilidad de los datos, de modo que esta Fase 3 implementa esos procedimientos en el contexto del señuelo. La implementación se concreta en la captura de los eventos del señuelo, el enriquecimiento con contexto, junto con la preservación de la cadena de custodia que mantiene la validez forense de los datos capturados.

Las brechas que justifican esta fase son las que el diagnóstico del primer objetivo específico identifica en la preservación y esta Fase 3 cierra directamente la brecha de preservación de evidencia digital que la metodología documenta como Grupo 2 Instrumento 7 (procedimientos de preservación de evidencia digital). Al ubicarse esta brecha en nivel básico de madurez, la fase requiere que la captura preserve la cadena de custodia desde el momento en que el evento se genera, lo que garantiza la validez forense de la evidencia que la Fase 4 y la Fase 5 consumen.

La Fase 2 entrega a esta fase el documento de despliegue que especifica la arquitectura de red, las reglas del firewall y los procedimientos operativos del señuelo, lo que permite configurar la captura de manera coherente con el aislamiento y la segmentación.

Como condiciones previas, esta fase requiere el documento de despliegue de la Fase 2, los sensores de captura instalados en las zonas de exposición, de captura y la configuración de los mecanismos de detección definidos en la Fase 1. Estas condiciones garantizan que la captura parte de la arquitectura aislada y segmentada que la Fase 2 verifica, de modo que los eventos capturados reflejan acciones del adversario sobre el señuelo y no ruido del entorno productivo.

Figura 1. Vista integral de la Fase 3 dentro de la cadena causal de la metodología Honeypot

![](data:image/png;base64...)

Nota. La Figura 1 muestra la vista integral de la Fase 3 con las tres razones que justifican la fase (brechas, normas, condiciones), las cinco actividades con su norma y la brecha que cierran, y el entregable con el bucle que recibe. La metodología se diseñó en un entorno controlado, y la ejecución operativa de la captura corresponde al tercer objetivo específico.

**Actividades de la Fase 3**

1. **Capturar los eventos del señuelo.** ISO/IEC 27035-1:2023 establece que la detección y el análisis de incidentes requieren la captura de eventos en tiempo real para alimentar el proceso de gestión de incidentes y la captura del señuelo es la fuente primaria de eventos que la metodología Honeypot procesa. La actividad captura los eventos del señuelo mediante sensores de red en la zona de exposición y la zona de captura, sensores de sistema operativo en el servicio tributario falso, junto con sensores de aplicación en los servicios web falsos, lo que genera un registro completo de las acciones del adversario. La actividad cubre las categorías funcionales de captura de eventos, registro de actividad del eje operativo y se alinea con el control A.8.16 de ISO/IEC 27002:2022 sobre las actividades de monitoreo, lo que garantiza que la metodología registra las acciones del adversario con la granularidad suficiente para la correlación. La Figura 2 ilustra el pipeline de captura, con los sensores en las zonas de red, el repositorio donde se almacenan los eventos y los mecanismos de preservación que la actividad de preservación activa.

*Figura 2. Pipeline de captura de eventos del señuelo*

![](data:image/png;base64...)

Nota. La Figura 2 muestra el pipeline de captura de eventos, con los sensores de red en la zona de exposición y la zona de captura, los sensores de sistema operativo en el servicio tributario falso, los sensores de aplicación en los servicios web falsos, y el repositorio de eventos firmados donde se almacenan los eventos con su firma criptográfica y su sello de tiempo. El pipeline garantiza que la captura registra las acciones del adversario con la granularidad necesaria para la correlación de la Fase 4 y la medición de la Fase 5.

1. **Enriquecer los eventos con contexto.** Una vez capturados, los eventos requieren enriquecimiento con contexto para que la correlación de la Fase 4 pueda identificar las técnicas del adversario y la severidad del incidente. La actividad enriquece los eventos con la geolocalización de la dirección IP, la clasificación de la técnica según MITRE ATT&CK, junto con la severidad estimada según el activo afectado y la referencia al incidente potencial en el sistema de gestión de incidentes. La actividad cubre las categorías funcionales de enriquecimiento de inteligencia, clasificación de amenazas del eje analítico y el enriquecimiento reduce el tiempo de análisis que la Fase 4 requiere, lo que mejora el tiempo medio de detección.
2. **Preservar la cadena de custodia.** La preservación de la cadena de custodia resulta esencial para que la evidencia mantenga su validez forense, ya que la correlación de la Fase 4 opera sobre la base de que los eventos no se alteran desde su captura. La actividad preserva la cadena de custodia mediante el registro inmutable del evento, la firma criptográfica que asegura la integridad, el sello de tiempo que certifica el momento de la captura, junto con la documentación del responsable de cada transferencia. La actividad cubre las categorías funcionales de preservación de evidencia y cadena de custodia del eje soporte y se alinea con la cláusula 5.5 de ISO/IEC 27037:2012 sobre la preservación de evidencia digital, lo que garantiza que los eventos mantienen su validez como evidencia.
3. **Validar la integridad de la evidencia.** Antes de entregar los eventos a la Fase 4, la organización debe verificar que la cadena de custodia permanece intacta y que la evidencia no se altera durante la captura y el enriquecimiento. La actividad valida la integridad de la evidencia mediante la verificación periódica de las firmas criptográficas, la auditoría del registro inmutable de eventos, junto con la prueba periódica del proceso de captura con eventos sintéticos, lo que garantiza que la metodología detecta cualquier intento de alteración de la evidencia. La actividad cubre las categorías funcionales de auditoría técnica y validación de integridad del eje soporte y la validación opera como control final antes de que la Fase 4 consuma los eventos, lo que reduce el riesgo de correlación sobre evidencia comprometida.
4. **Documentar la captura.** La captura cerrada requiere un documento que registre los eventos capturados, los enriquecimientos aplicados, las acciones de preservación realizadas, junto con los resultados de las validaciones de integridad, lo que permite a la Fase 4 consumir los eventos sobre una base documentada. La actividad documenta la captura con un informe que incluye el repositorio de eventos firmados, el registro de la cadena de custodia, los resultados de las auditorías periódicas, junto con las estadísticas de captura por periodo, lo que permite a la Fase 5 medir el impacto de la metodología con datos cuantitativos, la actividad cubre la categoría funcional de documentación técnica del eje soporte y la documentación opera como insumo directo para la correlación de la Fase 4 y la medición de la Fase 5.

**Cierre, transferencia y retroalimentación con la fase siguiente**

La Fase 3 cierra con un documento de captura enriquecida, que sirve como puente entre la captura operativa del señuelo y la correlación con la gestión de incidentes dentro de la cadena causal de la metodología Honeypot. El documento condensa las cinco actividades de la fase con sus respectivas justificaciones y articula la captura, el enriquecimiento, la preservación, la validación y la documentación, de modo que la Fase 4 cuenta con un insumo completo para correlacionar los eventos del señuelo con los incidentes que la administración tributaria registra. El documento incorpora además la especificación del bucle de retroalimentación que la Fase 4 envía a la Fase 3, con lo cual la cadena causal preserva su trazabilidad a partir del detalle del documento, y la metodología Honeypot mantiene su coherencia metodológica a lo largo de las cinco fases.

### 4.2.6 Fase 4. Correlación con gestión de incidentes

La correlación con la gestión de incidentes constituye el cuarto componente operativo de la cadena causal de la metodología Honeypot, dado que vincula los eventos capturados del señuelo con el sistema institucional de gestión de incidentes para que la organización active su respuesta. La vinculación debe ocurrir con la velocidad y la precisión suficientes para que la respuesta a incidentes se desencadene antes de que el adversario complete su objetivo sobre los servicios productivos.

La norma ISO/IEC 27035-1:2023 establece que la gestión de incidentes requiere un proceso formal de evaluación y respuesta que active los controles institucionales cuando los indicadores de compromiso se confirman y esta Fase 4 implementa ese proceso en el contexto del señuelo. La implementación se concreta en la correlación de los eventos del señuelo con el sistema de gestión de incidentes, la clasificación de los incidentes resultantes, junto con la activación de la respuesta institucional correspondiente.

Las brechas que justifican esta fase son las que el diagnóstico del primer objetivo específico identifica en el monitoreo y la respuesta a incidentes, esta Fase 4 cierra directamente la brecha que la metodología documenta como Grupo 1 Instrumento 4 (actividades de monitoreo). Al ubicarse esta brecha en nivel básico, la fase requiere que la correlación vincule los eventos del señuelo con el sistema de gestión de incidentes desde el momento en que el indicador de compromiso se confirma, lo que garantiza que la respuesta institucional se active dentro de los plazos que la metodología define.

La Fase 3 entrega a esta fase el documento de captura enriquecida que contiene los eventos firmados, el enriquecimiento de inteligencia y la cadena de custodia que la metodología aplica, lo que permite correlacionar con base en evidencia forense válida. La Fase 5 recibe los incidentes correlacionados para medir el impacto de la metodología y la Fase 1 recibe los patrones de ataque identificados para actualizar el señuelo, de modo que la correlación opera como insumo directo de la actualización del señuelo y de la medición del impacto.

Como condiciones previas, esta fase requiere el documento de captura enriquecida de la Fase 3, el sistema de gestión de incidentes institucional configurado para recibir eventos del señuelo y los responsables de respuesta asignados por la organización. Estas condiciones garantizan que la correlación opera sobre un sistema institucional listo y con responsables identificados, de modo que la respuesta se active sin necesidad de preparativos adicionales.

*Figura 1. Vista integral de la Fase 4 dentro de la cadena causal de la metodología Honeypot*

![](data:image/png;base64...)

*Nota.* La Figura 1 muestra la vista integral de la Fase 4 con las tres razones que justifican la fase (brechas, normas, condiciones), las cinco actividades con su norma y la brecha que cierran y el entregable con los dos bucles que la fase envía a la Fase 1 y a la Fase 3. La metodología se diseñó en un entorno controlado y la ejecución operativa de la correlación corresponde al tercer objetivo específico.

**Actividades de la Fase 4**

1. **Vincular los eventos con el sistema de gestión de incidentes.** ISO/IEC 27035-1:2023 establece que la evaluación de incidentes requiere un proceso formal de correlación que vincule los indicadores de compromiso con los eventos del sistema de monitoreo y la correlación del señuelo implementa ese proceso sobre los eventos capturados por la metodología Honeypot. La actividad vincula los eventos del señuelo con los incidentes potenciales del sistema de gestión mediante la comparación de los indicadores de compromiso del señuelo con los indicadores registrados en el sistema institucional, lo que genera una lista priorizada de incidentes que la organización debe atender. La actividad cubre las categorías funcionales de correlación de eventos e integración con gestión de incidentes del eje analítico y se alinea con la cláusula 6.4 de ISO/IEC 27035-1:2023 sobre el análisis de incidentes, lo que garantiza que la metodología conecta el señuelo con la respuesta institucional. La Figura 2 ilustra el flujo de correlación, con los eventos del señuelo entrando al Sistema de Gestión de Seguridad de la Información (SGSI) de la organización, el repositorio institucional de incidentes y los módulos de correlación, clasificación y notificación que las actividades siguientes operan.

*Figura 2. Flujo de correlación entre el señuelo y el sistema de gestión de incidentes*

![](data:image/png;base64...)

*Nota.* La Figura 2 muestra el flujo de correlación entre el señuelo y el sistema institucional, con los eventos del señuelo entrando al Sistema de Gestión de Seguridad de la Información (SGSI) de la organización, donde el módulo de vinculación los asocia con los incidentes potenciales, el módulo de clasificación los agrupa por tipo y severidad, el módulo de notificación los comunica a los responsables de respuesta, que corresponden al CSIRT (equipo de respuesta a incidentes), al área de TI (operaciones tecnológicas), y al área Legal (asesoría normativa). El flujo garantiza que la metodología opera sobre el sistema institucional sin duplicar infraestructura.

1. **Clasificar los incidentes según tipo y severidad.** NIST SP 800-61 Rev. 3 establece que la categorización de incidentes requiere funciones definidas para agrupar los eventos por tipo y severidad, la clasificación de los incidentes del señuelo implementa esa categorización sobre los eventos correlacionados, lo que facilita la respuesta de la organización. La actividad clasifica los incidentes según el tipo de ataque (malware, intrusión, exfiltración, denegación de servicio), junto con la severidad estimada según el activo afectado y la urgencia de respuesta según el potencial de propagación, de modo que los incidentes se asignan a los responsables designados dentro de los plazos que la metodología define. La actividad cubre las categorías funcionales de clasificación de incidentes y evaluación de severidad del eje analítico y la clasificación opera como filtro para la notificación, lo que reduce el ruido que los responsables de respuesta deben atender.
2. **Notificar a los responsables de respuesta.** Una vez clasificados los incidentes, la actividad notifica a los responsables de respuesta según la severidad asignada por la metodología, lo que activa la respuesta institucional dentro de los plazos definidos. La notificación opera mediante los canales formales que el sistema de gestión de incidentes configura, lo que garantiza que las acciones de contención se inicien sin demoras atribuibles a la falta de comunicación. La actividad cubre las categorías funcionales de notificación de incidentes y activación de respuesta del eje soporte y la notificación opera como puente entre la detección y la contención, lo que reduce el tiempo medio de respuesta que la organización necesita para mitigar el incidente.
3. **Priorizar los incidentes según impacto.** La priorización opera como guía para que la respuesta se enfoque en los incidentes de mayor impacto sobre los servicios de la administración tributaria. La actividad prioriza los incidentes según el impacto potencial en la confidencialidad, integridad y disponibilidad de los servicios, junto con la probabilidad de propagación y la criticidad del activo afectado, lo que genera un orden de atención que la organización puede ejecutar de forma secuencial. La actividad cubre las categorías funcionales de priorización de incidentes y análisis de impacto del eje soporte y la priorización opera como guía para la asignación de recursos, lo que reduce el desperdicio de capacidad de respuesta en incidentes de bajo impacto.
4. **Documentar la correlación.** La correlación cerrada requiere un documento que registre los eventos correlacionados, las clasificaciones asignadas, las notificaciones realizadas, junto con las priorizaciones resultantes, lo que permite a la Fase 5 medir el impacto de la metodología con datos cuantitativos. La actividad documenta la correlación con un informe que incluye el repositorio de incidentes correlacionados, el registro de clasificaciones y notificaciones, junto con las estadísticas de correlación por periodo y los indicadores de tiempo medio de detección y tiempo medio de respuesta que la organización registra. La actividad cubre la categoría funcional de documentación técnica del eje soporte y la documentación opera como insumo directo para la medición de la Fase 5 y la auditoría organizacional.

**Cierre, transferencia y retroalimentación con la fase siguiente**

La Fase 4 cierra con un documento de correlación de incidentes, que sirve como puente entre la captura del señuelo y la respuesta institucional dentro de la cadena causal de la metodología Honeypot. El documento condensa las cinco actividades de la fase con sus respectivas justificaciones y articula la vinculación, la clasificación, la notificación, junto con la priorización y la documentación, de modo que la Fase 5 cuenta con un insumo completo para medir el impacto de la metodología con datos cuantitativos. El documento incorpora además la especificación de los bucles de retroalimentación que la Fase 4 envía a la Fase 1 y a la Fase 3, con lo cual la cadena causal preserva su trazabilidad a partir del detalle del documento y la metodología Honeypot mantiene su coherencia metodológica a lo largo de las cinco fases.

### 4.2.7 Fase 5. Medición de impacto y lecciones aprendidas

La medición de impacto y las lecciones aprendidas constituyen el quinto y último componente operativo de la cadena causal de la metodología Honeypot, dado que cuantifican la efectividad de las cinco fases y generan aprendizaje organizacional para ciclos futuros. La cuantificación debe sustentarse en indicadores comparables entre el estado inicial y el estado posterior, de modo que la organización cuente con evidencia objetiva sobre el valor que la metodología aporta a la gestión de incidentes.

La norma ISO/IEC 27035-1:2023 establece que la fase de lecciones aprendidas debe identificar las causas raíz, documentar las mejoras identificadas y formalizar los cambios procedimentales que la organización adopta y esta Fase 5 implementa esa disposición formal sobre los datos generados por la metodología Honeypot. La implementación se concreta en la medición del impacto de la metodología, la comparación entre el estado inicial y el estado posterior, junto con la difusión de las lecciones aprendidas a la organización.

Las brechas que justifican esta fase son las que el diagnóstico del primer objetivo específico identifica en la capacitación y la mejora continua y esta Fase 5 cierra directamente la brecha que la metodología documenta como Grupo 4 Instrumento 13 (capacitación en gestión de incidentes). Al ubicarse esta brecha en nivel básico, la fase requiere que la medición documente no solo el impacto cuantitativo de la metodología, sino también el aprendizaje cualitativo que la organización requiere para sostener la gestión de incidentes en el tiempo, lo que garantiza que las lecciones aprendidas se traduzcan en cambios operativos verificables.

La Fase 4 entrega a esta fase el documento de correlación de incidentes que contiene los incidentes correlacionados, las clasificaciones asignadas y los indicadores de tiempo medio de detección y respuesta que la metodología mide. La Fase 1 recibe los patrones de ataque y las tendencias de impacto identificados en la medición, junto con las recomendaciones de actualización del señuelo que la fase genera, de modo que la medición opera como insumo directo de la actualización del señuelo y de la sostenibilidad de la cadena causal.

Como condiciones previas, esta fase requiere el documento de correlación de la Fase 4 con al menos un ciclo de medición completo, los indicadores cuantitativos que la organización define para la gestión de incidentes y los responsables de la mejora continua que la metodología asigna. Estas condiciones garantizan que la medición opera sobre datos consolidados del ciclo completo y sobre responsables identificados para la implementación de las mejoras, de modo que las lecciones aprendidas se traduzcan en acciones verificables dentro de los plazos que la organización define.

*Figura 1. Vista integral de la Fase 5 dentro de la cadena causal de la metodología Honeypot*

![](data:image/png;base64...)

*Nota.* La Figura 1 muestra la vista integral de la Fase 5 con las tres razones que justifican la fase (brechas, normas, condiciones), las cinco actividades con su norma y la brecha que cierran y el entregable con el bucle que la fase envía a la Fase 1. La metodología se diseñó en un entorno controlado y la ejecución operativa de la medición corresponde al cuarto objetivo específico.

**Actividades de la Fase 5**

1. **Medir el impacto con indicadores cuantitativos.** ISO/IEC 27004:2016 establece que la medición de la efectividad de un sistema de gestión de seguridad requiere indicadores cuantitativos que permitan comparar el estado inicial con el estado posterior a la implementación y la medición de la metodología Honeypot implementa ese marco sobre los datos generados por las cuatro fases previas. La actividad mide el impacto de la metodología mediante la construcción de indicadores cuantitativos (número de eventos capturados, número de incidentes correlacionados, número de respuestas activadas, tiempo medio de detección, tiempo medio de respuesta), lo que genera un cuadro de mando que la organización puede consultar para conocer el valor que la metodología aporta. La actividad cubre las categorías funcionales de medición de impacto y construcción de indicadores del eje analítico y la medición opera como insumo directo para la comparación que la actividad siguiente realiza, lo que permite a la organización contar con evidencia objetiva sobre la efectividad de la metodología. La Figura 2 ilustra el ciclo de medición, con los datos de la Fase 4 entrando al módulo de medición, comparación y evaluación operando sobre los datos cuantitativos, la documentación y difusión cerrando el ciclo con las lecciones aprendidas.

*Figura 2. Ciclo de medición de impacto y lecciones aprendidas*

![](data:image/png;base64...)

*Nota.* La Figura 2 muestra el ciclo de medición de impacto, con el documento de correlación de la Fase 4 entrando al módulo de medición, que construye el cuadro de mando con los indicadores MTTD (tiempo medio de detección) y MTTR (tiempo medio de respuesta); el módulo de comparación aplica una prueba de hipótesis pareada entre el estado inicial y el estado posterior; el módulo de evaluación analiza la sostenibilidad institucional; el módulo de documentación cataloga las lecciones con responsables y plazos; y el módulo de difusión lleva el informe a la alta dirección y a los equipos de respuesta, con un bucle de retroalimentación a la Fase 1 que rediseña el señuelo con los patrones identificados.

1. **Comparar el estado inicial con el estado posterior.** NIST SP 800-61 Rev. 3 establece que la fase de lecciones aprendidas requiere comparar el estado anterior al incidente con el estado posterior, de modo que la organización identifique las mejoras concretas que la gestión de incidentes aporta y la comparación de la metodología Honeypot implementa ese procedimiento sobre el conjunto del ciclo del honeypot. La actividad compara el estado inicial del diagnóstico del primer objetivo específico con el estado posterior de la medición, mediante la aplicación de una prueba de hipótesis pareada que determine si las mejoras observadas en la gestión de incidentes son estadísticamente significativas, lo que permite a la organización sustentar la continuidad de la metodología con evidencia cuantitativa. La actividad cubre las categorías funcionales de comparación de estados y prueba de hipótesis del eje analítico y la comparación opera como filtro objetivo sobre la medición, lo que reduce el riesgo de que la organización mantenga la metodología por inercia y no por evidencia.
2. **Evaluar la sostenibilidad institucional.** Una vez medida y comparada la efectividad, la actividad evalúa la sostenibilidad de la metodología en el contexto institucional, dado que una metodología efectiva pero insostenible pierde su valor con el tiempo. La actividad evalúa la sostenibilidad mediante el análisis de los recursos consumidos por cada fase, la disponibilidad de los responsables designados y la madurez institucional para mantener la operación sin intervención externa, junto con la identificación de los riesgos que podrían comprometer la continuidad, de modo que la organización cuente con un diagnóstico de la viabilidad de la metodología a mediano plazo. La actividad cubre las categorías funcionales de evaluación de sostenibilidad y análisis de riesgos del eje soporte y la evaluación opera como base para las recomendaciones que la actividad siguiente formula, lo que garantiza que las lecciones aprendidas incluyen tanto los logros como los riesgos identificados.
3. **Documentar las lecciones aprendidas.** La evaluación cerrada requiere un documento que registre los indicadores medidos, la comparación entre estados, la evaluación de sostenibilidad, junto con las lecciones aprendidas específicas que la organización debe implementar, lo que permite a la auditoría y a la mejora continua operar sobre una base documentada. La actividad documenta las lecciones aprendidas con un informe que incluye el cuadro de mando de la medición, junto con la tabla comparativa del estado inicial y el estado posterior, la evaluación de sostenibilidad, el catálogo de lecciones aprendidas con sus responsables y plazos y las recomendaciones específicas que la fase formula. La actividad cubre la categoría funcional de documentación técnica del eje soporte y la documentación opera como insumo directo para la difusión que la actividad siguiente realiza y para la actualización de la Fase 1 que la cadena causal requiere.
4. **Difundir las lecciones aprendidas.** La documentación de lecciones aprendidas requiere difusión activa a la organización para que el conocimiento generado no quede en el documento, sino que se traduzca en práctica institucional, dado que la documentación sin difusión no genera cambio. La actividad difunde las lecciones aprendidas mediante la presentación del informe a la alta dirección, los talleres de socialización con los equipos de respuesta, junto con la incorporación de las recomendaciones en los planes de capacitación institucional y la publicación de los indicadores en los reportes de gestión de la seguridad de la información, de modo que toda la organización conozca el valor que la metodología Honeypot aporta y los compromisos que la mejora continua implica. La actividad cubre las categorías funcionales de difusión del conocimiento y capacitación del eje soporte y la difusión opera como cierre del ciclo de aprendizaje que la metodología Honeypot establece, lo que garantiza que el conocimiento generado se mantiene vivo en la institución y se incorpora a la cultura organizacional.

**Cierre, transferencia y retroalimentación con la fase siguiente**

La Fase 5 cierra con un documento de lecciones aprendidas, que sirve como puente entre la medición de impacto y la actualización del señuelo dentro de la cadena causal de la metodología Honeypot. El documento condensa las cinco actividades de la fase con sus respectivas justificaciones y articula la medición, la comparación, la evaluación, junto con la documentación y la difusión, de modo que la cadena causal se retroalimenta con evidencia objetiva sobre la efectividad de la metodología. El documento incorpora además la especificación del bucle de retroalimentación que la Fase 5 envía a la Fase 1, con lo cual la cadena causal preserva su trazabilidad a partir del detalle del documento y la metodología Honeypot mantiene su coherencia metodológica a lo largo de las cinco fases.

### 2.8 Síntesis del diseño de la metodología Honeypot

El diseño de la metodología Honeypot articula los principios y decisiones establecidos a partir del diagnóstico con las cinco fases que conforman su estructura operativa, la secuencia comprende el diseño del señuelo, su despliegue en un entorno aislado, la captura y custodia de los eventos, su correlación con la gestión institucional de incidentes y la medición de los resultados obtenidos. Esta estructura mantiene la correspondencia entre las brechas identificadas, los referentes normativos y los indicadores definidos para la evaluación. Asimismo, los bucles de retroalimentación permiten ajustar progresivamente el diseño del señuelo, su configuración y las acciones de mejora a partir de los resultados obtenidos durante la operación.

**Figura N**

*Síntesis del diseño de la metodología Honeypot para la gestión de incidentes en servicios fiscales*

![](data:image/jpeg;base64...)

*Nota.* La figura sintetiza el diseño de la metodología desarrollado en la sección 4.2, cuya lectura parte de los cinco principios de fundamentación y los tres planos transversales, continúa con las brechas del diagnóstico y las cinco fases operativas, además de sus actividades y entregables y culmina con las métricas de evaluación. Los arcos superiores representan los bucles F3→F2, F4→F1 y F5→F1, correspondientes a los horizontes táctico, operacional y estratégico. P1–P5 = principios de diseño; D1–D4 = decisiones de diseño; G1–G4 = grupos de brechas del diagnóstico; Inst. = instrumento; F1–F5 = fases de la metodología; OE1 y OE3 = objetivos específicos primero y tercero; SGSI = sistema de gestión de seguridad de la información; IRP = plan de respuesta a incidentes; SIEM = gestión de información y eventos de seguridad; SOAR = orquestación, automatización y respuesta de seguridad; SHA-256 = algoritmo de hash seguro de 256 bits; NTP = protocolo de tiempo de red; WORM = almacenamiento de escritura única y lectura múltiple; ATT&CK = base de conocimiento de tácticas y técnicas adversarias de MITRE; MTTD = tiempo medio de detección; MTTR = tiempo medio de respuesta; IMGI = índice de madurez en gestión de incidentes; IIAM = índice de impacto del aprendizaje y la mejora. Fuente: elaboración propia.

## 4.3 Implementación de la metodología de honeypot para la gestión de incidentes

La implementación del prototipo materializa la metodología propuesta para la gestión de incidentes mediante honeypots en servicios fiscales, a partir de los elementos definidos en el diseño metodológico. En esta etapa se configura un entorno controlado que permite poner en práctica los componentes establecidos en la metodología, observar su funcionamiento y generar evidencias que respalden su implementación.

El desarrollo de esta etapa mantiene correspondencia con los elementos definidos en el apartado 4.2. Por esta razón, la implementación no constituye una selección independiente de tecnologías, sino la materialización técnica del diseño previamente establecido. Las funciones del prototipo se organizan de acuerdo con las cinco fases de la metodología y con las categorías funcionales que permiten ejecutar cada una de ellas, desde el diseño del señuelo hasta la medición del impacto y la generación de lecciones aprendidas.

La metodología establece catorce categorías funcionales distribuidas entre las cinco fases, de acuerdo con las funciones que requiere cada etapa, estas categorías comprenden la identificación del activo, la configuración del señuelo, la definición del perfil del atacante, el aislamiento de red, la preparación del entorno controlado, la captura y enriquecimiento de eventos, la custodia de la evidencia, la normalización, la correlación con tickets, el mapeo con MITRE ATT&CK, el cálculo del tiempo medio de detección (MTTD), el cálculo del índice de impacto del aprendizaje y la mejora (IIAM) y el reporte de lecciones aprendidas.

### 4.3.1 Propósito, alcance y línea base

El propósito de esta etapa consiste en materializar la metodología propuesta dentro de un entorno controlado, de manera que sus componentes puedan ser implementados, observados y verificados de acuerdo con las funciones definidas durante el diseño. Esta implementación se orienta al cumplimiento del tercer objetivo específico (OE3) de la investigación, relacionado con la implementación de la metodología de honeypot en un entorno controlado para su aplicación en la gestión de incidentes.

El alcance comprende las cinco fases establecidas en la metodología, estas corresponden al diseño del señuelo, el despliegue aislado, la captura, enriquecimiento y custodia de los eventos, la correlación con la gestión de incidentes y la medición del impacto junto con la generación de lecciones aprendidas. La estructura mantiene la secuencia definida en el diseño metodológico y permite que las funciones de cada fase se relacionen con las siguientes etapas del proceso.

La línea base utilizada en esta implementación corresponde a la estructura metodológica definida en el apartado 4.2. esta estructura establece tres planos transversales de trazabilidad y catorce categorías funcionales que permiten relacionar las decisiones metodológicas con su respaldo normativo, institucional u operativo. El plano normativo considera, entre otros referentes, ISO/IEC 27035-1:2023, NIST SP 800-61 Rev. 3, MITRE ATT&CK e ISO/IEC 27037:2012; el plano institucional se relaciona con los controles de ISO/IEC 27001:2022, mientras que el plano operativo incorpora las métricas utilizadas para evaluar el funcionamiento del proceso.

Las catorce categorías funcionales constituyen la referencia para organizar la implementación del prototipo, su distribución comprende tres categorías para la primera fase, dos para la segunda, tres para la tercera, tres para la cuarta y tres para la quinta, conformando las catorce funciones que requiere la ejecución completa de la metodología. Esta organización permite relacionar cada función con el componente tecnológico que la materializa, sin confundir la tecnología concreta utilizada en el prototipo con la metodología propuesta.

Entre las funciones previstas se encuentran la identificación del activo, la configuración del señuelo, el perfil del atacante, el aislamiento de red, el entorno controlado, la captura de eventos, el enriquecimiento, la custodia de evidencia, la normalización, la correlación con tickets, el mapeo con MITRE ATT&CK, el cálculo del tiempo medio de detección (MTTD), el cálculo del índice de impacto del aprendizaje y la mejora (IIAM) y el reporte de lecciones aprendidas. Estas funciones constituyen los elementos que deben ser verificados durante la implementación antes de ser considerados como materializados.

La trazabilidad constituye el criterio utilizado para relacionar cada elemento definido en el diseño con su correspondiente implementación y evidencia, bajo este criterio cada fase debe mantener su vínculo con la brecha diagnosticada, la norma internacional que respalda su ejecución y el indicador utilizado para su medición. Esta relación permite verificar que la implementación mantiene correspondencia con el diseño metodológico y evita incorporar como resultado elementos que no cuentan con respaldo suficiente.

### 4.3.2 Entorno controlado de implementación

La implementación se desarrolla en un entorno experimental denominado *TaxFisco Research Lab*, utilizado como espacio controlado para materializar el prototipo de la metodología Honeypot. En este entorno se integran los componentes necesarios para representar servicios señuelo, observar las interacciones generadas, registrar los eventos y proporcionar capacidades de análisis y gestión de incidentes. La denominación utilizada en la infraestructura permite identificar de manera conjunta los recursos que forman parte del laboratorio de investigación.

El entorno se construye mediante contenedores que permiten organizar los diferentes componentes del prototipo como servicios independientes. Esta organización facilita la separación de las funciones que intervienen en la metodología y permite establecer diferentes segmentos de comunicación según el propósito de cada componente. La descripción detallada de los servicios tecnológicos que conforman esta infraestructura se presenta posteriormente en el apartado 4.3.3.

A nivel de red, el entorno se organiza mediante cuatro segmentos virtuales denominados *taxfisco-dmz*, *taxfisco-honeypot*, *taxfisco-ids* y *taxfisco-soc*. Cada segmento dispone de un rango de direcciones independiente y agrupa componentes de acuerdo con su función dentro del prototipo. Esta distribución constituye la base sobre la cual se implementan las funciones de interacción con los señuelos, observación del tráfico y gestión de la información generada.

Para verificar esta estructura se ejecuta un comando que inspecciona cada una de las redes definidas en el entorno, el comando obtiene para cada segmento el rango de red, la puerta de enlace y los contenedores conectados, junto con la dirección del protocolo de Internet (IP) asignada a cada uno. El resultado permite observar la distribución de los componentes y establecer la estructura de comunicación utilizada por el prototipo.

Figura X

*Arquitectura de redes del entorno controlado de implementación*

![](data:image/png;base64...)

*Nota.* La figura presenta el resultado de la inspección de las cuatro redes virtuales que conforman el entorno experimental, el comando recorre *taxfisco-dmz*, *taxfisco-honeypot*, *taxfisco-ids* y *taxfisco-soc* y muestra para cada red el segmento asignado, la puerta de enlace, los contenedores conectados y sus respectivas direcciones IP. La salida identifica el segmento *10.20.0.0/24* para *taxfisco-dmz*, *10.21.0.0/24* para *taxfisco-honeypot*, *10.23.0.0/24* para *taxfisco-ids* y *10.22.0.0/24* para *taxfisco-soc*. Fuente: elaboración propia con base en la inspección del entorno de implementación.

Como se observa en la Figura X, el laboratorio presenta una organización diferenciada de sus componentes mediante cuatro segmentos de red. *taxfisco-dmz* concentra servicios relacionados con la zona de servicios señuelo, *taxfisco-honeypot* agrupa componentes destinados a la interacción con los señuelos, *taxfisco-ids* concentra los servicios de observación del tráfico y *taxfisco-soc* reúne los componentes destinados al procesamiento y gestión de la información.

La distribución de las redes permite organizar los componentes del laboratorio de acuerdo con las funciones que cumplen dentro del prototipo, la red *taxfisco-ids* concentra Suricata y Zeek para las funciones relacionadas con la observación del tráfico, mientras que *taxfisco-soc* reúne herramientas como Wazuh, TheHive, Cortex, MISP, Shuffle y Grafana para el procesamiento, análisis, gestión y visualización de la información generada. La descripción de cada componente, su función dentro del prototipo y su relación con las categorías funcionales definidas en la metodología se presenta en el apartado 4.3.3.

### 4.3.3 Plataforma tecnológica del prototipo

La plataforma tecnológica constituye la materialización concreta de las categorías funcionales definidas en la metodología propuesta, su implementación utiliza servicios desplegados mediante contenedores, organizados de acuerdo con las funciones requeridas por el entorno experimental. La plataforma integra componentes destinados al funcionamiento de los señuelos, captura de eventos, análisis de información, gestión de incidentes, almacenamiento y visualización.

La configuración del prototipo se organiza mediante Docker Compose, que permite definir los servicios que forman parte del laboratorio, la consulta de la configuración identifica veinticinco servicios, entre los que se encuentran decoy.api, decoy.portal, Cowrie, Heralding, OpenCanary, Suricata, Zeek, Wazuh, MISP, TheHive, Cortex, Shuffle, Velociraptor y Grafana, además de los servicios de soporte requeridos por estos componentes.

Figura X

*Servicios definidos para el prototipo mediante Docker Compose*

![](data:image/png;base64...)

*Nota.* La figura presenta el resultado de la consulta docker compose config --services, acompañada de una numeración consecutiva que facilita identificar la cantidad de servicios definidos en la configuración, la evidencia permite verificar la composición declarada del prototipo antes de analizar el estado de ejecución de sus componentes.

La distribución de estos servicios responde a las funciones que requiere la metodología, los componentes señuelo permiten representar servicios fiscales dentro del entorno experimental, mientras que las herramientas de monitoreo, análisis, gestión de incidentes y visualización proporcionan capacidades complementarias para el tratamiento de la información generada durante la interacción con el laboratorio. Esta organización permite que la plataforma tecnológica materialice las funciones definidas en las cinco fases de la metodología.

La implementación utiliza diferentes imágenes Docker para proporcionar los servicios que integran el prototipo, entre ellas se identifican imágenes correspondientes a los señuelos desarrollados para el laboratorio, herramientas de detección como Suricata y Zeek, plataformas de monitoreo como Wazuh, herramientas de gestión como TheHive, Cortex y MISP, además de componentes de soporte como PostgreSQL, Redis y Cassandra.

Figura X

*Imágenes Docker utilizadas en el prototipo*

![](data:image/png;base64...)

*Nota.* La figura presenta las imágenes Docker utilizadas por los servicios del prototipo, junto con las etiquetas disponibles y el tamaño registrado para cada imagen, la consulta permite identificar los componentes tecnológicos empleados para desplegar el entorno experimental. Entre las imágenes se encuentran taxfisco/decoy-api, taxfisco/decoy-portal, Wazuh, Suricata, Zeek, Cowrie, Heralding, OpenCanary, TheHive, Cortex, MISP, Shuffle, Velociraptor y Grafana.

La plataforma también incorpora mecanismos de almacenamiento persistente para conservar información generada por los diferentes servicios, la configuración de Docker Compose define volúmenes asociados con componentes como Wazuh, MISP, TheHive, Cassandra, Cortex, Shuffle, Velociraptor, Grafana, Cowrie, OpenCanary, Heralding, los servicios señuelo, PostgreSQL, Suricata y Zeek.

Figura X

*Volúmenes persistentes asociados a los servicios del prototipo*

![](data:image/png;base64...)

*Nota.* La figura presenta los volúmenes Docker utilizados por los servicios del prototipo junto con el controlador de almacenamiento registrado, se identifican volúmenes destinados a conservar datos y registros de componentes como Wazuh, MISP, TheHive, Cortex, Shuffle, Velociraptor, Grafana, Cowrie, OpenCanary, Heralding, los servicios señuelo, Suricata y Zeek. La evidencia permite verificar la existencia de almacenamiento persistente dentro del entorno.

Como se observa en la Figura X, el prototipo mantiene mecanismos de almacenamiento asociados con los diferentes componentes de la plataforma, esta organización permite separar los datos generados por los servicios según su función. El uso específico de cada mecanismo de almacenamiento se verifica posteriormente en las fases relacionadas con la captura, enriquecimiento y custodia de la información.

La plataforma tecnológica se relaciona con las catorce categorías funcionales establecidas en la metodología, estas categorías permiten organizar las funciones que debe cumplir el prototipo sin vincular la metodología a una tecnología específica. Por esta razón, los componentes utilizados en esta implementación representan una materialización concreta de las funciones definidas en el diseño metodológico.

**Tabla X**

*Correspondencia entre las categorías funcionales y los componentes tecnológicos del prototipo*

|  |  |  |
| --- | --- | --- |
| **Fase** | **Categoría funcional** | **Componente utilizado en el prototipo** |
| F1 | Identificación de activo | decoy.portal y decoy.api |
| F1 | Configuración del señuelo | decoy.portal y decoy.api |
| F1 | Perfil del atacante | Cowrie, Heralding y OpenCanary |
| F2 | Aislamiento de red | Redes virtuales Docker |
| F2 | Entorno controlado | Docker Compose y contenedores |
| F3 | Captura de eventos | Wazuh, Suricata, Zeek, Cowrie, Heralding y OpenCanary |
| F3 | Enriquecimiento | MISP, Cortex y Wazuh |
| F3 | Custodia de evidencia | Volúmenes persistentes y registros |
| F4 | Normalización | Wazuh |
| F4 | Correlación con tickets | TheHive |
| F4 | Mapeo con MITRE ATT&CK | MISP, Wazuh y TheHive |
| F5 | Cálculo del tiempo medio de detección (MTTD) | Registros de eventos y gestión de incidentes |
| F5 | Cálculo del índice de impacto del aprendizaje y la mejora (IIAM) | Registros de implementación y resultados de evaluación |
| F5 | Reporte de lecciones aprendidas | TheHive, Grafana y documentación |

*Nota.* La tabla relaciona las categorías funcionales definidas en la metodología con los componentes tecnológicos utilizados para su materialización en el prototipo, la asignación representa la implementación concreta del entorno experimental y no modifica el carácter transferible de la metodología. La verificación de cada función se desarrolla en los apartados correspondientes a las fases de implementación.

La distribución de los componentes permite organizar la plataforma de acuerdo con las funciones requeridas por las cinco fases de la metodología, los servicios señuelo constituyen el punto de interacción del entorno, mientras que los componentes de detección, análisis, gestión de incidentes, almacenamiento y visualización intervienen en las etapas posteriores del proceso. Esta organización mantiene la separación entre la metodología propuesta y las tecnologías utilizadas para materializarla.

La evidencia presentada en este apartado permite establecer la composición tecnológica del prototipo a partir de los servicios definidos, las imágenes utilizadas y los mecanismos de almacenamiento persistente, la comprobación específica del funcionamiento de cada categoría funcional se realiza en las fases siguientes, donde cada componente se analiza de acuerdo con la función que desempeña dentro del proceso metodológico.

### 4.3.4 Matriz de trabajo y criterios de verificación

La implementación de la metodología requiere una forma ordenada de comprobar que las funciones definidas en el diseño se encuentran materializadas en el entorno experimental, para este propósito se establece una matriz de trabajo que relaciona cada fase con las funciones que deben comprobarse, el elemento que debe ser observado y la evidencia necesaria para respaldar su estado de implementación.

La matriz permite organizar previamente el proceso de verificación y establecer qué evidencia se requiere para cada función de esta manera, la existencia de un componente tecnológico no se considera suficiente para afirmar que una función se encuentra implementada. La comprobación requiere relacionar el componente con la función que desempeña dentro de la metodología y con la evidencia que permite respaldar dicha relación.

Tabla X

*Matriz de trabajo para la verificación de la implementación*

|  |  |  |  |
| --- | --- | --- | --- |
| **Fase** | **Función que se verifica** | **Elemento que se comprueba** | **Evidencia requerida** |
| F1 | Identificación del activo | Identificación de los servicios que conforman el señuelo | Configuración y descripción de los servicios señuelo |
| F1 | Configuración del señuelo | Configuración de decoy.portal y decoy.api | Capturas de configuración o funcionamiento |
| F1 | Perfil del atacante | Mecanismos destinados a identificar características de la interacción | Evidencia de instrumentación y registros disponibles |
| F2 | Aislamiento de red | Distribución de los componentes entre las redes definidas | Capturas de redes, subredes y componentes asociados |
| F2 | Entorno controlado | Ejecución de los servicios dentro del laboratorio | Evidencia de contenedores y servicios activos |
| F3 | Captura de eventos | Generación y recepción de información derivada de las interacciones | Registros de eventos y capturas de las herramientas de monitoreo |
| F3 | Enriquecimiento | Incorporación o tratamiento de información adicional sobre los eventos | Registros o capturas del procesamiento realizado |
| F3 | Custodia de evidencia | Conservación de los datos y registros generados | Evidencia de almacenamiento y registros persistentes |
| F4 | Normalización | Preparación de los eventos para su tratamiento posterior | Registros que permitan observar el procesamiento de los eventos |
| F4 | Correlación con tickets | Relación entre eventos detectados e incidentes registrados | Evidencia de gestión de incidentes |
| F4 | Mapeo con MITRE ATT&CK | Asociación de los eventos con técnicas o tácticas del marco | Evidencia del mapeo realizado |
| F5 | Cálculo del tiempo medio de detección (MTTD) | Disponibilidad de los datos necesarios para determinar el indicador | Registros temporales de eventos e incidentes |
| F5 | Cálculo del índice de impacto del aprendizaje y la mejora (IIAM) | Disponibilidad de los elementos requeridos para el cálculo | Registros de evaluación e implementación |
| F5 | Reporte de lecciones aprendidas | Registro de aprendizajes derivados de la implementación | Reporte o registro de resultados y acciones de mejora |

*Nota.* La tabla organiza las funciones que requieren comprobación durante la implementación, junto con los elementos que deben observarse y las evidencias necesarias para respaldar cada verificación. La matriz orienta el proceso de documentación y no constituye una medición de resultados.

Cada evidencia se identifica de acuerdo con la fase y la función que respalda, de manera que su incorporación mantiene una relación directa con el elemento que se pretende comprobar este criterio permite conservar la trazabilidad entre el diseño metodológico, la implementación técnica y la evidencia obtenida, evitando atribuir a una captura información que no puede demostrarse a partir de su contenido.

### 4.3.5. Fase 1. Diseño del señuelo

La primera fase prepara el señuelo que se utiliza en el prototipo, su propósito es representar un servicio tributario dentro del entorno controlado y establecer las condiciones necesarias para registrar las interacciones que se producen con este servicio. El diseño de esta fase contempla las cinco decisiones definidas en la metodología, relacionadas con la identificación del activo, el nivel de interacción, el contenido, los mecanismos de detección y el perfil del atacante.

El prototipo representa servicios digitales tributarios mediante dos componentes principales. El primero corresponde al portal web identificado como *decoy.portal*, mientras que el segundo corresponde a la interfaz de programación de aplicaciones (API) identificada como *decoy.api*. Ambos componentes forman parte del entorno controlado y permiten disponer de una superficie de interacción sobre la cual se pueden observar las acciones realizadas durante las pruebas.

**Identificación y selección del activo**

La identificación del activo permite establecer qué servicio se representa mediante el señuelo, en esta implementación el activo corresponde a servicios digitales relacionados con la administración tributaria. La selección se mantiene alineada con el propósito de la metodología, ya que el señuelo debe representar un servicio cuya interacción pueda generar información útil para la gestión de incidentes.

El portal web constituye la parte visible del servicio simulado, su pantalla principal reúne las opciones disponibles para acceder a las funciones incorporadas en el señuelo. La Figura X presenta esta interfaz y permite verificar la existencia del componente destinado a representar el servicio tributario desde una interfaz web.

Figura X

*Interfaz principal del portal web del servicio tributario simulado*

![](data:image/png;base64...)

*Nota.* Interfaz principal del componente decoy.portal, implementado como parte del servicio tributario simulado.

El segundo componente corresponde a la API *decoy.api*. esta interfaz permite atender solicitudes dirigidas directamente a los servicios definidos en el prototipo, la Figura X presenta la respuesta inicial del componente, en la que se identifica el servicio tributario simulado junto con la información disponible en su respuesta principal.

Figura X

*Interfaz principal de la API del servicio tributario simulado*

![](data:image/png;base64...)

*Nota.* Respuesta inicial del componente decoy.api, correspondiente al servicio tributario simulado.

La utilización conjunta del portal web y de la API permite representar el activo mediante diferentes formas de interacción, esta configuración mantiene el señuelo dentro del propósito establecido en la metodología, ya que proporciona un servicio simulado sobre el cual pueden generarse solicitudes que posteriormente son objeto de captura y análisis.

**Configuración del señuelo**

Después de identificar el activo, se define el contenido que estará disponible para la interacción, el portal incorpora funciones relacionadas con el acceso de usuarios, la consulta de información tributaria, las declaraciones y la facturación. Estas funciones permiten representar distintas operaciones del servicio seleccionado dentro de una misma estructura.

La pantalla principal organiza las funciones disponibles para el usuario y establece el punto de entrada al servicio a partir de esta estructura, el portal incorpora las diferentes operaciones que forman parte del contenido definido para el señuelo. La configuración busca que las interacciones se desarrollen sobre funciones relacionadas con el servicio tributario representado, manteniendo una estructura coherente con el activo seleccionado.

Dentro del portal se incorpora una función para consultar información tributaria mediante el número de identificación tributaria (NIT), esta operación representa el acceso a información relacionada con los contribuyentes y amplía las posibilidades de interacción disponibles en el servicio simulado.

El portal cuenta además con una sección destinada a las declaraciones tributarias, su presencia permite representar una operación propia del ámbito tributario y amplía el conjunto de funciones disponibles dentro del servicio configurado para el señuelo.

La facturación completa las principales funciones incorporadas en el portal, mediante esta sección se representa otra operación del servicio tributario, con lo cual el contenido del señuelo reúne distintas funciones sobre las que pueden desarrollarse interacciones controladas.

Junto con el portal web, el prototipo incorpora la API decoy.api, encargada de atender las solicitudes dirigidas a las operaciones del servicio, su documentación registra diecinueve puntos de acceso asociados con las funciones definidas para el prototipo, lo que permite establecer una estructura concreta para recibir y procesar las solicitudes generadas durante las pruebas.

La Figura X presenta la documentación de los puntos de acceso mediante OpenAPI, una especificación utilizada para describir de forma estructurada las operaciones disponibles en una interfaz de programación de aplicaciones (API). Esta documentación permite identificar las funciones del servicio y revisar la estructura definida para atender las solicitudes dirigidas al señuelo.

Figura X

*Documentación de los puntos de acceso de la API del señuelo*

![](data:image/png;base64...)

*Nota*. La figura presenta la documentación estructurada de la interfaz de programación de aplicaciones (API) decoy.api mediante OpenAPI. En ella se identifican los puntos de acceso disponibles, sus operaciones asociadas y la estructura definida para atender las solicitudes del servicio tributario simulado.

La especificación OpenAPI permite representar de manera detallada cómo está organizada la API y qué elementos utiliza para atender las solicitudes recibidas, mientras la documentación anterior permite identificar los puntos de acceso disponibles, esta especificación muestra la estructura con la que cada operación se encuentra definida dentro del servicio. La Figura X presenta esta información y permite revisar la organización técnica de la API implementada en el señuelo.

Figura X

*Especificación OpenAPI de la API del señuelo*

![](data:image/png;base64...)

*Nota.* La figura presenta la especificación OpenAPI del componente decoy.api, se observa la estructura definida para describir las operaciones del servicio, junto con los elementos utilizados por la API para atender las solicitudes dirigidas al señuelo.

La configuración del contenido establece las funciones disponibles para la interacción con el señuelo, el portal proporciona una interfaz de acceso al servicio, mientras que la API ofrece operaciones mediante puntos de acceso definidos. Esta estructura constituye la base para las fases posteriores, en las que las solicitudes generadas durante las interacciones son capturadas para su procesamiento.

**Mecanismos de detección y perfil del atacante**

El diseño del señuelo considera también los mecanismos destinados a registrar las interacciones e identificar solicitudes asociadas con actividades sospechosas, la especificación de la API declara funciones de registro de ataques, detección de cargas sospechosas e instrumentación de técnicas de MITRE ATT&CK. Estas capacidades definen la información que el prototipo está preparado para registrar durante las interacciones.

Entre las capacidades declaradas se encuentra la detección de intentos de inyección de lenguaje de consulta estructurado (SQLi), secuencias de comandos entre sitios (XSS) e inyección de comandos. La especificación también indica el registro de las interacciones en archivos de eventos, estas funciones establecen las condiciones necesarias para obtener información que posteriormente puede ser utilizada en las fases de captura, enriquecimiento y análisis.

La información técnica que respalda estas capacidades forma parte de la especificación del servicio. La Figura X presenta los elementos asociados con los puntos de acceso de la API, incluidos los mecanismos de registro, detección e instrumentación declarados para el señuelo.

Figura X

*Capacidades de detección e instrumentación declaradas en la API*

![](data:image/png;base64...)

*Nota.* Información técnica asociada con los puntos de acceso de la API, incluyendo las capacidades de registro, detección e instrumentación declaradas para el señuelo.

La definición del perfil del atacante se incorpora al diseño del señuelo mediante la asociación de técnicas de MITRE ATT&CK con determinados puntos de acceso de la API, estas asociaciones permiten establecer qué tipos de acciones se consideran relevantes durante las pruebas controladas. Dentro de la especificación de la API se identifican técnicas relacionadas con el uso de credenciales válidas, la obtención de información de credenciales y el acceso a información almacenada. De esta manera, el señuelo queda preparado para considerar estas acciones durante el análisis de las interacciones que recibe.

La presencia de estas técnicas en la configuración indica que forman parte del comportamiento previsto para el señuelo, sin embargo, esta configuración por sí sola no permite afirmar que alguna de estas acciones haya ocurrido realmente ni que haya sido detectada. Para comprobarlo es necesario observar los eventos generados durante una prueba controlada y verificar si las interacciones registradas se relacionan con las técnicas configuradas, esta comprobación se realiza en las fases posteriores de captura, análisis y correlación de eventos.

Finalmente, se comprueba que la API se encuentra disponible mediante el recurso de estado incorporado en el componente *decoy.api*. La Figura X muestra la respuesta obtenida durante esta comprobación, en la que el servicio informa un estado saludable. Esta evidencia permite confirmar que la API se encuentra disponible dentro del entorno controlado y puede recibir las interacciones previstas para las siguientes fases de la implementación.

Figura X

*Estado operativo de la API del señuelo*

![](data:image/png;base64...)

Nota. Respuesta del recurso de estado de decoy.api durante la verificación del servicio.

La fase de diseño del señuelo establece el activo que se representa, las funciones que ofrece el servicio, los mecanismos previstos para registrar las interacciones y las técnicas consideradas para definir el perfil del atacante. Con estos elementos definidos, la implementación continúa con el despliegue aislado, etapa en la que el señuelo se integra en las redes establecidas para el entorno controlado.

### 4.3.6. Fase 2. Despliegue aislado

La segunda fase de la implementación materializa el despliegue aislado que el diseño metodológico estructura en cinco actividades, las cuales comprenden el aislamiento de la red de producción, la segmentación interna del entorno del señuelo, el despliegue de los servicios, la verificación de los controles y la documentación del resultado. Esta fase responde a una condición crítica de la metodología, dado que el señuelo solo cumple su función si el adversario que interactúa con él no puede alcanzar los sistemas productivos ni la infraestructura de gestión, por lo cual la verificación del aislamiento constituye la evidencia central que esta sección documenta. El contenido de la sección presenta primero la verificación de la segmentación de la red y después la comprobación de los servicios desplegados, de modo que la evidencia siga el mismo orden en el que el diseño ejecuta estas actividades.

El entorno controlado se organiza en cuatro redes virtuales que agrupan los componentes según su función dentro del prototipo. La primera corresponde a la red *taxfisco-dmz*, destinada a los servicios señuelo expuestos a la interacción externa, mientras que la segunda corresponde a la red *taxfisco-honeypot,* que agrupa los componentes de interacción directa con el señuelo. La tercera corresponde a la red *taxfisco-ids*, que concentra las herramientas de observación del tráfico, y la cuarta corresponde a la red *taxfisco-soc*, que reúne la plataforma de gestión, análisis y visualización. Esta distribución permite que cada grupo de componentes opere dentro de su propio segmento, de modo que la administración del laboratorio permanezca separada de las zonas que reciben las interacciones externas.

**Verificación de la segmentación de la red**

La primera verificación comprueba que las cuatro redes se encuentran registradas en el entorno Docker, para lo cual se ejecuta una consulta con filtro sobre el prefijo taxfisco. La consulta devuelve el identificador de cada red junto con su controlador y su ámbito, lo cual permite confirmar que las cuatro redes existen y que fueron creadas con el controlador bridge y el ámbito local. La Figura 1 presenta el resultado de esta consulta y permite verificar la existencia de cada segmento dentro del entorno.

Figura 1

*Redes virtuales registradas en el entorno de implementación*

*![](data:image/png;base64...)*

*Nota.* Resultado de la consulta de redes del entorno Docker con filtro sobre el prefijo taxfisco.

La segunda verificación inspecciona cada red para conocer el rango de direcciones asignado y la cantidad de contenedores conectados, información que se obtiene mediante un comando que recorre las cuatro redes de manera secuencial. La Figura 2 presenta el resultado de esta inspección y muestra que la red *taxfisco-dmz* opera con el segmento 10.20.0.0/24 y concentra 6 contenedores, la red *taxfisco-honeypot* utiliza el segmento 10.21.0.0/24 con 3 contenedores, la red *taxfisco-ids* emplea el segmento 10.23.0.0/24 con 2 contenedores y la red *taxfisco-soc* ocupa el segmento 10.22.0.0/24 con 19 contenedores.

Figura 2

*Segmentos de red y contenedores asociados a cada red del laboratorio*

![](data:image/png;base64...)

*Nota.* Inspección de las cuatro redes con el rango, la puerta de enlace y la cantidad de contenedores de cada segmento.

La distribución observada resulta coherente con el diseño, ya que la mayor cantidad de contenedores corresponde a la plataforma de gestión del segmento de operación, cuya dotación reúne los servicios de monitoreo, gestión de incidentes, enriquecimiento y visualización. Las zonas expuestas mantienen una dotación mínima que reduce la superficie del entorno, condición que disminuye la cantidad de componentes susceptibles de resultar afectados por una interacción hostil.

La tercera verificación examina las propiedades de configuración de cada red mediante una inspección detallada que muestra el controlador, el ámbito, el indicador de red interna y el segmento de direccionamiento. La Figura 3 presenta este resultado y confirma que las cuatro redes utilizan el controlador bridge, operan con ámbito local y se crean sin la marca de red interna.

Figura 3

*Propiedades de configuración de las redes del entorno*

*![](data:image/png;base64...)*

*Nota.* Inspección detallada de las redes con el controlador, el ámbito y el segmento de cada una.

El controlador bridge crea una red independiente para cada segmento y evita que los contenedores de una red comuniquen con los de otra de manera predeterminada, propiedad que constituye la base técnica del aislamiento que esta fase verifica. De este modo, un contenedor comprometido en la zona de exposición no dispone de una ruta de red hacia el segmento de operación, lo cual impide que el adversario use el señuelo como puente hacia la infraestructura de gestión.

En conjunto, estas verificaciones documentan que ningún contenedor de gestión comparte subred con los servicios señuelo, condición que el diseño establece para proteger la plataforma de administración frente a las interacciones hostiles. El aislamiento verificado protege además la evidencia que la fase de captura genera, dado que la contaminación del entorno de gestión invalidaría los registros que sustentan la investigación.

**Verificación de los servicios desplegados**

Con la segmentación verificada, la fase continúa con la comprobación de los servicios de la plataforma, ya que la metodología asigna a cada componente una función dentro de la cadena de captura, correlación y medición. Esta comprobación resulta necesaria porque la ausencia o el mal estado de cualquiera de estos servicios dejaría una fase posterior sin el soporte tecnológico que requiere, por lo cual el estado de cada componente se registra como evidencia del despliegue. La verificación se realiza mediante el acceso a la interfaz de cada servicio desde el entorno controlado, siguiendo el orden de la cadena de valor del prototipo, de modo que primero se comprueba la recepción de eventos y después la visualización, la gestión de incidentes, el soporte de la respuesta, el enriquecimiento, la orquestación y el análisis.

El primer servicio verificado corresponde a ***Wazuh***, plataforma de gestión de información y eventos de seguridad de código abierto, encargada de recibir los eventos que los sensores generan y ponerlos a disposición del análisis, función que la convierte en el punto de entrada de la telemetría del laboratorio. Su tablero de administración se encuentra disponible y muestra los patrones de índice *wazuh-alerts-\** y *wazuh-\** que la plataforma utiliza para organizar las alertas entrantes, lo cual indica que la canalización de recepción se encuentra configurada para recibir los eventos que la fase de captura genera.

Figura 4

*Tablero de administración de Wazuh*

![](data:image/png;base64...)

*Nota.* Consola de administración de Wazuh con los patrones de índice *wazuh-alerts-\** y *wazuh-*\* registrados.

El segundo servicio corresponde a ***Grafana***, plataforma de visualización de métricas y tableros de código abierto, destinada a presentar los indicadores que la fase de medición calcula sobre los eventos capturados y los incidentes correlacionados. Su interfaz de inicio de sesión en la versión 11.2.0 responde al acceso desde el entorno, lo cual confirma que el servicio de visualización se encuentra desplegado y disponible dentro del segmento de operación.

Figura 5

*Interfaz de inicio de sesión de Grafana*

*![](data:image/png;base64...)*

*Nota.* Pantalla de acceso de Grafana disponible en el segmento de operación.

El tercer servicio corresponde a ***TheHive***, plataforma de código abierto destinada a la gestión de incidentes, cuya función consiste en almacenar los casos y organizar la atención de los incidentes que la correlación de la fase siguiente registra. Su consola lista la organización default y presenta la interfaz de administración, con lo cual se verifica que la plataforma se encuentra desplegada y accesible dentro del entorno controlado.

Figura 6

*Consola de administración de TheHive*

![](data:image/png;base64...)

*Nota.* Interfaz de TheHive con la organización default disponible.

El cuarto servicio corresponde a ***Velociraptor***, plataforma de código abierto para la respuesta forense y la gestión remota de endpoints, cuya función es brindar soporte a la respuesta sobre los equipos del laboratorio. Su consola muestra la pantalla de bienvenida con la sesión del administrador activa y las opciones de gestión del servidor disponibles, lo cual confirma el despliegue del servicio dentro del segmento de operación.

Figura 7

*Consola de bienvenida de Velociraptor*

![](data:image/png;base64...)

*Nota.* Interfaz de Velociraptor con la sesión administrativa activa.

El quinto servicio corresponde a ***MISP***, plataforma de código abierto para el intercambio de información de amenazas, cuya función es aportar contexto de inteligencia al enriquecimiento de los eventos. Su interfaz muestra la pantalla de instalación inicial con la solicitud de configuración del acceso, lo cual indica que el servicio se encuentra desplegado en su primer arranque y requiere la configuración inicial del administrador antes de que el enriquecimiento pueda apoyarse en sus funciones. Este estado corresponde al primer despliegue del servicio y no representa un error, dado que la configuración inicial forma parte de la puesta en marcha prevista para este componente.

Figura 8

*Pantalla de instalación inicial de MISP*

![](data:image/png;base64...)

*Nota.* Interfaz de MISP en su estado de primer arranque con la configuración del acceso pendiente.

El sexto servicio corresponde a ***Shuffle***, plataforma de orquestación, automatización y respuesta de seguridad de código abierto, cuya función es encadenar las acciones automatizadas entre los servicios de la plataforma. Su interfaz presenta la pantalla de creación de la cuenta de administrador, estado que corresponde al primer arranque del servicio y que se resuelve con la definición del acceso inicial, de modo que la orquestación queda habilitada para las fases posteriores.

Figura 9

*Pantalla de creación de cuenta administradora de Shuffle*

![](data:image/png;base64...)

*Nota.* Interfaz de Shuffle en su primer arranque con la creación de la cuenta administradora pendiente.

El último servicio verificado corresponde a ***Cortex***, plataforma de código abierto para el análisis automatizado, cuya función es ejecutar los analizadores configurados sobre las evidencias recolectadas. Su página de inicio de sesión se encuentra disponible y responde al acceso desde el entorno, lo cual verifica el despliegue del servicio dentro del segmento de operación.

Figura 10

*Página de inicio de sesión de Cortex*

*![](data:image/png;base64...)*

*Nota.* Pantalla de acceso de Cortex disponible en el segmento de operación.

**Cierre de la fase**

La verificación de la fase confirma que la segmentación de la red opera según el diseño y que los servicios del segmento de operación se encuentran desplegados, con lo cual el entorno controlado queda establecido bajo las condiciones que la metodología exige para la captura de eventos. Cada comprobación queda registrada como evidencia dentro de la documentación del despliegue, de modo que la trazabilidad de la fase se conserva para las etapas posteriores de la investigación. Con el entorno desplegado, segmentado y verificado, la implementación continúa con la fase de captura, en la cual el señuelo comienza a registrar las interacciones que recibe.

### 4.3.7. Fase 3. Captura, enriquecimiento y custodia

La tercera fase de la implementación verifica la captura, el enriquecimiento y la custodia de los eventos que las interacciones con el señuelo generan, para lo cual el diseño metodológico estructura cinco actividades relacionadas con la captura de los eventos, el enriquecimiento con contexto, la preservación de la cadena de custodia, la validación de la integridad y la documentación del resultado. La captura de eventos se apoya en seis componentes que observan la actividad del entorno desde distintos puntos de vista, los cuales se describen a continuación junto con su función y su propósito dentro del prototipo, para después presentar la evidencia de su operación durante las pruebas controladas.

* **Suricata**, motor de detección de intrusiones de código abierto, inspecciona el tráfico de red en tiempo real y lo compara contra un conjunto de reglas que identifican patrones de ataque conocidos. Su propósito dentro del prototipo es observar las comunicaciones del segmento de detección y registrar las coincidencias con las reglas activas, entre las que figuran reglas personalizadas con metadatos de técnicas de MITRE ATT&CK.
* **Cowrie**, honeypot de interacción media de código abierto que emula un servidor SSH, registra los intentos de acceso remoto junto con las credenciales probadas y las sesiones que el adversario inicia. Su propósito dentro del prototipo es capturar los intentos de fuerza bruta contra el servicio SSH simulado, actividad que el perfil del atacante identifica como frecuente en los servicios expuestos.
* **OpenCanary**, daemon de honeypot de baja interacción de código abierto, emula servicios del entorno y emite eventos estructurados ante cualquier interacción que recibe. Su propósito dentro del prototipo es operar como sensor distribuido que señala con alta certeza la presencia de actividad no legítima, dado que ningún usuario autorizado se comunica con sus servicios simulados.
* **Heralding**, honeypot de credenciales de código abierto, emula servicios de autenticación como SSH, FTP, Telnet, RDP, HTTP y bases de datos, para registrar los intentos de acceso con el detalle de cada sesión. Su propósito dentro del prototipo es capturar los intentos de autenticación contra los servicios que un portal tributario expone de manera habitual, ampliando la cobertura de la captura más allá del servicio web.
* **El servicio decoy.api**, presentado en la fase de diseño, registra cada solicitud que recibe y clasifica las solicitudes sospechosas contra las técnicas de MITRE ATT&CK definidas en su instrumentación. Su propósito dentro del prototipo es capturar los intentos de explotación contra la API tributaria simulada con su clasificación ya incorporada, lo cual adelanta el trabajo de correlación que la fase siguiente ejecuta.
* **La plataforma Wazuh**, descrita en la fase de despliegue, recibe los eventos de los sensores y los honeypots, los indexa y los pone a disposición de la consulta y el análisis. Su propósito dentro del prototipo es operar como punto de convergencia de la captura, de modo que la totalidad de los registros generados durante las pruebas quede disponible en un repositorio consultable.

**Captura de eventos**

La primera verificación de la captura comprueba que los eventos generados en el entorno llegan a la plataforma de monitoreo y quedan indexados para su consulta, la Figura 12 presenta la consola de descubrimiento de ***Wazuh*** sobre el índice wazuh-alerts-\*, en la cual se observan 199 eventos registrados dentro del período de consulta, junto con los campos de descripción de la regla, nivel de la regla y nombre del agente que permite identificar el origen de cada registro.

Figura 12

*Eventos indexados en la plataforma de monitoreo*

![](data:image/png;base64...)

*Nota.* Consola de descubrimiento de Wazuh con los eventos indexados en el índice wazuh-alerts-\* durante el período de consulta.

La segunda verificación examina la estructura de un evento almacenado, dado que la custodia de la evidencia exige que cada registro conserve su contenido completo en un formato consultable. La Figura 13 presenta el documento expandido de un evento, en el cual se observa la estructura JSON con el índice de almacenamiento, el identificador único del documento y el origen del evento, elementos que garantizan la trazabilidad individual de cada registro.

Figura 13

*Estructura de un evento almacenado en la plataforma de monitoreo*

![](data:image/png;base64...)

*Nota.* Documento expandido de un evento almacenado en Wazuh, con la estructura JSON que conserva el índice, el identificador y el origen del registro.

La tercera verificación revisa la operación interna del gestor de la plataforma, dado que la captura continua requiere que la canalización de recepción opere de manera estable, la Figura 14 presenta el registro del gestor Wazuh, en el cual se observa la conexión establecida con el indexador, la carga de la plantilla de índices y la lectura continua del archivo de alertas que el servicio mantiene para la recepción de eventos.

Figura 14

*Operación interna del gestor de la plataforma de monitoreo*

![](data:image/png;base64...)

*Nota.* Registro operativo del gestor Wazuh con la conexión al indexador, la carga de la plantilla y la lectura del archivo de alertas.

La cuarta verificación corresponde al servicio señuelo ***decoy.api***, cuyo registro la Figura 15 presenta con las solicitudes atendidas durante la prueba controlada, el registro muestra la detección de un intento de inyección SQL dirigido al punto de acceso de contribuyentes, el cual el servicio clasifica automáticamente como la técnica T1190 de acceso inicial del marco MITRE ATT&CK y asocia con la dirección de origen de la solicitud.

Figura 15

*Detección de inyección SQL en el servicio señuelo decoy.api*

![](data:image/png;base64...)

*Nota*. Registro del servicio decoy.api con la detección de un intento de inyección SQL clasificado como la técnica T1190 de MITRE ATT&CK.

La quinta verificación corresponde al honeypot ***Cowrie***, cuyo registro la Figura 16 presenta con la captura de un intento de fuerza bruta SSH originado desde la dirección 10.20.0.99. El registro conserva la versión remota del cliente, la huella hassh del cliente SSH, los intentos de autenticación con las credenciales probadas y las sesiones iniciadas dentro del entorno emulado, detalle que permite reconstruir la secuencia completa del intento de acceso.

Figura 16

*Captura de fuerza bruta SSH en el honeypot Cowrie*

![](data:image/png;base64...)

*Nota*. Registro del honeypot Cowrie con la captura de un intento de fuerza bruta SSH, incluidas las credenciales probadas y las sesiones iniciadas.

La sexta verificación corresponde al motor de detección ***Suricata***, cuyo registro la Figura 17 presenta con el inicio del motor en modo de detección y la inicialización de sus salidas de registro en los archivos *fast.log*, *eve.json* y *http.log*. El registro muestra además el procesamiento del conjunto de reglas personalizadas del laboratorio, entre las que figuran firmas de inyección de comandos con metadatos de la técnica T1059 de MITRE ATT&CK, lo cual verifica que la inspección de red opera con reglas alineadas al marco de comportamiento adversario.

Figura 17

*Inicio del motor de detección Suricata*

*![](data:image/png;base64...)*

*Nota*. Registro del motor Suricata con el inicio en modo de detección, la inicialización de las salidas de registro y el procesamiento de las reglas personalizadas del laboratorio.

La séptima verificación corresponde al daemon ***OpenCanary***, cuyo registro la Figura 18 presenta con el evento estructurado que el sensor emite al ponerse en operación. El evento se registra en formato JSON con el identificador del nodo, la marca temporal y el tipo de registro, estructura que mantiene la uniformidad de los registros que la custodia de la evidencia requiere.

Figura 18

*Puesta en operación del sensor OpenCanary*

*![](data:image/png;base64...)*

*Nota*. Registro del sensor OpenCanary con el evento JSON de puesta en operación del nodo.

La octava verificación corresponde al honeypot ***Heralding***, cuyo registro la Figura 19 presenta con la inicialización de sus capacidades de emulación sobre los puertos estándar de los servicios de autenticación. El registro muestra la activación de las capacidades SSH, FTP, Telnet, RDP, HTTP y de bases de datos, junto con la configuración de los archivos de registro de autenticación y sesiones, lo cual verifica la cobertura de captura de credenciales del entorno.

Figura 19

*Inicialización de las capacidades del honeypot Heralding*

*![](data:image/png;base64...)*

*Nota*. Registro del honeypot Heralding con la inicialización de las capacidades de emulación y la configuración de los archivos de registro.

**Enriquecimiento de los eventos**

El enriquecimiento de los eventos corresponde a la segunda actividad de la fase, cuyo propósito consiste en incorporar contexto a los registros capturados para que la correlación y la medición operen sobre información completa. El enriquecimiento del prototipo agrega a cada evento la identificación de la técnica de MITRE ATT&CK, la táctica asociada, las marcas temporales de inicio y fin de la actividad, la herramienta empleada por el atacante, el objetivo alcanzado y la correspondencia con las fases del ciclo de incidentes de ISO/IEC 27035.

La verificación del enriquecimiento utiliza el archivo de resultados del escenario de ataque controlado S03 de fuerza bruta SSH, cuyo contenido la Figura 20 presenta en formato JSON. El archivo identifica la técnica T1110.001 de adivinación de contraseñas dentro de la táctica de acceso a credenciales, registra las marcas temporales de inicio y fin de la prueba en formato UTC, la herramienta de ataque empleada y el objetivo escaneado, junto con los puntos de detección esperados que comprenden la regla 5712 de Wazuh para fuerza bruta SSH y el registro del honeypot Cowrie.

El archivo incorpora además la correspondencia con las fases de detección y reporte y de evaluación del ciclo de incidentes de ISO/IEC 27035, lo cual verifica que el enriquecimiento no solo describe la actividad adversaria sino que la ubica dentro del proceso institucional de gestión que la metodología adopta.

Figura 20

*Resultados enriquecidos del escenario de fuerza bruta SSH*

![](data:image/png;base64...)

*Nota*. Archivo de resultados del escenario de fuerza bruta SSH con la identificación de la técnica, las marcas temporales, los puntos de detección esperados y la correspondencia con las fases de ISO/IEC 27035.

**Custodia de la evidencia**

La custodia de la evidencia corresponde a la tercera actividad de la fase y tiene por objeto preservar la integridad y la trazabilidad de los registros que las pruebas generan. La custodia del prototipo se implementa mediante tres mecanismos complementarios, cuyo primero es la generación de huellas criptográficas SHA-256 de cada archivo de evidencia, cuyo segundo es el sellado temporal del momento de la custodia y cuyo tercero es la verificación de las huellas contra los archivos almacenados.

El mecanismo de huella criptográfica se apoya en la función de hash SHA-256, la cual produce una cadena única de 256 bits a partir del contenido de un archivo, de modo que cualquier modificación posterior del archivo altera la huella de manera detectable. Su propósito dentro del prototipo es garantizar la integridad de la evidencia, dado que la comparación de la huella original con la huella recalculada demuestra si el archivo conserva su contenido original.

La primera verificación de la custodia presenta la generación de las huellas de la totalidad de los archivos de evidencia del laboratorio, la cual la Figura 21 muestra con el par huella y archivo para cada registro. La lista cubre la evidencia del entorno de servicios, del señuelo, del aislamiento de red, de la captura de eventos, de la correlación de incidentes y de las métricas, con lo cual la totalidad de las capturas que sustentan la investigación queda protegida por su huella criptográfica.

Figura 21

*Huellas criptográficas de los archivos de evidencia*

![](data:image/png;base64...)

*Nota*. Lista de huellas SHA-256 generadas para la totalidad de los archivos de evidencia del laboratorio.

La segunda verificación presenta el sellado temporal del momento en que se ejecuta la custodia, la cual la Figura 22 muestra con la marca temporal del sistema en formato ISO 8601 junto con la zona horaria correspondiente. El sellado registra el instante exacto de la operación de custodia con su desplazamiento horario, dato que permite ordenar la evidencia en el tiempo y respaldar la secuencia de las pruebas ante una revisión posterior.

Figura 22

*Sellado temporal de la custodia de la evidencia*

![](data:image/png;base64...)

*Nota*. Marca temporal del sistema con el registro del instante de la custodia en formato ISO 8601 y su zona horaria.

La tercera verificación se apoya en la herramienta sha256sum, la cual recalcula la huella de cada archivo y la compara con la huella registrada en la lista de custodia, la Figura 23 presenta la salida de la verificación, en la cual cada archivo reporta que la suma coincide, resultado que demuestra que la evidencia conserva su contenido original desde el momento del sellado.

Figura 23

*Verificación de integridad de la evidencia*

![](data:image/png;base64...)

*Nota*. Verificación de integridad de los archivos de evidencia mediante la comparación de huellas SHA-256, con resultado coincidente en cada archivo.

La cuarta verificación presenta la estructura de custodia del escenario de ataque controlado, cuyo contenido la Figura 24 muestra con los archivos de la evidencia del escenario S03. El directorio conserva los archivos de delimitación temporal con el instante de inicio y el instante de fin de la prueba en formato UTC, el archivo de salida de la herramienta de ataque junto con el archivo de resultados enriquecidos, de modo que la evidencia del escenario queda organizada, fechada y trazable desde su generación hasta su verificación.

Figura 24

*Estructura de custodia del escenario de ataque controlado*

*![](data:image/png;base64...)*

*Nota*. Estructura de custodia del escenario S03 con los archivos de delimitación temporal, la salida de la herramienta de ataque y los resultados enriquecidos.

**Cierre de la fase**

La verificación de la fase confirma que la captura, el enriquecimiento y la custodia operan como un solo proceso, en el cual los eventos fluyen desde los sensores y los señuelos hacia el punto de recepción, los registros incorporan la identificación de la técnica de MITRE ATT&CK y la correspondencia con las fases de ISO/IEC 27035, y la evidencia queda protegida mediante huellas criptográficas, sellado temporal y verificación de integridad. Este resultado verifica las actividades que el diseño metodológico asigna a la fase y establece la base de registros trazables sobre la cual la correlación con la gestión de incidentes opera. Con la captura, el enriquecimiento y la custodia verificados, la implementación continúa con la fase de correlación, en la cual los eventos se vinculan con los casos de la gestión institucional.

### 4.3.8. Fase 4. Correlación con gestión de incidentes

La cuarta fase de la implementación verifica la correlación de los eventos del señuelo con la gestión institucional de incidentes, para lo cual el diseño metodológico estructura cinco actividades relacionadas con la vinculación de los eventos al sistema de gestión, la clasificación por tipo y severidad, la notificación a los responsables, la priorización por impacto y la documentación del resultado. La verificación de esta fase se apoya en cuatro componentes que transforman la actividad observada en los señuelos en casos documentados dentro de la plataforma de gestión, los cuales se describen a continuación junto con su función y su propósito dentro del prototipo.

* **Wazuh**, plataforma de gestión de información y eventos de seguridad de código abierto, recolecta los eventos que los sensores del laboratorio generan y los evalúa contra reglas de detección que identifican patrones de ataque conocidos. Su propósito dentro del prototipo es actuar como motor de detección, dado que cada coincidencia de una regla produce una alerta que la cadena de correlación consume como punto de partida.
* **Shuffle**, plataforma de orquestación, automatización y respuesta de seguridad de código abierto conocida como SOAR, encadena acciones automatizadas entre los componentes del entorno mediante flujos de trabajo activados por eventos. Su propósito dentro del prototipo es eliminar la intervención manual en el paso de una alerta a un caso, de modo que la creación del registro de incidente ocurre de manera automática cuando la detección lo requiere.
* **TheHive**, plataforma de código abierto destinada a la gestión de incidentes, centraliza las alertas, las agrupa en casos, les asigna severidad y organiza su atención mediante tareas, líneas de tiempo y observables. Su propósito dentro del prototipo es operar como el punto institucional de gestión de incidentes, es decir, el lugar donde las alertas del señuelo se convierten en casos documentados con trazabilidad completa.
* **MISP**, plataforma de código abierto para el intercambio de información de amenazas, almacena y comparte inteligencia estructurada en forma de eventos con atributos, etiquetas y niveles de amenaza. Su propósito dentro del prototipo es aportar el contexto de inteligencia que enriquece los casos, de modo que cada incidente correlacionado queda vinculado con el conocimiento disponible sobre la técnica observada.

**Generación de alertas a partir de los eventos del señuelo**

La primera verificación de la fase corresponde a la lista de alertas que la plataforma de gestión recibe desde la cadena de detección, la cual la Figura 25 presenta con tres registros generados durante las pruebas controladas. El primer registro corresponde a un escaneo de puertos y reconocimiento asociado con la técnica T1595 del marco MITRE ATT&CK, el segundo corresponde a un intento de inyección SQL contra la API tributaria asociado con la técnica T1190 y el tercero corresponde a un intento de fuerza bruta SSH detectado en el honeypot Cowrie asociado con la técnica T1110.001.

Cada alerta incorpora la técnica de MITRE ATT&CK, la fuente del evento y una severidad asignada, lo cual verifica que la normalización de los eventos del señuelo produce alertas estructuradas listas para la gestión institucional.

Figura 25

*Alertas generadas desde los eventos de los señuelos*

*![](data:image/png;base64...)*

*Nota*. Lista de alertas generadas durante las pruebas controladas, con la técnica de MITRE ATT&CK, la fuente y la severidad de cada registro.

**Creación automatizada de casos mediante orquestación**

La segunda verificación corresponde al flujo de trabajo configurado en la plataforma de orquestación, cuya función es crear un caso en TheHive cada vez que la detección reporta una alerta de fuerza bruta SSH. La Figura 26 muestra el flujo, en el cual un webhook recibe la alerta de Wazuh y ejecuta una acción que invoca la interfaz de programación de aplicaciones de TheHive para registrar el caso de manera automática. Esta configuración verifica la actividad de vinculación de los eventos con el sistema de gestión que el diseño metodológico establece, dado que la creación del caso ocurre sin intervención manual del operador.

Figura 26

*Flujo de trabajo de orquestación para la creación de casos*

*![](data:image/png;base64...)*

*Nota*. Flujo de trabajo de la plataforma Shuffle que recibe la alerta de Wazuh mediante un webhook y crea el caso correspondiente en TheHive.

**Registro del caso con mapeo y trazabilidad**

La tercera verificación corresponde al caso registrado en la plataforma de gestión a partir de la alerta de fuerza bruta SSH, el cual la Figura 27 presenta con su información completa. El caso registra el origen de la actividad desde la dirección 10.20.0.99, los intentos de acceso que el honeypot Cowrie capturó con las credenciales root/hone y root/password, y el mapeo de la técnica T1110.001 de MITRE ATT&CK junto con las etiquetas brute-force, cowrie y honeypot.

El caso incorpora además la severidad MEDIA, la clasificación TLP:AMBER del protocolo de semáforo de tráfico y la clasificación PAP:AMBER del protocolo de acciones permisibles, las cuales delimitan la circulación del caso dentro de la organización y las acciones que corresponden aplicar sobre él. La descripción del caso declara su correlación con el evento número 1 de la plataforma de inteligencia y con el flujo de trabajo de la plataforma de orquestación, lo cual verifica que el registro del incidente conserva la trazabilidad hacia el evento de inteligencia y hacia el mecanismo que lo generó.

Figura 27

*Caso de fuerza bruta SSH registrado en la plataforma de gestión*

*![](data:image/png;base64...)*

*Nota*. Caso registrado en TheHive a partir de la alerta de fuerza bruta SSH, con el origen, las credenciales observadas, el mapeo de MITRE ATT&CK y los vínculos de correlación.

**Enriquecimiento del caso con inteligencia de amenazas**

La cuarta verificación corresponde al evento registrado en la plataforma de inteligencia, el cual la Figura 28 presenta con la denominación de fuerza bruta SSH asociada a la técnica T1110.001. El evento incorpora el nivel de amenaza MEDIO, el estado de análisis en curso y tres atributos que estructuran la información observable, lo cual verifica que el enriquecimiento del caso se apoya en un registro de inteligencia formal y no en una referencia informal.

Figura 28

*Evento de inteligencia asociado al caso de fuerza bruta SSH*

*![](data:image/png;base64...)*

*Nota*. Evento de fuerza bruta SSH registrado en la plataforma de inteligencia MISP, con el nivel de amenaza, el estado de análisis y los atributos del registro.

**Cierre de la fase**

La verificación de la fase confirma la cadena completa de correlación, en la cual un evento capturado por el señuelo se transforma en una alerta estructurada, la alerta origina un caso mediante orquestación automatizada y el caso queda documentado con el mapeo de MITRE ATT&CK y el vínculo a la inteligencia de amenazas. Este resultado verifica las actividades de vinculación, clasificación y documentación que el diseño metodológico asigna a la fase, de modo que la gestión de incidentes opera sobre registros trazables desde su origen hasta su cierre. Con la correlación verificada, la implementación continúa con la fase de medición, en la cual los indicadores de la cadena se calculan sobre los casos registrados.

### 4.3.9. Fase 5. Medición y lecciones aprendidas

La quinta fase de la implementación verifica la medición del impacto y las lecciones aprendidas, para lo cual el diseño metodológico estructura cinco actividades relacionadas con la medición del impacto mediante indicadores cuantitativos, la comparación del estado inicial con el estado posterior, la evaluación de la sostenibilidad institucional, la documentación de las lecciones aprendidas y la difusión de los resultados. La medición del prototipo se apoya en cinco componentes que consolidan los indicadores de la cadena y los presentan en tableros y reportes, los cuales se describen a continuación junto con su función y su propósito dentro del prototipo.

* **Grafana**, plataforma de visualización descrita en la fase de despliegue, construye tableros de indicadores sobre los datos indexados por la plataforma de monitoreo y los presenta en paneles consultables. Su propósito dentro del prototipo es ofrecer la vista consolidada de la operación, de modo que la medición del impacto se consulta en tableros actualizados con los datos de las pruebas.
* **Velociraptor**, plataforma de respuesta forense descrita en la fase de despliegue, supervisa el estado operativo de sus servicios mediante un tablero de estado del servidor. Su propósito dentro de esta fase es verificar que la plataforma de respuesta opera con los recursos del entorno bajo control durante la medición.
* **El reporte de indicadores**, archivo JSON que el laboratorio genera al cerrar los escenarios de prueba, consolida la ejecución de los escenarios y los valores de los indicadores de detección con su método de medición. Su propósito dentro del prototipo es documentar los indicadores de manera estructurada y reproducible, de modo que cada valor pueda rastrearse hasta el escenario y el evento que lo origina.
* **El reporte de cobertura**, archivo JSON que el laboratorio genera sobre la matriz de MITRE ATT&CK Enterprise, relaciona cada escenario de prueba con la técnica y la táctica que ejerce. Su propósito dentro del prototipo es medir la cobertura de detección sobre el conjunto de técnicas implementadas, de modo que la mejora continua del señuelo se oriente con datos.
* **El reporte de correspondencia normativa**, archivo JSON que documenta el soporte de las fases del ciclo de incidentes de ISO/IEC 27035 con los componentes del laboratorio. Su propósito dentro del prototipo es demostrar que la operación del laboratorio se sustenta en el marco normativo que la metodología adopta.

**Configuración de la medición**

La primera verificación comprueba que los tableros de medición se encuentran creados y organizados dentro de la plataforma de visualización. La Figura 29 presenta la lista de tableros del laboratorio, la cual incluye el tablero de panorama de la operación, el tablero de indicadores de detección y respuesta y el tablero de alertas detalladas, con las etiquetas que los clasifican.

Figura 29

*Tableros de medición del laboratorio*

*![](data:image/png;base64...)*

*Nota*. Lista de tableros de medición del laboratorio con sus etiquetas de clasificación.

La segunda verificación comprueba que los tableros se conectan al índice de eventos de la plataforma de monitoreo como fuente de datos. La Figura 30 presenta la configuración de la fuente de datos, en la cual se observa la conexión al indexador de Wazuh sobre la dirección interna del segmento de operación, con autenticación configurada y soporte de alertas habilitado, lo cual verifica que la medición opera sobre los datos reales de la captura.

Figura 30

*Configuración de la fuente de datos de la medición*

*![](data:image/png;base64...)*

*Nota*. Configuración de la fuente de datos del indexador de Wazuh con su dirección interna, autenticación y soporte de alertas.

**Indicadores de la operación**

La tercera verificación presenta el tablero de panorama de la operación, el cual la Figura 31 muestra con los indicadores consolidados del período de pruebas. El tablero registra 199 alertas totales, una distribución por severidad con predominio del nivel bajo, 45 alertas de severidad alta, un nivel promedio de 3,92 y un nivel máximo de 7, junto con la evolución temporal de las alertas y su concentración en las primeras semanas del período.

Figura 31

*Tablero de panorama de la operación*

*![](data:image/png;base64...)*

*Nota*. Tablero de panorama de la operación con el total de alertas, la distribución por severidad, el nivel promedio y la evolución temporal.

La cuarta verificación presenta el tablero de indicadores, el cual la Figura 32 muestra con el detalle de la severidad y de las reglas que más alertas generan. El tablero confirma los 199 eventos indexados, el nivel promedio de 3,92 y el nivel máximo de 7, y desagrega las alertas por severidad con 152 de nivel bajo, 45 de nivel alto y 2 de nivel medio, además de las cinco reglas principales con sus conteos.

Figura 32

*Tablero de indicadores de detección*

*![](data:image/png;base64...)*

*Nota*. Tablero de indicadores con el total de eventos, el nivel promedio, el nivel máximo, la severidad y las reglas principales.

La quinta verificación presenta el tablero de alertas detalladas, el cual la Figura 33 muestra con los últimos registros y sus campos de origen, descripción de la regla, identificador de la regla, nivel y marca temporal. Este tablero verifica que la medición se apoya en registros individuales trazables, dado que cada alerta conserva su origen y su instante de generación.

Figura 33

*Tablero de alertas detalladas*

![](data:image/png;base64...)

*Nota*. Tablero de alertas detalladas con los últimos registros y sus campos de origen, regla, nivel y marca temporal.

**Monitoreo operativo de la plataforma**

La sexta verificación presenta el estado del servidor de la plataforma de respuesta, el cual la Figura 34 muestra con el tablero de estado en el instante de la medición. El tablero registra la utilización de procesador y memoria, los clientes conectados y las organizaciones activas, lo cual verifica que la plataforma de respuesta opera con sus recursos bajo control mientras la medición se ejecuta.

Figura 34

*Estado operativo del servidor de la plataforma de respuesta*

![](data:image/png;base64...)

*Nota*. Tablero de estado del servidor de la plataforma de respuesta con la utilización de recursos, los clientes conectados y las organizaciones activas.

**Reporte consolidado de indicadores**

La séptima verificación presenta el reporte de indicadores que el laboratorio genera al cierre de los escenarios, el cual la Figura 35 muestra con su estructura en formato JSON. El reporte registra la ejecución de 10 escenarios, 46 ataques contra los señuelos, 1.758 solicitudes atendidas por la API, 8 conexiones capturadas por el honeypot SSH y 8.875 solicitudes del portal, junto con el método de medición del tiempo medio de detección a partir de eventos reales de los servicios señuelo.

Figura 35

*Reporte consolidado de indicadores*

*![](data:image/png;base64...)*

*Nota*. Reporte de indicadores con la ejecución de los escenarios, los registros de los señuelos y el método de medición del tiempo medio de detección.

El reporte consolida el tiempo medio de detección con un promedio de 41,598 segundos sobre 9 mediciones, con un mínimo de 0,141 segundos y un máximo de 260,108 segundos. El detalle por escenario muestra que 7 de las 9 mediciones registran tiempos inferiores a un minuto, lo cual indica que la detección opera en el orden de los segundos para la mayor parte de las técnicas ejercidas, mientras que los dos escenarios de mayor duración corresponden a la inyección SQL y a la fuerza bruta SSH.

**Cobertura del marco de comportamiento adversario**

La octava verificación presenta el reporte de cobertura sobre la matriz MITRE ATT&CK Enterprise, el cual la Figura 36 muestra con la relación entre los escenarios y las técnicas. El reporte registra 17 técnicas implementadas en los escenarios y 10 técnicas efectivamente detectadas, distribuidas en 6 tácticas que comprenden reconocimiento, acceso a credenciales, acceso inicial, ejecución, comando y control y exfiltración, con una correspondencia directa entre cada escenario y su técnica.

Figura 36

*Reporte de cobertura de técnicas de MITRE ATT&CK*

*![](data:image/png;base64...)*

*Nota*. Reporte de cobertura MITRE ATT&CK Enterprise con las técnicas implementadas, las técnicas detectadas y su distribución por táctica.

**Correspondencia normativa**

La novena verificación presenta el reporte de correspondencia normativa, el cual la Figura 37 muestra con la documentación de las fases del ciclo de incidentes de ISO/IEC 27035. El reporte registra para cada fase los componentes del laboratorio que la sustentan, entre los que figuran la plataforma de monitoreo preconfigurada, las plantillas de gestión de casos, los flujos de orquestación, las reglas personalizadas del motor de detección y los servicios señuelo instrumentados, lo cual verifica que la operación se apoya en la totalidad del ciclo normativo.

Figura 37

*Reporte de correspondencia con el ciclo de incidentes de ISO/IEC 27035*

*![](data:image/png;base64...)*

*Nota*. Reporte de correspondencia normativa con los componentes del laboratorio que sustentan cada fase del ciclo de incidentes de ISO/IEC 27035.

**Lecciones aprendidas**

La medición de la fase aporta tres lecciones aprendidas que el diseño metodológico incorpora al ciclo de mejora continua. La primera lección consiste en que la detección en el punto de origen, con la clasificación de la técnica incorporada desde la captura, reduce el tiempo de detección a segundos en la mayor parte de los escenarios, lo cual confirma el valor de la instrumentación del señuelo. La segunda lección consiste en que la orquestación automatizada del paso de alerta a caso elimina la intervención manual del operador y conserva la trazabilidad del incidente desde su origen. La tercera lección consiste en que la consolidación de los indicadores en tableros y reportes estructurados permite repetir la medición en cada ciclo y orientar el rediseño del señuelo con datos.

Estas lecciones se incorporan al bucle de retroalimentación que el diseño establece entre la medición y el diseño del señuelo, de modo que cada ciclo de operación alimenta el siguiente con la evidencia acumulada. Con la medición y las lecciones aprendidas verificadas, la implementación continúa con la prueba controlada de extremo a extremo, en la cual la cadena completa se ejerce en una secuencia integrada.

**Cierre de la fase**

La verificación de la fase confirma que la medición del impacto opera sobre indicadores trazables, con un tiempo medio de detección en el orden de los segundos para la mayor parte de los escenarios, una cobertura de detección sobre diez técnicas de seis tácticas y una correspondencia documentada con el ciclo de incidentes de ISO/IEC 27035. Este resultado verifica las actividades que el diseño metodológico asigna a la fase y cierra el ciclo de la metodología con la evidencia que la mejora continua requiere.

### 4.3.10. Prueba controlada de extremo a extremo

La verificación de la primera instanciación concluye con una prueba controlada de extremo a extremo, que ejerce la cadena completa de la metodología en una secuencia integrada: interacción con el señuelo, captura del evento, enriquecimiento y custodia de la evidencia, correlación con la gestión de incidentes y medición del indicador resultante. La prueba se etiqueta como evento sintético de prueba, dado que la interacción se genera de manera controlada dentro del entorno experimental con el propósito específico de demostrar la operación de la cadena.

*[Pendiente de evidencia: secuencia de capturas CAP-E2E con la interacción, el evento capturado, el caso correlacionado y el indicador medido. Fuente prevista: captura N.º 6 del checklist de evidencia del apartado 4.4.]*

**Figura X**

*Secuencia de la prueba controlada de extremo a extremo*

*[Pendiente: figura con la secuencia CAP-E2E.]*

*Nota.* *[Pendiente: nota de figura con la descripción de la secuencia y su etiqueta de evento sintético de prueba.]*

### 4.3.11. Matriz consolidada de trazabilidad

La matriz consolidada de trazabilidad relaciona cada elemento del diseño metodológico con su implementación, su evidencia y el apartado que la documenta, cerrando la verificación de la primera instanciación.

*[Pendiente de evidencia: tabla consolidada diseño → implementación → evidencia → apartado. Fuente prevista: captura N.º 7 del checklist de evidencia del apartado 4.4.]*

**Tabla X**

*Matriz consolidada de trazabilidad de la primera instanciación*

*[Pendiente: tabla consolidada.]*

*Nota.* *[Pendiente.]*

### 4.3.12. Síntesis de la primera instanciación

La primera instanciación verifica que las catorce categorías funcionales del diseño quedan materializadas en la práctica, con evidencia de operación en las cinco fases de la metodología, de la prueba controlada de extremo a extremo y de la matriz consolidada de trazabilidad. Esta verificación de componentes constituye la base sobre la cual el segundo prototipo evalúa el efecto de la metodología en los indicadores de gestión de incidentes.

*[Pendiente de redacción final: cierre con los conteos de componentes verificados al completar la matriz del 4.3.11.]*

### 4.3.13 Segunda instanciación: adaptación del prototipo al contexto SIN

Los apartados 4.3.1 a 4.3.12 documentaron la primera instanciación de la metodología en un entorno controlado construido sobre la base de una entidad homologada del rubro de servicios fiscales digitales, con el propósito de verificar que las catorce categorías funcionales del diseño quedan materializadas en la práctica. El presente apartado documenta la segunda instanciación, que replica la misma arquitectura adaptando el señuelo al contexto de un servicio de impuestos nacionales. La medición del efecto de la metodología sobre este segundo prototipo, mediante dos iteraciones de operación (preprueba y posprueba) conforme al diseño pre-experimental declarado en el apartado 3.2, se presenta en el apartado 4.4. La distinción entre la verificación de componentes y la validación del efecto preserva el carácter transferible de la metodología, dado que la operación de las categorías funcionales no depende de la marca ni del contexto institucional del señuelo.

El alcance de la segunda instanciación comprende la adaptación del señuelo al contexto del Servicio de Impuestos Nacionales de Bolivia y la verificación de las fases de despliegue aislado, captura, custodia y correlación en el segundo entorno.

El segundo prototipo replica la arquitectura del primero adaptando el contenido y la identidad visual del señuelo al contexto de un portal tributario nacional. La equivalencia entre ambos entornos se resume en la Tabla X, la cual muestra que la única diferencia sustantiva reside en el contenido del señuelo y la denominación de los artefactos del laboratorio.

**Tabla X**

*Equivalencia entre el prototipo I y el prototipo II*

| Elemento | Prototipo I (apartado 4.3) | Prototipo II (apartados 4.3.13 a 4.3.16) |
| --- | --- | --- |
| Denominación del laboratorio | TaxFisco Research Lab | SIN Research Lab *[pendiente: captura]* |
| Redes | taxfisco-dmz, taxfisco-honeypot, taxfisco-ids, taxfisco-soc | sin-dmz, sin-honeypot, sin-ids, sin-soc *[pendiente: captura de `docker network ls`]* |
| Imágenes de señuelo | taxfisco/decoy-portal, taxfisco/decoy-api | sin/decoy-portal, sin/decoy-api *[pendiente: captura de `docker images`]* |
| Servicios Docker Compose | 25 | 25 idénticos *[pendiente: captura de `docker compose config --services`]* |
| Contenido del señuelo | Entidad homologada | Portal tributario nacional (contexto SIN) *[pendiente: capturas del portal]* |
| Rol en la tesis | Verificación de componentes (OE3) | Validación con iteraciones (OE4) |

*Nota.* La tabla relaciona los elementos de infraestructura de ambos prototipos, con remisión a la evidencia de captura que respalda cada elemento del segundo prototipo. La equivalencia de arquitectura sostiene el carácter transferible de la metodología.

### 4.3.14 Verificación del aislamiento y del despliegue

Esta verificación comprueba que el segundo prototipo se despliega en el entorno aislado y que el señuelo resulta alcanzable únicamente desde las redes permitidas, condición que la metodología establece para la fase de despliegue aislado. La comprobación se realiza con la inspección de las cuatro redes del laboratorio y la revisión de las reglas de segmentación.

*[Pendiente de evidencia: capturas de la inspección de redes sin-* y de la verificación de aislamiento. Fuente prevista: capturas N.º 1 y N.º 5 del checklist de evidencia.]*

**Figura X**

*Arquitectura de redes y verificación de aislamiento del segundo prototipo*

*[Pendiente: figura.]*

### 4.3.15 Verificación de captura, custodia y correlación

Esta verificación comprueba que la interacción con el señuelo del segundo prototipo genera eventos capturados, con enriquecimiento, custodia de la evidencia y correlación con la gestión de incidentes, en correspondencia con las fases tres y cuatro de la metodología.

*[Pendiente de evidencia: capturas de eventos del señuelo SIN en el SIEM, del caso correlacionado y de la evidencia con hash de integridad. Fuente prevista: evidencias de la iteración 1.]*

**Figura X**

*Captura, custodia y correlación de eventos del segundo prototipo*

*[Pendiente: figura.]*

### 4.3.16 Síntesis de la implementación

La implementación de la metodología queda materializada en dos instanciaciones con arquitectura equivalente, la primera orientada a la verificación de las catorce categorías funcionales y la segunda adaptada al contexto de un servicio de impuestos nacionales, con verificación de aislamiento, captura, custodia y correlación. Sobre esta implementación, el apartado 4.4 presenta los resultados de la medición del impacto mediante dos iteraciones de operación.

*[Pendiente de redacción final: cierre con el conteo de funciones verificadas en el segundo prototipo al completar las evidencias pendientes.]*

## 4.4 Resultados

### 4.4.1 Diseño de la comparación preprueba-posprueba

La medición del impacto sigue el diseño pre-experimental de preprueba y posprueba sobre un mismo grupo declarado en el apartado 3.2. La preprueba corresponde a la primera iteración de operación del segundo prototipo y establece la línea base de los indicadores, mientras que la posprueba corresponde a la segunda iteración, ejecutada tras aplicar las mejoras derivadas de las lecciones aprendidas. La comparación se realiza escenario por escenario sobre los mismos escenarios de la campaña de ataque y con los mismos criterios de medición, de modo que las dos muestras resultan pareadas.

*[Pendiente de evidencia: tabla de condiciones invariantes entre iteraciones (escenarios, criterios de medición, invariantes de entorno).]*

**Tabla X**

*Condiciones invariantes entre la iteración 1 y la iteración 2*

*[Pendiente: tabla.]*

### 4.4.2 Medición de la iteración 1 (preprueba)

La primera iteración de la medición constituye la preprueba del diseño pre-experimental y establece la línea base de los indicadores sobre el segundo prototipo. La campaña de escenarios de ataque se ejecuta sobre el laboratorio en contexto SIN y el reporte de indicadores consolida los valores medidos con trazabilidad hasta el escenario y el evento que los origina.

*[Pendiente de evidencia: reporte consolidado de indicadores de la iteración 1 con el MTTD por escenario y la cobertura MITRE ATT&CK. Fuente prevista: captura N.º 8 del checklist de evidencia.]*

**Figura X**

*Reporte de indicadores de la iteración 1*

*[Pendiente: figura.]*

### 4.4.3 Análisis de la iteración 1 y lecciones aprendidas

El análisis de la línea base examina la distribución del tiempo medio de detección por escenario, los escenarios sin detección en el señuelo y las brechas de cobertura del marco de comportamiento adversario. Sobre este análisis se documentan las lecciones aprendidas del ciclo, cada una con su hallazgo, su causa raíz y su evidencia, conforme al ciclo de retroalimentación que la metodología establece entre la medición y el diseño del señuelo.

*[Pendiente de evidencia: tabla de lecciones aprendidas L1–Ln de la iteración 1 con sus causas raíz y los commits que las documentan.]*

**Tabla X**

*Lecciones aprendidas de la iteración 1*

*[Pendiente: tabla.]*

### 4.4.4 Medición de la iteración 2 (posprueba)

La segunda iteración de la medición constituye la posprueba del diseño pre-experimental y se ejecuta tras aplicar las mejoras derivadas de las lecciones aprendidas de la iteración 1. Las mejoras se aplican de modo que cada una cite su lección de origen y quede registrada en el control de versiones del laboratorio, de manera que la posprueba mide el efecto de los cambios sobre los mismos escenarios y los mismos criterios de medición de la preprueba.

*[Pendiente de evidencia: registro de mejoras aplicadas con su lección de origen, y reporte consolidado de indicadores de la iteración 2. Fuente prevista: captura N.º 9 del checklist de evidencia.]*

**Figura X**

*Reporte de indicadores de la iteración 2*

*[Pendiente: figura.]*

### 4.4.5 Comparación de iteraciones y prueba de hipótesis pareada

La comparación entre la preprueba y la posprueba se realiza escenario por escenario sobre los indicadores medidos en ambas iteraciones. La prueba de hipótesis pareada se aplica sobre las diferencias de tiempo medio de detección entre iteraciones, con el nivel de significancia establecido para el estudio, de modo que la conclusión sobre la mejora se sustenta en evidencia estadística y no en la observación aislada de valores.

*[Pendiente de evidencia: tabla comparativa iteración 1 versus iteración 2 por escenario, con el estadístico y el valor p de la prueba pareada. Fuente prevista: captura N.º 10 del checklist de evidencia.]*

**Tabla X**

*Comparación de indicadores entre la iteración 1 y la iteración 2*

*[Pendiente: tabla.]*

### 4.4.6 Evaluación de la hipótesis y de las metas

El resultado de la comparación alimenta la evaluación de la hipótesis de investigación y el cálculo de los índices de impacto que el diseño metodológico compromete. Los valores medidos se confrontan con las metas definidas en la operacionalización de la variable dependiente, de modo que la aceptación o el rechazo de la hipótesis se documenta con trazabilidad hasta la evidencia de las dos iteraciones.

*[Pendiente de evidencia: cálculo de los índices IIAM e IMGI con sus fórmulas y valores medidos, y confrontación con las metas de la Tabla 2 del apartado 1.6.]*

**Tabla X**

*Cumplimiento de metas de la variable dependiente*

*[Pendiente: tabla.]*

### 4.4.7 Síntesis de los resultados

La síntesis de los resultados resume lo que la operación de dos iteraciones demuestra sobre el efecto de la metodología en los indicadores de gestión de incidentes, con las limitaciones propias del diseño pre-experimental y de la muestra por conveniencia, y con la valoración de la transferibilidad de la metodología a otros contextos institucionales.

*[Pendiente de redacción final: síntesis con los resultados de la prueba pareada y el cumplimiento de metas.]*

# Capítulo V: Conclusiones y Recomendaciones de la Investigación

## 5.1 Conclusiones

*[Una conclusión por cada objetivo específico + una conclusión general. Deben derivarse directamente de los resultados del Marco Práctico. No introduzca información nueva.]*

Con respecto al objetivo específico 1: se concluye que [conclusión fundamentada en los resultados obtenidos].

Con respecto al objetivo específico 2: se concluye que [conclusión fundamentada en los resultados obtenidos].

Con respecto al objetivo específico 3: se concluye que [conclusión fundamentada en los resultados obtenidos].

Con respecto al objetivo específico 4: se concluye que [conclusión fundamentada en los resultados de la validación con iteraciones del apartado 4.4].

De manera general, la investigación permitió [conclusión global que responde al objetivo general y al problema planteado].

## 5.2 Recomendaciones

*[Proponga recomendaciones concretas, orientadas a actores específicos y fundamentadas en sus conclusiones.]*

1. Se recomienda a [actor/institución] que [acción concreta derivada de los hallazgos].
2. Para futuras investigaciones, se sugiere [línea de investigación que amplíe o profundice este trabajo].
3. Se recomienda a los administradores del [sistema/área] implementar [mejora específica].

# Anexos

*[Incluya material de soporte referenciado en el cuerpo del documento. Numere cada anexo con letras mayúsculas (Anexo A, Anexo B…).]*

## Anexo A: [Nombre del Primer Anexo]

*[Inserte el contenido del Anexo A (ej. formulario, tabla de datos, capturas de pantalla adicionales, código fuente, etc.).]*

## Anexo B: [Nombre del Segundo Anexo]

*[Inserte el contenido del Anexo B.]*

# Glosario

*[Defina los términos técnicos especializados utilizados en el documento. Ordénelos alfabéticamente.]*

**API (Application Programming Interface):** Conjunto de definiciones y protocolos que permiten la comunicación entre aplicaciones de software.

**[Término]:** [Definición del término en el contexto de su investigación].

# Apéndice

*[Incluya material elaborado por usted mismo que complementa la investigación pero que resultaría demasiado extenso en el cuerpo del texto (instrumentos de recolección, consentimientos informados, diagramas extensos, etc.).]*

## Apéndice A: Instrumento de Recolección de Datos

***Cuestionario / Guía de Entrevista / Lista de Cotejo***

*[Pegue aquí el instrumento tal como fue aplicado a los participantes.]*

## Apéndice B: Consentimiento Informado

Estimado/a participante:

Le informamos que su participación en este estudio es voluntaria y confidencial. Los datos recolectados serán utilizados únicamente con fines académicos y no será posible identificarle en ninguna publicación.

Al firmar, usted acepta participar voluntariamente en la investigación.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Firma del/la participante

# Bibliografía

**Formato APA 7.ª edición**

*[Liste TODAS las fuentes citadas, en orden ALFABÉTICO por apellido del primer autor. Use sangría francesa (primera línea a la izquierda, segunda línea y siguientes con sangría de 1.25 cm). Ejemplos:]*

Apellido, A. A., & Apellido, B. B. (2020). Título del libro en cursiva: Subtítulo si lo tiene (2.ª ed.). Editorial. https://doi.org/10.xxxxx/yyyyy

Apellido, C. C. (2021). Título del artículo. Nombre de la Revista en Cursiva, 15(3), 120–145. https://doi.org/10.xxxxx/yyyyy

Apellido, D. D. (2023). Título de la tesis en cursiva [Tesis de maestría, Universidad Mayor de San Andrés — Postgrado en Informática]. Repositorio Institucional UMSA. https://repositorio.umsa.bo/handle/xxxxx

Apellido, E. E. (2022, 15 de marzo). Título de la página web en cursiva. Nombre del Sitio. https://www.sitio.org/pagina

Asamblea Legislativa Plurinacional de Bolivia. (año). Ley N.° xxx: Nombre de la Ley. Gaceta Oficial del Estado Plurinacional de Bolivia.

Institución u Organización. (año). Nombre del documento técnico en cursiva (N.° de informe). Editorial o URL. https://www.url.org