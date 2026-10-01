# Propuesta de ajuste del apartado 4.3 para incorporar el Prototipo II

> Documento de planificación. No modifica el documento maestro todavía.
> Objetivo: acomodar el 4.3 (hoy 100 % centrado en el Prototipo I,
> *TaxFisco Research Lab*) para que la tesis refleje las **dos
> instanciaciones** de la metodología: el Prototipo I (entidad homologada,
> evidencia de componentes) y el Prototipo II (contexto SIN, instrumento de
> validación con iteraciones, OE4).
> Regla de oro: ninguna afirmación nueva sin evidencia; lo pendiente queda
> marcado como *pendiente* con su captura requerida.

## 1. Diagnóstico del estado actual

| Apartado | Estado actual | Problema |
|---|---|---|
| 4.3 (introducción) | Habla de "el prototipo" en singular | No reconoce la existencia de una segunda instanciación |
| 4.3.1 | Propósito ligado solo al OE3 | No distingue la verificación de componentes (4.3) de la validación de eficacia (4.4) |
| 4.3.2 | Describe *TaxFisco Research Lab*, redes `taxfisco-*` | El Prototipo II usa `sin-research-lab`, redes `sin-*`; el lector no sabe que el diseño se replicó |
| 4.3.3–4.3.9 | Evidencia del Prototipo I (37 figuras) | Válida como verificación de componentes; no debe duplicarse para el P2 |
| 4.3.9 (cierre) | Anuncia "la prueba controlada de extremo a extremo" como continuación | El documento salta al Capítulo V; referencia colgada |

Principio rector: la metodología es **agnóstica de tecnología y de marca**
(principio P2, 4.2). El 4.3 verifica que las catorce categorías funcionales
están materializadas; el 4.4 mide el efecto de la metodología. El Prototipo
II existe para cumplir la F5 **con iteraciones** (preprueba/posprueba) en un
contexto distinto, lo cual además *refuerza* la transferibilidad.

## 2. Estructura recomendada (opción C: 4.3 verifica, 4.4 valida)

```
4.3 Implementación de la metodología …
    4.3.1 Propósito, alcance y línea base        ← ajustado (marco de dos entornos)
    4.3.2 Entorno controlado de implementación   ← ajustado (entorno A + equivalencia con B)
    4.3.3 Plataforma tecnológica                 ← sin cambios de fondo (nota de instanciación)
    4.3.4 Matriz de trabajo                      ← sin cambios
    4.3.5–4.3.9 Fases F1–F5                      ← sin cambios (evidencia del entorno A)
4.4 Validación de la metodología (OE4)           ← índice ya propuesto (indice-4-4-validacion.md)
    4.4.3 Contexto de validación: adaptación al SIN = el "segundo prototipo"
```

Descartada la opción B (replicar las fases 4.3.5–4.3.9 completas para el P2):
duplicaría ~40 figuras sin aportar verificación nueva, porque el P2 replica la
misma arquitectura de 25 servicios y las mismas catorce categorías; lo que
cambia es el contenido del señuelo y el contexto, y eso se demuestra en 4.4.

## 3. Ediciones concretas propuestas

### 3.1 Introducción del 4.3 (después del primer párrafo, línea ~1798)

Añadir un párrafo de encuadre (borrador):

> *La metodología se instancia en dos entornos controlados consecutivos. El
> primero, denominado entorno de verificación, materializa el prototipo sobre
> la base de una entidad homologada del rubro de servicios fiscales digitales
> y se emplea para comprobar componente por componente que las catorce
> categorías funcionales del diseño quedan materializadas en la práctica; su
> evidencia se documenta en los apartados 4.3.2 a 4.3.9. El segundo, denominado
> entorno de validación, replica la misma arquitectura adaptando el señuelo al
> contexto de un servicio de impuestos nacionales y se emplea para medir el
> efecto de la metodología mediante dos iteraciones de operación
> (preprueba y posprueba), conforme al diseño pre-experimental declarado en el
> apartado 3.2; sus resultados se documentan en el apartado 4.4. La
> distinción entre ambos entornos preserva el carácter transferible de la
> metodología, dado que la verificación de componentes no depende de la marca
> ni del contexto institucional del señuelo.*

### 3.2 Párrafo de propósito del 4.3.1 (línea ~1806)

Ajustar el cierre del párrafo para distinguir OE3 de OE4:

> *…Esta implementación se orienta al cumplimiento del tercer objetivo
> específico (OE3) … en un entorno controlado. La comprobación de que los
> componentes operan no constituye por sí misma evidencia de eficacia: la
> medición del efecto de la metodología sobre los indicadores de gestión de
> incidentes corresponde al cuarto objetivo específico (OE4) y se desarrolla
> en el apartado 4.4 sobre el segundo entorno controlado.*

### 3.3 Apertura del 4.3.2 (línea ~1820)

Cambiar "un entorno experimental" por la denominación del primer entorno y
añadir el párrafo de equivalencia con el segundo:

> *La implementación se desarrolla en un entorno experimental denominado
> TaxFisco Research Lab, empleado como primer entorno controlado (entorno de
> verificación)…* (resto del párrafo sin cambios).

Añadir después del párrafo de los cuatro segmentos (línea ~1836) un párrafo +
tabla de equivalencias (borrador, evidencia pendiente):

> *El segundo entorno controlado (entorno de validación) replica esta misma
> estructura de cuatro segmentos con la denominación sin-dmz, sin-honeypot,
> sin-ids y sin-soc, conservando los rangos de direcciones y la distribución
> funcional de componentes, de modo que la única diferencia entre ambos
> entornos reside en el contenido y la identidad visual del señuelo. La
> equivalencia entre los dos entornos se resume en la Tabla X.*

**Tabla X. Equivalencia entre el entorno de verificación y el entorno de validación**

| Elemento | Entorno de verificación (P1) | Entorno de validación (P2) |
|---|---|---|
| Denominación del laboratorio | TaxFisco Research Lab | SIN Research Lab *(pendiente: captura docker ps / README)* |
| Redes | taxfisco-dmz, -honeypot, -ids, -soc | sin-dmz, -honeypot, -ids, -soc *(pendiente: captura `docker network ls` en evidencias/v2.0-it1/03-aislamiento-red)* |
| Imágenes de señuelo | taxfisco/decoy-portal, taxfisco/decoy-api | sin/decoy-portal, sin/decoy-api *(pendiente: captura `docker images`)* |
| Servicios Docker Compose | 25 | 25 (idénticos) *(pendiente: captura `docker compose config --services`)* |
| Contenido del señuelo | Entidad homologada | Portal tributario nacional (contexto SIN) *(pendiente: captura portal)* |
| Rol en la tesis | Verificación de componentes (OE3) | Validación con iteraciones (OE4) |

### 3.4 Nota al cierre del 4.3.3 (línea ~1904)

Añadir una frase de instanciación:

> *La misma correspondencia entre categorías funcionales y componentes aplica
> al segundo entorno controlado, dado que este replica la arquitectura del
> primero; la verificación específica de los componentes del entorno de
> validación se resume en el apartado 4.4.3 con remisión a su evidencia.*

### 3.5 Referencia colgada del 4.3.9 (línea ~2504)

Decisión pendiente (marcada también en indice-4-4-validacion.md): o bien se
crea el 4.3.10 con la prueba E2E (evidencia ya disponible en
`evidencias/v2.0-it1/08-extremo-a-extremo` si se capturó), o bien el párrafo
final se reescribe para remitir al 4.4. **Recomendación:** crear el 4.3.10
(prueba controlada E2E, evento sintético) porque el índice oficial 4.3 lo
contempla (4.3.10, 4.3.11 matriz consolidada, 4.3.12 síntesis); la matriz y la
síntesis también faltan y deben cerrar el 4.3.

## 4. Checklist de evidencia que falta capturar (para las tablas nuevas)

| # | Captura requerida | Sirve para |
|---|---|---|
| 1 | `docker network ls` del P2 (redes sin-*) | Tabla equivalencia 4.3.2 |
| 2 | `docker compose config --services` del P2 (25 servicios) | Tabla equivalencia 4.3.2 |
| 3 | `docker images` del P2 (sin/decoy-*) | Tabla equivalencia 4.3.2 |
| 4 | Pantalla del portal SIN (home y login) | Tabla equivalencia 4.3.2, 4.4.3 |
| 5 | Prueba E2E (secuencia completa, evento sintético) | 4.3.10 |
| 6 | Matriz consolidada de trazabilidad (tabla) | 4.3.11 |
