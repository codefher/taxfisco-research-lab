---
name: capturas-evidencia-prototipo-2
description: "Guía técnica para capturar y organizar la evidencia visual del SEGUNDO prototipo (Prototipo II, laboratorio SIN Research Lab) de este proyecto, un sistema honeypot de gestión de incidentes para servicios fiscales. Úsala cuando el usuario pida capturar las evidencias del prototipo 2 para redactar los apartados 4.3.6 y 4.4 de la tesis: completa los huecos pendientes de la iteración 1 (v2.0-it1, inmutable) o captura la iteración 2 (v2.1-it2, posprueba tras aplicar las lecciones L1–Ln). El agente inspecciona el laboratorio sin modificarlo, levanta los servicios, toma las capturas siguiendo el checklist de 10 capturas mapeado a las secciones de la tesis, las organiza en evidencias/<iteracion>/, actualiza el manifiesto, el registro de lecciones (evidencias/lecciones-aprendidas.md) y la tabla comparativa entre iteraciones (evidencias/comparacion-iteraciones.md), y commitea con prefijo [P2]. Si una captura no puede obtenerse de una ejecución real, se detiene y pregunta. Nunca inventa evidencia."
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

**Importante:** en la iteración 1 solo faltan por capturar las piezas que alimentan las capturas 3, 4, 8 y 9 (la 1, 2, 5, 6 y 7 ya existen en `evidencias/v2.0-it1/` bajo las secciones 01–06). Verifícalo con la reconciliación del Paso 2 antes de proponer nada.

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
- **A. Completar evidencia pendiente de it1** (`v2.0-it1`): capturas 3, 4, 8 y 9 del checklist.
- **B. Capturar la iteración 2** (`v2.1-it2`): requiere que las mejoras de las lecciones ya estén aplicadas y commiteadas; si el tag `v2.1-it2` no existe, detente y pregunta.

Resuelve tag y hash:

```bash
git describe --tags --exact-match 2>/dev/null || git rev-parse --short HEAD
```

### Paso 1. Verificar el entorno de ejecución
- Comprueba que Docker responde (`docker ps`). En Git Bash de Windows puede no estar en el PATH: usa la ruta completa `"/c/Program Files/Docker/Docker/resources/bin/docker.exe"` o `wsl -d Ubuntu-24.04 docker ...` según convenga.
- Verifica RAM disponible; si la máquina tiene 16 GB, consulta `PERFIL-LITE-16GB.md` antes de levantar los 25 servicios.
- Lee `docs/ACCESO-SERVICIOS-P2.md` para URLs, puertos y credenciales de los 9 servicios de gestión.

### Paso 2. Reconciliación con el estado actual
Inventaría lo que ya existe antes de proponer: recorre `evidencias/v2.0-it1/` y contrasta con el checklist. Presenta una tabla de estado: captura → existe (ruta) / pendiente / bloqueada y por qué.

### Paso 3. Plan de capturas y confirmación
Presenta el plan completo: número de checklist, qué se capturará, qué demuestra (una frase), comando o ruta, nombre de archivo propuesto y sección de la tesis que alimenta. **Espera confirmación. No captures sin plan aprobado.**

### Paso 4. Levantar el laboratorio
Arranca con `docker compose up -d` (o el perfil lite si aplica) y verifica que los servicios respondan antes de capturar. Si algo no arranca, informa el error exacto y pregunta. **Apaga el laboratorio al terminar** (`docker compose down`) salvo que el usuario pida lo contrario.

### Paso 5. Capturar
- **Interfaces web** (portal SIN, Wazuh, TheHive, Grafana, etc.): usa las herramientas de navegador disponibles (chrome-devtools MCP, Playwright u otra). Espera a que cargue el contenido real, viewport 1280×720.
- **Evidencia de terminal**: ejecuta el comando, guarda la salida en un `.txt` junto a la captura y, cuando sea posible, captura también el terminal.
- Para las capturas 8 y 10, ejecuta la campaña o localiza el `kpi_report.json` ya generado y captúralo junto a la tabla de indicadores.
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
- Presentar un evento de prueba como real (siempre `_prueba-sintetica`).
- Modificar código, configuración, decoys o escenarios de ataque sin autorización.
- Guardar capturas con credenciales, tokens o datos personales reales visibles.
- Sobrescribir o renombrar evidencia existente de `evidencias/v2.0-it1/`.
- Aplicar mejoras de la iteración 2 durante una misión de captura.
- Llenar la tabla comparativa con valores sin fuente.
- Dejar el laboratorio encendido al terminar sin autorización.
