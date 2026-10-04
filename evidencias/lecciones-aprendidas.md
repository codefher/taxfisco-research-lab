# Registro de lecciones aprendidas — Prototipo II (SIN)

> Registro vivo de la fase F5 (medición de impacto y lecciones aprendidas).
> Cada mejora de la iteración 2 debe citar su lección de origen en el mensaje
> de commit: `[P2] fix: <cambio> - leccion L<n>`.
> Estado actual: **reset a cero (2026-10-03)**. Se VACIÓ el registro completo
> (L1–L7 de las sesiones anteriores) para reiniciar la re-captura limpia de
> la iteración 1 desde un estado verificable. Las leccionesApplicable se
> registrarán de nuevo durante la re-captura, con evidencia y commit reales.

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

## Lecciones de la iteración 1 (v2.0-it1) — en curso de re-captura

| ID | Fase | Hallazgo | Causa raíz | Mejora aplicada | Commit | Estado |
|----|------|----------|------------|-----------------|--------|--------|
| — | — | (pendiente de la re-captura limpia) | — | — | — | — |

## Nota sobre el reset

Este registro se vació el 2026-10-03 como parte del reset completo del
laboratorio (ver commit `[P2] clean: reset total a cero`). Motivo: las lecciones
L1–L7 de las sesiones anteriores estaban ancladas a evidencia que se borró
(34 PNG en cuarentena, kpi_report.json de la sesión del 30 Sep, contenedores
con volúmenes re-inicializados), por lo que sus "Evidencia" ya no es
verificable. Bajo la regla de oro del proyecto (nada se afirma sin evidencia
verificable), se prefiere un registro vacío que se llenará con evidencia
fresca y verificable durante la re-captura.
