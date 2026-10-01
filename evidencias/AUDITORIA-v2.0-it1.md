# Auditoría de evidencia — v2.0-it1 (Prototipo II, laboratorio SIN)

> Fecha de auditoría: 2026-10-01. Auditor: sesión Kimi Work (agente de
> Fernando). Alcance: las 33 capturas PNG de `evidencias/v2.0-it1/`
> (secciones 01 a 06) y sus fuentes declaradas.
> Veredicto general: **la evidencia visual de v2.0-it1 NO es utilizable como
> evidencia de tesis en su estado actual.** El contenido es coherente con el
> laboratorio real, pero las capturas no son verificables como ejecuciones
> reales. Ver "Conclusión y recomendación".

## 1. Hallazgos

### H1. Las capturas de terminal son renders estilizados, no capturas reales (grave)

Las imágenes `01-entorno-servicios/*`, `03-aislamiento-red/*` y
`04-captura-eventos/05_wazuh-alertas.png` presentan marcos decorativos con
insignia "SIN / v2.0-it1", títulos compuestos, leyendas al pie
("Leyenda: red / contenedor / IP…") y pies de página ("Ejecución real en el
laboratorio SIN — proyecto docker-compose: sin-research-lab"). Ninguna
herramienta de captura de pantalla produce ese formato: son imágenes
**compuestas o generadas**, no screenshots.

Indicios técnicos adicionales:

- `04-captura-eventos/05_wazuh-alertas.png` afirma que su salida proviene de
  `python3 scripts/evidencia/fmt/wazuh.py`, **ruta que no existe en el
  repositorio** (la carpeta `scripts/` solo contiene scripts de
  certificados y verificación).
- Ninguna captura de terminal tiene su archivo `.txt` de respaldo, aunque el
  skill vigente (`capturas-evidencia-prototipo`) lo exige y la evidencia del
  Prototipo I sí lo tenía (p. ej. commit `8830f26`: `01_docker-ps.png` +
  `01_docker-ps.txt`).
- Los metadatos PNG están vacíos (sin software de captura), a diferencia de
  lo esperado en screenshots reales.
- Comparación directa: la evidencia del P1 (`8830f26`) sí son capturas
  auténticas de un terminal WSL (`fer@taxfisco:~/taxfisco-research-lab$`),
  con salida cruda e imperfecta (contenedores ajenos al lab visibles,
  servicios en estado Restarting). Las de v2.0-it1 son demasiado "limpias".

### H2. Sesión anterior incompleta: sin MANIFIESTO ni ÍNDICE

No existen `evidencias/v2.0-it1/MANIFIESTO.md` ni `evidencias/INDICE.md`,
entregables obligatorios del skill. Las 33 capturas llegaron en un único
commit (`7dd41df`), junto con la integración del analizador MISP en Cortex, y
la sesión se cerró sin trazabilidad (tag, hash, fecha, método de obtención
por captura). Es consistente con el relato del usuario: la sesión anterior se
confundió y colapsó.

### H3. Faltan las fuentes citadas de los KPI

`comparacion-iteraciones.md` cita como fuente `kpi_report.json` para los
MTTD de it1 (S01 16.40 s, S02 7.88 s, S05 1.05 s, S07 1.03 s), pero **no
existe ningún `kpi_report.json` en el repositorio**. Tampoco existe ningún
`attack-scenarios/*/evidencia/resultados.json` (las carpetas de escenarios
solo contienen `ejecutar.sh`). Los valores pueden haberse medido en su
momento, pero hoy son **no verificables** y no deben citarse en la tesis
hasta regenerar el reporte.

### H4. Secciones incompletas

Faltan las carpetas `07-metricas/`, `08-extremo-a-extremo/` y
`09-escenarios/` de la iteración 1, por lo que las capturas de checklist
N.º 8, 9 y 10 (indicadores it1, lecciones, comparativa) no tienen soporte.

### H5. Evento sintético mal etiquetado

`04-captura-eventos/05_wazuh-alertas.png` se titula a sí mismo
"(prueba sintetica)", pero el archivo no lleva el sufijo `_prueba-sintetica`
que exige el skill. Si se conservara, habría que renombrarlo; si se
re-captura, la etiqueta va en el nombre.

## 2. Lo que SÍ es coherente

- El contenido de las imágenes coincide con el laboratorio real: el
  proyecto docker-compose se llama efectivamente `sin-research-lab`
  (`docker-compose.yml`, línea 45), las redes `sin-dmz/soc/ids/honeypot` y
  los contenedores `sin-*` existen, y el señuelo usa la marca
  "Impuestos Nacionales" (contexto SIN, no TaxFisco).
- `05-enriquecimiento-custodia/02_thehive-caso.png` tiene apariencia de
  captura web real (TheHive 5.5.16, banner de licencia trial, caso #1 con
  fecha 30/09/2026). Aun así, sin manifiesto ni método de obtención
  documentado queda **no verificable** bajo la regla de oro.
- Las lecciones L1–L5 de `lecciones-aprendidas.md` sí tienen commits reales
  (`cf084b1`, `7eb1e16`, `67e623b`, `b1f9eca`, `7dd41df`) y son utilizables.

## 3. Conclusión y recomendación

Bajo la regla de oro del proyecto (nada se afirma sin evidencia verificable),
las 33 capturas quedan clasificadas como **NO VERIFICABLES**. No se borran
(queda a decisión del investigador), pero **no deben citarse en la tesis**.

Recomendación aprobada por el investigador (2026-10-01):

1. Re-capturar la evidencia de it1 con el protocolo del skill
   `capturas-evidencia-prototipo-2` (verificación previa obligatoria,
   capturas crudas + `.txt`, manifiesto obligatorio).
2. Regenerar `kpi_report.json` y los `resultados.json` de los escenarios
   antes de citar cualquier MTTD.
3. Completar secciones 07, 08 y 09 y los huecos del checklist (N.º 3, 4, 8,
   9 y 10).
4. Decidir el destino de las 33 imágenes auditadas: cuarentena
   (`_no-verificable/`) o eliminación, tras la re-captura exitosa.
5. Nota aparte: la evidencia original del Prototipo I (commit `8830f26`) fue
   vaciada de la carpeta por `e31ff30` ("clean: carpeta evidencias vacia
   para nuevo prototipo"). Si el apartado 4.3.5 aprobado cita rutas de ese
   material, verificar que las figuras vivas estén embebidas en el DOCX.
