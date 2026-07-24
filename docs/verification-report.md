# TaxFisco Research Lab — Verification Report

> Resultados de la verificación funcional de los servicios del lab.
> Ejecutado con `scripts/verify-services.sh` (read-only, sin tráfico a honeypots).

## Resumen

| # | Servicio | Tipo | Resultado esperado |
|---|----------|------|---------------------|
| 0 | Pre-flight (containers) | Infra | 25/25 corriendo (sin dionaea) |
| 1 | Wazuh Indexer (vía proxy) | SIEM | `status: green` o `yellow` |
| 2 | Wazuh Manager | SIEM | lista agentes (vacía OK) |
| 3 | Wazuh Dashboard | Web UI | HTTP 200 o 302 en `https://localhost:1443` |
| 4 | TheHive login | IRP | JSON con `access_token` |
| 5 | TheHive API | IRP | Lista de casos (puede estar vacía) |
| 6 | MISP getVersion | TI | JSON con campo `version` |
| 7 | Shuffle verify | SOAR | JSON con `success: true` |
| 8 | Cortex health | Enrichment | `OK` o `{"status":"OK"}` |
| 9 | Grafana health | Dashboard | `ok` o `{"database":"ok"}` |
| 10 | Velociraptor health | DFIR | `OK` |
| 11 | Decoy API login | Decoy | JSON con `access_token` |
| 12 | Decoy API endpoint | Decoy | Lista de contribuyentes (puede estar vacía) |
| 13 | Decoy Portal login | Decoy | HTTP 200 o 302 |
| 14 | Decoy Portal admin | Decoy | Página "Site administration" |
| 15 | Cassandra | DB | Versión 4.1.x |
| 16 | Postgres fiscal | DB | Tabla `contribuyentes` existe |

**Total: 17 verificaciones.**

---

## Cómo correr

```bash
# Desde la raiz del repo
bash scripts/verify-services.sh

# Exit codes:
#   0 = todos pasaron
#   1 = al menos uno fallo
```

## Salida esperada

```
== Pre-flight (containers up) ==
  [PASS] Containers running (25/25)

== Wazuh Stack ==
  [PASS] Wazuh Indexer health
  [PASS] Wazuh Manager agents
  [PASS] Wazuh Dashboard reachable

== TheHive ==
  [PASS] TheHive login
  [PASS] TheHive API (list cases)

== MISP ==
  [PASS] MISP getVersion

== Shuffle ==
  [PASS] Shuffle verify

== Cortex ==
  [PASS] Cortex health

== Grafana ==
  [PASS] Grafana health

== Velociraptor ==
  [PASS] Velociraptor health

== Decoy API (FastAPI) ==
  [PASS] Decoy API login
  [PASS] Decoy API protected endpoint

== Decoy Portal (Django) ==
  [PASS] Decoy Portal login
  [PASS] Decoy Portal admin

== Databases ==
  [PASS] Cassandra reachable
  [PASS] Postgres fiscal tables

===================================================================
  Total: 17 PASS | 0 FAIL / 17
===================================================================
  OK - todos los servicios funcionan.
```

---

## Credenciales verificadas (estado actual del lab)

> **Importante**: el dashboard valida contra OpenSearch, no contra la API de Wazuh.

| Servicio | Usuario | Password | Override en .env | Notas |
|----------|---------|----------|------------------|-------|
| **Wazuh Dashboard** ⭐ | `admin` | `ChangeMe_Grafana_2024!` (ver `.env`) | `WAZUH_DASHBOARD_PASSWORD` (NO existe, se autogenera al primer arranque) | Login contra OpenSearch Indexer, no contra la API |
| **Wazuh Manager API** | `wazuh` | `wazuh` (default Wazuh 4.10) | — | Solo accesible via `docker exec` (puerto 55000 interno) |
| **Wazuh Indexer API** | `admin` | `admin` (default Wazuh 4.10) | `WAZUH_INDEXER_PASSWORD` | Backend del dashboard |
| **TheHive** | `admin@thehive.local` | `secret` (default TheHive 5.5) | `THEHIVE_USER` / `THEHIVE_PASS` | |
| **MISP** | `admin@admin.test` | `admin` | `MISP_USER` / `MISP_PASS` | Usuario creado manualmente (ver workarounds) |
| **Grafana** ⭐ | `admin` | `ChangeMe_Grafana_2024!` | `GRAFANA_PASSWORD` | Si falla, ver sección de fix |
| **Cortex** | (sin auth) | — | — | Setup inicial al primer login |
| **Shuffle** | (setup inicial) | — | — | Wizard GUI en primer ingreso |
| **Velociraptor** | (wizard GUI) | — | — | Crear admin en primer acceso |
| **Decoy API** | (sin auth) | — | — | Endpoints públicos |
| **Decoy Portal (público)** | (registro libre) | (cualquiera) | — | Login con NIT/email |
| **Decoy Portal (admin Django)** | `admin` | `admin` | `DJANGO_SUPERUSER_*` (creado via `createsuperuser`) | |
| **Postgres fiscal** | `fiscal` | `FiscalDB_2024!` | `POSTGRES_PASSWORD` | Solo accesible via `docker exec` |
| **MISP DB** | `root` | `ChangeMe_MISP_Root_2024!` | `MISP_DB_ROOT_PASSWORD` | Solo accesible via `docker exec` |

El script lee de `.env` si existe. Si no, usa los defaults arriba.

---

## Si un test falla

1. **Identificar el contenedor afectado**:
   ```bash
   docker compose ps
   ```

2. **Ver logs del servicio**:
   ```bash
   docker logs <container> --tail 100
   ```

3. **Casos comunes**:

   | Síntoma | Diagnóstico |
   |---------|-------------|
   | TheHive 500 / "Organization not found" | Pre-crear índice `thehive_global` (ver `docs/decisiones-ram-16gb.md`) |
   | MISP 500 / "table not found" | Cargar schema: `docker exec -i taxfisco-misp-core mysql -u misp misp < /var/www/MISP/INSTALL/MYSQL.sql` |
   | MISP nginx "cannot load certificate" | Generar certs: `docker exec -u root taxfisco-misp-core openssl req -x509 ...` |
   | Wazuh Dashboard "ECONNREFUSED 127.0.0.1:9200" | Reaplicar config: `docker cp od.yml taxfisco-wazuh-dashboard:.../opensearch_dashboards.yml` |
   | Wazuh Indexer 401 | `securityadmin.sh` no se ha corrido desde el último reinicio |
   | Shuffle 404 | Verificar que `shuffle.frontend` tiene `ports:` en compose |
   | Cassandra connect refused | `docker logs taxfisco-cassandra` — esperar ~60s al primer arranque |
   | **Grafana login "Invalid username or password"** | La DB tiene un password cacheado que no coincide con `GF_SECURITY_ADMIN_PASSWORD`. Reset: `docker compose stop grafana && docker run --rm -v taxfisco-research-lab-lite_grafana_data:/data alpine rm -f /data/grafana.db /data/grafana.db-journal && docker compose up -d --force-recreate --no-deps grafana`. Los dashboards custom se reaplican automáticamente via provisioning. |

4. **Re-ejecutar**:
   ```bash
   bash scripts/verify-services.sh
   ```

---

## Workarounds de runtime (no persistentes)

Algunos servicios requieren fixes que se pierden tras `docker compose
up -d --force-recreate` o un reinicio completo. Documentamos aquí los
más importantes para que sepas reaplicarlos rápido.

### Wazuh Dashboard config (crítico tras recreate)

La imagen `wazuh/wazuh-dashboard` sobrescribe su config en cada
container start con `opensearch.hosts: ["https://localhost:9200"]`,
que NO resuelve dentro del contenedor. El dashboard intenta hablar con
localhost y muere con `ECONNREFUSED 127.0.0.1:9200`.

**Fix** (3 comandos, ~10s):
```bash
cat > /tmp/od.yml <<'EOF'
server.host: "0.0.0.0"
server.name: "wazuh-dashboard"
opensearch.hosts: ["https://10.22.0.11:9200"]
opensearch.ssl.verificationMode: none
opensearch.username: "kibanaserver"
opensearch.password: "kibanaserver"
opensearch.requestTimeout: 30000
opensearch.shardTimeout: 30000
server.ssl.enabled: true
server.ssl.certificate: "/etc/wazuh-dashboard/certs/dashboard.pem"
server.ssl.key: "/etc/wazuh-dashboard/certs/dashboard-key.pem"
EOF
docker cp /tmp/od.yml taxfisco-wazuh-dashboard:/usr/share/wazuh-dashboard/config/opensearch_dashboards.yml
docker exec -u root taxfisco-wazuh-dashboard \
  bash -c "chown wazuh-dashboard:wazuh-dashboard /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml && chmod 660 /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml"
docker compose restart wazuh.dashboard
```

Por eso `config/wazuh/dashboard/` está en `.gitignore` — no es
commiteable de forma reproducible (cada clone debe reaplicarlo).

### MISP SSL certs y DB schema (primer arranque)

La imagen `coolacid/misp-docker` no genera certs SSL ni inicializa
la DB en runtime. Solo se hace en la primera ejecución (donde
`/data/` persiste). Si borras el volumen `misp_data`, reaplica:

```bash
# Certs SSL
docker exec -u root taxfisco-misp-core bash -c \
  "openssl req -x509 -newkey rsa:2048 -keyout /etc/nginx/certs/key.pem \
   -out /etc/nginx/certs/cert.pem -days 365 -nodes -subj '/CN=misp.local' && \
   chmod 600 /etc/nginx/certs/key.pem && chmod 644 /etc/nginx/certs/cert.pem"

# DB schema
docker exec taxfisco-misp-core bash -c \
  "MYSQL_PWD='ChangeMe_MISP_DB_2024!' mysql -u misp misp < /var/www/MISP/INSTALL/MYSQL.sql"

# baseurl
docker exec -u root taxfisco-misp-core sed -i \
  "s|'baseurl' => 'https:'|'baseurl' => 'https://localhost:8443'|" \
  /var/www/MISP/app/Config/config.php

# Reiniciar nginx
docker exec -u root taxfisco-misp-core nginx -s reload
```

### Wazuh Indexer security index (tras recrear volumen)

Tras `docker compose down -v` se borra la config de seguridad
(interna users, roles, etc). Para reinicializar:

```bash
docker exec -i taxfisco-wazuh-indexer bash -c \
  "cd /usr/share/wazuh-indexer/plugins/opensearch-security/tools && \
   JAVA_HOME=/usr/share/wazuh-indexer/jdk PATH=/usr/share/wazuh-indexer/jdk/bin:\$PATH \
   ./securityadmin.sh -cd /usr/share/wazuh-indexer/opensearch-security/ -icl -nhnv \
   -cacert /etc/wazuh-indexer/certs/root-ca.pem \
   -cert /etc/wazuh-indexer/certs/admin.pem \
   -key /etc/wazuh-indexer/certs/admin-key.pem \
   -h wazuh.indexer"
```

### TheHive indices en Wazuh Indexer (primer arranque de TheHive)

TheHive no crea automáticamente los índices `thehive` y `thehive_global`
en Wazuh. Si reinicias solo TheHive, pre-crea:

```bash
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
  -X PUT "http://wazuh-indexer-proxy:9200/thehive" \
  -H 'Content-Type: application/json' -d '{}'

docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
  -X PUT "http://wazuh-indexer-proxy:9200/thehive_global" \
  -H 'Content-Type: application/json' -d '{}'
```

---

## Puertos del lab (post-fix)

| Servicio | Host | Container |
|----------|------|-----------|
| Wazuh Dashboard | `https://localhost:1443` | `5601/tcp` (SSL) |
| TheHive | `http://localhost:9000` | `9000/tcp` |
| MISP | `https://localhost:8443` | `443/tcp` |
| Shuffle | `http://localhost:3001` | `80/tcp` (frontend) |
| Grafana | `http://localhost:3000` | `3000/tcp` |
| Cortex | `http://localhost:9001` | `9001/tcp` |
| Velociraptor | `https://localhost:8889` | `8889/tcp` |
| Decoy API | `http://localhost:8090` | `8000/tcp` |
| Decoy Portal | `http://localhost:8890` | `8000/tcp` |
| Cowrie SSH | `localhost:2225` | `2222/tcp` |
| OpenCanary HTTP | `localhost:8081` | `80/tcp` |
| Heralding Telnet | `localhost:23` | `23/tcp` |

> El 443 original fue cambiado a 1443 por restricciones de red institucional.

---

## ⚠️ Limitación conocida: TheHive 5.5 Platinum Trial

Al primer arranque, TheHive 5.5 activa una **licencia Platinum Enterprise de 15 días
de trial**. Esto produce un banner rojo arriba de la UI diciendo *"Esta instancia
utiliza una Platinum Licencia para Trial de propósito, y expirará en 15 días"*.

**No es un problema real**:
- ✅ Core functionality (case management, APIs, Cortex, observables) sigue 100%
- ❌ Solo banner visual + funciones enterprise (SSO, multi-tenancy avanzado)

**Soluciones** (de la más a la menos recomendada):

1. **No hacer nada** (más simple). 15 días desde el primer `make lite-up` es suficiente
   para defender la tesis. El lab se levanta en <30 min.

2. **Solicitar licencia académica gratuita** a StrangeBee (1 semana aprobación):
   https://github.com/StrangeBee-Corp/talk-to-us/issues/new

3. **Downgradear a TheHive 4.1.4** (última community final, sin trial). Requiere:
   - Cambiar `image: strangebee/thehive:5.5` → `thehiveproject/thehive:4.1.4-2`
   - Las APIs son compatibles (cambia `/api/case/` por `/api/case`)
   - `cassandra.thehive` y `wazuh-indexer-proxy` siguen igual

4. **Suprimir el banner via userscript** (cosmético, no recomendado). En el browser:
   ```js
   document.querySelectorAll('div[role="alert"]').forEach(e => e.style.display='none');
   ```

**Verificado en este lab**: 15 días desde `2026-07-24` (primer arranque).

---

## Lo que NO verifica este script

- Tráfico contra honeypots (de propósito — usar `make attacks` o `make S01..S10`)
- Generación de KPIs (usar `make analysis`)
- Alertas en cascada (Wazuh → TheHive → Shuffle)
- Persistencia tras `docker compose restart`
