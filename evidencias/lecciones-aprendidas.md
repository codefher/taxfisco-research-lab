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
| L11 | Seis escenarios no dejan MTTD | ABIERTA  CERRADA en it2 | Resuelta en it2: el calculador leia `targets_scanned` y ningun escenario usaba ese nombre |
| L12 | La campaña S01–S10 se bloqueaba en S04 | ABIERTA  CERRADA en it2 | sqlmap, hydra y nikto se ejecutaban sin limite de tiempo |
| L13 | S09 informaba "Cowrie capturó los intentos" sin que hubiera conexion | ABIERTA  CERRADA en it2 | sshpass no estaba instalado y el escenario no lo comprobaba |
| L14 | S08 depositaba el fichero en OpenCanary y S10 exfiltraba por DNS, sin fuente que lo leyera | ABIERTA  CERRADA en it2 | El calculador no tenia fuentes para OpenCanary ni para el DNS de Zeek |

## Lecciones cerradas en la iteración 2 (v2.1-it2)

Estas cuatro eran el alcance de it2. Todas con la misma estructura de la
plantilla y con el commit que las aplica.

| ID | Fase | Hallazgo | Causa raíz | Mejora aplicada | Estado |
|----|------|----------|------------|-----------------|--------|
| L11 | F5 | Seis escenarios (S03, S04, S06, S08, S09, S10) quedaban como "sin deteccion" pese a que el señuelo sí registró el ataque | El calculador leía la clave `targets_scanned` para saber a qué señuelo atribuir la detección, pero S01 y S02 la escribían con ese nombre, S04 usaba `targets`, S03, S05 y S09 usaban `target` (como cadena) y S06, S07, S08 y S10 no la guardaban. `allowed_sources()` devolvía siempre el conjunto vacío y la detección por ventana no llegaba a aplicarse | `scenario_targets()` acepta las tres variantes, envuelve los valores de tipo cadena en lista y los cuatro escenarios sin objetivo lo declaran | CERRADA |
| L12 | F2 | La campaña se quedaba bloqueada en S04 y no llegaba a los escenarios siguientes | `sqlmap --level=3 --risk=2`, `hydra` y `nikto` se ejecutaban sin límite de tiempo | `timeout 180` en los dos sqlmap, `timeout 150` en hydra y nikto, más `--timeout=10` en sqlmap | CERRADA |
| L13 | F2 | S09 imprimía "[OK] Cowrie capturó los intentos" sin que hubiera conexión alguna | `sshpass` no estaba instalado en el contenedor atacante; el `|| true` del script ocultaba el fallo y el mensaje final no lo comprobaba | Se comprueba la herramienta al inicio y el cierre distingue `[OK]` de `[PARCIAL]`; además se instaló `sshpass` y `gobuster` | CERRADA |
| L14 | F3 | S08 (depósito de fichero en OpenCanary) y S10 (exfiltración por DNS) nunca podían detectarse | El calculador solo consultaba el log de ataques del decoy-api, las peticiones del portal y las conexiones de Cowrie; no existía fuente para OpenCanary ni para el DNS de Zeek, pese a que ambos registraban los eventos | `load_opencanary_alerts()` y `load_zeek_dns()` como fuentes de detección, con sus salidas en `allowed_sources()` | CERRADA |

### Efecto combinado sobre la medición

| | it1 | it2 |
|---|---|---|
| Escenarios con MTTD medido | 4 de 10 | **10 de 10** |
| MTTD medio | 5,22 s | 2,02 s |
| MTTD mínimo / máximo | 1,06 s / 16,85 s | 0,00 s / 15,91 s |

Las tres lecciones de instrumentación (L11, L13, L14) no mejoraron la
detección: **la detección ya funcionaba desde it1**. Lo que estaba roto era el
instrumento que la medía. Por eso la media baja: it1 medía solo los cuatro
escenarios que el calculador conseguía atribuir, y it2 mide los diez.

## Nota sobre el reset

Este registro se vació el 2026-10-03 como parte del reset completo del
laboratorio (ver commit `[P2] clean: reset total a cero`). Motivo: las lecciones
L1–L7 de las sesiones anteriores estaban ancladas a evidencia que se borró
(34 PNG en cuarentena, kpi_report.json de la sesión del 30 Sep, contenedores
con volúmenes re-inicializados), por lo que sus "Evidencia" ya no es
verificable. Bajo la regla de oro del proyecto (nada se afirma sin evidencia
verificable), se prefiere un registro vacío que se llenará con evidencia
fresca y verificable durante la re-captura.
