# Índice de evidencias — Prototipo II (laboratorio SIN)

Punto de entrada a la evidencia del prototipo. Cada figura va acompañada de su
fichero `.txt` con la salida real del comando, que es la fuente verificable.

## Iteración 1 (`v2.0-it1`)

- Fecha de captura: 2026-10-04
- Commit de captura: `385a2e1` (laboratorio y cadena de detección)
- Manifiesto con trazabilidad completa: [`v2.0-it1/MANIFIESTO.md`](v2.0-it1/MANIFIESTO.md)

| Subcarpeta | N.º | Contenido |
|---|---|---|
| `01-entorno-servicios/` | 4 | Contenedores, imágenes propias, servicios declarados e índices del SIEM |
| `02-senuelo/` | 5 | Portal SIN: inicio, acceso por NIT, verificación en dos pasos, alta y panel |
| `03-aislamiento-red/` | 4 | Redes `sin-*`, subredes y prueba de segmentación desde el atacante |
| `04-captura-eventos/` | 4 | Alertas del SIEM con MITRE, panel, reglas IDS y logs NDR |
| `05-enriquecimiento-custodia/` | 2 | Hash SHA-256 de la evidencia y registro de ataques con TLP |
| `06-correlacion-incidentes/` | 2 | Ataques con técnica MITRE y disponibilidad del SOAR |
| `07-metricas/` | 2 + JSON | Indicadores y cobertura; incluye los JSON fuente |

**Total: 23 figuras** (18 registros de terminal + 5 capturas de navegador).

## Iteración 2 (`v2.1-it2`)

- Fecha de ejecución: 2026-10-04
- Manifiesto con trazabilidad completa: [`v2.1-it2/MANIFIESTO.md`](v2.1-it2/MANIFIESTO.md)

Las figuras de esta iteración **no repiten** las de la iteración 1: cada una
documenta una mejora concreta, que es lo que corresponde a la fase de iteración
de la tesis.

| Subcarpeta | N.º | Contenido |
|---|---|---|
| `01-entorno-servicios/` | 1 | Las diez herramientas del atacante disponibles (L13) |
| `03-aislamiento-red/` | 1 | El atacante alcanza los señuelos y no alcanza la red SOC |
| `04-captura-eventos/` | 6 | S09 capturado por Cowrie (L13), S08 en OpenCanary y S10 en Zeek (L14), inventario de herramientas (L12), alertas del SIEM y panel |
| `05-enriquecimiento-custodia/` | 1 | Hash SHA-256 de la evidencia tras la campaña |
| `06-correlacion-incidentes/` | 1 | Ataques con técnica MITRE, táctica y TLP |
| `07-metricas/` | 3 | Indicadores, MTTD por escenario con su fuente (L11, L14) y comparación it1 vs it2 |

**Total: 16 figuras** (15 registros de terminal + 1 captura de navegador).

Las tres que sostienen la fase de iteración son
`07-metricas/03_mejora-it1-vs-it2` (los seis escenarios recuperados y el salto de
4/10 a 10/10), `07-metricas/02_mttd-por-escenario-con-fuente` (los diez con la
fuente que los detectó) y `04-captura-eventos/01_s09-capturado-por-cowrie`
(el evento que antes no se producía).

**Aviso de lectura:** la media de MTTD baja de 5,22 s a 2,02 s porque en it1 se
medían cuatro escenarios y en it2 los diez. El señuelo detectaba igual en
ambas. La comparación defendible es la por escenario.

## Fuentes de datos de las métricas

Ficheros versionados en `v2.0-it1/07-metricas/`:

| Fichero | Contenido |
|---|---|
| `kpi_report.json` | Indicadores de it1 (MTTD en 4 de 10 escenarios) |
| `mitre_coverage.json` | 17 técnicas implementadas, 10 detectadas |
| `iso27035_compliance.json` | Evidencia por las 5 fases de ISO/IEC 27035 |
| `resultados-escenarios/` | `resultados.json` de S01 a S10 |

En `v2.1-it2/07-metricas/` se versionan los equivalentes de la iteración 2:
`kpi_report.json` (MTTD en los 10 escenarios) y
`resultados-escenarios/` con los `resultados.json` de la segunda ejecución.

## Registros

| Documento | Contenido |
|---|---|
| [`lecciones-aprendidas.md`](lecciones-aprendidas.md) | Lecciones L1–L7 cerradas y L8–L11 abiertas, con causa raíz y commit |
| [`comparacion-iteraciones.md`](comparacion-iteraciones.md) | Tabla it1 con valores reales y su fuente; it2 pendiente |
| [`AUDITORIA-v2.0-it1.md`](AUDITORIA-v2.0-it1.md) | Auditoría que motivó la re-captura |

## Cómo se reprodujo

| Qué | Cómo |
|---|---|
| Figura de terminal | `bash scripts/fig.sh <carpeta> <nombre> "<comando>" [iteracion]` |
| Captura de navegador | Playwright con viewport 1280×720 |
| Ingesta IDS antes de capturar | `bash scripts/reset-ids-offset.sh` |
| Métricas | `python3 analysis/kpi_calculator.py` |
| Informe de it2 sin pisar it1 | `KPI_OUTPUT=analysis/kpi_report_it2.json python3 analysis/kpi_calculator.py` |
| Comprobar que las figuras son fieles | `python3 scripts/verificar-figuras.py evidencias/v2.0-it1` |

## Naturaleza de las figuras

Las de terminal son **registros de salida compuestos desde el `.txt` real**, no
fotografías de pantalla: el diseño lo compone la herramienta y el texto sale del
`.txt` sin modificar un carácter. Las de navegador (portal del señuelo y panel
del SIEM) son capturas directas.

`scripts/verificar-figuras.py` deshace las etiquetas del HTML de cada figura y lo
compara con su `.txt` línea a línea, además de comprobar el SHA-256 registrado
en el manifiesto de renderizado. Estado actual: **it1 17/17 e it2 16/16
verificadas**. Esta comprobación ya ha detectado dos fallos reales (un espacio
de más en el prompt y tres `.txt` de it1 alterados), con lo que no es un
trámite.

## Limitaciones conocidas

| ID | Asunto | Efecto |
|---|---|---|
| L8 | Wazuh Dashboard carga el shell pero no renderiza las vistas; la imagen local parece incompleta y la descarga se corta | La visualización del SIEM se aporta con Grafana contra el mismo índice |
| L9 | TheHive 5.5 redirige toda ruta a su página de organizaciones por el estado de licencia en prueba | Impide la vista de casos y, con ella, medir MTTR, MTTC y MTTContain |
| L10 | La red `sin-ids` (10.23.0.0/24) está declarada pero no se crea, porque Suricata y Zeek corren en `network_mode: host` | En ejecución hay tres segmentos, no cuatro como describe el capítulo |
| L11 | Cerrada en it2: seis escenarios no tenían MTTD medido | Resuelta: 10 de 10 escenarios con MTTD |

## Estado del laboratorio al cierre

| Comprobación | Resultado |
|---|---|
| Contenedores en ejecución | 25 de 25 |
| Reinicios de los contenedores críticos | 0 |
| Servicios de gestión autenticados | 7 de 7 responden 200 |
| Campaña de ataque | 10 de 10 escenarios ejecutados |
| Escenarios con MTTD medido | 10 de 10 |
| Figuras verificadas contra su fuente | it1 17/17, it2 16/16 |
