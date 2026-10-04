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

## Lecciones de la iteración 1 (v2.0-it1)

Detectadas durante la re-captura limpia del 2026-10-04. Todas tienen causa raíz
identificada y mejora aplicada y commiteada.

| ID | Fase | Hallazgo | Causa raíz | Mejora aplicada | Commit | Estado |
|----|------|----------|------------|-----------------|--------|--------|
| L1 | F3 | El SIEM no generaba alertas: `wazuh-analysisd` no ingería los logs de Suricata ni Zeek | `ossec.conf` quedaba con XML inválido porque el bloque de `localfile` se añadía **después** del elemento raíz, y el init de la imagen añade un segundo `<ossec_config>` sobrante | `10-sin-localfiles.sh` inserta los `localfile` dentro de la raíz y absorbe el bloque sobrante, con validación XML y copia de seguridad | `c66f7c7` | CERRADA |
| L2 | F3 | Las alertas nunca llegaban al índice: `400 unknown parameter [_type]` | filebeat 7.10.2 (el que trae `wazuh-manager 4.10.4`) incluye `_type` en la metadata del bulk; OpenSearch 2.19 lo rechaza. Se probó módulo `wazuh`, input `filestream`, input `log` y `es_doc_type` vacío: ninguno lo evita | Publicador propio `sin-alert-publisher.py` que indexa `alerts.json` por HTTP `_bulk` con basic auth, sin `_type` | `c66f7c7` | CERRADA |
| L3 | F2 | El manager reiniciaba cada ~2 min: `s6-finish` terminaba el container | Con `output.elasticsearch`, filebeat entra en panic al negociar TLS contra OpenSearch 2.19 y sale con código 2; s6 interpreta la caída del servicio como fin del container. Con `es_doc_type: ""` el crash era inmediato | filebeat queda con `output.console` y un input inerte; la indexación la hace el publicador | `20ee788` | CERRADA |
| L4 | F3 | Suricata seguía detectando pero Wazuh dejo de generar alertas tras miles de líneas | `wazuh-logcollector` guarda la posición de lectura de cada localfile en la base del manager; `alert-events.json` no rota, el offset queda desfasado y las líneas nuevas se ignoran | `scripts/reset-ids-offset.sh` (`make ids-reset`): trunca el archivo para forzar el reinicio de lectura y reinicia `analysisd` | `2d13573` | CERRADA |
| L5 | F5 | Los paneles de Grafana mostraban "No data" | El datasource `elasticsearch` de Grafana 11 genera `"order": {}` en toda agregación `terms`; OpenSearch 2.19 responde `400 Must specify at least one field for [order]`. Es una incompatibilidad de versión, no de configuración | `scripts/convert-grafana-ppl-to-lucene.py` convierte los 17 targets PPL; las categorías se obtienen con consultas Lucene por rango en vez de `terms` | `20ee788` | CERRADA |
| L6 | F5 | Los paneles devolvían 0 despite de haber documentos | Las alertas llevan el campo `timestamp`; el index pattern, los dashboards y el indexer usan `@timestamp` como campo temporal | El publicador copia `timestamp` a `@timestamp` y añade `rule.sev` (severidad), que antes se calculaba con PPL | `20ee788` | CERRADA |
| L7 | F2 | Un fallo puntual de un entrypoint tumbaba el laboratorio entero | Los entrypoint scripts corren con `set -e`: cualquier error aborta el init, s6 termina el container y `restart: unless-stopped` lo reinicia en bucle | Los tres scripts son a prueba de fallos: restauran copia de seguridad y devuelven 0 siempre | `c66f7c7` | CERRADA |

### Detalle de L1 (la más costosa)

Manifestación: `Error reading XML file 'etc/ossec.conf'`, luego
`Too many fields for JSON decoder` en bucle, luego nada. La detección costó
varios intentos porque el síntoma visible (cero alertas) no señalaba la causa.
El error quecerraba el diagnóstico fue que el propio script de captura había
degradado el archivo al absorber el bloque sobrante, de modo que el síntoma se
autofeeding.

### Lecciones abiertas

| ID | Hallazgo | Estado | Nota |
|----|----------|--------|------|
| L8 | Wazuh Dashboard carga el shell pero no renderiza las vistas; la imagen local parece incompleta y la descarga posterior se corta | ABIERTA | Se sustituyó por Grafana para la visualización del SIEM |
| L9 | TheHive 5.5 redirige toda ruta a `/administration/organisations` por su estado de licencia en prueba | ABIERTA | Impide la vista de casos y la medición de MTTR |
| L10 | `sin-ids` (10.23.0.0/24) está declarada en el compose pero nunca se crea | ABIERTA | Suricata y Zeek corren en `network_mode: host`; en ejecución hay 3 segmentos, no 4 |
| L11 | Seis escenarios (S03, S04, S06, S08, S09, S10) no dejan MTTD | ABIERTA | Requeriría instrumentar el registro del señuelo para esos vectores |

## Nota sobre el reset

Este registro se vació el 2026-10-03 como parte del reset completo del
laboratorio (ver commit `[P2] clean: reset total a cero`). Motivo: las lecciones
L1–L7 de las sesiones anteriores estaban ancladas a evidencia que se borró
(34 PNG en cuarentena, kpi_report.json de la sesión del 30 Sep, contenedores
con volúmenes re-inicializados), por lo que sus "Evidencia" ya no es
verificable. Bajo la regla de oro del proyecto (nada se afirma sin evidencia
verificable), se prefiere un registro vacío que se llenará con evidencia
fresca y verificable durante la re-captura.
