# Ajuste del apartado 4.3 — DECISIÓN v3: todo dentro del 4.3, dividido por prototipo

> Documento de planificación. **Decisión del investigador (2026-10-01, v3):**
> todo el contenido nuevo va **dentro de la sección 4.3**; no se crea apartado
> 4.4. El 4.3.1–4.3.9 (Prototipo I) está **aprobado por la tutora y no se
> modifica**; todo lo nuevo se agrega como sub-apartados 4.3.10 en adelante.
> Esta versión reemplaza a la v2 (que proponía un 4.4 separado).
> Regla de oro: ninguna afirmación nueva sin evidencia; lo pendiente queda
> marcado como *pendiente* con su captura requerida.

## 1. Estructura final del 4.3 (ambos prototipos)

```
4.3 Implementación de la metodología de honeypot …
│
│  PRIMER BLOQUE — Prototipo I (entidad homologada) — APROBADO, INTACTO
│
├── 4.3.1 Propósito, alcance y línea base            APROBADO — sin cambios
├── 4.3.2 Entorno controlado de implementación       APROBADO — sin cambios
├── 4.3.3 Plataforma tecnológica del prototipo       APROBADO — sin cambios
├── 4.3.4 Matriz de trabajo y criterios              APROBADO — sin cambios
├── 4.3.5 Fase 1. Diseño del señuelo                 APROBADO — sin cambios
├── 4.3.6 Fase 2. Despliegue aislado                 APROBADO — sin cambios
├── 4.3.7 Fase 3. Captura, enriquecimiento y custodia APROBADO — sin cambios
├── 4.3.8 Fase 4. Correlación con gestión de incidentes APROBADO — sin cambios
├── 4.3.9 Fase 5. Medición y lecciones aprendidas    APROBADO — sin cambios
│
│  SEGUNDO BLOQUE — Cierre de la primera instanciación (nuevo, agregado)
│
├── 4.3.10 Prueba controlada de extremo a extremo (evento sintético)
├── 4.3.11 Matriz consolidada de trazabilidad
├── 4.3.12 Síntesis de la primera instanciación
│
│  TERCER BLOQUE — Prototipo II (contexto SIN): segunda instanciación (nuevo)
│
├── 4.3.13 Segunda instanciación: propósito y adaptación al contexto SIN
│         (párrafo puente + tabla de equivalencias P1↔P2)
├── 4.3.14 Fase 1–F2 del Prototipo II: señuelo SIN y despliegue aislado
├── 4.3.15 Fase 3–F4 del Prototipo II: captura, custodia y correlación
├── 4.3.16 Fase 5, iteración 1 (preprueba): ejecución y medición (v2.0-it1)
├── 4.3.17 Análisis de la iteración 1 y lecciones aprendidas (L1–Ln)
├── 4.3.18 Fase 5, iteración 2 (posprueba): mejoras y re-ejecución (v2.1-it2)
├── 4.3.19 Comparación de iteraciones y prueba de Wilcoxon pareada
├── 4.3.20 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
└── 4.3.21 Síntesis de la validación, limitaciones y transferibilidad
```

## 2. Por qué esta numeración

- **4.3.10–4.3.12:** resuelven la referencia colgada del 4.3.9 (que anuncia la
  prueba E2E) y cierran el índice oficial que el propio diseño contemplaba;
  pertenecen a la primera instanciación.
- **4.3.13:** un solo sub-apartado de transición con el párrafo puente y la
  tabla de equivalencias; es el único lugar donde se explica la relación
  entre ambos prototipos.
- **4.3.14–4.3.15:** las fases F1–F4 del P2 se documentan de forma **resumida**
  (qué cambió: señuelo SIN, aislamiento verificado; qué se mantuvo: mismas 14
  categorías, mismos 25 servicios), con remisión a la evidencia del P2. No se
  duplican las 37 figuras del 4.3.5–4.3.8.
- **4.3.16–4.3.21:** la F5 **con iteraciones** (lo que pidió la tutora):
  preprueba → lecciones → posprueba → comparación con Wilcoxon → hipótesis.

## 3. Párrafo puente del 4.3.13 (borrador)

> *Los apartados 4.3.1 a 4.3.12 documentaron la primera instanciación de la
> metodología en un entorno controlado construido sobre la base de una entidad
> homologada del rubro de servicios fiscales digitales, con el propósito de
> verificar que las catorce categorías funcionales del diseño quedan
> materializadas en la práctica. Los apartados siguientes documentan la
> segunda instanciación, que replica la misma arquitectura adaptando el
> señuelo al contexto de un servicio de impuestos nacionales, y cuyo propósito
> es validar la eficacia de la metodología mediante dos iteraciones de
> operación (preprueba y posprueba), conforme al diseño pre-experimental
> declarado en el apartado 3.2. La distinción entre la verificación de
> componentes y la validación del efecto preserva el carácter transferible de
> la metodología, dado que la operación de las categorías funcionales no
> depende de la marca ni del contexto institucional del señuelo.*

## 4. Tabla de equivalencias (4.3.13, borrador con pendientes)

| Elemento | Prototipo I (4.3.1–4.3.12) | Prototipo II (4.3.13–4.3.21) |
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
| 1 | `docker network ls` del P2 (redes sin-*) | 4.3.13 equivalencias |
| 2 | `docker compose config --services` del P2 | 4.3.13 equivalencias |
| 3 | `docker images` del P2 (sin/decoy-*) | 4.3.13 equivalencias |
| 4 | Portal SIN (home y login) | 4.3.13, 4.3.14 |
| 5 | Aislamiento de red del P2 verificado | 4.3.14 |
| 6 | Prueba E2E del P1 o P2 (evento sintético) | 4.3.10 |
| 7 | Matriz consolidada de trazabilidad (tabla) | 4.3.11 |
| 8 | Ejecución it1 completa + kpi_report.json (P2) | 4.3.16 |
| 9 | Ejecución it2 completa + kpi_report.json (P2) | 4.3.18 |
| 10 | Tabla comparativa + cálculo Wilcoxon | 4.3.19 |

## 6. Historial de decisiones

- **v1 (descartada):** editar párrafos dentro del 4.3 aprobado para encuadrar
  los dos entornos.
- **v2 (descartada):** crear apartado 4.4 separado para el Prototipo II.
- **v3 (vigente):** todo dentro del 4.3. 4.3.1–4.3.9 intactos (aprobados);
  4.3.10–4.3.21 nuevos y agregativos; la sección queda dividida por prototipo
  en tres bloques: verificación (P1), cierre de P1, y validación con
  iteraciones (P2).
