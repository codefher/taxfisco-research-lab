# Estructura 4.3/4.4 — DECISIÓN v6: fases del P2 con escalón jerárquico (definitiva)

> Documento de planificación. **Decisión del investigador (2026-10-01, v6,
> definitiva):** el segundo prototipo recorre las **cinco fases F1–F5** como
> la primera instanciación, anidadas como subtítulo de cuarto nivel
> (#### Fase N) dentro del 4.3.13, para dar el escalón visual que separa el
> bloque del P2 de la numeración plana 4.3.1–4.3.12. Reemplaza a v1–v5.
> Regla de oro: ninguna afirmación nueva sin evidencia; lo pendiente queda
> marcado como *pendiente* con su captura requerida.

## 0. Estructura vigente (aplicada al documento maestro v10)

```
4.3 Implementación de la metodología de honeypot para la gestión de incidentes
├── 4.3.1 a 4.3.9    Prototipo I — APROBADO, INTACTO
├── 4.3.10 Prueba controlada de extremo a extremo      (NUEVO)
├── 4.3.11 Matriz consolidada de trazabilidad          (NUEVO)
├── 4.3.12 Síntesis de la primera instanciación        (NUEVO)
├── 4.3.13 Segunda instanciación: prototipo en contexto SIN
│   (puente + tabla de equivalencias P1↔P2)
│   #### Fase 1. Diseño del señuelo SIN
│   #### Fase 2. Despliegue aislado
│   #### Fase 3. Captura, enriquecimiento y custodia
│   #### Fase 4. Correlación con gestión de incidentes
│   #### Fase 5. Medición con iteraciones  (remite al 4.4)
└── 4.3.14 Síntesis de la implementación

4.4 Resultados
├── 4.4.1 Diseño de la comparación preprueba-posprueba
├── 4.4.2 Medición de la iteración 1 (preprueba)
├── 4.4.3 Análisis de la iteración 1 y lecciones aprendidas
├── 4.4.4 Medición de la iteración 2 (posprueba)
├── 4.4.5 Comparación de iteraciones y prueba de Wilcoxon pareada
├── 4.4.6 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
└── 4.4.7 Síntesis de los resultados
```

## 1. Lógica de la separación y del escalón

- **4.3 = implementación (¿existe y opera?):** ambos prototipos recorren las
  mismas cinco fases, lo cual evidencia transferibilidad (principio P2). Las
  fases del P2 son compactas y remiten a la evidencia; no duplican la
  redacción aprobada del 4.3.5–4.3.8.
- **Escalón ####:** las fases del P2 viven un nivel por debajo del 4.3.13, así
  el bloque se distingue visualmente sin romper la numeración 4.3.x.
- **4.4 = resultados (¿mejora?):** preprueba/posprueba, comparación pareada
  con Wilcoxon, evaluación de la hipótesis y de las metas.

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
- **v5 (descartada):** 4.3 = implementación de ambos prototipos en plano
  (4.3.13–4.3.16); 4.4 = resultados. Se veía raro la continuación plana.
- **v6 (definitiva):** el P2 recorre las cinco fases F1–F5 anidadas con
  subtítulo de cuarto nivel (#### Fase N) dentro del 4.3.13, que da el
  escalón visual. Síntesis del P2 en 4.3.14. 4.4 = resultados sin cambios.
