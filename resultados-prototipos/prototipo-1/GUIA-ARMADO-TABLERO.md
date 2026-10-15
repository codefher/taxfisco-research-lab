# Guía de armado del tablero del Prototipo 1

## Qué resuelve este documento

El tablero del segundo laboratorio ya existe en
`../prototipo-2/dashboard-resultados_prototipo_2.html` y este documento explica
cómo se construye el del primero, tomando ese tablero como plantilla. No se
trata de calcarlo, sino de decidir qué secciones sobreviven en un laboratorio que
corrió una sola vez.

La diferencia de fondo entre los dos prototipos es la que gobierna todo el
armado. El segundo laboratorio corrió dos iteraciones y puede comparar una vuelta
con otra. El primero corrió una sola, de manera que no existe línea base ni
comparación posible dentro de su propia medición.

## Dónde está la evidencia del primer laboratorio

La evidencia no está en la rama `prototipo-2-sin`. Está en la rama
`prototipo-1-entidad-homologada`, en la carpeta `evidencias/`, que el archivo
`.gitignore` excluye de los demás laboratorios.

| Archivo | Contenido |
| --- | --- |
| `evidencias/07-metricas/07_kpi-report.json` | Indicadores, tiempos por escenario, volumen y cobertura |
| `evidencias/07-metricas/08_mitre-coverage.json` | Inventario de diecisiete técnicas, matriz de tácticas y análisis de brechas |
| `evidencias/07-metricas/09_iso27035-compliance.json` | Correspondencia con las fases de ISO/IEC 27035 |
| `evidencias/MANIFIESTO.md` | Manifiesto de capturas |
| `evidencias/04-captura-eventos/` | Capturas de Wazuh, Cowrie, Suricata y OpenCanary |

Para leerlos desde la rama actual se usa el comando siguiente.

```
git show origin/prototipo-1-entidad-homologada:evidencias/07-metricas/07_kpi-report.json
```

## Datos verificados del primer laboratorio

Todo lo que sigue está leído de los archivos de la tabla anterior. Ninguna cifra
de este apartado procede del capítulo IV.

### Identificación del reporte

| Campo | Valor |
| --- | --- |
| Laboratorio | TaxFisco Research Lab |
| Fecha del reporte | 2026-09-14T07:31:44Z |
| Método | MTTD medido desde eventos reales frente al inicio del escenario |
| Entidad | Homologada del rubro de servicios fiscales digitales |

### Ejecución

| Indicador | Valor |
| --- | --- |
| Escenarios ejecutados | 10 |
| Escenarios con tiempo de detección medido | 9 de 10 |
| Ataques registrados en el señuelo | 46 |
| Peticiones atendidas por la interfaz de servicios | 1 758 |
| Conexiones capturadas por el emulador | 8 |
| Peticiones recibidas por el portal | 8 875 |

### Tiempo de detección

| Indicador | Valor |
| --- | --- |
| Tiempo medio | 41,598 s |
| Valor mínimo | 0,141 s |
| Valor máximo | 260,108 s |
| Mediciones por debajo de un minuto | 7 de 9 |

El percentil 95 no viene en el reporte del primer laboratorio. El tablero del
segundo lo presenta como indicador principal, de manera que ese cálculo queda
pendiente y no debe estimélo.

### Tiempo por escenario

| Escenario | Técnica | Tiempo | Fuente que lo registra |
| --- | --- | --- | --- |
| S01 · Reconocimiento activo | T1595 | 16,405 s | Interfaz de servicios, vista del atacante |
| S02 · Escaneo web | T1595.002 | 0,826 s | Portal del señuelo |
| S03 · Fuerza bruta por acceso remoto | T1110.001 | 85,000 s | Emulador de acceso remoto |
| S04 · Inyección de consultas | T1190 | 260,108 s | Interfaz de servicios |
| S05 · Suplantación de credenciales | T1110.004 | 0,141 s | Interfaz de servicios |
| S06 · Inyección en el navegador | T1059.007 | 0,824 s | Interfaz de servicios |
| S07 · Abuso de la interfaz | T1078 | 0,543 s | Interfaz de servicios, ruta |
| S08 · Depósito de archivo | T1105 | 0,533 s | Interfaz de servicios, ruta |
| S09 · Conexión inversa | T1059.004 | 10,000 s | Emulador de acceso remoto |
| S10 · Exfiltración por nombres de dominio | T1048.003 | fuera de la medición | Ninguna fuente lo registró |

### Cobertura y custodia

| Indicador | Valor |
| --- | --- |
| Técnicas implementadas en el inventario | 17 |
| Técnicas detectadas | 10 |
| Tácticas detectadas | 6 |
| Tácticas del inventario | 8 |
| Componentes que registran detección | 5 |
| Archivos de evidencia con huella | 68 |
| Calidad de la evidencia verificada | 100 de 100 |

Las cinco fuentes de detección son Cowrie, la interfaz de servicios, la interfaz
de servicios en su vista del atacante, la interfaz de servicios en su registro de
ruta y el portal del señuelo. El tablero del segundo laboratorio cuenta los
componentes por la cadena de fuentes que declara el reporte, de manera que esa
misma regla debe aplicarse aquí para que los dos tableros sean comparables.

Las siete técnicas del inventario que ningún escenario ejerce son T1059,
T1059.006, T1078.001, T1083, T1213, T1530 y T1595.003. Coinciden con las mismas
siete que el tablero del segundo laboratorio marca como no ejercidas.

## Las tres cosas que había que resolver antes de construir

Estas discrepancias no se resuelven dentro del tablero. Se resuelven antes, y su
respuesta queda escrita en el capítulo IV.

### La correspondencia con ISO/IEC 27035

La Tabla 13 del capítulo IV declara **cinco de cinco** fases de ISO/IEC 27035
sustentadas. El archivo `09_iso27035-compliance.json` lo confirma, porque
documenta evidencia de laboratorio para cada una de las cinco fases.

El bloque de conformidad que embebe `07_kpi-report.json` declara en cambio **una
de cinco**, con veinte por ciento, y esa única fase es la de detección. Los dos
archivos miden cosas distintas, porque el bloque resumido cuenta la fase en la
que la campaña produjo eventos medidos y el archivo de cumplimiento inventaría la
evidencia presente en el laboratorio por fase.

El tablero cita el archivo de cumplimiento, que es el que documenta la evidencia
una por una, y declara en una nota que existe la otra lectura. El capítulo IV
necesita una nota de definición que explique la diferencia.

### El número de escenarios

La Tabla 13 del capítulo IV declara **nueve escenarios ejecutados**. El reporte
declara `scenarios_executed: 10` y `MTTD.samples: 9`. El capítulo parece haber
tomado el número de mediciones por el número de ejecuciones.

El tablero declara las dos cosas por separado, porque significan cosas
distintas. Diez escenarios se ejecutaron y nueve produjeron tiempo de detección.

### El registro de lecciones

El capítulo IV atribuye tres lecciones aprendidas al primer laboratorio. **No
existe un registro de lecciones versionado en esa rama.** El segundo laboratorio
tiene el suyo en `evidencias/lecciones-aprendidas.md`, pero el primero no tiene
equivalente.

Mientras ese registro no se localice y versione, la sección de lecciones del
tablero del primer laboratorio queda fuera, igual que la sección institucional
del segundo tablero.

## Mapa de secciones

La plantilla tiene doce secciones. De esas, ocho se trasladan tal cual o con
ajustes menores, dos no aplican y dos se reinterpretan.

| Sección del Prototipo 2 | Aplica | Qué hacer |
| --- | --- | --- |
| A. Indicadores principales | Sí | Quitar la comparación con línea base. Quedan siete indicadores de una sola medición. |
| B. Vuelta 1 frente a vuelta 2 | No | Sustituir por el puente entre los dos laboratorios, que se explica abajo. |
| C. Tiempo de detección por escenario | Sí | Los nueve valores con su fuente. S10 aparece como fuera de la medición. |
| D. Distribución del tiempo de detección | Sí | Nueve barras en lugar de diez. |
| E. Fuentes que registran detección | Sí | Cinco componentes, con el mismo criterio de conteo del segundo tablero. |
| F. Cobertura de MITRE ATT&CK | Sí | Diecisiete implementadas, diez detectadas, ocho tácticas. |
| G. Ciclo de iteraciones | No | Sustituir por una tabla de ejecución con fecha, método y reporte de origen. |
| H. Aportación de cada fase | Sí | Los indicadores salen del reporte de este laboratorio. |
| I. Registro de lecciones | No | Queda fuera hasta que exista el registro versionado. |
| J. Volumen de actividad | Sí | Cuarenta y seis ataques, mil setecientos cincuenta y ocho peticiones al servicio, ocho conexiones y ocho mil ochocientas setenta y cinco peticiones al portal. |
| K. Evidencia visual | Sí | Capturas desde `evidencias/04-captura-eventos/` de esa rama. |
| L. Resultado institucional | No | Ese contenido pertenece al Servicio de Impuestos Nacionales. |

### El puente entre los dos laboratorios

La sección B del segundo tablero compara dos vueltas porque el segundo
laboratorio corrió dos. El primero no puede hacer eso, y esa es la sustitución
más útil que ofrece la guía.

El escenario **S10, exfiltración por nombres de dominio, no produjo tiempo de
detección en el primer laboratorio**, porque el cálculo solo consultaba tres
fuentes y ninguna leía el tráfico DNS. El registro de lecciones del segundo
laboratorio recoge ese hallazgo en la lección L14, cuya corrección añade la
consulta DNS como fuente. El mismo escenario se mide en 0,646 s en la medición
final del segundo laboratorio.

Esa secuencia demuestra el arco completo de la metodología con datos de los dos
laboratorios. El primer laboratorio expone el vacío del instrumental y el
segundo lo cierra. Presentada así, la comparación entre prototipos justifica la
existencia de las dos aplicaciones en lugar de solo medirlas.

## Reglas de redacción

La prosa del tablero se escribe con las mismas reglas duras que el capítulo IV.

| Regla | Aplicación |
| --- | --- |
| Presente intemporal | Se dice «el reporte declara» y no «el reporte declaró». |
| Sin dos puntos explicativos | Se eliminan del texto corrido. |
| Sin raya larga como inciso | Solo se usa como separador en rótulos de tabla. |
| Oraciones de treinta a sesenta palabras | Se parte la prosa larga. |
| Máximo dos «y» por oración | Se cuenta antes de dar por cerrada la oración. |
| Sin coma ante conjunción coordinante | Prohíbe el patrón «documental, y». |
| Números del uno al nueve en palabras | En prosa. Las tablas conservan el dígito. |

## Verificación de cierre

1. La consola del navegador queda sin errores ni advertencias.
2. Todas las imágenes resuelven su ruta y ninguna queda rota.
3. Cada cifra del tablero tiene un archivo de origen declarado en el pie.
4. Los nueve tiempos coinciden con `07_kpi-report.json`.
5. Las diecisiete técnicas coinciden con `08_mitre-coverage.json`.
6. El tablero declara la lectura de ISO/IEC 27035 que cita y menciona que existe
   la otra.
7. El tablero no presenta ninguna comparación antes y después dentro del primer
   laboratorio, porque ese laboratorio corrió una sola vez.

## Estado

Los siete puntos quedaron verificados el quince de octubre de 2026. El tablero
está construido y su prosa cumple las reglas duras de redacción sin una sola
infracción de coma ante conjunción coordinante.

## Archivos que produce este trabajo

| Archivo | Contenido |
| --- | --- |
| `dashboard-resultados_prototipo_1.html` | El tablero, con el mismo diseño del segundo. |
| `evidencia-visual/` | Capturas del primer laboratorio. |
| `LEEME.md` | Estado de la evidencia y vínculo al segundo tablero. |