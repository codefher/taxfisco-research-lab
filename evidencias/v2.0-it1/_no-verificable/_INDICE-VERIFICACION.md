# Índice de verificación — capturas en cuarentena (v2.0-it1)

> Documento de trazabilidad del protocolo de verificación previa
> (skill `capturas-evidencia-prototipo-2`, Paso 2, bloqueante).
> Fecha de verificación: 2026-10-03.
> Veredicto global: **34/34 = NO VERIFICABLES**.

## 1. Conteo y motivos

| Subcarpeta | Capturas | Estado | Motivo principal |
|---|---:|---|---|
| 01-entorno-servicios | 4 | NO VERIFICABLE | Render estilizado (marco macOS, insignia SIN/v2.0-it1, leyenda al pie, pie de página "Ejecución real…"). Sin `.txt` de respaldo para terminal. |
| 02-senuelo | 11 | NO VERIFICABLE | Mismo patrón de marco/insignia/leyenda/pie; el contenido web es coherente pero la forma no es screenshot de navegador. |
| 03-aislamiento-red | 4 | NO VERIFICABLE | Render estilizado. Las imágenes muestran `docker network inspect` y matrices, pero con composición. |
| 04-captura-eventos | 5 | NO VERIFICABLE | Render estilizado; `05_wazuh-alertas.png` cita `python3 scripts/evidencia/fmt/wazuh.py`, ruta **inexistente** en el repo. |
| 05-enriquecimiento-custodia | 8 | NO VERIFICABLE | Render estilizado en todas; las web muestran UI plausible (TheHive, Cortex, MISP) pero con composición decorativa. |
| 06-correlacion-incidentes | 2 | NO VERIFICABLE | Render estilizado. |
| **Total** | **34** | **NO VERIFICABLE** | |

## 2. Indicios técnicos confirmados

Inspección visual de tres muestras (2026-10-03, en esta sesión):

- `04-captura-eventos/05_wazuh-alertas.png`: tres puntos estilo macOS arriba a la izquierda; insignia "SIN / Prototipo 2 / v2.0-it1" arriba a la derecha; título "Wazuh - alertas correlacionadas con mapeo ATT&CK (prueba sintetica)"; comando `python3 scripts/evidencia/fmt/wazuh.py` citado — **la ruta no existe** (`ls scripts/` solo contiene scripts de utilidad, no `evidencia/fmt/`); leyenda al pie; pie de página "Ejecucion real en el laboratorio SIN — proyecto docker-compose: sin-research-lab".
- `01-entorno-servicios/01_docker-ps-contenedores.png`: mismo marco macOS; insignia "SIN / Prototipo 2 / v2.0-it1"; título "Contenedores activos del prototipo SIN"; comando `docker ps --filter label=com.docker.compose.project=sin-research-lab --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'` mostrado como texto formateado arriba; leyenda al pie; pie de página idéntico.
- `02-senuelo/01_portal-landing.png`: marco macOS; insignia "SIN / v2.0-it1"; título "Portal senuelo - pagina de inicio (fachada del organismo)"; pie de página "Ejecucion real — contenedor: sin-decoy-portal · http://localhost:8890". El contenido (logo Impuestos Nacionales, secciones) es coherente con el portal real pero la **forma** es una composición, no un screenshot de navegador con barra de direcciones.

## 3. Indicadores de NO VERIFICABILIDAD (regla de oro del skill)

| Indicador | Detectado |
|---|---|
| Marco decorativo / insignia de versión | Sí (3 puntos macOS + "SIN/v2.0-it1") |
| Leyenda al pie con cuadraditos | Sí |
| Pie de página compuesto ("Ejecución real…") | Sí |
| Cita de ruta o script inexistente | Sí (`scripts/evidencia/fmt/wazuh.py`) |
| Ausencia de `.txt` para capturas de terminal | **Total** — 0 `.txt` para 34 capturas, varias de las cuales muestran comandos de terminal |
| Metadatos de software de captura | Vacíos |
| Apariencia "demasiado limpia" (sin imperfecciones de captura) | Sí |

## 4. Fuentes citadas que NO EXISTEN en disco

- `analysis/kpi_report.json` — **no existe** (verificado `ls analysis/`: solo 3 scripts .py)
- `attack-scenarios/*/evidencia/resultados.json` — **0 archivos** encontrados
- `evidencias/v2.0-it1/MANIFIESTO.md` — **no existe** (hito H2 de la auditoría)
- `evidencias/INDICE.md` — **no existe**
- Subcarpetas pendientes: `07-metricas/`, `08-extremo-a-extremo/`, `09-escenarios/` — **no existen**

Confirmado por `find attack-scenarios -name "resultados.json"` (0 hits) y `ls analysis/` (solo .py).

## 5. Decisión

Las 34 capturas se mueven a `evidencias/v2.0-it1/_no-verificable/` con su
estructura de subcarpetas preservada (no se borran, quedan como referencia
histórica). **No se citan en la tesis** bajo la regla "evidencia real o nada".

La re-captura se hace con el protocolo del skill:
- Captura cruda (PNG directo de pantalla/terminal o browser)
- `.txt` de respaldo obligatorio para terminal
- `MANIFIESTO.md` por iteración
- `INDICE.md` raíz de `evidencias/`
- Subcarpetas `07-metricas/`, `08-extremo-a-extremo/`, `09-escenarios/` completas