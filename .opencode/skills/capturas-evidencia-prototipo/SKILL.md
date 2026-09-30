---
name: capturas-evidencia-prototipo
description: "Guía técnica para documentar visualmente el prototipo de software de este proyecto (un sistema honeypot de gestión de incidentes) POR ITERACIÓN. Úsala cuando el usuario pida analizar la implementación, ejecutar el proyecto, recorrer sus pantallas o funcionalidades con un navegador automatizado (chrome-devtools MCP) y obtener capturas de pantalla organizadas como evidencia. El agente recibe una iteración (por ejemplo v2.0-it1 o v2.1-it2), inspecciona el proyecto sin modificarlo, identifica qué funcionalidades pueden demostrarse visualmente, propone un plan de capturas para confirmación, ejecuta el proyecto, toma las capturas y las organiza en evidencias/<iteracion>/ con subcarpetas por funcionalidad y un manifiesto por iteración. Mantiene además un índice global evidencias/INDICE.md que compara las iteraciones. Si una funcionalidad no existe, falla o no puede demostrarse, el agente se detiene y pregunta al usuario. Nunca inventa evidencia ni altera el código innecesariamente."
---

# Captura y organización de evidencia visual del prototipo por iteración

Actúa como un documentalista técnico del proyecto. Tu objetivo es producir un conjunto ordenado de capturas que demuestren visualmente lo que el prototipo realmente hace **en una iteración concreta**, guardado en `evidencias/<iteracion>/`, más un índice global en `evidencias/INDICE.md`. No redactes contenido académico, no expliques teoría y no modifiques la implementación más allá de lo estrictamente necesario para ejecutarla.

## Contexto de iteraciones (leer antes de empezar)

Este proyecto versiona el prototipo por iteraciones de mejora, alineadas con tags de Git:

| Iteración | Tag de Git | Significado |
|---|---|---|
| 1 | `v2.0-it1` / `v2.0-it1-verificado` | Primera versión funcional y verificable. |
| 2 | `v2.1-it2` | Mejoras nacidas de las lecciones de la iteración 1. |

La iteración **1 es inmutable**: una vez capturada, no se sobrescribe. Cada iteración nueva vive en su propia carpeta y solo se enlaza desde el índice global.

Cada captura debe quedar trazada al estado exacto del código: registra en el manifiesto el **tag** y el **hash de commit** con el que se capturó.

## Principios rectores

1. **Evidencia real o nada.** Toda captura proviene de una ejecución real. Nunca fabriques pantallas, logs, datos ni resultados. Los eventos artificiales llevan el sufijo `_prueba-sintetica` en el nombre y en el manifiesto.
2. **Mínima intervención.** Prioriza leer, ejecutar y observar. No refactorices ni cambies configuración del prototipo salvo autorización expresa.
3. **Consulta obligatoria ante vacíos.** Si una funcionalidad no existe, no arranca o no puede demostrarse, detente, informa y pregunta.
4. **Sin datos sensibles.** Verifica que ninguna captura exponga contraseñas, tokens, claves o datos personales; si los hay, detente y pide autorización para enmascarar.
5. **Trazabilidad.** Toda captura se ata a un tag y a un hash de commit.
6. **Inmutabilidad.** No sobrescribas evidencia de una iteración cerrada.

## Flujo de trabajo

### Paso 0. Fijar la iteración
Pide o confirma el identificador de iteración (por ejemplo `v2.0-it1`). Resuelve su tag y hash de commit:

```bash
git describe --tags --exact-match 2>/dev/null || git rev-parse --short HEAD
```

Verifica que la carpeta `evidencias/<iteracion>/` no exista ya con contenido. Si existe, detente y pregunta si se trata de una re-captura autorizada.

### Paso 1. Analizar el proyecto
Explora la estructura sin modificar nada: README, `docker-compose.yml`, `Dockerfile`, carpetas de código, scripts de arranque, configuración y rutas de la interfaz. Determina el stack, cómo se ejecuta (comando, puertos, servicios) y dónde vive cada funcionalidad.

### Paso 2. Inventario de funcionalidades demostrables
Construye la lista de lo que puede mostrarse visualmente. Busca como mínimo:

- **Entorno y servicios**: contenedores activos, puertos expuestos, estado general.
- **Señuelo**: portal/API falsos en ejecución y su contenido.
- **Aislamiento de red**: redes de contenedores, segmentación, reglas de firewall.
- **Captura de eventos**: logs generados al interactuar con el señuelo.
- **Enriquecimiento y custodia**: contexto añadido, hashes de integridad, almacenamiento.
- **Correlación de incidentes**: alertas o tickets, clasificación, mapeo a técnicas de ataque.
- **Métricas**: pantallas, comandos o reportes con indicadores (tiempos, índices).
- **Recorrido extremo a extremo**: secuencia completa desde el señuelo hasta el indicador.

Si el proyecto tiene funcionalidades adicionales, agrégalas. Si algo de la lista no existe, aplica la consulta obligatoria.

### Paso 3. Plan de capturas y confirmación
Presenta el plan completo en una tabla: número, funcionalidad, qué se capturará, qué demuestra y nombre de archivo propuesto. Espera confirmación. No captures sin plan aprobado.

### Paso 4. Ejecutar el proyecto
Arranca el proyecto siguiendo sus instrucciones. Verifica que los servicios respondan antes de capturar. Si algo no arranca, informa el error exacto y pregunta.

### Paso 5. Capturar
- **Interfaces web**: usa el MCP **chrome-devtools**. Navega a cada pantalla, espera a que cargue el contenido real, usa viewport 1280×720 y captura la página completa cuando se justifique.
- **Evidencia de terminal**: ejecuta el comando, guarda la salida en un `.txt` junto a la captura y, cuando sea posible, toma también la captura del terminal.
- Cada captura demuestra una sola cosa concreta, expresable en una frase.

### Paso 6. Organizar en `evidencias/<iteracion>/`
Crea la estructura:

```
evidencias/
├── <iteracion>/
│   ├── 01-entorno-servicios/
│   ├── 02-senuelo/
│   ├── 03-aislamiento-red/
│   ├── 04-captura-eventos/
│   ├── 05-enriquecimiento-custodia/
│   ├── 06-correlacion-incidentes/
│   ├── 07-metricas/
│   ├── 08-extremo-a-extremo/
│   ├── 09-escenarios/        (resúmenes de attack-scenarios/*/evidencia)
│   └── MANIFIESTO.md
└── INDICE.md
```

Ajusta o agrega subcarpetas si el inventario real lo requiere. Nombra cada archivo `NN_descripcion-corta.png` (correlativo de dos dígitos dentro de su subcarpeta). Los eventos artificiales llevan el sufijo `_prueba-sintetica`.

La evidencia de escenarios (`attack-scenarios/*/evidencia/`) **no se duplica**: copia solo los `resultados.json` a `09-escenarios/` como resumen y referencia las rutas completas en el manifiesto.

### Paso 7. Manifiesto de la iteración
Crea `evidencias/<iteracion>/MANIFIESTO.md` con:

1. **Cabecera**: iteración, tag, hash de commit, fecha, estado del laboratorio y desviaciones conocidas (por ejemplo, ausencia de aislamiento total si fue autorizada).
2. **Tabla por captura**: archivo, funcionalidad, qué demuestra (una frase), cómo se obtuvo, fecha y observaciones.

### Paso 8. Índice global y comparación
Mantén `evidencias/INDICE.md` con una fila por iteración (tag, hash, fecha, resumen) y, cuando haya más de una, una **tabla comparativa** que para cada mejora indique: lección aprendida en la iteración anterior, cambio aplicado y captura que lo demuestra.

### Paso 9. Cierre
Resume: capturas por subcarpeta, funcionalidades sin demostrar y su motivo, capturas pendientes y decisiones que deba tomar el usuario.

## Lo que nunca debes hacer

- Inventar o retocar capturas, logs o salidas de comandos.
- Presentar un evento de prueba como real (siempre `_prueba-sintetica`).
- Modificar código, configuración o datos sin autorización.
- Guardar capturas con credenciales, tokens o IPs sensibles visibles.
- Sobrescribir la evidencia de una iteración cerrada.
- Escribir redacción académica extensa: el manifiesto registra hechos.
