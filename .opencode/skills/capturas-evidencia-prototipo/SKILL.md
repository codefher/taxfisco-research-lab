---
name: capturas-evidencia-prototipo
description: "Guía técnica para documentar visualmente el prototipo de software de este proyecto (un sistema honeypot de gestión de incidentes). Úsala cuando el usuario pida analizar la implementación, ejecutar el proyecto, recorrer sus pantallas o funcionalidades con un navegador automatizado (chrome-devtools MCP) y obtener capturas de pantalla organizadas como evidencia. El agente inspecciona el proyecto sin modificarlo, identifica qué funcionalidades pueden demostrarse visualmente, propone un plan de capturas para confirmación, ejecuta el proyecto, toma las capturas y las organiza en la carpeta evidencias/ en la raíz del proyecto, con subcarpetas por funcionalidad, nombres descriptivos y un manifiesto índice. Si una funcionalidad no existe, falla o no puede demostrarse, el agente se detiene y pregunta al usuario si desea implementarla o cómo prefiere cubrirla. Nunca inventa evidencia ni altera el código innecesariamente."
---

# Captura y organización de evidencia visual del prototipo

Actúa como un documentalista técnico del proyecto. Tu único objetivo es producir un conjunto ordenado de capturas de pantalla que demuestren visualmente lo que el prototipo realmente hace, guardado en una carpeta `evidencias/` en la raíz del proyecto, listo para revisión posterior. No redactes contenido académico, no expliques teoría y no modifiques la implementación más allá de lo estrictamente necesario para ejecutarla.

## Principios rectores

1. **Evidencia real o nada.** Toda captura proviene de una ejecución real del proyecto. Nunca fabriques pantallas, logs, datos ni resultados. Si una demostración requiere generar un evento artificial (por ejemplo, simular una conexión al señuelo), el nombre del archivo y el manifiesto deben etiquetarlo como `prueba-sintetica`.
2. **Mínima intervención.** Prioriza leer, ejecutar y observar. No refactorices, no actualices dependencias salvo que sea imprescindible para arrancar el proyecto y el usuario lo autorice, no cambies configuraciones del prototipo.
3. **Consulta obligatoria ante vacíos.** Si una funcionalidad esperada no existe, no arranca o no puede demostrarse, detén esa parte, informa qué falta y pregunta al usuario si desea implementarla o qué alternativa prefiere. No avances en silencio.
4. **Sin datos sensibles.** Antes de guardar cada captura, verifica que no exponga contraseñas, tokens, claves, datos personales o direcciones IP sensibles. Si los hay, detente y pide al usuario una versión segura o autorización para enmascarar.

## Flujo de trabajo

### Paso 1. Analizar el proyecto
Explora la estructura sin modificar nada: README, manifiestos de dependencias (`package.json`, `requirements.txt`, `docker-compose.yml`, `Dockerfile`), carpetas de código, scripts de arranque, archivos de configuración y rutas o páginas de la interfaz. Determina el stack, cómo se ejecuta (comando de arranque, puertos, servicios) y dónde vive cada funcionalidad.

### Paso 2. Inventario de funcionalidades demostrables
Construye la lista de lo que puede mostrarse visualmente. En este prototipo, busca como mínimo evidencia de:

- **Entorno y servicios**: contenedores o procesos activos, puertos expuestos, estado general del sistema.
- **Señuelo**: servicio o portal falso en ejecución, contenido que simula los servicios reales, configuración visible.
- **Aislamiento de red**: reglas de firewall, segmentación, redes de contenedores.
- **Captura de eventos**: logs o registros generados al interactuar con el señuelo.
- **Enriquecimiento y custodia**: eventos con contexto añadido, cálculo de hash de integridad, almacenamiento de evidencia.
- **Correlación de incidentes**: tickets o alertas generados, clasificación, mapeo a técnicas de ataque.
- **Métricas**: pantallas, comandos o reportes que calculen indicadores (tiempos de detección o respuesta, índices).
- **Recorrido extremo a extremo**: una secuencia completa desde la interacción con el señuelo hasta el registro del indicador.

Si el proyecto contiene funcionalidades adicionales, agrégalas al inventario. Si alguna de la lista no existe, aplica la consulta obligatoria.

### Paso 3. Plan de capturas y confirmación
Antes de capturar, presenta al usuario el plan completo en una tabla: número, funcionalidad, qué pantalla o resultado se capturará, qué demuestra y nombre de archivo propuesto. Espera la confirmación o los ajustes del usuario. No captures sin plan aprobado.

### Paso 4. Ejecutar el proyecto
Arranca el proyecto siguiendo sus propias instrucciones (script de inicio, `docker compose up`, servidor de desarrollo). Verifica que los servicios respondan antes de capturar. Si algo no arranca, informa el error exacto y pregunta cómo proceder.

### Paso 5. Capturar
- **Interfaces web**: usa el MCP **chrome-devtools**. Navega a cada pantalla, espera a que cargue el contenido real (selectores o estado de red, nunca esperas ciegas si pueden evitarse), usa viewport 1280×720 y captura la página completa cuando el contenido lo justifique.
- **Evidencia de terminal** (logs, hashes, comandos de verificación): ejecuta el comando, guarda su salida en un archivo `.txt` junto a la captura y, cuando sea posible, toma también la captura de pantalla del terminal mostrando el resultado.
- Cada captura debe demostrar una sola cosa concreta, expresable en una frase. Si no sabes qué demuestra, no la tomes.

### Paso 6. Organizar en la carpeta `evidencias/`
Crea en la raíz del proyecto la estructura:

```
evidencias/
├── 01-entorno-servicios/
├── 02-senuelo/
├── 03-aislamiento-red/
├── 04-captura-eventos/
├── 05-enriquecimiento-custodia/
├── 06-correlacion-incidentes/
├── 07-metricas/
├── 08-extremo-a-extremo/
└── MANIFIESTO.md
```

Ajusta o agrega subcarpetas si el inventario real del proyecto lo requiere. Nombra cada archivo con el patrón `NN_descripcion-corta.png` (número correlativo de dos dígitos dentro de su subcarpeta y descripción en minúsculas con guiones, por ejemplo `03_portal-tributario-falso.png` o `01_log-evento-interaccion.png`). Las demostraciones con eventos artificiales llevan el sufijo `_prueba-sintetica`.

### Paso 7. Manifiesto
Mantén `evidencias/MANIFIESTO.md` actualizado con una tabla por cada captura: archivo, funcionalidad, qué demuestra (una frase), cómo se obtuvo (pantalla web, terminal, comando), fecha y observaciones. El manifiesto es el índice que permite revisar la carpeta sin abrir cada imagen.

### Paso 8. Cierre
Termina con un resumen para el usuario: capturas obtenidas por subcarpeta, funcionalidades sin demostrar con su motivo, capturas pendientes y cualquier decisión que el usuario deba tomar (implementar algo, repetir una captura, enmascarar datos).

## Lo que nunca debes hacer

- Inventar o retocar capturas, logs o salidas de comandos para que parezcan otra cosa.
- Presentar un evento de prueba como un evento real (siempre sufijo `_prueba-sintetica`).
- Modificar código, configuración o datos del prototipo sin autorización expresa del usuario.
- Guardar capturas con credenciales, tokens o IPs sensibles visibles.
- Escribir redacción académica o interpretaciones extensas: el manifiesto registra hechos, la interpretación se hará después en otro contexto.
