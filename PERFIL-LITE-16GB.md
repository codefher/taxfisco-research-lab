# PERFIL LITE 16 GB - Guía Operativa

> Documento de operación específico para el perfil lite del laboratorio SIN Research Lab.
> Lee esto antes de levantar el lab si tienes 16 GB de RAM.

## 📊 Configuración aplicada para 16 GB de RAM

Este es el **perfil principal** del laboratorio, optimizado para correr en workstations académicas estándar con 16 GB de RAM. Todos los valores mostrados son la configuración que YA está aplicada en `docker-compose.yml`.

### Configuración técnica (ya aplicada en el lab)

| Componente | Valor configurado (16 GB) | Justificación |
|---|---|---|
| `thehive.es` | **Eliminado**, reusa Wazuh ES | Ahorra 1.5 GB |
| `cassandra.thehive` | **Añadido** (1.2 GB) | TheHive 5.5 lo necesita para Scalligraph/JanusGraph — el plan LITE original lo omitió, lo que dejaba TheHive no-funcional |
| `wazuh-indexer-proxy` | **Añadido** (64 MB, nginx) | Bridge HTTP→HTTPS para que el cliente ES 7.x de JanusGraph pueda hablar con OpenSearch 2.x de Wazuh |
| Wazuh Indexer JVM | `-Xms512m -Xmx768m` | Reducido de 1g |
| MISP workers PHP-FPM | 5/2/1/3 | Reducido de default |
| MISP MySQL | Buffer pool 384M, conexiones reducidas | Tuned para datos sintéticos |
| Shuffle workers | 2 | Reducido de 4 |
| Wazuh Manager | 1.5g | Optimizado para 16 GB |
| Wazuh Dashboard | 768m | Optimizado para 16 GB |
| Velociraptor | 256m | Suficiente para DFIR básico |
| Grafana | 256m | Suficiente para dashboards |
| Cowrie | 384m | Suficiente para SSH/Telnet |
| Dionaea | **Deshabilitado** | Imágenes públicas tienen bug (lib/dionaea/python3.so faltante). SMB/FTP/MSSQL/SIP ya cubiertos por OpenCanary |
| Decoy API | 384m | Suficiente para FastAPI + ATT&CK instrumentation |
| Decoy Portal | 384m | Suficiente para Django |
| Postgres fiscal | 256m | Datos sintéticos pequeños |
| Suricata | 384m | Suficiente para IDS |
| Zeek | 384m | Suficiente para NDR |
| Atacante Kali | 1g (CLI) | Sin GUI, ahorra RAM |
| Swap | **8 GB obligatorio** | Margen para picos |

### Cambios operativos (visibles para el usuario)

1. **Swap de 8 GB obligatorio** (lo crea `make lite-up` automáticamente)
2. **TheHive y Cortex usan el mismo Elasticsearch que Wazuh** (índices dedicados: `thehive`, `cortex`)
3. **Kali es solo CLI** (sin GUI/X11)
4. **Disciplina operativa** requerida (ver tips abajo)

## 🛠️ Preparación del entorno

### Paso 1: Verificar RAM

```bash
free -h
# Debe decir: total: 15Gi o 16Gi
```

### Paso 2: Verificar espacio en disco

```bash
df -h /
# Necesitas al menos 50 GB libres
```

### Paso 3: Instalar Docker

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
docker --version
docker compose version
```

### Paso 4: Clonar/copiar el lab

```bash
cd ~
# Si está en USB
cp -r /media/usb/lab-1-lite ~/sin-lite

# Si está en GitHub
git clone https://github.com/TU_USUARIO/sin-lite.git ~/sin-lite
cd ~/sin-lite
```

### Paso 5: Configurar entorno

```bash
cp .env.example .env
nano .env
# Cambiar TODAS las contraseñas
```

### Paso 6: Levantar el lab

```bash
make lite-up
# Esto:
# 1. Crea 8 GB de swap (si no existe)
# 2. Levanta todos los servicios
# 3. Espera 90 segundos
# 4. Configura el índice TheHive en Wazuh
# 5. Muestra el estado
```

## 📋 Tips operativos para 16 GB

### Hacer

- ✅ **Cerrar el navegador** (Chrome consume 200-500 MB por tab) cuando ejecutes escenarios pesados
- ✅ **Ejecutar escenarios uno por uno** (S01, esperar, S02, etc.)
- ✅ **Monitorear con `make lite-status`** cada 15-30 minutos
- ✅ **Reiniciar servicios** específicos que uses poco: `docker compose restart misp.core`
- ✅ **Revisar logs** con `docker logs --tail 50 <container>` si algo falla
- ✅ **Mantener el swap activo** (8 GB)

### NO hacer

- ❌ **No abrir 3+ dashboards simultáneamente** en el navegador
- ❌ **No ejecutar 2+ escenarios en paralelo**
- ❌ **No modificar mem_limit** de wazuh.manager a menos que sea < 1.5 GB
- ❌ **No eliminar la swap** (`swapoff /swapfile`)
- ❌ **No intentar correr Kali con GUI** (Burp, Wireshark visual)
- ❌ **No correr análisis pesados en Velociraptor** con todos los servicios activos

## 🚨 Qué hacer si ves problemas de RAM

### Síntoma 1: Contenedor reiniciado con OOM (Out of Memory)

```bash
# Ver cuál cayó
docker ps -a | grep -i restart

# Ver el evento
docker inspect <container_name> | grep -A 5 "OOMKilled"

# Solución: reiniciar
docker compose restart <container_name>
```

### Síntoma 2: Todo va muy lento

```bash
# 1. Ver qué consume más RAM
make stats

# 2. Detener servicios que no uses temporalmente
docker compose stop misp.core       # ahorra ~1 GB
docker compose stop velocraptor     # ahorra ~256 MB
docker compose stop grafana         # ahorra ~256 MB

# 3. Liberar caché del sistema
sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

# 4. Reanudar servicios cuando los necesites
docker compose start misp.core
```

### Síntoma 3: Wazuh Indexer no arranca

Síntoma: Wazuh Dashboard muestra "OpenSearch not available"

```bash
# 1. Esperar más (puede tomar 2-3 minutos la primera vez)
docker logs -f sin-wazuh-indexer

# 2. Si no arranca, reiniciar
docker compose restart wazuh.indexer
sleep 60

# 3. Verificar
curl -k https://localhost:9200
```

### Síntoma 4: TheHive no conecta con Wazuh ES

```bash
# Ejecutar el script de configuración
make thehive-setup

# Si sigue fallando, ver logs
docker logs sin-thehive | tail -50
```

## 📊 Comandos de monitoreo

```bash
# Ver uso de RAM en tiempo real (1 línea por contenedor)
make stats

# Ver uso de RAM y CPU específicos
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}"

# Ver swap
free -h

# Ver espacio en disco
df -h /var/lib/docker
```

## 🎯 Orden de servicios por criticidad

Si necesitas liberar RAM en orden de criticidad (menos crítico primero):

| Prioridad | Servicio | RAM (MB) | Se puede detener |
|---|---|---|---|
| 1 (menos crítico) | Velociraptor | 256 | Sí, si no haces DFIR |
| 2 | Grafana | 256 | Sí, si no ves dashboards |
| 3 | MISP modules | 384 | Sí, no afecta core MISP |
| 4 | OpenCanary | 192 | Sí, ya hay otros honeypots |
| 5 | Heralding | 192 | Sí, ya hay Cowrie |
| 6 | MISP core | 1024 | Solo si no usas threat intel |
| 7 | TheHive | 1024 | Solo si no usas case management |
| 8 | Cortex | 384 | Solo si no usas analyzers |
| 9 | Wazuh Dashboard | 768 | Sí, logs siguen ingestándose |
| 10 | Suricata | 384 | NO, pierdes detección de paquetes |
| 11 | Zeek | 384 | NO, pierdes NDR |
| 12 | Wazuh Manager | 1536 | **NO, es el SIEM central** |
| 13 (más crítico) | Wazuh Indexer | 1024 | **NO, sin él no funciona nada** |

## ⚠️ Limitación conocida: TheHive 5.5 Platinum Trial

TheHive 5.5 viene con una **licencia Platinum Enterprise de 15 días de trial** que se
activa al primer arranque del contenedor. Esto produce un banner rojo arriba
de la UI que dice *"Esta instancia utiliza una Platinum Licencia para Trial de
propósito, y expirará en 15 días"`.

**Impacto**:
- ❌ Solo banner UI (no afecta backend)
- ✅ Case management, APIs REST, Cortex integration, observables: **siguen funcionando al 100%**
- ❌ Funcionalidades enterprise (SSO, multi-tenancy avanzado, reporting avanzado) requieren licencia

**Para tu defensa de tesis**:
- 15 días desde el primer `make lite-up` es suficiente para levantar el lab y demostrar
- Si necesitas más tiempo: solicitar licencia académica gratuita a StrangeBee (https://github.com/StrangeBee-Corp/talk-to-us/issues/new) — 1 semana de aprobación
- Alternativa: downgradear a TheHive 4.1.4 (community final), pero requiere cambios al compose

**Workaround para eliminar el banner** (sin licencia válida):
- El banner es cosmético. Se puede ocultar via CSS con userscript pero no es necesario.

Ver `docs/verification-report.md` para más detalles.

```bash
# Detener un servicio temporalmente
docker compose stop velocraptor

# Reiniciarlo cuando lo necesites
docker compose start velocraptor
```

## 🔄 ¿Y si en el futuro amplías a 32 GB? (Opcional)

Si más adelante decides ampliar tu workstation a 32 GB de RAM (upgrade opcional, no necesario para la tesis), el directorio hermano `../lab-1/` contiene la versión "completa" sin las restricciones de RAM. La migración sería:

1. **Copia** todo este directorio como respaldo
2. **Usa el proyecto `lab-1/`** (versión sin restricciones) que está en `../lab-1/`
3. **Copia** tu `.env` y tus datos de los volúmenes
4. Sigue las instrucciones del README de `lab-1`

La migración tomaría ~15 minutos. Tus escenarios, KPIs y datos se preservarían.

**Importante**: Esta migración es **estrictamente opcional** y NO es necesaria para la defensa de la tesis. El perfil LITE de 16 GB mantiene la cobertura funcional y académica completa.

## 🆕 Cambios del plan original (post-instalación)

El plan LITE original de 16 GB tenía **3 problemas** que se descubrieron
al levantar el lab y se corrigieron en una segunda iteración. Documentados
para trazabilidad académica:

### 1. TheHive no arrancaba (olvidaron Cassandra)

El plan original asumía que TheHive compartía ES con Wazuh y no necesitaba
DB propia. **Incorrecto**: TheHive 5.5 usa Scalligraph/JanusGraph que
requiere Cassandra (o HBase) obligatoriamente. Sin él, el thehive
container ciclaba con `ClassNotFoundException: local` cada 30s.

**Fix**: añadir `cassandra.thehive` (cassandra:4.1, mem_limit 1.2g) con
TH_CQL_HOSTNAMES apuntando a él.

### 2. JanusGraph no podía hablar con OpenSearch 2.x

El cliente ES 7.x embebido en JanusGraph falla con OpenSearch 2.x (errores
`Could not instantiate ElasticSearchIndex`, conexiones cerradas). El plan
asumía compatibilidad pero no la hay.

**Fix**: añadir `wazuh-indexer-proxy` (nginx 1.27-alpine, mem_limit 64m)
que expone el Wazuh Indexer HTTPS como HTTP en 9200. JanusGraph habla
HTTP, el proxy traduce a HTTPS upstream.

### 3. dionaea inestable

Todas las imágenes públicas (dinotools, cowrie, amazedostrich) crashean
en el arranque por `lib/dionaea/python3.so` faltante o símbolos
indefinidos. Intentamos construir desde source (Dockerfile en
`docker-images/dionaea/`) pero faltan dependencias (libemu, libcurl-dev)
que añadirían complejidad sin valor académico claro.

**Fix**: deshabilitar dionaea. SMB/FTP/MSSQL/SIP ya están cubiertos por
OpenCanary. La cobertura funcional del lab no cambia.

## 📚 Documentación adicional

- [`README.md`](./README.md) — Visión general del proyecto
- [`docs/decisiones-ram-16gb.md`](./docs/decisiones-ram-16gb.md) — Justificación académica de la adaptación
- [`docs/limitaciones.md`](./docs/limitaciones.md) — Limitaciones reconocidas del lab
- [`docs/arquitectura.md`](./docs/arquitectura.md) — Arquitectura detallada
- [`docs/decision-log.md`](./docs/decision-log.md) — Por qué cada herramienta fue elegida
- [`docs/mapeo-iso27035.md`](./docs/mapeo-iso27035.md) — Mapeo ATT&CK ↔ ISO 27035
- [`docs/mapeo-iso27001.md`](./docs/mapeo-iso27001.md) — Mapeo a controles ISO 27001
- [`../lab-1/README.md`](../lab-1/README.md) — Versión sin restricciones de RAM (opcional, para futura ampliación)

## 💡 Resumen ejecutivo

**¿Funciona el lab con 16 GB?** Sí, con 8 GB de swap y disciplina operativa.

**¿Es defendible académicamente?** Sí, documentado como adaptación técnica que demuestra portabilidad.

**¿Se pierde funcionalidad?** No, los 10 escenarios funcionan idéntico.

**¿Cuándo migrar a 32 GB?** Cuando puedas permitírtelo (~$30-50 USD en RAM).
