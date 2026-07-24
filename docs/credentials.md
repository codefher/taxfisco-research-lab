# TaxFisco Research Lab — Credenciales

> ⚠️ **ADVERTENCIA**: estas son credenciales de un **LAB DE INVESTIGACIÓN** (no producción). Para entornos productivos, cambiar TODAS via `.env` antes de levantar el stack.

## 🔐 Tabla completa de credenciales

| Servicio | URL | Usuario | Password | Override en .env | Notas |
|----------|-----|---------|----------|------------------|-------|
| **Wazuh Dashboard** | `https://localhost:1443` | `admin` | `ChangeMe_Grafana_2024!` (ver `.env`) | `WAZUH_DASHBOARD_PASSWORD` (NO existe) | Login contra OpenSearch Indexer |
| **Wazuh Manager API** | `https://localhost:55000` (interno) | `wazuh` | `wazuh` (default Wazuh 4.10) | — | Solo via `docker exec` |
| **Wazuh Indexer API** | `http://localhost:19200` | `admin` | `admin` (default Wazuh 4.10) | `WAZUH_INDEXER_PASSWORD` | Backend del dashboard |
| **TheHive** | `http://localhost:9000` | `admin@thehive.local` | `secret` (default TheHive 5.5) | `THEHIVE_USER` / `THEHIVE_PASS` | Sesión cookie-based |
| **MISP** | `https://localhost:8443` | `admin@admin.test` | `admin` | `MISP_USER` / `MISP_PASS` | Usuario creado vía script |
| **Grafana** | `http://localhost:3000` | `admin` | `ChangeMe_Grafana_2024!` | `GRAFANA_PASSWORD` | |
| **Cortex** | `http://localhost:9001` | (sin auth) | — | — | Setup inicial al primer login |
| **Shuffle** | `http://localhost:3001` | (setup inicial) | — | — | Wizard GUI en primer ingreso |
| **Velociraptor** | `https://localhost:8889` | (wizard GUI) | — | — | Crear admin en primer acceso |
| **Decoy API** | `http://localhost:8090/docs` | (sin auth) | — | — | Endpoints públicos |
| **Decoy Portal (público)** | `http://localhost:8890/login/` | (registro libre) | (cualquiera) | — | Login con NIT/email |
| **Decoy Portal (admin Django)** | `http://localhost:8890/admin/login/` | `admin` | `admin` | — | Creado vía `createsuperuser` |
| **Postgres fiscal** | (interno) | `fiscal` | `FiscalDB_2024!` | `POSTGRES_PASSWORD` | Solo via `docker exec` |
| **MISP DB** | (interno) | `root` | `ChangeMe_MISP_Root_2024!` | `MISP_DB_ROOT_PASSWORD` | Solo via `docker exec` |

## 🔑 Credenciales creadas manualmente (no en `.env`)

Estas credenciales se crean **dentro de los contenedores** y NO están en `.env`. Se aplican automáticamente con `scripts/setup-credentials.sh`:

| Recurso | Valor | Cómo se crea |
|---------|-------|--------------|
| **Django superuser** | `admin` / `admin` | `docker exec ... createsuperuser` |
| **MISP user** | `admin@admin.test` / `admin` | INSERT SQL en `misp.users` |
| **MISP API key** | `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (40 A's) | INSERT SQL en `misp.auth_keys` |
| **TheHive indices** | `thehive`, `thehive_global` | PUT en Wazuh Indexer |
| **Wazuh Dashboard config** | apunta a `10.22.0.11:9200` | `docker cp opensearch_dashboards.yml` |

## 🛠️ Setup automático (recomendado)

Después de `make lite-up`, corre **una sola vez**:

```bash
bash scripts/setup-credentials.sh
```

Esto aplica las 6 secciones (Django, migraciones, MISP user+key, Grafana, TheHive indices, Wazuh Dashboard config) en orden, es **idempotente** y tarda ~30 segundos.

### Salida esperada

```
[ok] .env cargado
================================================================
 1/6 - Django superuser (admin/admin)
================================================================
  [ok] Django superuser admin creado
================================================================
 2/6 - Django migrations
================================================================
  [ok] Migraciones aplicadas (o ya estaban)
================================================================
 3/6 - MISP user + API key
================================================================
  [ok] Usuario MISP admin@admin.test insertado
  [ok] API key MISP insertada
================================================================
 4/6 - Grafana password
================================================================
  [ok] Grafana password reseteado
================================================================
 5/6 - TheHive indices (pre-crear)
================================================================
  [ok] Indices TheHive listos
================================================================
 6/6 - Wazuh Dashboard config reaplicar
================================================================
  [ok] Config reaplicado. Reiniciando dashboard...
  [ok] Dashboard reiniciado

Exitosos: 7
Fallidos:  0
```

## 🔄 Setup manual (si el script falla)

Si algún paso falla, puedes hacerlo manualmente:

### Django superuser
```bash
docker exec -i taxfisco-decoy-portal bash -c "
  DJANGO_SUPERUSER_USERNAME=admin \
  DJANGO_SUPERUSER_PASSWORD=admin \
  DJANGO_SUPERUSER_EMAIL=admin@taxfisco.local \
  python3 manage.py createsuperuser --noinput
"
```

### MISP user + API key
```bash
docker exec taxfisco-misp-db mysql -u root -p'ChangeMe_MISP_Root_2024!' misp <<'SQL'
INSERT INTO users (email, password, org_id, server_id, role_id, autoalert, invited_by, nids_sid, termsaccepted, change_pw)
VALUES ('admin@admin.test', '$2a$12$VcCDgh2NDk07JGN0rjGbM.Ad41qVR/YFJcgHp0UGns5JDymv..TOG', 1, 0, 1, 0, 0, 0, 1, 0)
ON DUPLICATE KEY UPDATE password=VALUES(password), role_id=VALUES(role_id);
SET @uid = (SELECT id FROM users WHERE email='admin@admin.test' LIMIT 1);
INSERT INTO auth_keys (uuid, authkey, authkey_start, authkey_end, created, expiration, user_id, comment)
VALUES (UUID(), 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAA', 'AAAA', UNIX_TIMESTAMP(), 0, @uid, 'auto')
ON DUPLICATE KEY UPDATE authkey=VALUES(authkey);
SQL
```

### Grafana reset (si la DB tiene password cacheado)
```bash
docker compose stop grafana
docker run --rm -v taxfisco-research-lab-lite_grafana_data:/data alpine \
  sh -c "rm -f /data/grafana.db /data/grafana.db-journal"
docker compose up -d --force-recreate --no-deps grafana
```
Los dashboards reaplican automáticamente via provisioning.

### TheHive indices
```bash
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
  -X PUT "http://wazuh-indexer-proxy:9200/thehive" \
  -H 'Content-Type: application/json' -d '{}'
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
  -X PUT "http://wazuh-indexer-proxy:9200/thehive_global" \
  -H 'Content-Type: application/json' -d '{}'
```

## 📋 Comandos de testing rápido

```bash
# Login Wazuh Dashboard
curl -sk -X POST "https://localhost:1443/auth/login" \
  -H "Content-Type: application/json" -H "osd-xsrf: osd-fetch" \
  -d '{"username":"admin","password":"ChangeMe_Grafana_2024!"}'

# Login TheHive
curl -sk -c /tmp/cookies.txt -X POST "http://localhost:9000/api/v1/login" \
  -H "Content-Type: application/json" \
  -d '{"user":"admin@thehive.local","password":"secret"}'
curl -sk -b /tmp/cookies.txt "http://localhost:9000/api/case/"

# Login Grafana
curl -sk -X POST "http://localhost:3000/login" \
  -H "Content-Type: application/json" \
  -d '{"user":"admin","password":"ChangeMe_Grafana_2024!"}'

# Login MISP (API key)
curl -sk -H "Authorization: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
  "https://localhost:8443/servers/getVersion.json"

# Login Decoy Portal admin
# (necesario CSRF cookie, ver scripts/verify-services.sh)

# Test Decoy API (sin auth)
curl -s "http://localhost:8090/docs" | head -5
```

## 🔐 Para producción: cambiar TODAS las passwords

Antes de exponer el lab a una red pública:

1. **Cambiar `.env`** con passwords fuertes y únicas:
   ```bash
   nano .env  # editar todos los ChangeMe_*
   ```

2. **Re-crear contenedores** para que tomen los nuevos env vars:
   ```bash
   docker compose up -d --force-recreate
   ```

3. **Re-correr setup-credentials.sh** para regenerar passwords de Django/MISP/Grafana:
   ```bash
   bash scripts/setup-credentials.sh
   ```

4. **Cambiar passwords de los servicios que NO están en .env**:
   - Wazuh Manager API (`wazuh` / `wazuh`): via Wazuh API
   - Wazuh Indexer (`admin` / `admin`): via securityadmin
   - TheHive (`admin@thehive.local` / `secret`): via UI o API
   - Shuffle: via setup inicial

5. **Rotar las API keys**:
   - MISP API key: regenerar via UI de MISP
   - Django secret: regenerar
