# Estructura 4.3/4.4 — DECISIÓN v8: marco general + 4.3.5 P1 + 4.3.6 P2 (definitiva)

> Documento de planificación. **Decisión del investigador (2026-10-01, v8,
> definitiva):** el 4.3 abre con cuatro apartados generales que conciernen a
> ambos prototipos (propósito, entorno, plataforma, matriz de trabajo) y
> después se divide en dos ramas: 4.3.5 Prototipo I (aprobado) y 4.3.6
> Segundo prototipo con su esquema de iteraciones de mejora.
> Reemplaza a v1–v7. Regla de oro: ninguna afirmación nueva sin evidencia.

## 0. Estructura vigente (aplicada al documento maestro v10)

```
4.3 Implementación de la metodología de honeypot para la gestión de incidentes
├── 4.3.1 Propósito, alcance y línea base            (general, ambos prototipos)
├── 4.3.2 Entorno controlado de implementación      (general)
├── 4.3.3 Plataforma tecnológica del prototipo      (general)
├── 4.3.4 Matriz de trabajo y criterios de verificación  (general)
├── 4.3.5 Implementación del prototipo I (entidad homologada)   APROBADO
│   ├── 4.3.5.1 Fase 1. Diseño del señuelo
│   ├── 4.3.5.2 Fase 2. Despliegue aislado
│   ├── 4.3.5.3 Fase 3. Captura, enriquecimiento y custodia
│   ├── 4.3.5.4 Fase 4. Correlación con gestión de incidentes
│   ├── 4.3.5.5 Fase 5. Medición y lecciones aprendidas
│   ├── 4.3.5.6 Prueba controlada de extremo a extremo
│   ├── 4.3.5.7 Matriz consolidada de trazabilidad
│   └── 4.3.5.8 Síntesis de la primera instanciación
└── 4.3.6 Segundo prototipo: adaptación al contexto del SIN e iteraciones de mejora
    ├── 4.3.6.1 Adaptación del señuelo y equivalencia entre prototipos
    ├── 4.3.6.2 Esquema de iteraciones de mejora   (NUEVO: preprueba →
    │   lecciones → mejoras → posprueba; muestras pareadas; remite al 4.4)
    ├── 4.3.6.3 Fase 1. Diseño del señuelo SIN
    ├── 4.3.6.4 Fase 2. Despliegue aislado
    ├── 4.3.6.5 Fase 3. Captura, enriquecimiento y custodia
    ├── 4.3.6.6 Fase 4. Correlación con gestión de incidentes
    ├── 4.3.6.7 Fase 5. Medición con iteraciones  (remite a 4.3.6.2 y 4.4)
    └── 4.3.6.8 Síntesis del segundo prototipo

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
- **v7 (descartada):** dos ramas numeradas — 4.3.1 Prototipo I (aprobado
  anidado como 4.3.1.1–4.3.1.12) y 4.3.2 Segundo prototipo (4.3.2.1–4.3.2.7).
  El investigador observó que propósito, entorno, plataforma y matriz son
  comunes a los dos prototipos y no debían quedar bajo el Prototipo I.
- **v8 (definitiva):** cuatro apartados generales 4.3.1–4.3.4 (subidos del
  antiguo 4.3.1.1–4.3.1.4 de la v7, por criterio del investigador) y luego
  4.3.5 Prototipo I (4.3.5.1–4.3.5.8) y 4.3.6 Segundo prototipo
  (4.3.6.1–4.3.6.8). Nueva subsección 4.3.6.2 "Esquema de iteraciones de
  mejora" que demuestra el ciclo preprueba → lecciones → mejoras → posprueba
  y materializa la diferencia metodológica frente al Prototipo I (muestras
  pareadas según diseño pre-experimental del 3.2; comparación y Wilcoxon en
  el 4.4). Referencias cruzadas renumeradas y verificadas sin huérfanas.
