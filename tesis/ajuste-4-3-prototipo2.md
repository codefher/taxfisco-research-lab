# Estructura 4.3/4.4 — DECISIÓN v5: implementación en 4.3, resultados en 4.4 (definitiva)

> Documento de planificación. **Decisión del investigador (2026-10-01, v5,
> definitiva):**
> - **4.3 Implementación de la metodología de honeypot para la gestión de
>   incidentes** — con su título original. Contiene **toda la implementación
>   de ambos prototipos**.
> - **4.4 Resultados** — solo resultados: comparación preprueba-posprueba,
>   iteraciones, Wilcoxon, hipótesis.
>
> Reemplaza a v1–v4. Regla de oro: ninguna afirmación nueva sin evidencia;
> lo pendiente queda marcado como *pendiente* con su captura requerida.

## 0. Estructura vigente (aplicada al documento maestro v10)

```
4.3 Implementación de la metodología de honeypot para la gestión de incidentes
├── 4.3.1 a 4.3.9    Prototipo I — APROBADO, INTACTO
├── 4.3.10 Prueba controlada de extremo a extremo      (NUEVO)
├── 4.3.11 Matriz consolidada de trazabilidad          (NUEVO)
├── 4.3.12 Síntesis de la primera instanciación        (NUEVO)
├── 4.3.13 Segunda instanciación: adaptación al contexto SIN
│          (puente + tabla de equivalencias P1↔P2)
├── 4.3.14 Verificación del aislamiento y del despliegue
├── 4.3.15 Verificación de captura, custodia y correlación
└── 4.3.16 Síntesis de la implementación

4.4 Resultados
├── 4.4.1 Diseño de la comparación preprueba-posprueba
├── 4.4.2 Medición de la iteración 1 (preprueba)
├── 4.4.3 Análisis de la iteración 1 y lecciones aprendidas
├── 4.4.4 Medición de la iteración 2 (posprueba)
├── 4.4.5 Comparación de iteraciones y prueba de Wilcoxon pareada
├── 4.4.6 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
└── 4.4.7 Síntesis de los resultados
```

## 1. Lógica de la separación

- **4.3 = implementación (¿existe y opera?):** ambos prototipos. El 4.3.1–4.3.12
  verifica las 14 categorías funcionales en el Prototipo I (evidencia
  aprobada). El 4.3.13–4.3.16 documenta la segunda instanciación: adaptación
  del señuelo al contexto SIN, tabla de equivalencias, verificación de
  aislamiento y de captura/custodia/correlación.
- **4.4 = resultados (¿mejora?):** la medición del efecto con el diseño
  pre-experimental preprueba-posprueba (3.2): línea base it1, lecciones,
  posprueba it2, comparación pareada con Wilcoxon, evaluación de la
  hipótesis y de las metas.

## 2. Párrafo puente del 4.3.13 (borrador, ya aplicado)

> *Los apartados 4.3.1 a 4.3.12 documentaron la primera instanciación … El
> presente apartado documenta la segunda instanciación, que replica la misma
> arquitectura adaptando el señuelo al contexto de un servicio de impuestos
> nacionales. La medición del efecto … se presenta en el apartado 4.4.*

## 3. Tabla de equivalencias (4.3.13, borrador con pendientes)

| Elemento | Prototipo I (4.3.1–4.3.12) | Prototipo II (4.3.13–4.3.16) |
|---|---|---|
| Denominación del laboratorio | TaxFisco Research Lab | SIN Research Lab *(pendiente: captura)* |
| Redes | taxfisco-dmz, -honeypot, -ids, -soc | sin-dmz, -honeypot, -ids, -soc *(pendiente: `docker network ls`)* |
| Imágenes de señuelo | taxfisco/decoy-portal, taxfisco/decoy-api | sin/decoy-portal, sin/decoy-api *(pendiente: `docker images`)* |
| Servicios Docker Compose | 25 | 25 idénticos *(pendiente: `docker compose config --services`)* |
| Contenido del señuelo | Entidad homologada | Portal tributario nacional (contexto SIN) *(pendiente: capturas portal)* |
| Rol en la tesis | Verificación de componentes (OE3) | Validación con iteraciones (OE4) |

## 4. Checklist de evidencia pendiente

| # | Captura requerida | Sirve para |
|---|---|---|
| 1 | `docker network ls` del P2 (redes sin-*) | 4.3.13 equivalencias |
| 2 | `docker compose config --services` del P2 | 4.3.13 equivalencias |
| 3 | `docker images` del P2 (sin/decoy-*) | 4.3.13 equivalencias |
| 4 | Portal SIN (home y login) | 4.3.13, 4.3.14 |
| 5 | Aislamiento de red del P2 verificado | 4.3.14 |
| 6 | Prueba E2E (evento sintético) | 4.3.10 |
| 7 | Matriz consolidada de trazabilidad (tabla) | 4.3.11 |
| 8 | Ejecución it1 completa + kpi_report.json (P2) | 4.4.2 |
| 9 | Ejecución it2 completa + kpi_report.json (P2) | 4.4.4 |
| 10 | Tabla comparativa + cálculo Wilcoxon | 4.4.5 |

## 5. Historial de decisiones

- **v1 (descartada):** editar párrafos dentro del 4.3 aprobado.
- **v2 (descartada):** 4.4 separado sin título propio definido.
- **v3 (descartada):** todo dentro del 4.3 (4.3.10–4.3.21), sin 4.4.
- **v4 (descartada):** un apartado por prototipo, 4.3 = P1, 4.4 = P2 completo.
- **v5 (definitiva):** 4.3 = implementación de ambos prototipos (título
  original restaurado); 4.4 = resultados (iteraciones, Wilcoxon, hipótesis).
