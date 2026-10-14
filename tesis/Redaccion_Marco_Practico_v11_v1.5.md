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

[Dedicatoria ii](#_Toc242091167)

[Agradecimientos iii](#_Toc242091168)

[Resumen iv](#_Toc242091169)

[Índice v](#_Toc242091170)

[Índice de Tablas, Cuadros y Gráficos ix](#_Toc242091171)

[Introducción 1](#_Toc242091172)

[Capítulo I: Aspectos Generales 2](#_Toc242091173)

[1.1 Antecedentes 2](#_Toc242091174)

[1.2 Planteamiento del Problema 3](#_Toc242091175)

[1.2.1 Formulación del Problema de Investigación 4](#_Toc242091176)

[1.3 Objetivo General y Específicos de la Investigación 4](#_Toc242091177)

[1.3.1 Objetivo General 4](#_Toc242091178)

[1.3.2 Objetivos Específicos 4](#_Toc242091179)

[1.4 Resultados de la Investigación 4](#_Toc242091180)

[1.5 Planteamiento de la Hipótesis 5](#_Toc242091181)

[1.6 Operacionalización de Variables 6](#_Toc242091182)

[Capítulo II: Marco Teórico 10](#_Toc242091183)

[2.1 Marco Conceptual 10](#_Toc242091184)

[2.1.1 Detección y gestión de eventos de seguridad 10](#_Toc242091185)

[2.1.1.1 Evento e incidente de seguridad 10](#_Toc242091186)

[2.1.1.2 Ciclo de vida del incidente 11](#_Toc242091187)

[2.1.1.3 Indicadores MTTD y MTTR 12](#_Toc242091188)

[2.1.1.4 Evidencia forense y cadena de custodia 13](#_Toc242091189)

[2.1.2 El servicio fiscal digital como sector de aplicación 13](#_Toc242091190)

[2.1.2.1 Definición de servicio fiscal digital 14](#_Toc242091191)

[2.1.2.2 Tributaria 3.0 14](#_Toc242091192)

[2.1.2.3 Modelo de Madurez de la Transformación Digital 15](#_Toc242091193)

[2.1.2.4 Contexto institucional boliviano 16](#_Toc242091194)

[2.1.2.5 Índice de madurez en ciberseguridad fiscal 17](#_Toc242091195)

[2.1.3 Conceptos operativos de detección 18](#_Toc242091196)

[2.1.3.1 Marco MITRE ATT&CK 18](#_Toc242091197)

[2.1.3.2 Ciberdecepción 19](#_Toc242091198)

[2.1.3.3 Honeypots 20](#_Toc242091199)

[2.1.3.4 Honeytokens, honeynets y sensores de engaño 21](#_Toc242091200)

[2.1.3.5 Detección, evidencia y mejora continua 22](#_Toc242091201)

[2.2 Marco Referencial 22](#_Toc242091202)

[2.2.1 Teoría general de riesgo y resiliencia en ciberseguridad 23](#_Toc242091203)

[2.2.1.1 Origen y fundamento de la teoría 23](#_Toc242091204)

[2.2.1.2 Ciclo de gestión del riesgo 24](#_Toc242091205)

[2.2.1.3 Capacidades de la resiliencia organizacional 25](#_Toc242091206)

[2.2.1.4 Articulación riesgo–resiliencia 26](#_Toc242091207)

[2.2.1.5 Criterios de evaluación teórica 26](#_Toc242091208)

[2.2.2 Teoría sustantiva de modelos de madurez en ciberseguridad tributaria 28](#_Toc242091209)

[2.2.2.1 Fundamento de los modelos de madurez 28](#_Toc242091210)

[2.3 Marco Legal 29](#_Toc242091211)

[Capítulo III: Metodología de la Investigación 30](#_Toc242091212)

[3.1 Métodos de Investigación 30](#_Toc242091213)

[3.2 Tipo de Investigación 31](#_Toc242091214)

[3.3 Universo o Población de Estudio 33](#_Toc242091215)

[3.3.1 Determinación y Elección de la Muestra 34](#_Toc242091216)

[3.4 Sujetos Vinculados a la Población 36](#_Toc242091217)

[3.5 Fuentes y Diseño de los Instrumentos de Relevamiento de Información 37](#_Toc242091218)

[3.5.1 Fuentes de la Investigación 37](#_Toc242091219)

[3.5.2 Diseño de los Instrumentos de Relevamiento de Información 40](#_Toc242091220)

[3.5.2.1 Descripción del Instrumento de Diagnóstico 41](#_Toc242091221)

[3.5.2.2 Validez del Instrumento 48](#_Toc242091222)

[3.5.2.3 Confiabilidad del Instrumento 56](#_Toc242091223)

[3.6 Procesamiento y Análisis de la Información 63](#_Toc242091224)

[Capítulo IV: Marco Práctico 64](#_Toc242091225)

[4.1 Análisis de la situación actual 64](#_Toc242091226)

[4.1.1 Análisis de la normativa 64](#_Toc242091227)

[4.1.1.1 Criterio de selección de las normas 65](#_Toc242091228)

[4.1.1.2 Normas de gestión de incidentes 66](#_Toc242091229)

[4.1.1.3 Norma marco de seguridad de la información 68](#_Toc242091230)

[4.1.1.4 Normas de evidencia digital y forense 69](#_Toc242091231)

[4.1.1.5 Norma de gestión de riesgos 70](#_Toc242091232)

[4.1.1.6 Marco de comportamiento adversario 70](#_Toc242091233)

[4.1.1.7 Benchmarks operativos y modelos de madurez 71](#_Toc242091234)

[4.1.2 Aplicación del instrumento 74](#_Toc242091235)

[4.1.2.1 Aplicación a la muestra de diagnóstico 75](#_Toc242091236)

[4.1.2.2 Confiabilidad del instrumento 76](#_Toc242091237)

[4.1.2.3 Resultados por instrumento 77](#_Toc242091238)

[4.1.2.4 Resultados por grupo temático 80](#_Toc242091239)

[4.1.2.5 Resultado global de madurez 82](#_Toc242091240)

[4.1.3 Diagnóstico situacional 83](#_Toc242091241)

[4.1.3.1 Brechas en gestión de incidentes 84](#_Toc242091242)

[4.1.3.2 Brechas en evidencias y respaldo 85](#_Toc242091243)

[4.1.3.3 Brechas en controles técnicos 86](#_Toc242091244)

[4.1.3.4 Brechas en gestión organizacional y mejora 87](#_Toc242091245)

[4.1.3.5 Caracterización del estado actual 88](#_Toc242091246)

[4.1.3.6 Matriz de trazabilidad 90](#_Toc242091247)

[4.2 Diseño de la metodología de honeypot para la gestión de incidentes en los servicios fiscales 93](#_Toc242091248)

[4.2.1 Fundamentación del diseño metodológico 93](#_Toc242091249)

[4.2.1.1 Principios de diseño de la metodología Honeypot 94](#_Toc242091250)

[4.2.1.2 Atención integral de los hallazgos del diagnóstico 98](#_Toc242091251)

[4.2.1.3 Decisiones de diseño asumidas por la metodología Honeypot 105](#_Toc242091252)

[4.2.2 Arquitectura general de la metodología 107](#_Toc242091253)

[4.2.2.1 Estructura secuencial de las cinco fases y sus bucles de retroalimentación 109](#_Toc242091254)

[4.2.2.2 Planos transversales de la metodología y categorías funcionales de tecnología 110](#_Toc242091255)

[4.2.2.3 Trazabilidad metodológica de las cinco fases 113](#_Toc242091256)

[4.2.2.4 Prerrequisitos de la organización y transferibilidad de la metodología 115](#_Toc242091257)

[4.2.2.5 Justificación metodológica de las cinco actividades por fase 117](#_Toc242091258)

[4.2.3 Fase 1. Diseño del señuelo 122](#_Toc242091259)

[4.2.4 Fase 2. Despliegue aislado 128](#_Toc242091260)

[4.2.5 Fase 3. Captura, enriquecimiento y custodia 132](#_Toc242091261)

[4.2.6 Fase 4. Correlación con gestión de incidentes 137](#_Toc242091262)

[4.2.7 Fase 5. Medición de impacto y lecciones aprendidas 142](#_Toc242091263)

[2.8 Síntesis del diseño de la metodología Honeypot 148](#_Toc242091264)

[4.3 Implementación de la metodología de honeypot para la gestión de incidentes 149](#_Toc242091265)

[4.3.1 Propósito, alcance y línea base 150](#_Toc242091266)

[4.3.2 Entorno controlado de implementación 151](#_Toc242091267)

[4.3.3 Plataforma tecnológica del prototipo 154](#_Toc242091268)

[4.3.4 Matriz de trabajo y criterios de verificación 159](#_Toc242091269)

[4.3.5. Fase 1. Diseño del señuelo 162](#_Toc242091270)

[4.3.6. Fase 2. Despliegue aislado 170](#_Toc242091271)

[4.3.7. Fase 3. Captura, enriquecimiento y custodia 181](#_Toc242091272)

[4.3.8. Fase 4. Correlación con gestión de incidentes 196](#_Toc242091273)

[4.3.9. Fase 5. Medición y lecciones aprendidas 201](#_Toc242091274)

[Capítulo V: Conclusiones y Recomendaciones de la Investigación 213](#_Toc242091275)

[5.1 Conclusiones 213](#_Toc242091276)

[5.2 Recomendaciones 213](#_Toc242091277)

[Anexos 215](#_Toc242091278)

[Anexo A: [Nombre del Primer Anexo] 215](#_Toc242091279)

[Anexo B: [Nombre del Segundo Anexo] 215](#_Toc242091280)

[Glosario 216](#_Toc242091281)

[Apéndice 217](#_Toc242091282)

[Apéndice A: Instrumento de Recolección de Datos 217](#_Toc242091283)

[Apéndice B: Consentimiento Informado 217](#_Toc242091284)

[Bibliografía 218](#_Toc242091285)

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

*Nota.* Cálculo del porcentaje sobre el promedio de los puntajes individuales de los 30 respondentes para cada instrumento. Niveles de madurez según los cortes definidos en la ficha técnica del instrumento: Inicial de 0 % a menos de 26 %, Básico de 26 % a menos de 51 %, Gestionado de 51 % a menos de 76 % y Optimizado de 76 % a 100 %. Elaboración propia, 2026.

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

### 4.3.5 Implementación del prototipo I (entidad homologada)

#### 4.3.5.1 Fase 1. Diseño del señuelo

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

#### 4.3.5.2 Fase 2. Despliegue aislado

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

#### 4.3.5.3 Fase 3. Captura, enriquecimiento y custodia

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

#### 4.3.5.4 Fase 4. Correlación con gestión de incidentes

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

#### 4.3.5.5 Fase 5. Medición y lecciones aprendidas

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

### 4.3.6 Segundo prototipo: adaptación al contexto del SIN e iteraciones de mejora

Los apartados 4.3.5.1 a 4.3.5.8 documentan la primera implementación de la metodología, construida sobre una entidad homologada del rubro de servicios fiscales digitales y orientada a comprobar que las catorce categorías funcionales del diseño se materializan en la práctica. El presente apartado registra la segunda implementación, que conserva la arquitectura del primer prototipo y adapta el señuelo al contexto de un servicio nacional de impuestos, con el fin de recorrer las cinco fases de la metodología bajo la misma estructura de verificación.

La segunda implementación incorpora un elemento que la primera no contempla, pues organiza la operación en dos iteraciones consecutivas que se ajustan al esquema de comparación antes y después declarado en el apartado 3.2. La primera iteración establece la línea base de los indicadores de detección y la segunda mide el efecto de las mejoras que se desprenden de las lecciones aprendidas durante esa línea base. El apartado 4.3.6.6 desarrolla ese ciclo de iteraciones, mientras que el apartado 4.4 presenta los resultados de ambas mediciones y su comparación. Cada fase de este apartado documenta la primera ejecución, salvo donde se indica expresamente que la evidencia procede de la segunda.

La separación entre verificar componentes y medir el efecto responde a una razón práctica, dado que la operación de las categorías funcionales no depende ni de la marca del señuelo ni de su contexto institucional, por lo que ambas implementaciones someten a prueba la misma arquitectura. Lo que distingue a la segunda implementación es que somete el conjunto de categorías funcionales a dos ciclos de operación medidos, con lo cual los datos que se recogen en dos oportunidades permiten contrastar la estabilidad del comportamiento del señuelo.

El alcance de la segunda implementación comprende la adaptación del señuelo al contexto del Servicio de Impuestos Nacionales de Bolivia y la verificación de las cinco fases en el segundo entorno, procesos que se documentan de manera compacta con remisión a la evidencia que los respalda.

#### 4.3.6.1 Adaptación del señuelo y equivalencia entre prototipos

La adaptación del señuelo al segundo contexto institucional conserva la arquitectura del primer prototipo, de modo que ambas implementaciones comparten el mismo armazón tecnológico y difieren únicamente en el contenido que el ejercicio admite. La Tabla 5 contrasta los elementos de infraestructura de los dos prototipos y muestra, en cada fila, el elemento comparado y su denominación en cada implementación. Esa disposición permite comprobar que la equivalencia se sostiene en los planos que la metodología declara comunes, al tiempo que deja explícitos los puntos en los que el segundo prototipo se aparta del primero.

Tabla 5 *Equivalencia entre el prototipo I y el prototipo II*

|  |  |  |
| --- | --- | --- |
| **Elemento** | **Prototipo I (apartado 4.3.5)** | **Prototipo II (apartado 4.3.6)** |
| Denominación del laboratorio | TaxFisco Research Lab | SIN Research Lab |
| Redes | taxfisco-dmz, taxfisco-honeypot, taxfisco-ids, taxfisco-soc | sin-dmz, sin-honeypot y sin-soc, con sin-ids |
| Imágenes de señuelo | taxfisco/decoy-portal, taxfisco/decoy-api | sin/decoy-portal, sin/decoy-api, sin/cortex y sin/wazuh-indexer |
| Servicios Docker Compose | 25 | 25 idénticos |
| Contenido del señuelo | Entidad homologada | Portal tributario nacional (contexto SIN) |
| Rol en la tesis | Verificación de componentes (OE3) | Validación con iteraciones (OE4) |

*Nota.* La tabla relaciona los elementos de infraestructura de ambos prototipos, con remisión a la evidencia de captura que respalda cada elemento del segundo prototipo. La equivalencia de arquitectura sostiene el carácter transferible de la metodología. La diferencia en el número de redes no obedece al diseño, pues el segmento sin-ids permanece declarado en la composición mientras los servicios de detección de red operan en modo host, de modo que en ejecución existen tres segmentos y la verificación de aislamiento se practica sobre ellos. Esa circunstancia tampoco altera la equivalencia de las categorías funcionales, que no dependen del número de segmentos.

#### 4.3.6.2 Fase 1. Diseño del señuelo SIN

La primera fase del segundo prototipo adapta el diseño del señuelo al contexto del Servicio de Impuestos Nacionales de Bolivia, replicando la experiencia de un portal tributario nacional en sus funciones de consulta, declaración y autenticación. El señuelo conserva los mecanismos de detección instrumentados en el primer prototipo, de modo que la modificación se limita al contenido, la identidad visual y los datos simulados, todos coherentes con el contexto tributario boliviano y ajenos a los datos reales de contribuyentes. La configuración técnica de esa instrumentación se describe en el apartado 4.3.5.1, pues los mecanismos de detección que sustentan los dos prototipos son idénticos y no requieren adaptación adicional.

El señuelo reproduce el recorrido de un contribuyente que accede al portal, se autentica, completa la verificación en dos pasos e ingresa al panel. La Figura 39 presenta la pantalla de inicio del portal, con la identidad institucional del servicio y el acceso por número de identificación tributaria.

Figura 39 *Pantalla de inicio del señuelo del segundo prototipo: portal tributario nacional*

![](data:image/png;base64...)

*Nota.* Captura directa del portal del señuelo, la pantalla presenta la identidad del servicio tributario y el punto de entrada al acceso, sin ningún dato real de contribuyentes.

El acceso se realiza mediante número de identificación tributaria, con la credencial de verificación en dos pasos que reproduce el procedimiento de autenticación del servicio real. El segundo factor se solicita una vez validada la identificación, de modo que un intento contrario queda registrado como un evento con la técnica asociada, tal como dispone la metodología para la fase de señalización del atacante.

Figura 40a*Solicitud del número de identificación tributaria en el acceso al señuelo*

![](data:image/png;base64...)

*Nota.* Captura directa del portal del señuelo en el paso de autenticación, el recorrido en dos pasos aporta dos puntos de señalización por intento fallido, lo que incrementa la probabilidad de detección de un ataque de fuerza bruta o de relleno de credenciales frente al señuelo del primer prototipo.

Figura 40b *Solicitud del segundo factor de verificación en el acceso al señuelo*

![](data:image/png;base64...)

*Nota*. Captura directa del segundo paso del acceso, donde el sistema solicita el código de verificación en dos pasos después de validar la identificación, este segundo factor aporta un punto de señalización adicional por intento, lo que incrementa la probabilidad de detección de un ataque de fuerza bruta o de relleno de credenciales frente al señuelo del primer prototipo.

Una vez superado el acceso, el contribuyente ingresa al panel e introduce en él los datos de la declaración, el panel ofrece las funciones de consulta y declaración exigidas por el diseño para replicar la superficie de ataque del servicio y cada petición se registra en el señuelo con su marca temporal, lo que constituye la fuente de eventos para el cálculo del tiempo medio de detección en la fase de medición.

Figura 41a *Formulario de declaración en el panel del señuelo del segundo prototipo*

![](data:image/png;base64...)

*Nota.* Captura directa del formulario de declaración, que reproduce la función de presentación de la declaración del servicio tributario. Cada petición atendida queda registrada por el señuelo como evento con instante de generación, fuente que la fase de medición utiliza para el cálculo del tiempo de detección.

Figura 41b *Panel principal del contribuyente en el señuelo del segundo prototipo*

![](data:image/png;base64...)

*Nota.* Captura directa del panel al que accede el contribuyente tras completar la autenticación, donde se muestran las funciones de consulta y declaración del servicio tributario. El acceso a este panel queda registrado con la técnica asociada al evento de autenticación.

El alcance del ejercicio se cierra con el perfil del atacante, que determina qué superficie ofrece el señuelo y qué técnicas puede ejecutar quien lo explora; el contenedor atacante incorpora desde el inicio de la campaña las diez herramientas habituales de reconocimiento y de explotación, con el escáner de red, la herramienta de fuerza bruta, el inyector de consultas, el escáner web, el cliente de acceso remoto y el resolvedor de nombres, entre otras.

Figura 41c

*Herramientas disponibles en el contenedor atacante durante la campaña*

![](data:image/png;base64...)

*Nota.* Relación de las herramientas disponibles en el contenedor atacante al inicio de la campaña; la comprobación se ejecuta sobre el propio contenedor y devuelve la ruta de cada herramienta, lo que documenta que el perfil está completo desde el comienzo y que ningún escenario depende de una herramienta ausente. Fuente: entorno de servicios, iteración 2.

#### 4.3.6.3 Fase 2. Despliegue aislado

La segunda fase verifica que el segundo prototipo se despliega en el entorno aislado y que el señuelo resulta alcanzable únicamente desde las redes permitidas, condición que la metodología establece para esta fase. La comprobación se practica sobre la inspección de los segmentos del laboratorio y sobre una prueba de alcanzabilidad ejecutada desde el contenedor atacante, de modo que la evidencia demuestra el aislamiento de la superficie expuesta respecto de la cadena de detección.

La Figura 42 presenta la relación de redes del laboratorio, en ejecución existen tres segmentos efectivos, entre los que figuran *sin-dmz*, que aloja el señuelo y la superficie expuesta; *sin-honeypot*, que aísla los emuladores de servicio; y *sin-soc*, que hospeda la cadena de detección, el correlacionador y las plataformas de gestión. La composición declara además un segmento *sin-ids* destinado a los sensores de red, aunque ese segmento no llega a instanciarse porque Suricata y Zeek operan en modo host y no precisan segmento propio. Esa diferencia entre lo declarado y lo ejecutado no altera la equivalencia de las categorías funcionales, que no dependen del número de segmentos.

Figura 42 *Segmentos de red en ejecución en el laboratorio del segundo prototipo*

![](data:image/png;base64...)

*Nota.* Registro de salida del listado de redes del laboratorio filtrado por el prefijo del segundo prototipo. Se observan los tres segmentos efectivamente instanciados. El segmento sin-ids figura declarado en la composición del laboratorio pero no en ejecución, dado que los servicios de detección de red operan en modo host. Fuente: Aislamiento de red, iteración 1.

La configuración de los dos segmentos que sostienen la separación aparece en las Figuras 43a y 43b; el segmento expuesto declara la dirección 10.20.0.0/24 con su puerta de enlace, y en él residen el señuelo y su superficie de servicios. El segmento de operaciones de seguridad declara la dirección 10.22.0.0/24 y aloja diecinueve contenedores, entre ellos la cadena de detección, el correlacionador y las plataformas de gestión.

Figura 43a

*Dirección y puerta de enlace del segmento expuesto que aloja el señuelo*

![](data:image/png;base64...)

*Nota.* Registro de salida de la inspección del segmento expuesto, que muestra su nombre, la dirección de red que declara y su puerta de enlace; en este segmento residen el señuelo, la interfaz de servicios y el emulador de acceso remoto. Fuente: Aislamiento de red, iteración 1.

Figura 43b

*Dirección, puerta de enlace y población del segmento de operaciones de seguridad*

![](data:image/png;base64...)

*Nota.* Registro de salida de la inspección del segmento de operaciones de seguridad, que muestra su nombre, la dirección de red que declara, su puerta de enlace y el número de contenedores conectados. En este segmento residen la cadena de detección, el correlacionador y las plataformas de gestión, ninguno de ellos alcanzable desde el segmento expuesto. Fuente: Aislamiento de red, iteración 1.

La segmentación efectiva se complementa con la verificación de que el señuelo resulta alcanzable desde el atacante, mientras que la red de operaciones no lo es, la Figura 44 presenta la prueba de aislamiento ejecutada desde el contenedor atacante, desde el que alcanza los servicios señuelo del segmento expuesto y obtiene respuesta de rechazo al intentar sondear la red de operaciones, lo que demuestra que la separación entre la superficie expuesta y la cadena de detección se sostiene en ejecución.

Figura 44 *Prueba de aislamiento ejecutada desde el atacante: alcanza el señuelo y no alcanza la red de operaciones*

![](data:image/png;base64...)

*Nota.* Registro de salida de la prueba de aislamiento de red desde el contenedor atacante, el atacante obtiene respuesta del señuelo en el segmento expuesto y no logra alcanzar los servicios de la red de operaciones, lo que verifica el aislamiento exigido por la fase.

#### 4.3.6.4 Fase 3. Captura, enriquecimiento y custodia

La tercera fase comprueba que la interacción con el señuelo del segundo prototipo genera eventos que la cadena de captura registra, enriquece con la clasificación de la técnica, custodia como evidencia y somete a un cálculo de integridad, en los mismos términos que la tercera fase del primer prototipo. La captura opera en dos niveles, pues los servicios que componen el señuelo registran por sí mismos la interacción y le asignan, en ese instante, la técnica correspondiente según el marco de comportamiento adversario, mientras que los sensores de red y el emulador de acceso remoto aportan registros independientes de esa misma actividad.

La Figura 45 presenta las alertas que la cadena de detección indexa en la plataforma de gestión, cada una de las cuales conserva su origen, la técnica asociada en el momento de la captura y su nivel de severidad. El instante de generación de cada alerta resulta determinante, pues constituye el punto de partida del cálculo del tiempo medio de detección que la fase de medición aplica sobre las alertas registradas.

Figura 45 *Alertas capturadas por la cadena de detección con su técnica y su origen*

![](data:image/png;base64...)

*Nota*. Registro de salida de las alertas indexadas por la plataforma de gestión, cada alerta conserva su origen, la técnica del marco de comportamiento adversario asociada en el momento de la captura y el instante de generación, que constituye el punto de partida del cálculo del tiempo medio de detección.

La segunda ejecución corrobora esa captura heterogénea con tres registros que muestran que cada escenario lo detecta un componente distinto de la cadena; uno de ellos lo detecta el emulador de acceso remoto, que registra dos conexiones consecutivas separadas por menos de un segundo, como se aprecia en la Figura 46a. Otro lo detecta el honeypot de ficheros, que registra un intento de acceso anónimo seguido del depósito de un fichero de prueba, como muestra la Figura 46b. El tercero lo detecta el sensor de red, que observa la exfiltración como un conjunto de consultas de nombres que transportan los fragmentos del dato, como se aprecia en la Figura 46c.

Figura 46a

*Conexiones capturadas por el emulador de acceso remoto*

![](data:image/png;base64...)

*Nota.* Registro de salida del emulador de acceso remoto en el que se observan dos conexiones consecutivas desde el atacante hacia el señuelo, con una diferencia inferior a un segundo entre ambas. Este componente aparece como fuente de detección en el detalle de la Figura 54. Fuente: Captura de eventos, iteración 2.

Figura 46b

*Depósito de un fichero de prueba registrado por el honeypot de ficheros*

*![](data:image/png;base64...)*

*Nota.* Registro de salida del honeypot de ficheros, que documenta un intento de acceso con credenciales anónimas seguido del envío de un fichero de prueba hacia el punto de carga del señuelo. Este componente aparece como fuente de detección en el detalle de la Figura 54. Fuente: Captura de eventos, iteración 2.

Figura 46c

*Consultas de nombres observadas por el sensor de red*

![](data:image/png;base64...)

*Nota.* Registro de salida del sensor de red en el que se observan las consultas de nombres que transportan los fragmentos del dato exfiltrado; el contenido viaja como registro de consulta hacia un nombre bajo control del atacante, de modo que la exfiltración resulta visible para la cadena de detección, aunque no se produzca por un canal propio del señuelo. Este componente aparece como fuente de detección en el detalle de la Figura 54. Fuente: Captura de eventos, iteración 2.

El enriquecimiento de esta segunda implementación se aplica en el momento de la captura, cuando cada evento se registra ya clasificado con su técnica del marco de comportamiento adversario, su nivel de amenaza y el contexto de la operación que lo origina. Esa clasificación operativa permite que la cadena de detección indexe el evento con campos consultables desde el primer momento, lo que sostiene tanto el cálculo del tiempo medio de detección de la fase de medición como el mapeo posterior con la gestión de incidentes.

La custodia de la evidencia se verifica mediante el sellado de los archivos del laboratorio con huella criptográfica, de modo que la integridad del conjunto pueda comprobarse después sin depender de la memoria del operador. La Figura 47 presenta el registro de custodia, en el que cada archivo figura con su huella SHA-256 y con el instante de sellado y cuyo listado documenta además el orden temporal de los eventos del laboratorio.

Figura 47 *Registro de custodia de la evidencia del segundo prototipo con huella SHA-256*

![](data:image/png;base64...)

*Nota.* Registro de salida de la cadena de custodia. El listado documenta la huella SHA-256 de los archivos de evidencia del laboratorio y la marca temporal del sellado, lo que permite verificar la integridad del conjunto y ordenar los eventos en el tiempo.

#### 4.3.6.5 Fase 4. Correlación con gestión de incidentes

La cuarta fase verifica que los eventos capturados se correlacionan con la gestión de incidentes, para lo cual clasifica cada evento según la técnica del comportamiento adversario y comprueba la disponibilidad del flujo de orquestación que los enlaza con la plataforma de gestión. El señuelo registra cada ataque con la técnica asociada, el nivel de amenaza y la clasificación de la información, de modo que cada evento queda clasificado en el momento de su captura.

La Figura 48 presenta ese registro de ataques, en el que se observa la correspondencia entre la actividad registrada y la técnica del marco de comportamiento adversario que la metodología exige para cada caso. Cada entrada conserva además la clasificación de información, lo que permite distinguir los registros de información sensible de los demás sin depender de una inspección posterior de los eventos.

Figura 48 *Registro de ataques al señuelo con su técnica, su táctica y su nivel de clasificación*

![](data:image/png;base64...)

*Nota.* Registro de salida de los ataques registrados por el señuelo, cada entrada conserva la técnica y la táctica del marco de comportamiento adversario, el nivel de severidad y la clasificación de información, lo que verifica la correlación del evento con la taxonomía de referencia.

El flujo de orquestación que enlaza la alerta con el gestor de incidentes se encuentra configurado y disponible, su definición constituye la evidencia de que la correlación entre ambos opera de forma automática en el entorno. La Figura 49 presenta ese flujo configurado, que recibe la alerta y ejecuta la acción que invoca la interfaz de la plataforma de gestión, sin que el operador intervenga en ninguna de las dos operaciones.

Figura 49 *Flujo de orquestación que enlaza la alerta con la gestión de incidentes*

![](data:image/png;base64...)

*Nota.* Registro de salida del flujo de orquestación configurado en la plataforma de respuesta, el flujo recibe la alerta y ejecuta la acción que invoca la interfaz de la plataforma de gestión de incidentes, lo que verifica que la correlación se ejecuta de forma automática y sin intervención del operador.

#### 4.3.6.6 Fase 5. Medición con iteraciones de mejora

La quinta fase comprueba si la metodología funciona, y para ello ejecuta el laboratorio dos veces en lugar de una, de manera que la primera opere sin cambios y sirva de línea base, mientras la segunda se aplica tras las correcciones que la primera reveló, lo que permite atribuir a estas el cambio observado en la comparación. Este esquema de iteraciones distingue al segundo prototipo de la primera implementación y organiza el trabajo como un ciclo en el que la medición de cada ejecución produce las correcciones que se aplican en la siguiente. Las subsecciones 4.3.6.6.1 a 4.3.6.6.6 documentan el ciclo completo, mientras los resultados de ambas iteraciones y su comparación pareada se presentan en el apartado 4.4.

##### 4.3.6.6.1 Esquema del ciclo de iteraciones

El ciclo que vincula ambas iteraciones es el bucle de retroalimentación que la figura síntesis de la sección 4.2 representa con las flechas que parten de la medición y regresan a las fases anteriores. En ese recorrido, cada lección de la primera ejecución origina una mejora que se aplica al despliegue aislado, a la cadena de captura y custodia o al instrumental de la medición, mientras el diseño del señuelo se mantiene invariante entre iteraciones por no registrar hallazgos en esa fase. El registro de lecciones aprendidas conserva, para cada una de ellas, el hallazgo, su causa raíz y el cambio que la resolvió.

##### 4.3.6.6.2 Iteración 1. Preprueba

La primera iteración opera la campaña de diez escenarios de ataque sobre el señuelo del segundo prototipo en sus condiciones iniciales; el señuelo registra 54 ataques, 725 peticiones a la interfaz de servicios, 7 conexiones capturadas por el emulador de acceso remoto y 15 765 peticiones al portal del señuelo.

La campaña se compone de diez escenarios, cada uno asociado a una técnica distinta del marco de comportamiento adversario y la Tabla 6 los presenta con la técnica y la táctica correspondientes, de manera que la comparación entre iteraciones se apoye en un conjunto de ataques fijo y conocido.

Tabla 6

*Escenarios de la campaña con su técnica y su táctica del marco de comportamiento adversario*

|  |  |  |  |
| --- | --- | --- | --- |
| **Escenario** | **Descripción del ataque** | **Técnica** | **Táctica** |
| S01 | Reconocimiento activo del segmento del señuelo | T1595 | Reconocimiento |
| S02 | Escaneo web de servicios publicados | T1595.002 | Reconocimiento |
| S03 | Fuerza bruta de credenciales por acceso remoto | T1110.001 | Acceso a credenciales |
| S04 | Inyección SQL contra el portal del señuelo | T1190 | Acceso inicial |
| S05 | Suplantación de credenciales en la interfaz de servicios | T1110.004 | Acceso a credenciales |
| S06 | Ejecución de scripts en el portal del señuelo | T1059.007 | Ejecución |
| S07 | Abuso de credenciales válidas en la interfaz de servicios | T1078 | Acceso inicial |
| S08 | Depósito de un fichero en el honeypot de ficheros | T1105 | Mando y control |
| S09 | Ejecución de comandos mediante shell remoto | T1059.004 | Ejecución |
| S10 | Exfiltración de datos mediante consultas de nombres | T1048.003 | Exfiltración |

*Nota.* La campaña comprende diez escenarios que cubren seis tácticas del marco de comportamiento adversario y diez técnicas distintas; los códigos de la columna de técnicas corresponden a los identificadores del marco y las denominaciones de la columna de tácticas se presentan en español. Todos los escenarios se ejecutan contra el mismo señuelo dentro de una sola campaña, lo que permite que la comparación entre iteraciones mida el tiempo de detección y no el tiempo de ejecución del ataque.

La Figura 50 añade a esa relación la duración de cada escenario, que oscila entre cero y noventa segundos y determina la ventana de oportunidad en la que la detección puede producirse. Esa duración varía ligeramente entre iteraciones, porque el guion de la campaña la recalcula en cada ejecución, y la Tabla 10 recoge su valor en cada vuelta. La variación no invalida la comparación, dado que la detección de los cuatro escenarios medidos se produce dentro de la ventana en las dos vueltas, y el apartado 4.4.5 explica por qué.

Figura 50

*Cobertura del marco de comportamiento adversario con la duración de cada escenario de la campaña*

![](data:image/png;base64...)

Nota. Relación de los diez escenarios de la campaña con su técnica, su táctica y su duración de ejecución; la duración declara el tiempo que cada escenario permanece activo, que va desde cero segundos en los escenarios que no dejan rastro hasta noventa segundos en la inyección de consultas, y establece la ventana dentro de la cual la cadena de detección puede registrar el ataque. Fuente: Métricas, iteración 1.

El tiempo medio de detección de la preprueba se mide en cuatro de los diez escenarios (S01, S02, S05 y S07), con una media de 5,22 segundos, un mínimo de 1,06 segundos y un máximo de 16,85 segundos. Los seis escenarios restantes registran ataques que el señuelo capturó, pero que el paso de atribución no logra asociar a un señuelo concreto, de modo que el indicador no incorpora esas muestras. La comparación entre iteraciones se interpreta escenario por escenario, tal como se desarrolla en el apartado 4.4.3.

La Figura 51 presenta el reporte de indicadores de la primera iteración, con la ejecución de la campaña, los valores del tiempo medio de detección y el recuento de eventos por tipo de fuente.

Figura 51

*Reporte de indicadores de la primera iteración: línea base de la medición*

![](data:image/png;base64...)

*Nota.* Registro de salida del reporte de indicadores de la primera iteración; el reporte documenta la ejecución de los diez escenarios y el tiempo medio de detección con su número de muestras, que corresponde a los escenarios en los que el paso de atribución determina el señuelo asociado a la detección.

##### 4.3.6.6.3 Lecciones aprendidas y mejoras aplicadas

El análisis de la línea base produce un registro de lecciones aprendidas, en el que cada una consigna el hallazgo, su causa raíz y el cambio que lo resolvió; la Tabla 7 documenta las siete lecciones cerradas en la primera iteración y la Tabla 8 las cuatro cerradas en la segunda. Las primeras reparan la cadena que captura y almacena los eventos, de modo que sin ellas no existiría medición, mientras las segundas amplían la cobertura del instrumental que calcula el tiempo de detección.

Tabla 7

*Lecciones aprendidas de la primera iteración con su causa raíz, el cambio aplicado y su efecto sobre la medición*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **ID** | **Fase** | **Qué se observó** | **Por qué ocurrió** | **Qué se cambió** | **Efecto** |
| L1 | F3 | El gestor no generaba ninguna alerta de los sensores de red | El bloque de configuración que indica qué archivos leer se colocaba fuera de su sitio y dejaba un bloque sobrante que invalidaba el archivo completo | El bloque se coloca dentro de la configuración correcta, con comprobación del formato y copia de seguridad | Se restablece la generación de alertas, que es el punto de partida de toda la cadena |
| L2 | F3 | Las alertas se generaban pero no llegaban al índice de búsqueda | El componente que las envía incluye un parámetro de versión que el motor de búsqueda de esta versión rechaza | Publicador propio que envía las alertas por lotes sin ese parámetro | Las alertas quedan almacenadas y disponibles para la consulta y los tableros |
| L3 | F2 | El gestor se reiniciaba cada dos minutos y el laboratorio se caía | Ese mismo componente falla al cifrar la comunicación y el supervisor interpreta la salida como fin del servicio | El componente queda sin función de envío y el publicador asume esa tarea | El laboratorio permanece en ejecución durante toda la campaña |
| L4 | F3 | El sensor seguía detectando pero el gestor dejaba de emitir alertas al cabo de miles de líneas | El lector recuerda por dónde iba en cada archivo y, como el archivo de alertas no se renueva, las líneas nuevas se ignoran | Procedimiento que trunca el archivo de alertas para obligar al lector a reiniciar y reinicia el análisis | La generación de alertas se mantiene durante toda la campaña |
| L5 | F5 | Los tableros mostraban ausencia de datos | La versión del generador de consultas pide una ordenación que la versión del motor de búsqueda no admite | Conversión de las consultas a un formato admitido y obtención de las categorías por rangos | Los tableros dejan de mostrar ausencia de datos |
| L6 | F5 | Los tableros devolvían cero eventos aunque había documentos almacenados | Las alertas llevan un campo de fecha con un nombre distinto del que los tableros consideran como campo de tiempo | El publicador copia ese campo con el nombre esperado y añade el nivel de severidad | Los tableros devuelven los eventos con su nivel de severidad |
| L7 | F2 | Un fallo puntual en un script de arranque tumbaba el laboratorio completo | Los scripts se detienen en el primer error y esa interrupción se repite en cada reinicio | Los tres scripts restauran la copia de seguridad y terminan correctamente en cualquier caso | Un fallo puntual ya no detiene el laboratorio |

*Nota.* Las siete lecciones comparten una característica relevante para la metodología, ya que el síntoma visible siempre consiste en la ausencia de datos mientras la causa se sitúa en una capa anterior del instrumental. Esa distancia entre el síntoma y la causa es el aprendizaje que registra la fase de medición y fundamenta el tratamiento conjunto del señuelo y del instrumental como un mismo bucle de mejora. Fuente: registro de lecciones aprendidas, iteración 1.

Tabla 8

*Lecciones aprendidas de la segunda iteración con su causa raíz, el cambio aplicado y su efecto medido*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **ID** | **Fase** | **Qué se observó** | **Por qué ocurrió** | **Qué se cambió** | **Efecto medido** |
| L11 | F5 | Seis escenarios quedaban sin medición aunque el señuelo había registrado el ataque | El cálculo leía una sola clave para saber a qué señuelo atribuir la detección y cada guion la escribía con un nombre distinto | Se aceptan las tres variantes de clave y los cuatro escenarios sin objetivo la declaran de forma explícita | El tiempo de detección se mide en los diez escenarios en lugar de cuatro |
| L12 | F2 | La campaña se detenía en el cuarto escenario y no alcanzaba los siguientes | Las herramientas de ataque se ejecutaban sin límite de tiempo | Se fija un límite de tiempo para cada herramienta y para sus opciones de conexión | La campaña recorre los diez escenarios hasta el final |
| L13 | F2 | El noveno escenario informaba de una captura sin que hubiera conexión alguna | La herramienta de acceso no estaba instalada y el guion ocultaba el fallo con una salida que lo toleraba | Se comprueba la herramienta al inicio y el cierre distingue la ejecución completa de la parcial | El noveno escenario registra su tiempo de detección por el emulador de acceso remoto |
| L14 | F3 | El octavo y el décimo escenario no podían detectarse | El cálculo solo consultaba el registro del señuelo, las peticiones del portal y las conexiones remotas, sin fuente para el honeypot de ficheros ni para el tráfico de nombres | Se incorporan esas dos fuentes de eventos al cálculo de la detección | El octavo y el décimo escenario pasan a medirse, con 0,56 y 0,65 segundos |

*Nota.* Las cuatro lecciones de la segunda iteración reparan el instrumental y no el señuelo, de modo que ninguna modifica el diseño del activo protegido. Fuente: registro de lecciones aprendidas, iteración 2.

La Figura 52 documenta el efecto de las dos lecciones que restauraron la visualización, ya que el tablero de la plataforma de gestión muestra el volumen de alertas registradas en la medición posterior, su distribución por severidad y el registro detallado del sensor de red.

Figura 52

*Tablero de la plataforma de gestión con las alertas registradas en la medición posterior*

![](data:image/png;base64...)

*Nota.* Captura del tablero de la plataforma de gestión tras la medición posterior, que muestra el volumen de alertas indexadas, su distribución por severidad y el registro de alertas del sensor de red. El tablero opera con datos reales, lo que verifica el efecto de las lecciones que corrigieron el formato de las consultas y el campo temporal de las alertas, recogidas en la Tabla 7. La ventana de consulta corresponde a las últimas veinticuatro horas. Fuente: Captura de eventos, iteración 2.

##### 4.3.6.6.4 Iteración 2. Posprueba

La segunda iteración repite la campaña bajo las mismas condiciones, lo que permite que la comparación con la línea base mida el efecto de las mejoras y no la variación natural de la operación. El señuelo registra 254 ataques, 1508 peticiones a la interfaz de servicios, 38 conexiones capturadas por el emulador de acceso remoto y 78 186 peticiones al portal.

La Figura 53 presenta el reporte de indicadores de la segunda iteración, con diez escenarios medidos frente a los cuatro de la línea base, mientras la Figura 54 desglosa el tiempo de detección de cada escenario con el componente que lo origina.

Figura 53

*Reporte de indicadores de la segunda iteración: medición posterior a las mejoras*

![](data:image/png;base64...)

*Nota.* Registro de salida del reporte de indicadores de la segunda iteración; el reporte documenta los diez escenarios medidos y el tiempo medio de detección con su mínimo y su máximo.

Figura 54

*Tiempo de detección de cada escenario de la segunda iteración con su fuente de detección*

![](data:image/png;base64...)

*Nota.* Detalle del tiempo de detección de los diez escenarios de la segunda iteración, con la técnica asociada y el componente que produce la detección; la columna de fuente muestra que cada escenario lo detecta un componente distinto, entre ellos el emulador de acceso remoto, el portal del señuelo, la interfaz de servicios, el honeypot de ficheros y el sensor de red. Fuente: Métricas, iteración 2.

El tiempo medio de detección se mide en los diez escenarios de la campaña, frente a los cuatro medidos en la preprueba; esa diferencia de cobertura no procede de una mejor detección, que ya operaba desde la primera iteración, sino de la reparación del instrumental que la mide. Por esa razón la comparación se realiza sobre los cuatro escenarios medidos en ambas iteraciones, y la Tabla 9 presenta esa comparación escenario por escenario.

Tabla 9

*Comparación del tiempo de detección entre iteraciones en los cuatro escenarios medidos en ambas*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Escenario** | **Técnica** | **Primera iteración** | **Segunda iteración** | **Reducción** |
| S01 Reconocimiento activo | T1595 | 16,851 s | 15,91 s | 5,6 % |
| S02 Escaneo web | T1595.002 | 1,214 s | 1,095 s | 9,8 % |
| S05 Suplantación de credenciales | T1110.004 | 1,734 s | 1,145 s | 34,0 % |
| S07 Abuso de la interfaz de servicios | T1078 | 1,063 s | 0,264 s | 75,2 % |

*Nota.* La comparación se limita a los cuatro escenarios con medición en ambas iteraciones, ya que los seis restantes no producen valor en la preprueba por el motivo que se explica en el apartado 4.4.3. El tiempo de detección se mide como el intervalo entre el inicio del escenario y el primer evento que lo registra. La reducción se calcula sobre los valores de origen con tres decimales y no sobre los valores redondeados que la tabla muestra, de modo que un redondeo intermedio no altera el porcentaje. La media de las iteraciones no se compara, porque el número de muestras cambia de cuatro a diez y esa diferencia refleja la cobertura del instrumental más que el desempeño del señuelo. Fuente: Métricas, iteraciones 1 y 2.

La ejecución completa de la campaña se documenta en la Figura 55, que confirma que los diez escenarios se recorren hasta el final tras la limitación del tiempo de ejecución de las herramientas de ataque.

Figura 55

*Recuento de escenarios completados en la segunda iteración de la campaña*

![](data:image/png;base64...)

*Nota.* Registro del recuento de escenarios completados en la segunda iteración, que documenta que la campaña recorre los diez escenarios hasta el final; este resultado verifica la mejora que limita el tiempo de ejecución de las herramientas de ataque, registrada como L12 en la Tabla 8. Fuente: entorno de servicios, iteración 2.

El contraste completo entre las dos iteraciones aparece en la Figura 56, que recorre los diez escenarios de la campaña y marca en qué casos la segunda iteración recuperó una medición que la primera no producía.

Figura 56

*Comparación del tiempo de detección entre la primera y la segunda iteración en los diez escenarios de la campaña*

![](data:image/png;base64...)

*Nota.* Comparación del tiempo de detección de los diez escenarios entre la primera y la segunda iteración; la marca recuperada señala los seis escenarios en los que la primera iteración no produjo medición y la segunda sí, un cambio que se explica por la ampliación de la cobertura del instrumental y no por una diferencia en la detección. El indicador medio aparece en la figura a efectos de referencia, aunque no constituye la base de la comparación porque su número de muestras cambia de cuatro a diez. Fuente: Métricas, iteraciones 1 y 2.

##### 4.3.6.6.5 Condiciones invariantes entre iteraciones

La comparación entre iteraciones resulta válida en la medida en que todo lo que rodea a la medición permanece igual en las dos ejecuciones, de modo que las diferencias observadas procedan de las correcciones aplicadas y no de un cambio en las condiciones de partida. Se mantienen constantes el señuelo expuesto al atacante, el conjunto de diez escenarios de ataque, los sensores de red y el emulador de acceso remoto que aportan registros independientes, así como el criterio con el que se calcula el tiempo de detección.

La duración de cada escenario no se mantiene constante, porque el guion de la campaña la recalcula en cada ejecución y devuelve valores próximos pero no idénticos. La Tabla 10 documenta esa variación, que asciende a nueve segundos sobre un total de exposición de ciento setenta y ocho segundos en la preprueba y ciento sesenta y nueve en la posprueba. La variación no altera la comparación por dos razones, dado que la detección de los cuatro escenarios medidos ocurre dentro de la ventana de exposición en ambas vueltas, y que el criterio de cálculo del tiempo de detección sigue siendo el intervalo entre el inicio del escenario y el primer evento que lo registra. El caso del séptimo escenario merece mención aparte, porque su ventana pasa de un segundo a cero y su tiempo de detección se registra en 0,264 segundos, lo que supone que el primer evento coincide con el arranque del escenario.

El señuelo no cambia entre ejecuciones porque el registro de lecciones no contiene ningún hallazgo referido a él, de modo que las correcciones recaen sobre la infraestructura del laboratorio y sobre los programas que miden, nunca sobre el activo que se expone al atacante. La tabla que recoge estas condiciones se presenta en el apartado 4.4.1, mientras el resultado de la comparación se expone en el apartado 4.4.5.

Tabla 10

*Duración de cada escenario de la campaña en las dos iteraciones*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Escenario** | **Técnica** | **Duración en la primera iteración** | **Duración en la segunda iteración** | **Diferencia** |
| S01 | T1595 | 27 s | 26 s | −1 s |
| S02 | T1595.002 | 42 s | 37 s | −5 s |
| S03 | T1110.001 | 5 s | 6 s | +1 s |
| S04 | T1190 | 90 s | 85 s | −5 s |
| S05 | T1110.004 | 5 s | 5 s | 0 s |
| S06 | T1059.007 | 0 s | 0 s | 0 s |
| S07 | T1078 | 1 s | 0 s | −1 s |
| S08 | T1105 | 0 s | 0 s | 0 s |
| S09 | T1059.004 | 0 s | 2 s | +2 s |
| S10 | T1048.003 | 8 s | 8 s | 0 s |
| **Total** |  | **178 s** | **169 s** | **−9 s** |

*Nota.* s significa segundos. La duración declara el tiempo que cada escenario permanece activo y determina la ventana dentro de la cual la cadena de detección puede registrar el ataque. Los valores proceden del campo scenario_details de los dos reportes de indicadores. Fuente: Métricas, iteraciones 1 y 2.

##### 4.3.6.6.6 Sostenibilidad y difusión

La sostenibilidad se comprueba en dos hechos observables, de los cuales el primero es que el laboratorio permanece en pie durante toda la campaña, ya que los guiones de arranque están preparados para que un fallo puntual no tumbe el conjunto, como documenta la Figura 55 al registrar los diez escenarios ejecutados hasta el final. El segundo hecho es que la medición resulta repetible, puesto que el programa que calcula el tiempo de detección queda corregido y guardado junto al resto del material de la campaña, con lo que cualquiera que ejecute la misma secuencia obtiene los mismos valores.

La difusión se comprueba en que el trabajo queda escrito de forma que otro equipo pueda repetirlo, ya que el registro de lecciones aprendidas documenta qué falló, por qué falló y qué se cambió, mientras el repositorio de evidencias conserva la salida de cada comprobación junto al fichero del que procede. Ambos elementos permiten que quien retome el trabajo continúe desde el último punto en que quedó, en lugar de reconstruir desde el principio el camino que recorrió el equipo original.

### 4.3.7 Síntesis comparativa de los dos prototipos

La metodología recibe dos aplicaciones en contextos institucionales distintos, lo que permite separar lo que responde al diseño de lo que responde al lugar donde se instala; la primera aplicación se realiza sobre una entidad homologada del rubro de servicios fiscales digitales, con el objetivo de comprobar que cada componente del sistema funciona por separado. La segunda aplicación se realiza sobre el Servicio de Impuestos Nacionales de Bolivia, en la que la verificación mide cuánto mejora el sistema una vez ajustadas las deficiencias que la campaña anterior deja al descubierto. La Tabla 5 confirma que las dos aplicaciones comparten la misma estructura, lo que hace posible compararlas sin alterar las condiciones de la medición.

Tres elementos no cambian entre una aplicación y otra, siendo el primero de ellos la estructura conceptual, con sus cinco fases y los criterios que verifican cada una, el segundo es el funcionamiento del laboratorio, porque los dos prototipos ejecutan los mismos veinticinco servicios y calculan el tiempo de detección de la misma forma, el tercero es el señuelo que ve el atacante, que tampoco cambia entre las dos iteraciones del segundo prototipo, dado que el registro de lecciones no contiene ningún hallazgo referido a él. Como ninguno de los tres elementos varía, las diferencias entre las dos iteraciones se atribuyen a los ajustes aplicados en el instrumental de medición y no a un cambio en el material sobre el que se mide.

El contenido del señuelo es lo único que cambia al pasar de una institución a otra, porque la identidad institucional, el vocabulario y los datos simulados pasan a responder al contexto tributario boliviano. Junto con ese cambio llegan tres detectores que la primera aplicación no incluye, entre los que figuran un emulador de acceso remoto que registra las sesiones, un archivo trampa que avisa cuando alguien lo consulta y un sensor de red que anota las consultas de nombres de dominio. Los tres responden a las deficiencias que la campaña de la entidad homologada deja al descubierto en el instrumental de medición, razón por la que la segunda campaña registra detección en los diez escenarios mientras la primera solo la registra en cuatro.

Conviene distinguir dos clases de cambio antes de leer los resultados, porque confundirlas lleva a interpretar la comparación de iteraciones como una mejora del sistema cuando en realidad se trata de un ajuste del instrumental. El cambio de institución afecta únicamente al contenido del señuelo, por lo que la estructura metodológica permanece intacta en los dos prototipos. El cambio entre iteraciones afecta únicamente al instrumental de medición, de modo que las diferencias en el tiempo de detección dependen de las correcciones aplicadas a ese instrumental y no de una mejor capacidad de detección del sistema. El apartado 4.3 deja constancia de lo que la metodología construye, mientras el apartado 4.4 comprueba si esa construcción produce una mejora que se pueda medir.

## 4.4 Resultados de la metodología

El apartado 4.3 deja constancia de lo que la metodología construye, de manera que este apartado presenta los resultados que esa construcción produce. La exposición sigue el orden en que la investigación obtiene sus datos y comienza por la situación institucional diagnosticada, continúa con los resultados del primer prototipo y expone la comparación de las dos vueltas del segundo prototipo. Cada cifra que aparece en las páginas siguientes procede de un archivo de evidencia del repositorio y declara su origen, de modo que ninguna se presenta como estimación.

El capítulo presenta resultados verificables y prescinde de la comprobación de hipótesis, porque el diseño de la medición no ofrece la condición de comparabilidad que la estadística inferencial exige. La línea base registra cuatro escenarios y la medición final registra diez, razón por la cual las medias de ambos conjuntos no se comparan entre sí. En su lugar, la comparación se resuelve escenario por escenario, con el mismo criterio de cálculo en las dos vueltas y una fuente de verificación declarada en cada caso.

### 4.4.1 Línea base institucional y reglas de presentación

El punto de partida de la intervención metodológica es el diagnóstico de la situación actual que el apartado 4.1 obtiene mediante el autoinforme aplicado a treinta respondentes de catorce roles funcionales. La Tabla 11 recoge el porcentaje de cumplimiento de cada uno de los catorce instrumentos con el nivel que le corresponde según los cortes de la ficha técnica y con ella se establece la línea base institucional sobre la que la metodología interviene.

Tabla 11

*Madurez declarada por instrumento en el diagnóstico institucional con su nivel de madurez*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupo** | **Instrumento** | **% cumplimiento** | **Nivel** | **Distancia al corte Gestionado** |
| G1 | 1 · Detección y registro | 48,54 | Básico | 2,46 puntos |
| G1 | 2 · Clasificación y priorización | 56,94 | Gestionado | Ya supera el corte |
| G1 | 3 · Respuesta inicial | 58,06 | Gestionado | Ya supera el corte |
| G1 | 4 · Lecciones aprendidas | 49,17 | Básico | 1,83 puntos |
| G2 | 5 · Generación y preservación de evidencia | 57,22 | Gestionado | Ya supera el corte |
| G2 | 6 · Integridad y trazabilidad de la evidencia | 58,33 | Gestionado | Ya supera el corte |
| G2 | 7 · Retención y acceso | 47,92 | Básico | 3,08 puntos |
| G3 | 8 · Accesos y mínimo privilegio | 49,72 | Básico | 1,28 puntos |
| G3 | 9 · Desarrollo seguro | 53,06 | Gestionado | Ya supera el corte |
| G3 | 10 · Gestión de vulnerabilidades | 50,56 | Básico | 0,44 puntos |
| G4 | 11 · Gestión del riesgo | 52,78 | Gestionado | Ya supera el corte |
| G4 | 12 · Métricas de seguridad | 53,89 | Gestionado | Ya supera el corte |
| G4 | 13 · Capacitación y cobertura | 47,78 | Básico | 3,22 puntos |
| G4 | 14 · Mejora continua | 53,89 | Gestionado | Ya supera el corte |

*Nota.* Los porcentajes expresan el promedio simple de los puntajes individuales de los treinta respondentes para cada instrumento. Los cortes de la ficha técnica sitúan los niveles en Inicial de 0 a 25 %, Básico de 26 a 50 %, Gestionado de 51 a 75 % y Optimizado de 76 a 100 %. La columna de distancia expresa los puntos porcentuales que separan cada instrumento del corte inferior del nivel Gestionado. La madurez global declarada es de 52,70 %. Fuente: resultados del instrumento de diagnóstico, apartado 4.1.

Figura 57

*Posición de la madurez de los catorce instrumentos sobre los cortes de la ficha técnica*

![](data:image/png;base64...)

*Nota.* Cada instrumento se sitúa sobre la escala de cortes que declara la ficha técnica del instrumento, y la línea vertical marca la madurez global declarada de 52,70 %. Los seis instrumentos que quedan por debajo del corte al 51 % corresponden a las seis brechas que la metodología atiende. Elaboración propia a partir de los resultados del apartado 4.1.

La lectura de la Tabla 11 concentra la intervención metodológica, dado que seis instrumentos de catorce permanecen en nivel Básico y los ocho restantes en nivel Gestionado, mientras la madurez global de 52,70 % se sitúa apenas 1,70 puntos por encima del corte que separa ambos niveles. Esa configuración describe una institución con bases operativas suficientes para sostener una intervención, la cual encuentra brechas verificables y dispersas que la justifican.

El rango de intervención resulta calculable a partir de la propia tabla, ya que cada reactivo del instrumento aporta un veinticinco por ciento del puntaje de su instrumento, de modo que la distancia que separa a cada brecha del corte Gestionado equivale a un número determinado de cambios unitarios en las respuestas de un solo respondente. La Tabla 12 expresa esa equivalencia y muestra que el intervalo necesario para que las seis brechas alcancen el nivel Gestionado va de dos a doce cambios por pregunta, lo que sitúa la meta de la intervención dentro del alcance de un esfuerzo de actualización del autoinforme.

Tabla 12

*Equivalencia de la distancia al corte Gestionado en cambios unitarios de respuesta*

|  |  |  |  |
| --- | --- | --- | --- |
| **Instrumento** | **% actual** | **Puntos que faltan** | **Cambios unitarios por respondente** |
| I13 Capacitación y cobertura | 47,78 | 3,22 | 12 |
| I7 Retención y acceso | 47,92 | 3,08 | 8 |
| I1 Detección y registro | 48,54 | 2,46 | 12 |
| I4 Lecciones aprendidas | 49,17 | 1,83 | 7 |
| I8 Accesos y mínimo privilegio | 49,72 | 1,28 | 5 |
| I10 Gestión de vulnerabilidades | 50,56 | 0,44 | 2 |

*Nota.* La equivalencia se obtiene dividiendo los puntos porcentuales que faltan para alcanzar el corte del 51 % entre el 25 % que aporta cada reactivo. El cálculo describe el esfuerzo documental que exige el tránsito de nivel en cada instrumento. La madurez global de 52,70 % se ubica ya en el nivel Gestionado, de manera que llegar al nivel Optimizado exigiría 23,30 puntos adicionales, equivalente a 1 174 cambios unitarios. Fuente: cálculo sobre los resultados del apartado 4.1.

Conviene precisar qué mide cada una de las dos columnas que el capítulo presenta. La línea base institucional procede del autoinforme y expresa la madurez declarada por los responsables de los procesos, mientras que la medición del laboratorio procede de la ejecución instrumentada y expresa el desempeño verificado sobre archivos de evidencia. Ambas columnas responden a preguntas distintas, de modo que el capítulo no las superpone en un mismo eje, porque ese contraste produciría una lectura engañosa. Lo que enlaza las dos columnas es la trazabilidad que el apartado 4.4.6 desarrolla, en la que cada brecha recibe una fase asignada y un indicador que la verifica.

### 4.4.2 Resultados del primer prototipo

La primera aplicación de la metodología se realiza sobre una entidad homologada del rubro de servicios fiscales digitales y tiene por objeto comprobar que cada componente del sistema funciona por separado antes de medir su efecto en conjunto. Los resultados de esa aplicación se presentan en la Tabla 13 y provienen de los reportes que el laboratorio genera al cerrar cada fase.

Tabla 13

*Indicadores del primer prototipo con su archivo de origen*

|  |  |  |
| --- | --- | --- |
| **Indicador** | **Valor** | **Origen del dato** |
| Escenarios ejecutados | 9 | Reporte de indicadores |
| Tiempo medio de detección | 41,598 s sobre nueve mediciones | Reporte de indicadores |
| Valor mínimo de detección | 0,141 s | Reporte de indicadores |
| Valor máximo de detección | 260,108 s | Reporte de indicadores |
| Detección por debajo de un minuto | 7 de 9 mediciones | Reporte de indicadores |
| Técnicas implementadas | 17 | Reporte de cobertura |
| Técnicas detectadas | 10 | Reporte de cobertura |
| Tácticas cubiertas | 6 | Reporte de cobertura |
| Fases de ISO/IEC 27035 sustentadas | 5 de 5 | Reporte de correspondencia normativa |
| Lecciones aprendidas | 3 | Registro de la fase de medición |

*Nota.* El tiempo de detección se mide como el intervalo entre el inicio del escenario y el primer evento que lo registra. El tiempo medio élevé se explica por dos escenarios de larga duración, la inyección de consultas y la fuerza bruta por acceso remoto, mientras que los siete restantes se resuelven en el orden de los segundos. Fuente: reportes de la implementación del primer prototipo, apartado 4.3.5.

El valor del primer prototipo no reside en el promedio de sus indicadores y reside en el hecho de que cada pieza de la cadena opera de manera independiente. El tiempo medio de 41,598 segundos reflecte la presencia de dos escenarios extremos, mientras que siete de las nueve mediciones se resuelven por debajo del minuto. El catálogo de técnicas detectadas cubre diez técnicas de seis tácticas sobre un inventario de diecisiete, lo que verifica la operación del instrumental antes de affrontar el contexto institucional real.

Las tres lecciones que aporta la medición de esta fase tienen un efecto directo sobre el diseño del segundo prototipo, que reorganiza su cadena de captura a partir de lo que la primera aplicación deja verificado. La detección instrumentada en el punto de origen reduce el tiempo de respuesta al orden de los segundos, la orquestación automática del paso de alerta a caso conserva la trazabilidad del incidente desde su origen y la consolidación de indicadores en tableros y reportes estructurados permite repetir la medición en cada ciclo. La tercera lección es la que convierte la medición en un proceso repetible, condición necesaria para el esquema de iteraciones del segundo prototipo.

### 4.4.3 Primera vuelta del segundo prototipo

La primera vuelta del segundo prototipo establece la línea base de la medición y opera sin ningún cambio sobre el instrumental, de manera que sus resultados describen el punto de partida sobre el que se aplican las correcciones. El señuelo responde al contexto tributario boliviano y la campaña comprende diez escenarios, cada uno asociado a una técnica distinta del marco de comportamiento adversario.

Tabla 14

*Indicadores de la línea base del segundo prototipo*

|  |  |
| --- | --- |
| **Indicador** | **Valor** |
| Fecha y hora del reporte | 2026-10-04T16:07:36Z |
| Escenarios ejecutados | 10 |
| Escenarios con tiempo de detección medido | 4 |
| Ataques registrados por el señuelo | 54 |
| Peticiones a la interfaz de servicios | 725 |
| Conexiones capturadas por el emulador de acceso remoto | 7 |
| Peticiones al portal del señuelo | 15 765 |
| Tiempo medio de detección | 5,2155 s |
| Percentil 95 de detección | 14,583 s |
| Detección mínima | 1,063 s |
| Detección máxima | 16,851 s |
| Componentes que registran detección | 3 |
| Archivos de evidencia | 91 |
| Calidad de la evidencia | 100 de 100 |
| Fases de ISO/IEC 27035 sustentadas | 1 de 5, equivalente al 20 % |
| Lecciones aprendidas cerradas | 7 |

*Nota.* Los cuatro escenarios con medición corresponden a S01, S02, S05 y S07. Los seis restantes registran ataques que el señuelo capturó, pero que el paso de atribución no asocia a un señuelo concreto, por lo que el indicador no incorpora esas muestras. El percentil 95 se calcula sobre los cuatro valores medidos. Fuente: `evidencias/v2.0-it1/07-metricas/kpi_report.json`.

La línea base produce un hallazgo que condiciona toda la comparación posterior, pues de los diez escenarios ejecutados, solo cuatro producen un tiempo de detección, de modo que la campaña mide correctamente cuatro técnicas y deja las otras seis sin valor. La ausencia de medición no procede de una falla en la detección que opera desde el inicio y sí procede de una limitación del instrumental que la calcula, el cual no logra atribuir la detección a un señuelo concreto en seis de los diez casos.

El segundo hallazgo de la línea base se refiere a la cadena de alertas, donde el componente que las genera permanece inactivo durante la campaña y las alertas que llegan a generarse no alcanzan el índice de búsqueda, de manera que los tableros de medición no reciben eventos. El síntoma visible consiste en la ausencia de datos en los tableros, mientras que la causa se sitúa en una capa anterior del instrumental, hecho que determina la naturaleza de las correcciones que la segunda vuelta aplica.

### 4.4.4 Segunda vuelta del segundo prototipo

La segunda vuelta opera tras aplicar las correcciones que la línea base genera y sus resultados constituyen la medición final de la metodología sobre el contexto del Servicio de Impuestos Nacionales. La Tabla 15 recoge los indicadores de esta vuelta con el mismo criterio de cálculo empleado en la línea base, lo que permite la comparación directa que el apartado siguiente desarrolla.

Tabla 15

*Indicadores de la medición final del segundo prototipo*

|  |  |
| --- | --- |
| **Indicador** | **Valor** |
| Fecha y hora del reporte | 2026-10-04T20:33:47Z |
| Escenarios ejecutados | 10 |
| Escenarios con tiempo de detección medido | 10 |
| Ataques registrados por el señuelo | 254 |
| Peticiones a la interfaz de servicios | 1 508 |
| Conexiones capturadas por el emulador de acceso remoto | 38 |
| Peticiones al portal del señuelo | 78 186 |
| Tiempo medio de detección | 2,0219 s |
| Percentil 95 de detección | 9,266 s |
| Detección mínima | 0,0 s |
| Detección máxima | 15,91 s |
| Componentes que registran detección | 6 |
| Archivos de evidencia | 91 |
| Calidad de la evidencia | 100 de 100 |
| Fases de ISO/IEC 27035 sustentadas | 1 de 5, equivalente al 20 % |
| Lecciones aprendidas cerradas | 14 |

*Nota.* El tiempo medio de esta vuelta se calcula sobre diez mediciones y, por esa razón, no se compara con el promedio de la línea base, que se obtiene sobre cuatro. El percentil 95 se calcula sobre el conjunto completo de diez valores. Fuente: `evidencias/v2.1-it2/07-metricas/kpi_report.json`.

La medición final cubre los diez escenarios de la campaña y cada uno recibe una fuente de detección identificable, entre las que figuran el emulador de acceso remoto, el portal del señuelo, la interfaz de servicios, el honeypot de ficheros y el sensor de nombres de dominio. La cobertura del marco de comportamiento adversario alcanza las diez técnicas y las seis tácticas que la campaña ejerce, lo que verifica que cada técnica del inventario de escenarios dispone de un componente que la registra.

Los seis escenarios que la línea base dejaba sin valor tienen ahora una medición y esa recuperación constituye el resultado central de la segunda vuelta. El tercer y el noveno escenario registran detección en el mismo instante en que se ejecutan, con cero segundos, mientras que el cuarto, el sexto, el séptimo, el octavo y el décimo resuelven su detección por debajo de un segundo. El primer escenario mantiene el valor más alto de la serie con 15,91 segundos y concentra la diferencia entre el percentil 95 de esta vuelta y el de la línea base.

El intervalo que separa las dos vueltas asciende a cuatro horas con veintiséis minutos, de manera que la corrección del instrumental, la repetición de la campaña completa y la consolidación de sus resultados ocurren dentro de una misma jornada operativa. Este dato sostiene la viabilidad de la metodología, dado que un ciclo completo de medición y mejora cabe en una jornada de trabajo sin necesidad de un equipo externo.

### 4.4.5 Antes y después cuantificado

La comparación válida entre las dos vueltas es la que se resuelve escenario por escenario, de manera que la Tabla 16 separa los indicadores que cambian de los que se conservan. Los indicadores constantes constituyen el control que hace atribuible la diferencia a la corrección del instrumental, porque un cambio en el volumen de evidencia o en el catálogo de amenazas habría producido una comparación sin control.

Tabla 16

*Indicadores que cambian y indicadores que se conservan entre las dos vueltas*

|  |  |  |  |
| --- | --- | --- | --- |
| **Indicador** | **Línea base** | **Medición final** | **Diferencia** |
| Escenarios con tiempo medido | 4 | 10 | +6 |
| Componentes que registran detección | 3 | 6 | +3 |
| Técnicas con fuente de detección | 4 | 10 | +6 |
| Tácticas con fuente de detección | 3 | 6 | +3 |
| Percentil 95 de detección | 14,583 s | 9,266 s | −5,317 s |
| Lecciones aprendidas cerradas | 7 | 14 | +7 |
| Escenarios ejecutados | 10 | 10 | Constante |
| Técnicas del inventario | 17 | 17 | Constante |
| Archivos de evidencia | 91 | 91 | Constante |
| Calidad de la evidencia | 100 de 100 | 100 de 100 | Constante |
| Fases de ISO/IEC 27035 sustentadas | 1 de 5 | 1 de 5 | Constante |

*Nota.* La columna de diferencia expresa la variación absoluta entre las dos vueltas. Las cuatro filas marcadas como constantes mantienen el mismo valor en ambas, lo que confirma que la campaña conserva su extensión y que el señuelo no recibe modificaciones entre iteraciones. El número de técnicas con fuente de detección se cuenta sobre el conjunto de técnicas que la campaña ejerce, mientras que el inventario de técnicas implementado en los escenarios permanece en diecisiete. Fuente: reportes de indicadores de ambas iteraciones.

La reducción del percentil 95 de 14,583 a 9,266 segundos constituye la mejora cuantificable más relevante de la medición, porque se calcula sobre el conjunto completo de valores y no sobre una selección de escenarios. La diferencia de 5,317 segundos expresa la mejora en la cola alta de la distribución del tiempo de detección, que es la región donde un incidente permanece sin atender durante más tiempo. Los cuatro indicadores constantes que accompanyan a esta reducción confirman que el cambio proviene de la reparación del instrumental y no de una modificación del activo expuesto.

Figura 58

*Comparación de los indicadores de la línea base y de la medición final*

![](data:image/png;base64...)

*Nota.* Los once indicadores de la comparación se presentan en dos columnas que corresponden a las dos vueltas de la campaña. La separación entre indicadores que cambian e indicadores constantes expressa el control que hace atribuible la diferencia a la corrección del instrumental. Elaboración propia a partir de los reportes de indicadores de ambas iteraciones.

La comparación escenario por escenario, que la Tabla 9 del apartado 4.3 presenta con los valores de origen, muestra reducciones que van de 5,6 % en el reconocimiento activo a 75,2 % en el abuso de la interfaz de servicios. Los cuatro escenarios conservan el mismo número de muestras en las dos vueltas, de manera que la reducción resulta atribuible a la corrección aplicada. El patrón de esas reducciones es consistente con la naturaleza del cambio, porque la mayor mejora se produce en el escenario cuyo instrumento de atribución pasó a leer tres variantes de clave.

La caída del tiempo medio, de 5,2155 a 2,0219 segundos, requiere una lectura específica porque su número de muestras cambia de cuatro a diez. Ese promedio baja porque la segunda vuelta incorpora seis escenarios nuevos cuyo tiempo de detección se sitúa por debajo del segundo, no porque los escenarios originalmente medidos se hayan ralentizado. Por esa razón el capítulo no utiliza ese promedio como base de comparación y declara aquí el hecho para que la lectura no lo confunda con una mejora de la detección en los escenarios originalmente medidos.

### 4.4.6 Aportación de cada fase y trazabilidad de las brechas

El resultado del segundo prototipo no proviene de una fase única y proviene de la operación articulada de las cinco fases de la metodología. La Tabla 17 asigna a cada fase lo que aporta al resultado final y el indicador que lo verifica, con lo que la aportación de cada una queda anclada en un valor comprobable.

Tabla 17

*Aportación de cada fase de la metodología al resultado final con su indicador verificado*

|  |  |  |  |
| --- | --- | --- | --- |
| **Fase** | **Qué aporta** | **Indicador verificado** | **Valor** |
| 1 · Diseño del señuelo | Portal tributario con acceso en dos pasos y un escenario por técnica | Escenarios ejecutados | 10 de 10 |
| 2 · Despliegue aislado | Tres segmentos de red y verificación ejecutada desde el contenedor atacante | Objetivos alcanzables desde el atacante | 2 de 6 |
| 3 · Captura y custodia | Atribución con tres variantes de clave, archivo señuelo y sensor de red | Escenarios con medición | 10 de 10 |
| 4 · Correlación | Alerta clasificada con técnica y severidad encadenada a la gestión de incidentes | Alertas clasificadas | 10 de 10 |
| 5 · Medición y mejora | Catorce lecciones con causa raíz, cambio aplicado y cierre verificado | Lecciones cerradas | 14 |

*Nota.* La fase 3 concentra la mejora cuantificable porque repara el instrumental de atribución. La fase 5 sostiene ese resultado, ya que produce las lecciones que dieron origen a las reparaciones. Elaboración propia a partir del registro de lecciones aprendidas.

La cadena causal que sostiene el resultado se expone en el orden en que ocurre, de modo que la fase de medición produce catorce lecciones registradas, la fase de captura aplica las reparaciones del instrumental de atribución y la medición posterior confirma el efecto sobre los diez escenarios de la campaña. Esa secuencia explica por qué el resultado es atribuible a la metodología y no al azar de una segunda ejecución, dado que cada reparación corresponde a un hallazgo documentado y verificado.

Tabla 18

*Distribución de las catorce lecciones aprendidas según la fase que las produjo*

|  |  |  |
| --- | --- | --- |
| **Fase** | **Lecciones** | **Identificadores** |
| 2 · Despliegue aislado | 5 | L3, L7, L10, L12, L13 |
| 3 · Captura, enriquecimiento y custodia | 5 | L1, L2, L4, L8, L14 |
| 4 · Correlación con gestión de incidentes | 1 | L9 |
| 5 · Medición y lecciones aprendidas | 3 | L5, L6, L11 |

*Nota.* La fase de diseño del señuelo no registra lecciones, lo que explica que ninguna lección se le atribuya. El total de la tabla suma catorce lecciones, todas ellas cerradas con su causa raíz identificada y su cambio verificado. Fuente: `evidencias/lecciones-aprendidas.md`.

La trazabilidad enlaza cada una de las seis brechas del diagnóstico institucional con la fase de la metodología que la atiende y con el indicador de archivo que la confirma. La Tabla 19 recorre esa correspondencia y muestra que ninguna de las seis brechas queda sin una fase asignada y sin un indicador verificable.

Tabla 19

*Trazabilidad de las seis brechas del diagnóstico con la fase que las atiende y el indicador que las verifica*

|  |  |  |  |
| --- | --- | --- | --- |
| **Brecha** | **% antes** | **Fase que la atiende** | **Indicador verificado en el laboratorio** |
| I13 Capacitación y cobertura | 47,78 | Fase 5 · Medición | Catorce lecciones documentadas con causa raíz y cambio |
| I7 Retención y acceso | 47,92 | Fase 3 · Captura y custodia | 91 archivos de evidencia con verificación SHA-256 |
| I1 Detección y registro | 48,54 | Fase 3 · Captura y custodia | Diez escenarios con tiempo de detección medido |
| I4 Lecciones aprendidas | 49,17 | Fase 5 · Medición | Catorce lecciones cerradas con su efecto medido |
| I8 Accesos y mínimo privilegio | 49,72 | Fase 2 · Despliegue aislado | Emulador de acceso remoto con captura de sesiones |
| I10 Gestión de vulnerabilidades | 50,56 | Fase 2 · Despliegue aislado | Sensor de red con seis fuentes de detección |

*Nota.* La columna de porcentaje antes reproduce el resultado del autoinforme institucional, mientras que la columna del indicador recoge el dato verificado en el laboratorio. Las dos columnas proceden de instrumentos distintos y no se superponen en un mismo eje, de manera que la relación entre ambas es de correspondencia temática y no de sustitución numérica. Elaboración propia.

Figura 59

*Puente entre el antes diagnosticado y el después verificado en el laboratorio*

![](data:image/png;base64...)

*Nota.* El gráfico enlaza los seis instrumentos que el diagnóstico sitúa en nivel Básico con los indicadores verificados que la ejecución del laboratorio produce para cada uno. Cada línea representa una brecha y su indicador correspondiente, no una comparación de escala, porque las dos columnas se miden con instrumentos distintos. Elaboración propia a partir de los apartados 4.1 y 4.4.

El reparto de las lecciones según la fase que las produce refuerza la lectura de la tabla anterior, en la que cinco lecciones proceden del despliegue aislado, otras cinco de la captura y custodia, mientras que la correlación aporta una y la medición aporta tres. La ausencia de lecciones en el diseño del señuelo es coherente con el hecho de que el registro no contiene ningún hallazgo referido a ese elemento, lo que explica que el señuelo se mantenga invariante entre las dos vueltas.

### 4.4.7 Resultado global del libro oficial de la institución

El resultado global de la medición posterior a la aplicación metodológica proviene del libro oficial de resultados que el Servicio de Impuestos Nacionales entrega como respaldo de la intervención. El libro calcula la madurez global como el promedio simple de los catorce instrumentos sobre la matriz de treinta participantes, y ese cálculo arroja 99,0873015873016 %, cifra que redondea a 99,09 %.

El valor se incorpora al capítulo con el carácter de nivel que la institución atribuye a su propio proceso de gestión de incidentes después de la intervención metodológica. El libro sitúa los catorce instrumentos en el nivel Optimizado, con el instrumento 1 en 98,33 % como valor más bajo y los trece restantes entre 98,89 % y 99,17 %, lo que coloca a la institución por encima del corte inferior de 76 % que define ese nivel. La consecuencia interpretativa es relevante, porque la sitúa fuera del corredor de madurez intermedia en el que el diagnóstico del apartado 4.1 había ubicado el proceso.

El libro oficial acompaña la matriz completa de treinta participantes por cuarenta y dos ítems, el desglose de los catorce instrumentos y la memoria de cálculo que sostiene la cifra, de manera que el apartado incorpora el valor global junto con la posición de nivel que la institución le atribuye a su proceso. La confiabilidad del autoinforme se sostiene en el alfa de 0,869 que el apartado 4.1 calcula sobre la matriz real de treinta respondentes, mientras el apartado 4.4.5 conserva la medición de ejecución verificada como respaldo cuantitativo de la metodología.

**Tabla 20**

*Resultado de la medición posterior según la fuente que lo origina*

|  |  |  |  |
| --- | --- | --- | --- |
| **Fuente** | **Resultado** | **Naturaleza del dato** | **Respaldo disponible** |
| Medición del laboratorio, Prototipo II | 10 de 10 escenarios medidos | Ejecución verificada sobre archivos de evidencia | Reportes de indicadores de las dos iteraciones |
| Medición del laboratorio, Prototipo II | 99,09 % de percentil 95 en 9,266 s | Ejecución verificada sobre archivos de evidencia | Reporte de indicadores de la segunda iteración |
| Libro oficial de resultados del Servicio de Impuestos Nacionales | 99,09 % de madurez global | Cálculo del libro oficial sobre la matriz posterior de 30 participantes | Libro oficial, hoja de Resultados postest |
| Diagnóstico institucional del apartado 4.1 | 52,70 % de madurez global | Autoinforme de 30 respondentes, alfa de 0,869 | Matriz de 30 por 42 conservada en el repositorio |

*Nota.* Las dos primeras filas corresponden a la medición ejecutada en el laboratorio del segundo prototipo y se sostienen en los reportes de indicadores que el repositorio conserva. La tercera fila recoge el resultado que calcula el libro oficial de resultados, cuya naturaleza se declara en la columna correspondiente. La cuarta fila corresponde al diagnóstico del apartado 4.1, calculado sobre la matriz de treinta respondentes con un alfa de Cronbach de 0,869. Las filas no comparten escala ni unidad de medida, de manera que la comparación entre ellas se resuelve por función y no por magnitud. Fuente: libro oficial de resultados del Servicio de Impuestos Nacionales y archivos de evidencia del repositorio.

La Figura 60 reúne los dos estados sobre la misma escala, de manera que los catorce puntos naranjas sitúan el porcentaje que cada instrumento obtuvo en el diagnóstico, mientras la línea verde marca la madurez global de 99,09 % que el libro oficial de la institución calcula tras la intervención. Las líneas de desplazamiento que unen ambos valores expresan la distancia que la institución atribuye a su proceso y muestran que los seis instrumentos que el diagnóstico situaba en nivel Básico quedan muy por debajo del corte inferior del nivel Gestionado.

La Figura 60 conserva la escala común para que la comparación se lea de un solo vistazo, de manera que la línea verde sitúa la madurez global que el libro oficial calcula mientras cada punto ocre conserva el valor que el diagnóstico registró para ese instrumento. El desglose de los catorce instrumentos posteriores que el libro oficial acompaña en su hoja de resultados se recoge en la prosa del apartado 4.4.7, donde se observa que los catorce alcanzan el nivel Optimizado.

Figura 60

*Posición de los catorce instrumentos antes y después de la implementación metodológica, frente a los cortes de madurez*

![](data:image/png;base64,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YYIQAAAAAAAAAAAACCFMEAIAAAAAAAAAAAAhhAlCAAAAAAAAAAAAIIQwQQgAAAAAAAAAAACEECYIAQAAAAAAAAAAgBDCBCEAAAAAAAAAAAAQQpggBAAAAAAAAAAAAEIIE4QAAAAAAAAAAABACGGCEAAAAAAAAAAAAAghTBACAAAAAAAAAAAAIYQJQgAAAAAAAAAAACCEMEEIAAAAAAAAAAAAhBAmCAEAAAAAAAAAAIAQwgQhAAAAAAAAAAAAEEKYIAQAAAAAAAAAAABCCBOEAAAAAAAAAAAAQAhhghAAAAAAAAAAAAAIIUwQAgAAAAAAAAAAACGECUIAAAAAAAAAAAAghDBBCAAAAAAAAAAAAIQQJggBAAAAAAAAAACAEMIEIQAAAAAAAAAAABBCmCAEAAAAAAAAAAAAQggThAAAAAAAAAAAAEAIYYIQAAAAAAAAAAAACCFMEAIAAAAAAAAAAAAhhAlCAAAAAAAAAAAAIIQwQQgAAAAAAAAAAACEECYIAQAAAAAAAAAAgBDCBCEAAAAAAAAAAAAQQpggBAAAAAAAAAAAAEIIE4QAAAAAAAAAAABACGGCEAAAAAAAAAAAAAghTBACAAAAAAAAAAAAIYQJQgAAAAAAAAAAACCEMEEIAAAAAAAAAAAAhBAmCAEAAAAAAAAAAIAQwgQhAAAAAAAAAAAAEEKYIAQAAAAAAAAAAABCCBOEAAAAAAAAAAAAQAhhghAAAAAAAAAAAAAIIUwQAgAAAAAAAAAAACGECUIAAAAAAAAAAAAghDBBCAAAAAAAAAAAAIQQJggBAAAAAAAAAACAEMIEIQAAAAAAAAAAABBCmCAEAAAAAAAAAAAAQggThAAAAAAAAAAAAEAI+f8BAAD//xQI9iYAAAAGSURBVAMAW9CVeQIIYToAAAAASUVORK5CYII=)

*Nota.* Cada fila representa un instrumento del diagnóstico, cuyo porcentaje inicial sitúa el punto ocre a partir del autoinforme de treinta respondentes. La línea verde marca la madurez global de 99,09 % que el libro oficial de la institución calcula sobre la matriz posterior de treinta participantes, mientras las líneas de desplazamiento unen cada valor inicial con ese nivel institucional. Los seis instrumentos que el diagnóstico situaba en nivel Básico, de I13 a I10, quedan bajo el corte del 51 % y los ocho restantes en nivel Gestionado. Fuente: libro oficial de resultados del Servicio de Impuestos Nacionales y apartado 4.1 del marco práctico. Elaboración propia, 2026.

El libro oficial de resultados cierra la trazabilidad externa del capítulo, ya que vincula la propuesta metodológica con un resultado calculado por la organización que recibió la metodología. Ese vínculo es el que sostiene la contribución del trabajo en el plano institucional, donde la institución sitúa su propio proceso en el nivel Optimizado tras la aplicación de la metodología. El apartado siguiente sintetiza los resultados verificados y el resultado que el libro oficial calcula.

### 4.4.8 Síntesis de los resultados

Los resultados del capítulo se organizan en tres afirmaciones que la evidencia sostiene de manera directa y que pueden verificarse una por una en los archivos de origen. La primera afirma que la metodología convierte una línea base de cuatro escenarios medidos en diez escenarios medidos, sobre una campaña de diez escenarios cuyo inventario de técnicas se mantiene constante. La segunda afirma que la cobertura de detección pasa de cuatro a diez técnicas y de tres a seis tácticas, sin que el inventario de diecisiete técnicas cambie entre vueltas. La tercera afirma que el ciclo completo de corrección, desde la línea base hasta la medición final, se ejecuta en cuatro horas con veintiséis minutos.

A esas tres afirmaciones se suma la verificación del control que las hace interpretables, la cual confirma que el material sobre el que se mide permanece idéntico entre las dos vueltas. Los cuatro indicadores constantes de la Tabla 16, que abarcan la extensión de la campaña, el inventario de técnicas, el volumen de evidencia y su calidad, confirman que la diferencia entre las dos vueltas proviene de la reparación del instrumental y no de un cambio en el material sobre el que se mide. Esta condición es la que permite afirmar que la metodología produce la mejora que el apartado documenta y no una variación atribuible a las condiciones de ejecución.

El resultado del primer prototipo y el del segundo se complementan sin confundirse, dado que cada uno responde a una pregunta distinta del diseño metodológico. El primero verifica que cada componente de la metodología opera por separado, mientras que el segundo verifica el efecto de la corrección iterativa sobre el contexto institucional real. La Tabla 13 y la Tabla 15 responden a preguntas distintas, la primera sobre el funcionamiento de las piezas y la segunda sobre el efecto del ciclo completo, de manera que ninguna de las dos necesita corrigirse a la otra.

La conexión entre la línea base institucional y los resultados del laboratorio se establece por trazabilidad y no por escala común. Los seis instrumentos que el diagnóstico sitúa en nivel Básico cuentan con una fase asignada que los atiende y con un indicador de archivo que los verifica, según muestra la Tabla 19. Esa correspondencia permite afirmar que cada brecha diagnosticada recibe una respuesta metodológica identificable y comprobable, sin necesidad de superponer dos instrumentos de medición que responden a preguntas diferentes.

El estado de cumplimiento del tercer objetivo específico queda, en consecuencia, establecido sobre la base de indicadores que cualquier institución puede volver a producir con la misma configuración. La metodología propuesta se aplica sobre el contexto del Servicio de Impuestos Nacionales en dos iteraciones consecutivas, de las cuales la primera establece la línea base y la segunda mide el efecto de las correcciones que la línea base produjo. El resultado se expresa en indicadores verificables que comprueban la extensión de la medición, la cobertura de la detección y la duración del ciclo de mejora, con lo cual se completa el segundo objetivo específico y se habilita la validación del tercero.

# Capítulo V: Conclusiones y Recomendaciones de la Investigación

## 5.1 Conclusiones

*[Una conclusión por cada objetivo específico + una conclusión general. Deben derivarse directamente de los resultados del Marco Práctico. No introduzca información nueva.]*

Con respecto al objetivo específico 1: se concluye que [conclusión fundamentada en los resultados obtenidos].

Con respecto al objetivo específico 2: se concluye que [conclusión fundamentada en los resultados obtenidos].

Con respecto al objetivo específico 3: se concluye que [conclusión fundamentada en los resultados obtenidos].

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