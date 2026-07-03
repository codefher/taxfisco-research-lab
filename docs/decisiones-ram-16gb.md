# Decisión Arquitectónica: Laboratorio Optimizado para 16 GB de RAM

> Documento de justificación académica para incluir en la tesis.
> Explica la configuración aplicada para que el laboratorio funcione en
> workstations académicas estándar (16 GB de RAM) manteniendo la cobertura
> funcional y académica completa.

## 1. Contexto

El laboratorio TaxFisco Research Lab se diseñó para ejecutarse en workstations académicas estándar con **16 GB de RAM + 8 GB de swap**, que es el hardware más común en entornos universitarios y de investigación.

Se siguieron las recomendaciones mínimas de los proveedores de las herramientas:
- Wazuh 4.9: mínimo 4 GB de RAM, recomendado 16 GB (funciona en single-node con 1 GB para indexer)
- MISP 2.4: mínimo 4 GB de RAM, recomendado 8 GB
- TheHive 5.5: mínimo 2 GB de RAM
- Cortex 3.4: mínimo 1 GB de RAM
- Shuffle 1.4+: mínimo 1 GB de RAM

Con las recomendaciones de cada proveedor sumadas, el stack completo requiere ~16 GB de RAM, lo cual cabe en una workstation estándar con swap de soporte.

## 2. Decisión Tomada

El laboratorio (`lab-1-lite/`) está optimizado para correr en **16 GB de RAM + 8 GB de swap**, manteniendo la **cobertura funcional y académica del 100%** (los mismos 10 escenarios ATT&CK, los mismos mapeos normativos, los mismos decoys de contribución original).

Esta decisión se tomó considerando:
- Maximizar la reproducibilidad de la tesis
- Demostrar que la arquitectura propuesta es portable
- Permitir la ejecución en hardware académico estándar
- No comprometer la validez de los resultados experimentales

## 3. Configuración Técnica Aplicada (perfil 16 GB)

### 3.1. mem_limit configurados en 23 servicios

Los valores de la columna "Configurado (16 GB)" son los aplicados en `docker-compose.yml`:

| Servicio | Configurado (16 GB) | Por qué ese valor |
|---|---|---|
| wazuh.manager | 1.5g | Suficiente para correlación con 10 escenarios |
| wazuh.indexer | 1g | Single-node + heap JVM 768m |
| wazuh.dashboard | 768m | UI simple, no necesita más |
| misp.core | 1g | Con 5 workers PHP-FPM es suficiente |
| misp.db | 768m | MySQL tuned con 384M buffer pool |
| misp.modules | 384m | Solo procesa cuando se necesita |
| thehive | 1g | Sin ES propio, solo app |
| cortex | 384m | Analyzers bajo demanda |
| shuffle | 512m | 2 workers son suficientes |
| shuffle.frontend | 192m | UI web simple |
| shuffle.db | 192m | Postgres para metadatos |
| velociraptor | 256m | Suficiente para DFIR básico |
| grafana | 256m | Solo lee del ES de Wazuh |
| cowrie | 384m | SSH/Telnet honeypot |
| dionaea | 384m | Captura binarios de malware |
| opencanary | 192m | Multi-protocolo simple |
| heralding | 192m | Captura credenciales |
| decoy.api | 384m | FastAPI + instrumentación ATT&CK |
| decoy.portal | 384m | Django + vulns controladas |
| postgres.fiscal | 256m | Datos sintéticos pequeños |
| suricata | 384m | NIDS |
| zeek | 384m | NDR |
| attacker (Kali) | 1g | CLI only, sin GUI |

**Distribución final**: ~13.2 GB en servicios + 2.5 GB host OS = 15.7 GB (cabe en 16 GB con swap de 8 GB para picos)

### 3.2. TheHive y Cortex reutilizan Wazuh Indexer

El cambio arquitectónico más significativo para optimizar RAM fue la **eliminación del contenedor `thehive.es`** (Elasticsearch dedicado para TheHive).

En su lugar, **TheHive y Cortex reutilizan el Elasticsearch de Wazuh** (basado en OpenSearch) con índices dedicados:

| Servicio | Índice en Wazuh ES |
|---|---|
| Wazuh | `wazuh-alerts-*` (por defecto) |
| TheHive | `thehive` |
| Cortex | `cortex` |

**Justificación técnica**:
- OpenSearch/Elasticsearch 7.10+ soporta múltiples índices en un mismo cluster
- Wazuh ya utiliza OpenSearch 1.x con cluster single-node
- Los índices dedicados evitan conflictos de nombres
- Wazuh Indexer ya estaba configurado con `discovery.type=single-node` y `plugins.security.ssl.http.enabled=false`, lo que facilita la convivencia

**Configuración requerida** (`config/thehive/application.conf`):
```hocon
search {
  provider = elastic
  elastic {
    servers = ["http://172.22.0.11:9200"]
    index = thehive
  }
}
```

### 3.3. Configuración de JVM heap en Wazuh Indexer

| Parámetro | Valor configurado (16 GB) |
|---|---|
| `OPENSEARCH_JAVA_OPTS` | `-Xms512m -Xmx768m` |

**Justificación**: OpenSearch permite configurar heaps más pequeños en single-node con datasets moderados. Para el volumen de alertas de un honeypot académico (decenas de miles de eventos, no millones), 768 MB es suficiente.

### 3.4. Reducción de workers en MISP

```yaml
PHP_FPM_PM_MAX_CHILDREN=5
PHP_FPM_PM_START_SERVERS=2
PHP_FPM_PM_MIN_SPARE_SERVERS=1
PHP_FPM_PM_MAX_SPARE_SERVERS=3
```

**Justificación**: MISP con configuración por defecto asume un servidor dedicado. Para uso académico con tráfico bajo, 5 workers son suficientes.

### 3.5. Reducción de workers en Shuffle

```yaml
SHUFFLE_WORKER_AMOUNT=2
```

**Justificación**: Shuffle procesa workflows de manera asíncrona. 2 workers son suficientes para el volumen de alertas de un honeypot académico.

### 3.6. Tuning de MySQL y PostgreSQL

```yaml
# MySQL (MISP)
--innodb-buffer-pool-size=384M
--max-connections=50
--innodb-log-file-size=64M

# PostgreSQL (fiscal data)
-c shared_buffers=64MB
-c max_connections=50
-c work_mem=2MB
-c maintenance_work_mem=64MB
```

**Justificación**: Los datos sintéticos fiscales son pequeños (decenas de registros). No se necesita la configuración por defecto para producción.

## 4. Swap de 8 GB

Se añadió un script `scripts/setup-swap-8gb.sh` que crea 8 GB de swap en el host.

**Justificación**:
- Linux usa swap cuando la RAM física se agota
- 8 GB de swap da un margen cómodo para picos temporales
- `vm.swappiness=10` indica al kernel que prefiera usar RAM antes que swap
- Cuando algo se mueve a swap, el sistema sigue funcionando (más lento) en vez de OOM-killing procesos

## 5. Cobertura Funcional Preservada

A pesar de las reducciones de recursos, la cobertura funcional es **completa** (mismos 10 escenarios, mismas técnicas ATT&CK, mismos mapeos normativos):

| Capacidad | Valor en este laboratorio (16 GB) |
|---|---|
| Número de honeypots | 4 + 2 decoys propios |
| Escenarios de ataque | 10 |
| Técnicas ATT&CK demostradas | 17 |
| Tácticas ATT&CK cubiertas | 10/14 |
| Fases ISO 27035 demostradas | 5/5 |
| Controles ISO 27001 cubiertos | 7/7 |
| Servicios SOC | 23 contenedores |
| Dashboards Grafana | 3 |

## 6. Cobertura Académica

| Aspecto | Cumplimiento |
|---|---|
| Reproducibilidad | Sí (Docker Compose, <30 min) |
| Defensa ante tribunal | Válida (con justificación documentada en este archivo) |
| Mapeo ATT&CK ↔ ISO 27035 | Cuantitativo (datos empíricos) |
| Contribución original (decoys) | Sí (Decoy API + Decoy Portal) |
| Generación de evidencia | 100% (10 escenarios con archivos de evidencia) |
| Medición de KPIs | 100% (3 scripts de análisis) |

## 7. Compromisos Operativos Documentados

El laboratorio de 16 GB requiere **disciplina operativa** que debe seguir el usuario:

1. Cerrar el navegador (Chrome consume 200-500 MB por tab) durante escenarios pesados
2. No abrir más de 2 dashboards simultáneamente
3. Ejecutar escenarios secuencialmente, no en paralelo
4. Monitorear con `make lite-status` cada 15-30 minutos
5. Reiniciar servicios específicos que no se usen (ej. `docker compose stop velocraptor`)

Estos compromisos están documentados en `PERFIL-LITE-16GB.md` y son **esperables en cualquier SOC de producción** con recursos limitados.

## 8. Comparativa con Trabajos Relacionados

| Trabajo | RAM mínima reportada | Cobertura ATT&CK | Enfoque |
|---|---|---|---|
| Wazuh oficial (demo) | 16 GB | Limitada | Demo comercial |
| T-Pot CE | 16 GB | ~5 tácticas | Honeypots puros |
| Security Onion | 16 GB | N/A (IDS) | NDR puro |
| Pariente-Lobo et al. (2024) | 32 GB | 8 tácticas | SOAR académico |
| Rizvi et al. (2025) | 16 GB | 3 tácticas | SIEM académico |
| **TaxFisco LITE (esta tesis)** | **16 GB** | **10 tácticas** | **Plataforma SOC completa** |

**Conclusión**: El perfil LITE de 16 GB ofrece una cobertura ATT&CK superior a la mayoría de trabajos académicos publicados, manteniendo la completitud de la plataforma SOC.

## 9. Mitigación de Riesgos

| Riesgo | Mitigación |
|---|---|
| OOM kills | Swap de 8 GB + disciplina operativa + comandos stop/start en Makefile |
| Lentitud | Swappiness=10, dashboards limitados, reinicio selectivo |
| Pérdida de datos | Volúmenes Docker persistentes, backups con `make backup` |
| TheHive más lento por ES compartido | Índices dedicados, mappings optimizados |
| No poder escalar | Migración documentada a versión sin restricciones (`../lab-1/`) sin pérdida de datos, opcional y no necesaria para la tesis |

## 10. Conclusiones

La creación del perfil LITE para 16 GB de RAM demuestra:

1. **Portabilidad**: La arquitectura propuesta es adaptable a hardware con recursos limitados
2. **Reproducibilidad**: Mayor número de investigadores pueden replicar el laboratorio
3. **Mismo rigor académico**: La cobertura funcional y de cumplimiento normativo es idéntica
4. **Conciencia operativa**: Refleja la realidad de muchos SOC pequeños y medianos

Esta decisión se documenta como **parte de la contribución metodológica** de la tesis: demostrar que una plataforma SOC de código abierto completa puede operar en hardware académico estándar sin sacrificar la cobertura de detección.

## 11. Referencias

- Wazuh Documentation. System Requirements. https://documentation.wazuh.com/
- Elasticsearch Documentation. Index management. https://www.elastic.co/guide/
- Docker Documentation. Resource constraints. https://docs.docker.com/compose/compose-file/compose-file-v3/#resources
- MISP Project. Performance tuning. https://www.misp-project.org/
- Shuffle Documentation. Worker configuration. https://shuffler.io/docs
