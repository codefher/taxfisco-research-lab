#!/usr/bin/env bash
# =============================================================================
# SIN Research Lab - Setup Manual Credentials + Fresh-Install Fixes
# =============================================================================
# Aplica credenciales que se crean MANUALMENTE dentro de los contenedores
# (no estan en .env). Tambien aplica fixes de primer arranque (MISP DB
# schema, Wazuh securityadmin, MISP SSL certs, etc.).
#
# Uso:
#   bash scripts/setup-credentials.sh
#
# Pre-requisito:
#   - make lite-up ya ejecutado (containers corriendo)
#   - .env existe (cp .env.example .env)
#
# Que hace:
#   1. Inicializa Wazuh Indexer security (securityadmin)
#   2. Inicializa MISP DB schema (MYSQL.sql si no existe)
#   3. Genera SSL certs para MISP nginx (si no existen)
#   4. Corrige MISP baseurl (workaround de config)
#   5. Crea superuser Django (admin/admin)
#   6. Corre migraciones Django
#   7. Crea usuario MISP admin@admin.test/admin + API key
#   8. Verifica credenciales Grafana
#   9. Pre-crea indices TheHive en Wazuh Indexer (evita 404)
#  10. Reaplica config Wazuh Dashboard (opensearch_dashboards.yml)
# =============================================================================

set -u  # variable no definida = error. NO set -e: queremos continuar tras fallos.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(dirname "$SCRIPT_DIR")"
cd "$LAB_DIR"

# Cargar .env si existe
if [ -f .env ]; then
    set -a; source .env; set +a
    echo "[ok] .env cargado"
else
    echo "[error] .env no existe. Ejecuta primero: cp .env.example .env"
    exit 1
fi

# Defaults para variables que .env.example define
MISP_DB_ROOT_PASSWORD="${MISP_DB_ROOT_PASSWORD:-ChangeMe_MISP_Root_2024!}"
MISP_DB_PASSWORD="${MISP_DB_PASSWORD:-ChangeMe_MISP_DB_2024!}"
GRAFANA_PASSWORD="${GRAFANA_PASSWORD:-ChangeMe_Grafana_2024!}"
DJANGO_PORT="${DJANGO_PORT:-8890}"

# Passwords generados (mismos que usamos en el lab institucional)
DJANGO_ADMIN_USER="admin"
DJANGO_ADMIN_PASS="admin"
DJANGO_ADMIN_EMAIL="admin@sin.local"

MISP_ADMIN_EMAIL="admin@admin.test"
MISP_ADMIN_PASS="admin"
MISP_API_KEY="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

PASSED=0
FAILED=0

print_ok()   { echo -e "  \033[32m[ok]\033[0m $1";   PASSED=$((PASSED+1)); }
print_fail() { echo -e "  \033[31m[fail]\033[0m $1"; FAILED=$((FAILED+1)); }
print_info() { echo -e "  \033[36m[info]\033[0m $1"; }

# Esperar a que un container este running (max 60s)
# Acepta healthy O running (algunos containers no tienen health check)
wait_for_container() {
    local container=$1
    local max_wait=60
    local waited=0
    while [ $waited -lt $max_wait ]; do
        local health=$(docker inspect --format='{{.State.Health.Status}}' "$container" 2>/dev/null)
        local state=$(docker inspect --format='{{.State.Status}}' "$container" 2>/dev/null)
        # Si tiene health check y esta healthy, OK
        if [ "$health" = "healthy" ]; then
            return 0
        fi
        # Si no tiene health check (null) y esta running, OK
        if [ "$health" = "<no value>" ] || [ "$health" = "null" ] || [ -z "$health" ]; then
            if [ "$state" = "running" ]; then
                # Esperar 5s extra para que termine de inicializar
                sleep 5
                return 0
            fi
        fi
        sleep 3
        waited=$((waited+3))
    done
    return 1
}

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 1/10 - Esperar Wazuh Indexer healthy"
echo "================================================================"
print_info "Esperando que wazuh.indexer responda..."
if wait_for_container sin-wazuh-indexer; then
    print_ok "Wazuh Indexer healthy"
else
    print_fail "Wazuh Indexer no respondio en 60s"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 2/10 - Wazuh Indexer security (securityadmin)"
echo "================================================================"
print_info "Inicializando Wazuh Indexer security (idempotente)..."
docker exec -i sin-wazuh-indexer bash -c "
cd /usr/share/wazuh-indexer/plugins/opensearch-security/tools
JAVA_HOME=/usr/share/wazuh-indexer/jdk PATH=/usr/share/wazuh-indexer/jdk/bin:\$PATH \
./securityadmin.sh -cd /usr/share/wazuh-indexer/opensearch-security/ -icl -nhnv \
  -cacert /etc/wazuh-indexer/certs/root-ca.pem \
  -cert /etc/wazuh-indexer/certs/admin.pem \
  -key /etc/wazuh-indexer/certs/admin-key.pem \
  -h wazuh.indexer
" > /tmp/wazuh_securityadmin.log 2>&1
if grep -q "Done with success" /tmp/wazuh_securityadmin.log 2>/dev/null; then
    print_ok "Wazuh Indexer security inicializado"
else
    if grep -qE "ERROR|failed" /tmp/wazuh_securityadmin.log 2>/dev/null; then
        print_fail "securityadmin fallo (ver /tmp/wazuh_securityadmin.log)"
    else
        print_info "securityadmin (puede ya estar inicializado, OK)"
    fi
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 3/10 - MISP DB schema (init si no existe)"
echo "================================================================"
print_info "Verificando si la DB MISP tiene tablas..."
TABLE_COUNT=$(docker exec sin-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -N -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='misp'" 2>/dev/null | tail -1)
if [ "$TABLE_COUNT" -lt 10 ] 2>/dev/null; then
    print_info "DB MISP vacia. Corriendo MYSQL.sql..."
    docker exec -i sin-misp-core bash -c "MYSQL_PWD='$MISP_DB_PASSWORD' mysql -u misp misp < /var/www/MISP/INSTALL/MYSQL.sql" > /tmp/misp_schema.log 2>&1
    TABLE_COUNT=$(docker exec sin-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -N -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='misp'" 2>/dev/null | tail -1)
    if [ "$TABLE_COUNT" -gt 50 ] 2>/dev/null; then
        print_ok "MISP DB inicializada ($TABLE_COUNT tablas)"
    else
        print_fail "MISP DB schema fallo"
    fi
else
    print_ok "MISP DB ya tiene $TABLE_COUNT tablas (idempotente)"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 4/10 - MISP SSL certs (generar si faltan)"
echo "================================================================"
print_info "Verificando certs SSL en MISP nginx..."
if docker exec sin-misp-core test -f /etc/nginx/certs/cert.pem 2>/dev/null; then
    print_ok "MISP SSL certs ya existen"
else
    print_info "Generando certs autofirmados para MISP..."
    docker exec -u root sin-misp-core bash -c "
openssl req -x509 -newkey rsa:2048 -keyout /etc/nginx/certs/key.pem -out /etc/nginx/certs/cert.pem -days 365 -nodes -subj '/CN=misp.local' 2>&1 | tail -1
chmod 600 /etc/nginx/certs/key.pem
chmod 644 /etc/nginx/certs/cert.pem
" > /tmp/misp_certs.log 2>&1
    if docker exec sin-misp-core test -f /etc/nginx/certs/cert.pem 2>/dev/null; then
        print_ok "MISP SSL certs generados"
    else
        print_fail "MISP SSL certs no se pudieron generar"
    fi
fi

# Reiniciar nginx MISP
print_info "Reiniciando nginx MISP..."
docker exec -u root sin-misp-core bash -c "supervisorctl restart nginx 2>&1 || pkill -HUP nginx 2>&1" > /tmp/misp_nginx_restart.log 2>&1
sleep 5
if timeout 5 curl -sk -o /dev/null -w '%{http_code}' https://localhost:8443 | grep -qE '^(200|302)$'; then
    print_ok "MISP nginx respondiendo"
else
    print_info "MISP nginx aun reiniciando, continuando..."
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 5/10 - MISP baseurl (workaround config)"
echo "================================================================"
print_info "Corrigiendo baseurl de MISP (https: -> https://localhost:8443)..."
CURRENT_BASEURL=$(docker exec sin-misp-core bash -c "grep \"'baseurl'\" /var/www/MISP/app/Config/config.php" 2>/dev/null | head -1)
if echo "$CURRENT_BASEURL" | grep -q "https://localhost:8443"; then
    print_ok "MISP baseurl ya esta correcto"
else
    docker exec -u root sin-misp-core sed -i \
        "s|'baseurl' => 'https:'|'baseurl' => 'https://localhost:8443'|" \
        /var/www/MISP/app/Config/config.php
    print_ok "MISP baseurl corregido"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 6/10 - Django superuser (admin/admin)"
echo "================================================================"
print_info "Contenedor: sin-decoy-portal"
docker exec -i sin-decoy-portal bash -c "
  DJANGO_SUPERUSER_USERNAME=$DJANGO_ADMIN_USER \
  DJANGO_SUPERUSER_PASSWORD=$DJANGO_ADMIN_PASS \
  DJANGO_SUPERUSER_EMAIL=$DJANGO_ADMIN_EMAIL \
  python3 manage.py createsuperuser --noinput 2>&1
" > /tmp/django_createsuperuser.log 2>&1 && \
  print_ok "Django superuser $DJANGO_ADMIN_USER creado" || \
  print_info "Django superuser probablemente ya existe (no es problema)"

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 7/10 - Django migrations"
echo "================================================================"
print_info "Corriendo migrate en sin-decoy-portal..."
docker exec sin-decoy-portal python3 manage.py migrate --noinput > /tmp/django_migrate.log 2>&1
if grep -qE "Applying|No migrations to apply" /tmp/django_migrate.log 2>/dev/null; then
    if grep -q "No migrations to apply" /tmp/django_migrate.log; then
        print_ok "Migraciones ya estaban aplicadas (idempotente)"
    else
        print_ok "Migraciones aplicadas"
    fi
else
    print_fail "Migraciones fallaron (ver /tmp/django_migrate.log)"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 8/10 - MISP user + API key"
echo "================================================================"
print_info "Insertando usuario $MISP_ADMIN_EMAIL en MISP DB..."
docker exec sin-misp-db mysql -t -u root -p"$MISP_DB_ROOT_PASSWORD" misp > /tmp/misp_setup.log 2>&1 <<SQL
INSERT INTO users (email, password, org_id, server_id, role_id, autoalert, invited_by, nids_sid, termsaccepted, change_pw)
VALUES ('$MISP_ADMIN_EMAIL', '\$2a\$12\$VcCDgh2NDk07JGN0rjGbM.Ad41qVR/YFJcgHp0UGns5JDymv..TOG', 1, 0, 1, 0, 0, 0, 1, 0)
ON DUPLICATE KEY UPDATE password=VALUES(password), role_id=VALUES(role_id);

SET @uid = (SELECT id FROM users WHERE email='$MISP_ADMIN_EMAIL' LIMIT 1);

INSERT INTO auth_keys (uuid, authkey, authkey_start, authkey_end, created, expiration, user_id, comment)
VALUES (UUID(), '$MISP_API_KEY', 'AAAA', 'AAAA', UNIX_TIMESTAMP(), 0, @uid, 'auto-setup')
ON DUPLICATE KEY UPDATE authkey=VALUES(authkey);
SQL
if docker exec sin-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -e "SELECT COUNT(*) FROM users WHERE email='$MISP_ADMIN_EMAIL' AND role_id=1" 2>/dev/null | grep -q "^1$"; then
    print_ok "Usuario MISP $MISP_ADMIN_EMAIL insertado/actualizado"
    print_info "API key: $MISP_API_KEY"
    if docker exec sin-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -e "SELECT COUNT(*) FROM auth_keys WHERE user_id=(SELECT id FROM users WHERE email='$MISP_ADMIN_EMAIL')" 2>/dev/null | grep -q "^1$"; then
        print_ok "API key MISP insertada"
    else
        print_info "API key MISP ya existe o fallo al insertar"
    fi
else
    print_fail "Insercion MISP fallo (ver /tmp/misp_setup.log)"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 9/10 - Grafana password"
echo "================================================================"
print_info "Aplicando GRAFANA_PASSWORD=$GRAFANA_PASSWORD..."
docker exec sin-grafana grafana cli admin reset-admin-password "$GRAFANA_PASSWORD" > /tmp/grafana_reset.log 2>&1
if grep -q "successfully" /tmp/grafana_reset.log 2>/dev/null; then
    print_ok "Grafana password reseteado a: $GRAFANA_PASSWORD"
else
    print_fail "Grafana reset fallo (puede que la DB este corrupta; ver /tmp/grafana_reset.log)"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 10/10 - TheHive indices + Wazuh Dashboard config"
echo "================================================================"
print_info "Pre-creando indices 'thehive' y 'thehive_global' en Wazuh Indexer..."
# Usar --network container: para reusar la network del wazuh-indexer-proxy
# (no dependemos del nombre del network, que cambia segun el proyecto)
docker run --rm --network container:sin-wazuh-indexer-proxy curlimages/curl -sk -u admin:admin \
    -X PUT "http://wazuh-indexer-proxy:9200/thehive" \
    -H 'Content-Type: application/json' -d '{}' > /tmp/thehive_idx.log 2>&1
docker run --rm --network container:sin-wazuh-indexer-proxy curlimages/curl -sk -u admin:admin \
    -X PUT "http://wazuh-indexer-proxy:9200/thehive_global" \
    -H 'Content-Type: application/json' -d '{}' > /tmp/thehive_idx.log 2>&1
docker run --rm --network container:sin-wazuh-indexer-proxy curlimages/curl -sk -u admin:admin \
    "http://wazuh-indexer-proxy:9200/_cat/indices/thehive*?v" 2>&1 | grep thehive > /tmp/thehive_idx.log
if [ -s /tmp/thehive_idx.log ]; then
    print_ok "Indices TheHive listos"
else
    print_fail "Indices TheHive no se crearon (Wazuh Indexer no respondio)"
fi

print_info "Reaplicando opensearch_dashboards.yml (workaround runtime)..."
TMPFILE=$(mktemp /tmp/od.XXXXXX.yml)
cat > "$TMPFILE" <<'EOF'
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
docker cp "$TMPFILE" sin-wazuh-dashboard:/usr/share/wazuh-dashboard/config/opensearch_dashboards.yml 2>&1
docker exec -u root sin-wazuh-dashboard bash -c \
  "chown wazuh-dashboard:wazuh-dashboard /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml && chmod 660 /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml" 2>&1
rm -f "$TMPFILE"
if docker exec sin-wazuh-dashboard test -f /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml 2>/dev/null; then
    print_ok "Config reaplicado. Reiniciando dashboard..."
    docker compose restart wazuh.dashboard > /dev/null 2>&1
    sleep 5
    print_ok "Dashboard reiniciado"
else
    print_fail "No se pudo reaplicar config"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " RESUMEN"
echo "================================================================"
echo "  Exitosos: $PASSED"
echo "  Fallidos:  $FAILED"
echo ""
if [ $FAILED -eq 0 ]; then
    echo "OK - todas las credenciales aplicadas."
    echo ""
    echo "Login rapido:"
    echo "  - Wazuh Dashboard: https://localhost:1443  (admin / $GRAFANA_PASSWORD)"
    echo "  - TheHive:          http://localhost:9000   (admin@thehive.local / secret)"
    echo "  - Grafana:          http://localhost:3000   (admin / $GRAFANA_PASSWORD)"
    echo "  - MISP:             https://localhost:8443  ($MISP_ADMIN_EMAIL / $MISP_ADMIN_PASS)"
    echo "  - Decoy Portal:     http://localhost:$DJANGO_PORT/admin/login/  (admin / admin)"
    echo "  - Decoy API:        http://localhost:8090/docs"
    echo ""
    echo "Mas detalles en docs/credentials.md"
    exit 0
else
    echo "FAIL - revisa los logs en /tmp/*.log"
    exit 1
fi
