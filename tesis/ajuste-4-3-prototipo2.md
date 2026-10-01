# Estructura 4.3/4.4 — DECISIÓN v4: un apartado por prototipo (definitiva)

> Documento de planificación. **Decisión del investigador (2026-10-01, v4,
> definitiva):** estructura de **un apartado por prototipo**:
> - **4.3 Implementación del prototipo I (entidad homologada)** — contenido
>   ya aprobado por la tutora, intacto.
> - **4.4 Segundo prototipo: adaptación al contexto del SIN e iteraciones de
>   mejora** — todo el contenido nuevo.
>
> Reemplaza a v1 (edits dentro del 4.3), v2 (4.4 sin título propio) y v3 (todo
> dentro del 4.3). Regla de oro: ninguna afirmación nueva sin evidencia; lo
> pendiente queda marcado como *pendiente* con su captura requerida.

## 1. Estructura final

```
4.3 Implementación del prototipo I (entidad homologada)     ← APROBADO, INTACTO
├── 4.3.1 Propósito, alcance y línea base
├── 4.3.2 Entorno controlado de implementación
├── 4.3.3 Plataforma tecnológica del prototipo
├── 4.3.4 Matriz de trabajo y criterios de verificación
├── 4.3.5 Fase 1. Diseño del señuelo
├── 4.3.6 Fase 2. Despliegue aislado
├── 4.3.7 Fase 3. Captura, enriquecimiento y custodia
├── 4.3.8 Fase 4. Correlación con gestión de incidentes
├── 4.3.9 Fase 5. Medición y lecciones aprendidas
└── (cierre: el párrafo final aprobado anuncia la prueba E2E; se decide abajo
     si el E2E va en 4.3.10 o se asigna al 4.4)

4.4 Segundo prototipo: adaptación al contexto del SIN e iteraciones de mejora
├── 4.4.1 Propósito, alcance y relación con el prototipo I      (puente)
├── 4.4.2 Adaptación del señuelo al contexto SIN + tabla equivalencias P1↔P2
├── 4.4.3 Verificación del aislamiento y del despliegue (F2 del P2)
├── 4.4.4 Verificación de captura, custodia y correlación (F3–F4 del P2)
├── 4.4.5 Fase 5, iteración 1 (preprueba): ejecución y medición (v2.0-it1)
├── 4.4.6 Análisis de la iteración 1 y lecciones aprendidas (L1–Ln)
├── 4.4.7 Fase 5, iteración 2 (posprueba): mejoras y re-ejecución (v2.1-it2)
├── 4.4.8 Comparación de iteraciones y prueba de Wilcoxon pareada
├── 4.4.9 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
└── 4.4.10 Síntesis, limitaciones y transferibilidad
```

## 2. Decisión pendiente menor: la prueba E2E

El párrafo final **aprobado** del 4.3.9 dice que «la implementación continúa
con la prueba controlada de extremo a extremo». Dos opciones, ambas sin tocar
texto aprobado:

- **(a) Agregar 4.3.10** «Prueba controlada de extremo a extremo» al final del
  4.3 — la continuación prometida ocurre donde el texto aprobado anuncia.
- **(b) Dejar que el 4.4.5 ejerza la secuencia E2E** y reescribir solo la
  transición… — NO: implicaría tocar el párrafo aprobado. Descartada.

**Recomendación: opción (a).** Además, el índice oficial del diseño
contempla 4.3.10 (prueba E2E), 4.3.11 (matriz consolidada) y 4.3.12
(síntesis); si la tutora los quiere, también se agregan como 4.3.10–4.3.12
sin conflicto con el 4.4.

## 3. Párrafo puente del 4.4.1 (borrador)

> *El apartado 4.3 documentó la implementación de la metodología en un primer
> prototipo construido sobre la base de una entidad homologada del rubro de
> servicios fiscales digitales, con el propósito de verificar que las catorce
> categorías funcionales del diseño quedan materializadas en la práctica. El
> presente apartado documenta el segundo prototipo, que replica la misma
> arquitectura adaptando el señuelo al contexto de un servicio de impuestos
> nacionales y opera la fase de medición en dos iteraciones consecutivas
> (preprueba y posprueba), conforme al diseño pre-experimental declarado en el
> apartado 3.2. La distinción entre la verificación de componentes del primer
> prototipo y la validación del efecto en el segundo preserva el carácter
> transferible de la metodología, dado que la operación de las categorías
> funcionales no depende de la marca ni del contexto institucional del
> señuelo.*

## 4. Tabla de equivalencias (4.4.2, borrador con pendientes)

| Elemento | Prototipo I (4.3) | Prototipo II (4.4) |
|---|---|---|
| Denominación del laboratorio | TaxFisco Research Lab | SIN Research Lab *(pendiente: captura)* |
| Redes | taxfisco-dmz, -honeypot, -ids, -soc | sin-dmz, -honeypot, -ids, -soc *(pendiente: `docker network ls`)* |
| Imágenes de señuelo | taxfisco/decoy-portal, taxfisco/decoy-api | sin/decoy-portal, sin/decoy-api *(pendiente: `docker images`)* |
| Servicios Docker Compose | 25 | 25 idénticos *(pendiente: `docker compose config --services`)* |
| Contenido del señuelo | Entidad homologada | Portal tributario nacional (contexto SIN) *(pendiente: capturas portal)* |
| Rol en la tesis | Verificación de componentes (OE3) | Validación con iteraciones (OE4) |

## 5. Checklist de evidencia pendiente

| # | Captura requerida | Sirve para |
|---|---|---|
| 1 | `docker network ls` del P2 (redes sin-*) | 4.4.2 equivalencias |
| 2 | `docker compose config --services` del P2 | 4.4.2 equivalencias |
| 3 | `docker images` del P2 (sin/decoy-*) | 4.4.2 equivalencias |
| 4 | Portal SIN (home y login) | 4.4.2, 4.4.3 |
| 5 | Aislamiento de red del P2 verificado | 4.4.3 |
| 6 | Prueba E2E (evento sintético, P1 o P2) | 4.3.10 |
| 7 | Matriz consolidada de trazabilidad (tabla) | 4.3.11 |
| 8 | Ejecución it1 completa + kpi_report.json (P2) | 4.4.5 |
| 9 | Ejecución it2 completa + kpi_report.json (P2) | 4.4.7 |
| 10 | Tabla comparativa + cálculo Wilcoxon | 4.4.8 |

## 6. Historial de decisiones

- **v1 (descartada):** editar párrafos dentro del 4.3 aprobado.
- **v2 (descartada):** 4.4 separado sin título propio definido.
- **v3 (descartada):** todo dentro del 4.3 (4.3.10–4.3.21).
- **v4 (definitiva):** un apartado por prototipo.
  `4.3 Implementación del prototipo I (entidad homologada)` +
  `4.4 Segundo prototipo: adaptación al contexto del SIN e iteraciones de
  mejora`.
