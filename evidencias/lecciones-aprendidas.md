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
| L6 | | | | | | |
| L7 | | | | | | |
| L8 | | | | | | |
