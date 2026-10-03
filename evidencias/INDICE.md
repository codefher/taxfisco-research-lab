# Índice general de evidencias — Prototipo II (SIN Research Lab)

> Documento de navegación cruzada para la carpeta `evidencias/`.
> Generado durante la re-captura de la iteración 1 (v2.0-it1) el 2026-10-03.

## Estructura

```
evidencias/
├── v2.0-it1/                        iteración 1 (preprueba, evidencia verificada)
│   ├── MANIFIESTO.md                obligatorio por skill
│   ├── 01-entorno-servicios/        capturas N.º 2 (docker images + compose config)
│   ├── 02-senuelo/                  capturas N.º 3 y 4 (portal SIN landing/login/dashboard/2FA)
│   ├── 03-aislamiento-red/          capturas N.º 1 y 5 (redes docker + aislamiento)
│   ├── 04-captura-eventos/          captura N.º 6 (Wazuh alertas + hallazgo Suricata)
│   ├── 05-enriquecimiento-custodia/ captura N.º 7 (TheHive + MISP)
│   ├── 06-correlacion-incidentes/   PENDIENTE (sin caso TheHive en esta sesión)
│   ├── 07-metricas/                 capturas N.º 8 y 9 (KPI + lecciones) + fuentes canónicas
│   ├── 08-extremo-a-extremo/        cadena F1→F5 narrativa
│   ├── 09-escenarios/               resumen S01-S10 + resultados.json
│   └── _no-verificable/             34 PNG previas (renders estilizados) + informe de auditoría
├── AUDITORIA-v2.0-it1.md            auditoría del estado previo de la evidencia
├── comparacion-iteraciones.md       tabla it1 vs it2 (a completar en it2)
├── lecciones-aprendidas.md          registro L1-L7 (L6+L7 nuevas en esta sesión)
└── INDICE.md                        este archivo
```

## Itinerario de uso para la tesis

| Apartado de la tesis | Carpeta / archivo a citar |
|---|---|
| 4.3.5 Prototipo I | (ya aprobado; fuera de `evidencias/`) |
| 4.3.6.1 Adaptación y plataforma | `v2.0-it1/01-entorno-servicios/` + `v2.0-it1/03-aislamiento-red/01_*` |
| 4.3.6.2 Fase 1 — diseño del señuelo | `v2.0-it1/02-senuelo/01_portal-landing.png` + `02_portal-dashboard.png` + `03_portal-login.png` + `04_portal-segundo-factor.png` |
| 4.3.6.3 Fase 2 — despliegue aislado | `v2.0-it1/03-aislamiento-red/07_resumen-aislamiento.png` |
| 4.3.6.4 Fase 3 — captura y custodia | `v2.0-it1/04-captura-eventos/*` + `v2.0-it1/05-enriquecimiento-custodia/*` |
| 4.3.6.5 Fase 4 — correlación | (PENDIENTE — ver `06-correlacion-incidentes/`) |
| 4.3.6.6.1 Esquema de iteraciones | `evidencias/lecciones-aprendidas.md` (intro) |
| 4.3.6.6.2 Iteración 1 (preprueba) | `v2.0-it1/07-metricas/01_kpi-report-iter1.png` + `v2.0-it1/MANIFIESTO.md` + `v2.0-it1/08-extremo-a-extremo/README.md` |
| 4.3.6.6.3 Lecciones aprendidas | `evidencias/lecciones-aprendidas.md` + `v2.0-it1/07-metricas/02_lecciones-aprendidas.png` |
| 4.3.6.6.4 Iteración 2 (posprueba) | (PENDIENTE — no se aborda en esta sesión) |
| 4.4.2 Medición iteración 1 | `v2.0-it1/07-metricas/kpi_report.json` |
| 4.4.3 Análisis iteración 1 | `v2.0-it1/08-extremo-a-extremo/README.md` + `evidencias/lecciones-aprendidas.md` |
| 4.4.5 Comparación it1 vs it2 | `evidencias/comparacion-iteraciones.md` (columna it1 con datos reales; it2 pendiente) |

## Cómo verificar una captura

1. Localizar el archivo en la tabla del MANIFIESTO.
2. Si tiene `.txt` asociado, ese `.txt` es la fuente primaria (salida literal del comando).
3. El `.png` es la representación visual del mismo contenido (screenshot del navegador sobre `file://...txt` o sobre la URL del servicio).
4. Para los `.json`, el hash SHA-256 se puede obtener con `sha256sum archivo.json` desde el host.

## Auditoría original

- `evidencias/AUDITORIA-v2.0-it1.md`: clasificación de las 34 PNG previas como NO VERIFICABLES (marco macOS, insignia SIN/v2.0-it1, ruta inexistente `scripts/evidencia/fmt/wazuh.py`).
- `evidencias/v2.0-it1/_no-verificable/_INDICE-VERIFICACION.md`: re-verificación independiente hecha en esta sesión (2026-10-03), confirmación del veredicto NO VERIFICABLE.

## Convenciones de nombre

- `NN_descripcion-corta.png` (correlativo de 2 dígitos dentro de la subcarpeta)
- `NN_descripcion-corta.txt` (respaldo textual del comando)
- Archivos con `_prueba-sintetica` (sin uso en esta re-captura — toda la evidencia es de ejecuciones reales).