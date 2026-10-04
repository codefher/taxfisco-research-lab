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

**Total: 22 figuras** (17 registros de terminal + 5 capturas de navegador).

## Fuentes de datos de las métricas

Ficheros versionados en `v2.0-it1/07-metricas/`:

| Fichero | Contenido |
|---|---|
| `kpi_report.json` | Indicadores (MTTD medido; MTTR/MTTC/MTTContain sin muestras) |
| `mitre_coverage.json` | 17 técnicas implementadas, 10 detectadas |
| `iso27035_compliance.json` | Evidencia por las 5 fases de ISO/IEC 27035 |
| `resultados-escenarios/` | `resultados.json` de S01 a S10 |

## Registros

| Documento | Contenido |
|---|---|
| [`lecciones-aprendidas.md`](lecciones-aprendidas.md) | Lecciones L1–L7 cerradas y L8–L11 abiertas, con causa raíz y commit |
| [`comparacion-iteraciones.md`](comparacion-iteraciones.md) | Tabla it1 con valores reales y su fuente; it2 pendiente |
| [`AUDITORIA-v2.0-it1.md`](AUDITORIA-v2.0-it1.md) | Auditoría que motivó la re-captura |

## Cómo se reprodujo

| Qué | Cómo |
|---|---|
| Figura de terminal | `bash scripts/fig.sh <carpeta> <nombre> "<comando>"` |
| Captura de navegador | Playwright con viewport 1280×720 |
| Ingesta IDS antes de capturar | `bash scripts/reset-ids-offset.sh` |
| Métricas | `python3 analysis/kpi_calculator.py` |

## Naturaleza de las figuras

Las de terminal son **registros de salida renderizados desde el `.txt` real**, no
fotografías de pantalla. Las de navegador (portal del señuelo y panel del SIEM)
son capturas directas.
