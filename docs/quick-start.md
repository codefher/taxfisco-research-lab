# TaxFisco Research Lab - Quick Start

Esta guía permite levantar el laboratorio completo en menos de 30 minutos.

## Prerrequisitos

```bash
# Verificar Docker
docker --version  # >= 26
docker compose version  # >= 2.27

# Verificar RAM (mínimo 16 GB)
free -h
# Debe mostrar: total: 15Gi o 16Gi

# Si tienes menos de 16 GB, considera el script de swap
bash scripts/setup-swap-8gb.sh
```

## Paso 1: Configurar variables de entorno

```bash
cd taxfisco-research-lab
cp .env.example .env
# Editar y cambiar todas las contraseñas
nano .env
```

## Paso 2: Levantar servicios

```bash
# Levantar todo
docker compose up -d

# Ver estado
docker compose ps

# Ver logs
docker compose logs -f wazuh.manager
```

## Paso 3: Esperar a que los servicios arranquen (~3-5 minutos)

```bash
# Verificar salud
docker compose ps
# Todos deben estar "healthy" o "running"
```

## Paso 4: Acceder a los servicios

| Servicio | URL | Credenciales |
|---|---|---|
| Wazuh Dashboard | https://localhost:443 | admin / (ver docker logs) |
| TheHive | http://localhost:9000 | admin@thehive.local / secret |
| Cortex | http://localhost:9001 | (configurar en primer login) |
| MISP | https://localhost:8443 | admin@admin.test / admin |
| Shuffle | http://localhost:3001 | (configurar) |
| Grafana | http://localhost:3000 | admin / (configurado en .env) |
| Velociraptor | https://localhost:8889 | (ver docker logs para password) |
| Decoy API | http://localhost:8080 | (sin auth) |
| Decoy Portal | http://localhost:8888 | (sin auth) |

## Paso 5: Ejecutar escenarios de ataque

```bash
# Acceder al contenedor atacante
docker compose exec attacker bash

# Ejecutar escenario
cd /root/attack-scenarios/S04-sql-injection
bash ejecutar.sh
```

## Solución de problemas

### Los servicios no arrancan

```bash
# Ver logs detallados
docker compose logs wazuh.manager
docker compose logs thehive

# Ver uso de recursos
docker stats
```

### Wazuh Indexer no inicia

```bash
# Esperar más (puede tomar 5+ minutos la primera vez)
docker compose logs -f wazuh.indexer
```

### Decoy API no responde

```bash
# Verificar logs
docker compose logs decoy.api
docker compose exec decoy.api curl -f http://localhost:8000/health
```

### Reiniciar todo

```bash
docker compose down
docker compose up -d
```

## Comandos útiles

```bash
# Ver uso de recursos
docker stats

# Limpiar todo (incluye datos)
docker compose down -v

# Backup de datos
docker compose exec postgres.fiscal pg_dump -U fiscal taxfisco > backup.sql
```
