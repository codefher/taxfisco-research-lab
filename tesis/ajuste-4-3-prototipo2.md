# Estructura 4.3/4.4 — DECISIÓN v7: 4.3.1 = Prototipo I, 4.3.2 = Prototipo II (definitiva)

> Documento de planificación. **Decisión del investigador (2026-10-01, v7,
> definitiva):** el 4.3 se organiza en dos grandes ramas numeradas:
> - **4.3.1 Implementación del prototipo I (entidad homologada)** — lo ya
>   aprobado por la tutora, renumerado y anidado como 4.3.1.1 a 4.3.1.12.
> - **4.3.2 Segundo prototipo: adaptación al contexto del SIN e iteraciones
>   de mejora** — con subsecciones numeradas 4.3.2.1 a 4.3.2.7.
> Reemplaza a v1–v6. Regla de oro: ninguna afirmación nueva sin evidencia.

## 0. Estructura vigente (aplicada al documento maestro v10)

```
4.3 Implementación de la metodología de honeypot para la gestión de incidentes
├── 4.3.1 Implementación del prototipo I (entidad homologada)   APROBADO
│   ├── 4.3.1.1 Propósito, alcance y línea base
│   ├── 4.3.1.2 Entorno controlado de implementación
│   ├── 4.3.1.3 Plataforma tecnológica del prototipo
│   ├── 4.3.1.4 Matriz de trabajo y criterios de verificación
│   ├── 4.3.1.5 Fase 1. Diseño del señuelo
│   ├── 4.3.1.6 Fase 2. Despliegue aislado
│   ├── 4.3.1.7 Fase 3. Captura, enriquecimiento y custodia
│   ├── 4.3.1.8 Fase 4. Correlación con gestión de incidentes
│   ├── 4.3.1.9 Fase 5. Medición y lecciones aprendidas
│   ├── 4.3.1.10 Prueba controlada de extremo a extremo
│   ├── 4.3.1.11 Matriz consolidada de trazabilidad
│   └── 4.3.1.12 Síntesis de la primera instanciación
└── 4.3.2 Segundo prototipo: adaptación al contexto del SIN e iteraciones
    ├── 4.3.2.1 Adaptación del señuelo y equivalencia entre prototipos
    ├── 4.3.2.2 Fase 1. Diseño del señuelo SIN
    ├── 4.3.2.3 Fase 2. Despliegue aislado
    ├── 4.3.2.4 Fase 3. Captura, enriquecimiento y custodia
    ├── 4.3.2.5 Fase 4. Correlación con gestión de incidentes
    ├── 4.3.2.6 Fase 5. Medición con iteraciones  (remite al 4.4)
    └── 4.3.2.7 Síntesis del segundo prototipo

4.4 Resultados
├── 4.4.1 Diseño de la comparación preprueba-posprueba
├── 4.4.2 Medición de la iteración 1 (preprueba)
├── 4.4.3 Análisis de la iteración 1 y lecciones aprendidas
├── 4.4.4 Medición de la iteración 2 (posprueba)
├── 4.4.5 Comparación de iteraciones y prueba de Wilcoxon pareada
├── 4.4.6 Evaluación de la hipótesis y de las metas (IIAM, IMGI, Tabla 2)
└── 4.4.7 Síntesis de los resultados
```

## 5. Historial de decisiones

- **v1 (descartada):** editar párrafos dentro del 4.3 aprobado.
- **v2 (descartada):** 4.4 separado sin título propio definido.
- **v3 (descartada):** todo dentro del 4.3 (4.3.10–4.3.21), sin 4.4.
- **v4 (descartada):** un apartado por prototipo, 4.3 = P1, 4.4 = P2 completo.
- **v5 (descartada):** 4.3 = implementación de ambos prototipos en plano
  (4.3.13–4.3.16); 4.4 = resultados. Se veía raro la continuación plana.
- **v6 (descartada):** fases del P2 con subtítulo #### sin número bajo 4.3.13;
  se veía raro que la numeración plana continuara.
- **v7 (definitiva):** dos ramas numeradas — 4.3.1 Prototipo I (aprobado
  anidado como 4.3.1.1–4.3.1.12) y 4.3.2 Segundo prototipo (4.3.2.1–4.3.2.7).
  Referencias cruzadas renumeradas (4.3.3→4.3.1.3, 4.3.5→4.3.1.5,
  4.3.11→4.3.1.11).
