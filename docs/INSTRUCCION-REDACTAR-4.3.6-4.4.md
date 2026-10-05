# Instrucción de redacción — apartados 4.3.6 y 4.4 (Prototipo II)

> Fecha: 2026-10-05. Base: evidencia real re-capturada el 2026-10-04
> (`v2.0-it1`, 28 figuras; `v2.1-it2`, 16 figuras), verificada 17/17 y
> 16/16 por `scripts/verificar-figuras.py`.
> Objetivo: reajustar y redactar los puntos pendientes del segundo
> prototipo y del apartado de resultados, sustituyendo las marcas
> `[Pendiente...]` por contenido con fuente. Documento maestro:
> `tesis/Redaccion_Marco_Practico_v10.md` (estructura v9, aprobada).

## 1. Reglas de oro

1. **Nada sin fuente versionada.** Cada número, figura o afirmación técnica
   debe poder rastrearse a `evidencias/v2.0-it1/`, `evidencias/v2.1-it2/`
   o a un commit. Si la fuente no existe, la marca `[Pendiente]` se
   conserva.
2. **El 4.3.5 (Prototipo I) no se toca.** Está aprobado por la tutora.
   Solo se toca el 4.3.6, el 4.4 y las referencias cruzadas que apunten a
   evidencia del P2.
3. **Naturaleza honesta de las figuras.** Las figuras de terminal son
   *registros de salida compuestos desde el `.txt` real* (texto sin
   modificar, verificado contra su fuente). En la tesis se llaman
   "registro de salida", nunca "captura de pantalla". Las figuras de
   navegador (portal del señuelo, consolas) sí son capturas directas y se
   llaman "captura".
4. **Las limitaciones se declaran, no se ocultan.** Las restricciones
   conocidas (L8–L10, MISP sin eventos, Cortex sin usuario) se redactan
   como limitaciones explícitas, no se maquillan.
5. **Estilo.** Presente intemporal, registro académico UMSA, notas de
   figura/tablas en formato APA 7. Aplicar el skill
   `humanizar-redaccion-v7` sobre la redacción final.
6. **Commits.** Prefijo `[P2] tesis:` y referencia al apartado
   (p. ej. `[P2] tesis: 4.4.5 - comparacion por escenario it1 vs it2`).

## 2. Lectura obligatoria antes de redactar

| Orden | Archivo | Para qué |
|---|---|---|
| 1 | `evidencias/INDICE.md` | Mapa completo de las 44 figuras y avisos de lectura |
| 2 | `evidencias/v2.0-it1/MANIFIESTO.md` | Trazabilidad de it1 (tag, commit, método) |
| 3 | `evidencias/v2.1-it2/MANIFIESTO.md` | Trazabilidad de it2 |
| 4 | `evidencias/comparacion-iteraciones.md` | Tabla it1 vs it2 ya rellena con fuentes |
| 5 | `evidencias/lecciones-aprendidas.md` | L1–L7 cerradas en it1; L11–L14 cerradas en it2; L8–L10 abiertas |
| 6 | `evidencias/v2.0-it1/07-metricas/kpi_report.json` y `v2.1-it2/07-metricas/kpi_report.json` | Valores reales de MTTD |
| 7 | `evidencias/v2.0-it1/07-metricas/mitre_coverage.json` y `iso27035_compliance.json` | Cobertura ATT&CK e ISO 27035 |

## 3. Datos reales disponibles (no inventar otros)

### Iteración 1 (2026-10-04, commit de captura `385a2e1`)

- Campaña: 10 de 10 escenarios ejecutados. 54 ataques registrados por el
  señuelo, 725 peticiones a la API, 7 conexiones Cowrie, 15 765 peticiones
  al portal.
- **MTTD medido en 4 de 10 escenarios** (media 5,22 s; mín 1,06 s; máx
  16,85 s): S01 = 16,85 s (T1595, decoy-api), S02 = 1,21 s (T1595.002,
  decoy-portal), S05 = 1,73 s (T1110.004), S07 = 1,06 s. Los otros seis
  quedaron como "sin detección" **por atribución rota del calculador, no
  por ausencia de eventos** (lección L11) — matiz obligatorio en la
  redacción.
- 17 técnicas ATT&CK implementadas, 10 detectadas; cobertura ISO/IEC
  27035: 5 de 5 fases.

### Iteración 2 (2026-10-04)

- Campaña: 10 de 10. 254 ataques registrados, 1 508 peticiones API, 38
  conexiones Cowrie, 78 186 peticiones al portal.
- **MTTD medido en 10 de 10 escenarios** (media 2,02 s; mín 0,00 s; máx
  15,91 s): S01 15,91 s; S02 1,09 s; S03 0,00 s (cowrie); S04 0,14 s
  (decoy-portal); S05 1,15 s; S06 0,46 s (decoy-portal); S07 0,26 s;
  S08 0,56 s (opencanary); S09 0,00 s (cowrie); S10 0,65 s (zeek-dns).

### Comparación defendible

- **Solo por escenario, nunca por la media.** La media de it1 (5,22 s, 4
  muestras) no es comparable con la de it2 (2,02 s, 10 muestras): el
  instrumento de it1 no atribuía seis detecciones ya existentes.
  Reducciones por escenario: S01 −5,6 %, S02 −9,9 %, S05 −33,5 %,
  S07 −75,5 %.
- MTTR / MTTC / MTTContain: **no medidos** (TheHive 5.5 bloqueado por
  licencia de prueba, L9). Se declaran como no disponibles, con la causa.
- IIAM e IMGI: **no medidos** (pendiente de decisión, ver sección 6).

## 4. Mapeo punto por punto (qué evidencia rellena qué apartado)

| Apartado | Evidencia que lo sostiene | Qué hacer |
|---|---|---|
| 4.3.6.1 Tabla de equivalencia | `01-entorno-servicios/`, `03-aislamiento-red/01_docker-network-ls` (+`.txt`), `02-senuelo/` | Quitar todas las marcas `[pendiente: captura]`; la fila de redes debe reflejar que `sin-ids` quedó declarada pero no creada (L10) |
| 4.3.6.2 Fase 1 (diseño SIN) | `02-senuelo/01`–`05` (inicio, login por NIT, verificación en dos pasos, alta, panel) | Sustituir marcas N.º 3 y 4 por las cinco capturas de navegador |
| 4.3.6.3 Fase 2 (aislamiento) | `03-aislamiento-red/01`–`04` | **Reajuste:** el texto actual dice "cuatro redes"; en ejecución hay **tres segmentos** (L10). Redactar: tres segmentos efectivos, con la cuarta red declarada pero no instanciada, y justificación |
| 4.3.6.4 Fase 3 (captura/custodia) | `04-captura-eventos/01`–`04`, `05-enriquecimiento-custodia/01` (hash SHA-256) | Sustituir marcas; **no afirmar enriquecimiento MISP** (sin eventos) ni análisis Cortex (sin usuario) |
| 4.3.6.5 Fase 4 (correlación) | `06-correlacion-incidentes/01`–`02` (ataques con técnica MITRE; SOAR disponible) | Redactar correlación como mapeo a MITRE + disponibilidad del SOAR; declarar que la vista de casos de TheHive quedó restringida por licencia (L9) — no afirmar casos creados |
| 4.3.6.6.1 Esquema de iteraciones | Figura de diseño propio (no es evidencia) | Dibujar el ciclo preprueba → lecciones → mejoras → posprueba; reemplazar la marca de figura |
| 4.3.6.6.2 Iteración 1 | `07-metricas/01_kpi-indicadores`, `kpi_report.json` (it1) | Sustituir marca N.º 8; reportar 4/10 con el matiz de atribución (L11) |
| 4.3.6.6.3 Lecciones y mejoras | `lecciones-aprendidas.md` (L1–L7, commits `c66f7c7`, `20ee788`, `2d13573`) | Tabla de lecciones con causa raíz y commit; sustituir marca N.º 9 |
| 4.3.6.6.4 Iteración 2 | `v2.1-it2/07-metricas/01`–`03` | Reportar 10/10; sustituir marca N.º 10 |
| 4.3.6.6.5 Invariantes | Tabla de condiciones invariantes (redactar; base en `comparacion-iteraciones.md`) | Escenarios, criterios de medición y arquitectura idénticos; remitir al 4.4.1 |
| 4.3.6.7 Síntesis P2 | Todo lo anterior | Cierre con conteos reales: 28 figuras it1 + 16 it2, 10/10 escenarios ambas |
| 4.4.1 Diseño de comparación | Definición de MTTD de `analysis/kpi_calculator.py` | Tabla de invariantes; declarar la definición exacta de inicio (marca del escenario) y detección (primer evento del sensor) |
| 4.4.2 Medición it1 | `kpi_report.json` it1, `mitre_coverage.json`, `iso27035_compliance.json` | Tabla MTTD por escenario (4 valores + 6 "sin atribución"); coberturas ATT&CK (17/10) e ISO 27035 (5/5) |
| 4.4.3 Análisis it1 | `lecciones-aprendidas.md` (L1–L7) | Tabla de lecciones con evidencia y commit |
| 4.4.4 Medición it2 | `kpi_report.json` it2 | Tabla MTTD completa 10/10 con la fuente que detectó cada escenario |
| 4.4.5 Comparación | `comparacion-iteraciones.md`, `v2.1-it2/07-metricas/03_mejora-it1-vs-it2` (+`.txt`) | **Tabla por escenario como comparación principal.** La prueba de Wilcoxon queda condicionada a la decisión 6-a |
| 4.4.6 Hipótesis y metas | Datos por escenario; Tabla 2 del apartado 1.6 | Evaluar la meta de reducción de MTTD con los cuatro escenarios pareados; IIAM/IMGI según decisión 6-b |
| 4.4.7 Síntesis | Todo lo anterior | Incluir limitaciones L8–L10 y servicios no operativos (MISP sin eventos, Cortex sin usuario) como limitaciones reconocidas |

## 5. Reajustes obligatorios detectados

1. **Redes: "cuatro" → tres segmentos efectivos** (4.3.6.1 y 4.3.6.3), con
   `sin-ids` declarada pero no instanciada (Suricata y Zeek en
   `network_mode: host`). Justificar la decisión y citar L10.
2. **Eliminar cualquier afirmación de enriquecimiento MISP o casos
   TheHive** en el 4.3.6 y el 4.4 (pertenecían a la evidencia no
   verificable). Sustituir por el estado real: correlación por mapeo
   MITRE, SOAR disponible, casos bloqueados por licencia (L9).
3. **La media de MTTD no es la comparación principal.** Usar la tabla por
   escenario; si se mencionan las medias, acompañarlas siempre del número
   de muestras (4 vs 10) y del matiz de atribución.
4. **MTTR, MTTC y MTTContain: declarar "no medidos"** con su causa (L9),
   no omitirlos ni estimarlos.
5. **Figuras: numeración final.** Reemplazar todos los placeholders
   "Figura X" / "Tabla X" del 4.3.6 y el 4.4 por numeración correlativa
   definitiva, con nota y fuente bajo cada una.

## 6. Decisiones pendientes del investigador (resolver antes de redactar el 4.4.5–4.4.6)

| # | Decisión | Opciones |
|---|---|---|
| a | **Prueba de Wilcoxon.** El 4.2.7 comprometió una prueba pareada, pero it1 solo tiene 4 escenarios atribuibles | A) Re-ejecutar la campaña it1 con el calculador corregido (10 muestras pareadas) y hacer la Wilcoxon; B) presentar la comparación por escenario y declarar la prueba como limitación. **Recomendación: A si el lab sigue operativo; consultar con la tutora** |
| b | **IIAM e IMGI.** Dependen de casos de TheHive que no se pudieron crear | A) Recalcular con los datos disponibles redefiniendo el índice; B) declararlos fuera del alcance por L9 y ajustar el 1.6/4.2.7 |
| c | **Cuarentena definitiva.** Los 34 PNG no verificables siguen en `_no-verificable/` | Tras cerrar la redacción del 4.3.6, decidir borrado definitivo o conservación |
| d | **Figura del ciclo de iteraciones (4.3.6.6.1)** | Dibujarla como diagrama propio (herramienta de diagramas o TikZ en el DOCX final) |

## 7. Flujo de trabajo sugerido

1. Resolver las decisiones 6-a y 6-b (son las que condicionan el 4.4).
2. Redactar el 4.3.6 en orden (4.3.6.1 → 4.3.6.7), verificando cada cifra
   contra su fuente antes de escribirla.
3. Redactar el 4.4 en orden, alimentándose de `comparacion-iteraciones.md`.
4. Revisar las referencias cruzadas (4.3.6.x ↔ 4.4.x ↔ 3.2 ↔ 1.6) y
   actualizar las que cambien.
5. Aplicar `humanizar-redaccion-v7` al texto nuevo.
6. Rellenar la columna it2 de `comparacion-iteraciones.md` (hoy pendiente
   aunque los valores ya existen en `v2.1-it2/07-metricas/`).
7. Commits por bloque con prefijo `[P2] tesis:`.
