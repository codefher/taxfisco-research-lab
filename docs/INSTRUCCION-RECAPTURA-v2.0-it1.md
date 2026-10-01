# Instrucción de re-captura — iteración 1 (v2.0-it1) del Prototipo II

> Lista para copiar y pegar en OpenCode (Linux), una vez hecho `git pull`
> en la rama `prototipo-2-sin` (commit base: `02594af` o posterior).
> Contexto: la evidencia previa quedó NO VERIFICABLE
> (ver `evidencias/AUDITORIA-v2.0-it1.md`).

## Qué debe leer la IA (en este orden)

1. `.opencode/skills/capturas-evidencia-prototipo-2/SKILL.md` — el skill completo.
2. `evidencias/AUDITORIA-v2.0-it1.md` — por qué la evidencia anterior no sirve.
3. `evidencias/comparacion-iteraciones.md` y `evidencias/lecciones-aprendidas.md`.
4. `docs/ACCESO-SERVICIOS-P2.md` — URLs, puertos y credenciales.
5. Solo si la máquina tiene 16 GB de RAM: `PERFIL-LITE-16GB.md`.

## Mensaje para la IA (copiar y pegar tal cual)

```text
Usa el skill capturas-evidencia-prototipo-2. Lee primero el skill completo,
evidencias/AUDITORIA-v2.0-it1.md, evidencias/comparacion-iteraciones.md,
evidencias/lecciones-aprendidas.md y docs/ACCESO-SERVICIOS-P2.md.

MISIÓN A: re-capturar la iteración 1 (v2.0-it1) del laboratorio SIN.

Autorizaciones y alcance:
- Autorizo mover las 33 capturas antiguas de evidencias/v2.0-it1/ a
  evidencias/v2.0-it1/_no-verificable/ antes de capturar (quedan como
  referencia, no se borran).
- Levanta el laboratorio (si la máquina tiene 16 GB RAM, aplica
  PERFIL-LITE-16GB.md), ejecuta la campaña completa S01–S10 y regenera
  las fuentes: los resultados.json de cada escenario y el kpi_report.json
  con analysis/kpi_calculator.py.
- IMPORTANTE: analysis/*.json y attack-scenarios/*/evidencia/ están en
  .gitignore. Copia el kpi_report.json y los resultados.json a
  evidencias/v2.0-it1/07-metricas/ para que queden versionados.
- Captura el checklist N.º 1 al 9 en CRUDO: screenshots directos de
  pantalla/terminal, sin marcos, sin leyendas, sin insignias, NADA de
  imágenes generadas por IA. Toda captura de terminal va acompañada de su
  .txt con la salida exacta. La N.º 10 (iteración 2) NO va en esta misión.
- Completa las secciones 07-metricas, 08-extremo-a-extremo y 09-escenarios.
- Escribe evidencias/v2.0-it1/MANIFIESTO.md (obligatorio) y
  evidencias/INDICE.md: tag, hash de commit, fecha, estado del laboratorio
  y tabla por captura (archivo, N.º de checklist, qué demuestra, cómo se
  obtuvo, sección de la tesis).
- Actualiza evidencias/comparacion-iteraciones.md sustituyendo los valores
  "pendiente de verificar" de it1 con los valores reales regenerados y su
  fuente. Si algo no se pudo medir, déjalo como pendiente con explicación.
- Commitea todo con prefijo [P2] evidencia: y haz push.
- Al terminar, deja el laboratorio apagado (docker compose down).
```

## Advertencias de control (para el usuario, no para la IA)

- No omitir la autorización de cuarentena (`_no-verificable/`): sin ella la
  IA choca con su propia regla de no sobrescribir evidencia existente.
- Si la IA presenta imágenes con marcos, leyendas o insignias "SIN / v2.0-it1",
  rechazarlas: es exactamente el error de la sesión anterior.
- Al volver a Windows, comparar los MTTD regenerados con los valores de
  referencia (S01 16.40 s, S02 7.88 s, S05 1.05 s, S07 1.03 s) antes de
  redactar los apartados 4.4.2 y 4.3.6.6.2 de la tesis.
