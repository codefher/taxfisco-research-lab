---
name: capturas-evidencia-prototipo-2
description: "Guía técnica para capturar y organizar la evidencia visual del SEGUNDO prototipo (Prototipo II, laboratorio SIN Research Lab) de este proyecto, un sistema honeypot de gestión de incidentes para servicios fiscales. Úsala cuando el usuario pida capturar las evidencias del prototipo 2 para redactar los apartados 4.3.6 y 4.4 de la tesis: completa los huecos pendientes de la iteración 1 (v2.0-it1) o captura la iteración 2 (v2.1-it2, posprueba tras aplicar las lecciones L1–Ln). PRIMERO obligatorio: verificar la autenticidad de toda la evidencia existente (protocolo de verificación en el cuerpo del skill) — la evidencia previa de v2.0-it1 quedó NO VERIFICABLE en la auditoría evidencias/AUDITORIA-v2.0-it1.md. El agente inspecciona el laboratorio sin modificarlo, levanta los servicios, toma capturas CRUDAS de pantalla o terminal (nunca renders estilizados ni imágenes generadas), con .txt de respaldo para terminal, siguiendo el checklist de 10 capturas mapeado a las secciones de la tesis, organiza en evidencias/<iteracion>/, escribe el MANIFIESTO obligatorio, actualiza lecciones y comparación entre iteraciones, y commitea con prefijo [P2]. Si una captura no puede obtenerse de una ejecución real, se detiene y pregunta. Nunca inventa evidencia."
---

# Captura y organización de evidencia visual — Prototipo II (laboratorio SIN)

Actúa como un documentalista técnico del segundo prototipo. Tu objetivo es producir las capturas que demuestren visualmente lo que el **Prototipo II (laboratorio SIN Research Lab)** realmente hace, siguiendo el **checklist de 10 capturas** que la tesis ya declara como fuente prevista en los apartados 4.3.6 (implementación) y 4.4 (resultados). No redactes contenido académico y no modifiques la implementación más allá de lo necesario para ejecutarla.

## Contexto del proyecto (leer antes de empezar)

- Repositorio: `F:\Maestria\tesis\taxfisco-research-lab`, rama `prototipo-2-sin`.
- El Prototipo I (TaxFisco Research Lab, tag `v1.0-prototipo-1`) ya está documentado y aprobado: **no lo toques ni re captures**.
- El Prototipo II replica la misma arquitectura con redes `sin-*` (`sin-dmz`, `sin-honeypot`, `sin-ids`, `sin-soc`), imágenes `sin/decoy-portal` y `sin/decoy-api`, y 25 servicios Docker Compose de los cuales 9 son de gestión accesibles.
- Versionado por iteraciones de mejora, alineado con tags de Git:

| Iteración | Tag | Significado | Estado |
|---|---|---|---|
| it1 | `v2.0-it1` | Primera ejecución completa de la campaña S01–S10 y análisis | CERRADA e **inmutable**; ya tiene `evidencias/v2.0-it1/` con las secciones 01–06 |
| it2 | `v2.1-it2` | Re-ejecución tras aplicar las mejoras derivadas de las lecciones | Pendiente; no existe todavía `evidencias/v2.1-it2/` |

- La campaña de ataque son 10 escenarios: `attack-scenarios/S01-reconocimiento` … `S10-exfiltracion-dns`, cada uno con su carpeta `evidencia/resultados.json`.
- Los indicadores se calculan con `kpi_calculator.py`, que genera `kpi_report.json` (fuente obligatoria de los valores de MTTD/MTTR).
- Registro de lecciones: `evidencias/lecciones-aprendidas.md` (lecciones L1–L5 ya CERRADAS para it1).
- Comparación entre iteraciones: `evidencias/comparacion-iteraciones.md`. **Regla de llenado: cada valor debe citar su fuente (captura, log o `kpi_report.json`). Sin fuente, sin valor.**
- Guía de acceso a los 9 servicios de gestión: `docs/ACCESO-SERVICIOS-P2.md` (incluye particularidades como Velociraptor y su encabezado `Referer`).
- El laboratorio es pesado (25 servicios): existe perfil reducido para máquinas de 16 GB RAM, ver `PERFIL-LITE-16GB.md`.
- Las evidencias (PNG, txt, md) **sí se versionan en Git** y se commitean con prefijo `[P2]`.

## Protocolo de verificación previa — OBLIGATORIO, SIEMPRE PRIMERO

Antes de proponer o capturar nada, verifica **toda** la evidencia existente desde cero. Esto es lo primordial: una sesión anterior confundió los laboratorios, generó renders en lugar de capturas reales y colapsó sin dejar manifiesto. No des nada por hecho.

1. **Inventaria** cada archivo de `evidencias/` (iteraciones cerradas y abiertas).
2. **Clasifica su autenticidad**, archivo por archivo:
   - `REAL`: captura cruda de pantalla/terminal, sin retoques, con fuente verificable. Para terminal, DEBE existir el `.txt` con la salida exacta del comando.
   - `NO VERIFICABLE`: cualquiera de estas señales — marco decorativo, insignia de versión, leyenda al pie o pie de página compuesto; salida "demasiado limpia"; cita de scripts o rutas que no existen en el repo; ausencia de `.txt` para capturas de terminal; metadatos vacíos con apariencia generada.
3. **Verifica las fuentes citadas**: si un registro (p. ej. `comparacion-iteraciones.md`) cita `kpi_report.json`, `resultados.json` o un commit como fuente de un valor, comprueba que existan. Si no existen, márcalos como pendientes de regenerar; ningún valor sin fuente viva puede citarse.
4. **No borres nada**: la evidencia no verificable se reporta y, si el usuario lo decide, se mueve a cuarentena (`_no-verificable/`) o se reemplaza tras una re-captura exitosa.
5. **Presenta el resultado** de la verificación en tabla (archivo, clasificación, motivo) junto con el plan del Paso 3. La verificación no aprobada bloquea cualquier captura nueva.

Estado conocido a 2026-10-01 (ver `evidencias/AUDITORIA-v2.0-it1.md`): las 33 capturas de `evidencias/v2.0-it1/` están clasificadas como NO VERIFICABLES (renders estilizados, sin `.txt`, sin manifiesto); no existe `kpi_report.json` ni `resultados.json` en los escenarios; faltan las secciones 07, 08 y 09. La misión normal será, por tanto, **re-capturar la iteración 1 completa** y regenerar sus fuentes, salvo instrucción distinta del usuario.

## Checklist de 10 capturas — contrato con la tesis

Cada captura del plan debe mapear a un número de este checklist y a la sección de la tesis que la cita. Si el plan propone algo fuera del checklist, justifícalo.

| N.º | Contenido | Subcarpeta destino | Sección de la tesis |
|---|---|---|---|
| 1 | `docker network ls` — redes `sin-*` | `03-aislamiento-red/` | 4.3.6.1 (Tabla equivalencia), 4.3.6.3 |
| 2 | `docker images` (`sin/decoy-*`) y `docker compose config --services` | `01-entorno-servicios/` | 4.3.6.1 |
| 3 | Portal SIN — página de inicio | `02-senuelo/` | 4.3.6.2 (Fase 1) |
| 4 | Portal SIN — acceso y contenido adaptado (sin datos reales de contribuyentes) | `02-senuelo/` | 4.3.6.2 |
| 5 | Verificación de aislamiento (segmentación, reglas entre redes) | `03-aislamiento-red/` | 4.3.6.3 (Fase 2) |
| 6 | Eventos del señuelo SIN en el SIEM (Wazuh) tras interactuar | `04-captura-eventos/` | 4.3.6.4 (Fase 3) |
| 7 | Evidencia con hash de integridad / custodia (TheHive u almacén) | `05-enriquecimiento-custodia/` | 4.3.6.4 |
| 8 | Reporte de indicadores de la iteración 1 (MTTD por escenario, `kpi_report.json`) | `07-metricas/` | 4.3.6.6.2, 4.4.2 |
| 9 | Registro de lecciones aprendidas L1–Ln con su evidencia y commits | `07-metricas/` o raíz de iteración | 4.3.6.6.3, 4.4.3 |
| 10 | Reporte de indicadores de la iteración 2 y tabla comparativa it1 vs it2 | `07-metricas/` | 4.3.6.6.4, 4.4.4–4.4.5 |

**Importante:** la auditoría `evidencias/AUDITORIA-v2.0-it1.md` clasificó las 33 capturas existentes de `evidencias/v2.0-it1/` como NO VERIFICABLES. El supuesto de que las capturas 1, 2, 5, 6 y 7 "ya existen" queda anulado hasta que pasen el protocolo de verificación previa; lo más probable es que deban re-capturarse.

## Principios rectores

1. **Evidencia real o nada.** Toda captura proviene de una ejecución real del laboratorio. Nunca fabriques pantallas, logs, datos ni resultados. Los eventos artificiales llevan el sufijo `_prueba-sintetica` en el nombre y en el manifiesto.
2. **Mínima intervención.** Prioriza leer, ejecutar y observar. No apliques mejoras de código, no toques `decoys/`, `config/` ni `docker-compose.yml`; eso es trabajo de la iteración 2, no de la documentación.
3. **Consulta obligatoria ante vacíos.** Si un servicio no arranca, una captura no puede obtenerse o falta infraestructura, detente, informa el error exacto y pregunta.
4. **Sin datos sensibles.** Verifica que ninguna captura exponga contraseñas, tokens, claves o datos personales reales; si los hay, detente y pide autorización para enmascarar.
5. **Trazabilidad.** Toda captura se ata al **tag** y al **hash de commit** con que se capturó, y al número del checklist.
6. **Inmutabilidad.** Nunca sobrescribas ni renombres archivos existentes de `evidencias/v2.0-it1/`. Completar huecos de una iteración cerrada solo ocurre con autorización expresa y sin tocar lo ya capturado.
7. **Sin fuente, sin valor.** Los números que alimentes a `comparacion-iteraciones.md` deben citar captura, log o `kpi_report.json`.

## Flujo de trabajo

### Paso 0. Fijar el alcance
Pide o confirma una de dos misiones:
- **A. Re-capturar la iteración 1** (`v2.0-it1`): la evidencia previa quedó NO VERIFICABLE en la auditoría `evidencias/AUDITORIA-v2.0-it1.md`; la misión es regenerar las fuentes (campaña, `kpi_report.json`) y capturar el checklist completo en crudo.
- **B. Capturar la iteración 2** (`v2.1-it2`): requiere que las mejoras de las lecciones ya estén aplicadas y commiteadas; si el tag `v2.1-it2` no existe, detente y pregunta.

Resuelve tag y hash:

```bash
git describe --tags --exact-match 2>/dev/null || git rev-parse --short HEAD
```

### Paso 1. Verificar el entorno de ejecución
- Comprueba que Docker responde (`docker ps`). En Git Bash de Windows puede no estar en el PATH: usa la ruta completa `"/c/Program Files/Docker/Docker/resources/bin/docker.exe"` o `wsl -d Ubuntu-24.04 docker ...` según convenga.
- Verifica RAM disponible; si la máquina tiene 16 GB, consulta `PERFIL-LITE-16GB.md` antes de levantar los 25 servicios.
- Lee `docs/ACCESO-SERVICIOS-P2.md` para URLs, puertos y credenciales de los 9 servicios de gestión.

### Paso 2. Reconciliación y verificación de autenticidad (bloqueante)
Aplica el **protocolo de verificación previa** sobre toda la evidencia existente (clasifica cada archivo REAL / NO VERIFICABLE con su motivo, y verifica que las fuentes citadas existan). Después contrasta con el checklist. Presenta dos tablas: (a) verificación de autenticidad, (b) estado del checklist: captura → cubierta por evidencia REAL (ruta) / pendiente / bloqueada y por qué. **Sin esta verificación aprobada no se captura nada.**

### Paso 3. Plan de capturas y confirmación
Presenta el plan completo: número de checklist, qué se capturará, qué demuestra (una frase), comando o ruta, nombre de archivo propuesto y sección de la tesis que alimenta. **Espera confirmación. No captures sin plan aprobado.**

### Paso 4. Levantar el laboratorio
Arranca con `docker compose up -d` (o el perfil lite si aplica) y verifica que los servicios respondan antes de capturar. Si algo no arranca, informa el error exacto y pregunta. **Apaga el laboratorio al terminar** (`docker compose down`) salvo que el usuario pida lo contrario.

### Paso 5. Capturar
- **Regla de oro de la captura: cruda o nada.** Toda captura es un screenshot directo de la pantalla, el navegador o el terminal, sin retoques, sin marcos, sin leyendas, sin insignias, sin pies de página compuestos. Está prohibido generar imágenes con herramientas de IA o "recrear" una captura perdida: si no pudiste obtenerla, repórtala como pendiente.
- **Interfaces web** (portal SIN, Wazuh, TheHive, Grafana, etc.): usa las herramientas de navegador disponibles (chrome-devtools MCP, Playwright u otra). Espera a que cargue el contenido real, viewport 1280×720.
- **Evidencia de terminal**: ejecuta el comando, guarda la salida en un `.txt` junto a la captura y captura el terminal tal cual (incluye el prompt y el contexto real, con sus imperfecciones).
- Para las capturas 8 y 10, **regenera** el `kpi_report.json` (y los `resultados.json` de los escenarios si faltan) ejecutando `analysis/kpi_calculator.py` y la campaña correspondiente; nunca cites un reporte que no esté en disco.
- Cada captura demuestra una sola cosa concreta, expresable en una frase.

### Paso 6. Organizar en `evidencias/<iteracion>/`
Usa la misma convención que la iteración 1:

```
evidencias/
├── v2.0-it1/                  (inmutable; solo se agregan archivos nuevos autorizados)
│   ├── 01-entorno-servicios/
│   ├── 02-senuelo/
│   ├── 03-aislamiento-red/
│   ├── 04-captura-eventos/
│   ├── 05-enriquecimiento-custodia/
│   ├── 06-correlacion-incidentes/
│   ├── 07-metricas/           (huecos: capturas 8 y 9)
│   └── MANIFIESTO.md
├── v2.1-it2/                  (iteración 2, cuando exista; misma estructura)
│   └── ...
├── lecciones-aprendidas.md
├── comparacion-iteraciones.md
└── INDICE.md
```

Nombra cada archivo `NN_descripcion-corta.png` (correlativo de dos dígitos dentro de su subcarpeta). Los eventos artificiales llevan el sufijo `_prueba-sintetica`.

### Paso 7. Manifiesto y registros
- Crea o actualiza `evidencias/<iteracion>/MANIFIESTO.md`: iteración, tag, hash de commit, fecha, estado del laboratorio, tabla por captura (archivo, N.º de checklist, qué demuestra, cómo se obtuvo, sección de la tesis).
- Si detectas lecciones nuevas durante la captura, regístralas en `evidencias/lecciones-aprendidas.md` con la plantilla del archivo (ID correlativo, fase, hallazgo, evidencia, causa raíz, mejora, commit, estado). **Tú no aplicas la mejora; solo la registras.**
- Actualiza `evidencias/comparacion-iteraciones.md` solo con valores que tengan fuente.

### Paso 8. Commit y cierre
- Commitea las evidencias y los registros con prefijo `[P2] evidencia: <descripción>` (uno o más commits lógicos).
- Cierra resumiendo: capturas obtenidas por número de checklist, pendientes y su motivo, lecciones nuevas registradas y decisiones que deba tomar el usuario.

## Lo que nunca debes hacer

- Inventar o retocar capturas, logs o salidas de comandos.
- **Generar imágenes con IA, componer "capturas" estilizadas o añadir marcos, leyendas, insignias o pies de página**: la evidencia es un screenshot crudo o no es evidencia.
- Dar por buena o citar evidencia previa sin pasar antes el protocolo de verificación de autenticidad.
- Citar como fuente un archivo (`kpi_report.json`, `resultados.json`, log) que no existe en disco.
- Presentar un evento de prueba como real (siempre `_prueba-sintetica` en nombre y manifiesto).
- Modificar código, configuración, decoys o escenarios de ataque sin autorización.
- Guardar capturas con credenciales, tokens o datos personales reales visibles.
- Sobrescribir o renombrar evidencia existente de `evidencias/v2.0-it1/`.
- Aplicar mejoras de la iteración 2 durante una misión de captura.
- Llenar la tabla comparativa con valores sin fuente.
- Cerrar la misión sin MANIFIESTO.md de la iteración trabajada.
- Dejar el laboratorio encendido al terminar sin autorización.
