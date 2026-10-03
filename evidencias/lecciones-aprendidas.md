# Registro de lecciones aprendidas — Prototipo II (SIN)

> Registro vivo de la fase F5 (medición de impacto y lecciones aprendidas).
> Cada mejora de la iteración 2 debe citar su lección de origen en el mensaje
> de commit: `[P2] fix: <cambio> - leccion L<n>`.
> Fuente de las lecciones de la iteración 1: historial de Git entre `v2.0-it1`
> y el cierre de la ejecución/análisis de la iteración 1.

## Convención de estados

| Estado | Significado |
|---|---|
| CERRADA | Causa raíz identificada y mejora aplicada y commiteada |
| ABIERTA | Detectada, mejora aún no aplicada |
| MONITOREO | Mitigada; se observa su recurrencia en la siguiente iteración |

## Plantilla para nuevas lecciones

```text
ID:           L<n>            ( correlativo, sin reutilizar )
Iteración:    it<n>           ( iteración donde se detectó )
Fase:         F1..F5          ( fase de la metodología donde ocurre )
Fecha:        YYYY-MM-DD
Hallazgo:     qué se observó, en qué escenario/servicio
Evidencia:    captura, log o commit que lo demuestra
Causa raíz:   por qué ocurrió
Mejora:       cambio propuesto o aplicado
Commit:       hash del commit [P2] que aplica la mejora
Estado:       CERRADA / ABIERTA / MONITOREO
```

## Lecciones de la iteración 1 (v2.0-it1)

| ID | Fase | Hallazgo | Causa raíz | Mejora aplicada | Commit | Estado |
|----|------|----------|------------|-----------------|--------|--------|
| L1 | F2 | Tras el primer `docker compose up` del P2, los nueve servicios no quedaron accesibles. | Servicios no iniciados/verificados en orden; dependencias sin esperar healthy. | Se dejaron accesibles los 9 servicios y se verificó la detección real de red y SIEM. | `cf084b1`, `7eb1e16` | CERRADA |
| L2 | F3 | Pérdida de los índices de TheHive, Cortex y Shuffle al recrear el contenedor del indexer. | `opensearch.yml` no definía `path.data`; OpenSearch usaba `<home>/data` (efímero) en lugar del volumen montado. | Se define `path.data` y `path.logs` al volumen; se regeneraron los índices (`cortex_6`, `thehive`, `thehive_global`) y la cuenta admin. | `67e623b` | CERRADA |
| L3 | F5 | El JSON de resultados del escenario S08 rompía el parser de KPIs. | Ruta Windows mal escapada en `drop_locations`. | Se simplificó `drop_locations` a rutas válidas. | `b1f9eca` | CERRADA |
| L4 | F2 | Velociraptor no respondía como el resto de servicios de gestión. | Usa autenticación HTTP Basic y su API exige el encabezado `Referer`. | Documentado en `docs/ACCESO-SERVICIOS-P2.md`; verificado acceso con sesión admin. | `b1f9eca` | CERRADA |
| L5 | F4 | El analizador MISP de Cortex no venía operativo en la imagen base. | La imagen oficial no incluía `cortexutils`/`pymisp` ni runner local. | Imagen propia (python3 + cortexutils + pymisp) con analizadores montados desde `config/cortex/analyzers`; MISP_2_1 operativo (1 evento de la campaña S01–S10). | `7dd41df` | CERRADA |

## Lecciones nuevas (iteración 2 en adelante)

| ID | Fase | Hallazgo | Causa raíz | Mejora aplicada | Commit | Estado |
|----|------|----------|------------|-----------------|--------|--------|
| L6 | F5 | El script maestro `attack-scenarios/run_all.sh` no podía ejecutar la campaña completa: construía `ATTACK_DIR=$SCRIPT_DIR/attack-scenarios` con `SCRIPT_DIR=/root/attack-scenarios`, dando una ruta duplicada inexistente; `ANALYSIS_DIR` apuntaba también a un path inexistente. | Bug de paths al maquetar `run_all.sh`: asume que el script vive un nivel arriba del árbol de escenarios, cuando realmente está dentro de `attack-scenarios/`. Sin el fix no se regeneran `kpi_report.json` ni `resultados.json` actualizados. | Re-cálculo mínimo de `ATTACK_DIR=$SCRIPT_DIR` y `ANALYSIS_DIR=/root/analysis` (volumen montado). Cambio verificado con `bash -x run_all.sh`. Mejora aplicada durante la re-captura de it1 para no bloquear la generación de fuentes; se documenta aquí como antecedente para que la corrección entre al release de la iteración 2. | (commit durante esta sesión) | CERRADA |
| L7 | F2 | La imagen `kalilinux/kali-rolling` del atacante llega sin `curl`, `jq`, `openssl`, `python3` instalados, por lo que los escenarios S04–S10 fallan en silencio (los `resultados.json` se escriben vacíos) y la fase 2 (kpi_calculator.py, mitre_coverage.py, iso27035_mapping.py) aborta con `python3: command not found`. | La imagen base oficial de Kali sólo trae las herramientas ofensivas (`nmap`, `sqlmap`, `hydra`); no incluye las utilidades que los `ejecutar.sh` y los scripts de análisis invocan. | Instalación efímera en el contenedor atacante durante la re-captura de it1: `apt-get update && apt-get install -y --no-install-recommends curl jq openssl python3 python3-pip`. Acción efímera (no persistente); para que entre a la release de it2 debe trasladarse a un Dockerfile propio con `FROM kalilinux/kali-rolling` + `RUN apt-get install ...`. | (commit durante esta sesión) | MONITOREO |
| L8 | | | | | | |
