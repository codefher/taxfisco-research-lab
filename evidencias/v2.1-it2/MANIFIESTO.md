# MANIFIESTO DE EVIDENCIAS — Prototipo II, iteración 2 (`v2.1-it2`)

## Identificación de la iteración

| Campo | Valor |
|---|---|
| Iteración | 2 (`v2.1-it2`) |
| Rama | `prototipo-2-sin` |
| Fecha de ejecución | 2026-10-04 |
| Campaña | S01–S10 re-ejecutada sobre el mismo laboratorio |
| Fuente de métricas | `07-metricas/kpi_report.json` |
| Alcance | Cerrar las lecciones de instrumentación L11, L12, L13 y L14 |

## Qué cambió respecto de it1

Esta iteración **no modificó la arquitectura del laboratorio ni los señuelos**.
Actuó sobre el instrumento de medición y sobre la robustez de la campaña:

| Lección | Qué se corrigió |
|---|---|
| L11 | El calculador leía `targets_scanned`, clave que ningún escenario escribía con ese nombre. Ahora acepta `targets_scanned`, `targets` y `target`, y cuatro escenarios declaran su objetivo |
| L12 | `sqlmap`, `hydra` y `nikto` se ejecutaban sin límite de tiempo y bloqueaban la campaña |
| L13 | S09 informaba una captura en Cowrie que nunca ocurría, por `sshpass` ausente y sin comprobación |
| L14 | OpenCanary y el DNS de Zeek registraban eventos que ninguna fuente de detección leía |

También se instalaron en el contenedor atacante las herramientas que los
escenarios necesitan y que faltaban: `sshpass`, `openssh-client` y `gobuster`,
además de las nueve instaladas en la iteración 1.

## Resultado de la medición

| Indicador | it1 | it2 |
|---|---|---|
| Escenarios con MTTD medido | 4 de 10 | **10 de 10** |
| MTTD medio | 5,22 s (4 muestras) | 2,02 s (10 muestras) |
| MTTD mínimo / máximo | 1,06 s / 16,85 s | 0,00 s / 15,91 s |
| MTTR / MTTC / MTTContain | n/d | n/d |

### Aviso metodológico

La diferencia entre las medias de it1 e it2 **no es una mejora del
laboratorio**. El señuelo detectaba igual en ambas iteraciones; lo que estaba
roto era el instrumento que medía. Las medias no son comparables entre
iteraciones porque tienen distinto número de muestras. La comparación válida
es la de cada escenario por separado, que sí es pareada.

Si la tesis necesita comparar medias con la prueba de Wilcoxon, habría que
volver a ejecutar la campaña de it1 con el instrumento corregido, de modo que
ambas columnas tengan diez muestras. Eso es una tercera ejecución, no un
recálculo.

## Trazabilidad por figura

| Figura | Qué demuestra | Fuente |
|---|---|---|
| `07-metricas/01_kpi-indicadores` | Indicadores de la iteración 2 | `kpi_report.json` |
| `07-metricas/02_kpi-mtfd-por-escenario` | Los 10 escenarios con MTTD y su fuente de detección | `kpi_report.json` |

## Fuentes de datos de la iteración 2

| Fichero | Contenido |
|---|---|
| `07-metricas/kpi_report.json` | Informe completo de indicadores |
| `07-metricas/resultados-escenarios/` | `resultados.json` de S01 a S10 |

Las demás subcarpetas de it2 se completarán en la siguiente fase de captura.

## Lecciones cerradas en esta iteración

L11, L12, L13 y L14 quedan como **CERRADAS** en
[`../lecciones-aprendidas.md`](../lecciones-aprendidas.md), con su causa raíz y
el cambio aplicado. La comparación it1 frente a it2 está en
[`../comparacion-iteraciones.md`](../comparacion-iteraciones.md).

## Reproducibilidad

```bash
bash scripts/reset-ids-offset.sh          # reinicia la ingesta IDS
docker compose exec attacker bash /root/attack-scenarios/run_all.sh
python3 analysis/kpi_calculator.py        # genera el informe
python3 scripts/verificar-figuras.py      # comprueba las figuras contra su .txt
```
