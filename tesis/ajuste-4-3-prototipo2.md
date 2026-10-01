# Ajuste del apartado 4.3/4.4 — DECISIÓN v2: secciones divididas por prototipo

> Documento de planificación. **Decisión del investigador (2026-10-01):** el
> apartado 4.3 está **aprobado por la tutora y no se modifica en absoluto**.
> La incorporación del Prototipo II se resuelve con estructura aditiva:
> secciones divididas por prototipo. Este documento reemplaza a la propuesta
> anterior (opción C con ediciones dentro del 4.3), que queda descartada.
> Regla de oro: ninguna afirmación nueva sin evidencia; lo pendiente queda
> marcado como *pendiente* con su captura requerida.

## 1. Estructura final acordada

```
4.3 Implementación de la metodología de honeypot …     ← Prototipo I
   4.3.1 a 4.3.9     APROBADO — SIN NINGÚN CAMBIO
   4.3.10 Prueba controlada de extremo a extremo       ← NUEVO (se agrega al final)
   4.3.11 Matriz consolidada de trazabilidad           ← NUEVO
   4.3.12 Síntesis de la implementación                ← NUEVO
4.4 Segunda instanciación: prototipo en contexto SIN … ← Prototipo II (TODO NUEVO)
   4.4.1 Propósito, alcance y relación con el prototipo I   (puente explicativo)
   4.4.2 Adaptación del señuelo al contexto SIN + tabla de equivalencias P1↔P2
   4.4.3 Diseño de comparación preprueba-posprueba y condiciones invariantes
   4.4.4 Preprueba: ejecución y medición de la iteración 1 (v2.0-it1)
   4.4.5 Análisis de resultados y lecciones aprendidas de la iteración 1
   4.4.6 Aplicación de mejoras y ejecución de la iteración 2 (v2.1-it2)
   4.4.7 Comparación de iteraciones y prueba de Wilcoxon pareada
   4.4.8 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
   4.4.9 Síntesis de la validación, limitaciones y transferibilidad
```

## 2. Por qué esta estructura

- **4.3 intacto:** la tutora aprobó su redacción y sus 37 figuras; ningún
  párrafo aprobado se reescribe. Esto también preserva intacta la numeración
  de figuras y tablas ya revisadas.
- **4.3.10–4.3.12 nuevos:** el 4.3.9 termina anunciando «la prueba controlada
  de extremo a extremo» como continuación, y el índice oficial del apartado
  4.3 contempla 4.3.10, 4.3.11 y 4.3.12, que hoy no existen. Agregarlos al
  final **resuelve la referencia colgada sin tocar una sola línea aprobada**.
- **4.4 como sección del Prototipo II:** concentra todo lo que cambia y todo
  lo que se mide (OE4). El único "puente" narrativo es el párrafo de apertura
  del 4.4.1, que explica al lector la relación entre las dos instanciaciones.

## 3. Párrafo puente del 4.4.1 (borrador)

> *El apartado 4.3 documentó la primera instanciación de la metodología en un
> entorno controlado construido sobre la base de una entidad homologada del
> rubro de servicios fiscales digitales, con el propósito de verificar que las
> catorce categorías funcionales del diseño quedan materializadas en la
> práctica. El presente apartado documenta la segunda instanciación, que
> replica la misma arquitectura adaptando el señuelo al contexto de un
> servicio de impuestos nacionales, y cuyo propósito es validar la eficacia de
> la metodología mediante dos iteraciones de operación (preprueba y
> posprueba), conforme al diseño pre-experimental declarado en el apartado
> 3.2. La distinción entre la verificación de componentes y la validación del
> efecto preserva el carácter transferible de la metodología, dado que la
> operación de las categorías funcionales no depende de la marca ni del
> contexto institucional del señuelo.*

## 4. Tabla de equivalencias para el 4.4.2 (borrador con pendientes)

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
| 4 | Portal SIN (home y login) | 4.4.2 equivalencias, 4.4.3 |
| 5 | Prueba E2E del P2, secuencia completa (evento sintético) | 4.3.10 |
| 6 | Matriz consolidada de trazabilidad (tabla) | 4.3.11 |
| 7 | Ejecución it1 completa + kpi_report.json | 4.4.4 |
| 8 | Ejecución it2 completa + kpi_report.json | 4.4.6 |
| 9 | Tabla comparativa + cálculo Wilcoxon | 4.4.7 |

## 6. Historial de decisiones

- **v1 (descartada):** ajustar párrafos dentro del 4.3 (introducción, 4.3.1,
  4.3.2) para encuadrar los dos entornos. Descartada porque el 4.3 ya fue
  aprobado por la tutora y tocarlo obligaría a re-aprobar texto validado.
- **v2 (vigente):** secciones divididas por prototipo. 4.3 intacto +
  4.3.10–4.3.12 agregados + 4.4 completo como sección del Prototipo II.
