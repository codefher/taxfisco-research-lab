#!/usr/bin/env bash
# =============================================================================
# TaxFisco Research Lab - Setup Manual Credentials
# =============================================================================
# Aplica las credenciales que se crean MANUALMENTE dentro de los contenedores
# (no estan en .env). Idempotente: se puede correr multiples veces sin fallar.
#
# Uso:
#   bash scripts/setup-credentials.sh
#
# Pre-requisito:
#   - make lite-up ya ejecutado (containers corriendo)
#   - .env existe (cp .env.example .env)
#
# Que hace:
#   1. Crea superuser Django (admin/admin)
#   2. Corre migraciones Django
#   3. Crea usuario MISP admin@admin.test/admin + API key
#   4. Verifica credenciales Grafana
#   5. Pre-crea indices TheHive en Wazuh Indexer (evita 404)
#   6. Reaplica config Wazuh Dashboard (opensearch_dashboards.yml)
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
GRAFANA_PASSWORD="${GRAFANA_PASSWORD:-ChangeMe_Grafana_2024!}"
DJANGO_PORT="${DJANGO_PORT:-8890}"

# Passwords generados (mismos que usamos en el lab institucional)
DJANGO_ADMIN_USER="admin"
DJANGO_ADMIN_PASS="admin"
DJANGO_ADMIN_EMAIL="admin@taxfisco.local"

MISP_ADMIN_EMAIL="admin@admin.test"
MISP_ADMIN_PASS="admin"
MISP_API_KEY="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

PASSED=0
FAILED=0

print_ok()   { echo -e "  \033[32m[ok]\033[0m $1";   PASSED=$((PASSED+1)); }
print_fail() { echo -e "  \033[31m[fail]\033[0m $1"; FAILED=$((FAILED+1)); }
print_info() { echo -e "  \033[36m[info]\033[0m $1"; }

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 1/6 - Django superuser (admin/admin)"
echo "================================================================"
print_info "Contenedor: taxfisco-decoy-portal"
docker exec -i taxfisco-decoy-portal bash -c "
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
echo " 2/6 - Django migrations"
echo "================================================================"
print_info "Corriendo migrate en taxfisco-decoy-portal..."
docker exec taxfisco-decoy-portal python3 manage.py migrate --noinput > /tmp/django_migrate.log 2>&1
# OK si: "Applying" (se aplicaron migraciones) o "No migrations to apply" (ya estaban)
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
echo " 3/6 - MISP user + API key"
echo "================================================================"
print_info "Insertando usuario $MISP_ADMIN_EMAIL en MISP DB..."
# INSERT IGNORE no funciona en MySQL 8.0; usamos ON DUPLICATE KEY UPDATE
docker exec taxfisco-misp-db mysql -t -u root -p"$MISP_DB_ROOT_PASSWORD" misp > /tmp/misp_setup.log 2>&1 <<SQL
INSERT INTO users (email, password, org_id, server_id, role_id, autoalert, invited_by, nids_sid, termsaccepted, change_pw)
VALUES ('$MISP_ADMIN_EMAIL', '\$2a\$12\$VcCDgh2NDk07JGN0rjGbM.Ad41qVR/YFJcgHp0UGns5JDymv..TOG', 1, 0, 1, 0, 0, 0, 1, 0)
ON DUPLICATE KEY UPDATE password=VALUES(password), role_id=VALUES(role_id);

SET @uid = (SELECT id FROM users WHERE email='$MISP_ADMIN_EMAIL' LIMIT 1);

INSERT INTO auth_keys (uuid, authkey, authkey_start, authkey_end, created, expiration, user_id, comment)
VALUES (UUID(), '$MISP_API_KEY', 'AAAA', 'AAAA', UNIX_TIMESTAMP(), 0, @uid, 'auto-setup')
ON DUPLICATE KEY UPDATE authkey=VALUES(authkey);

SELECT id, email, role_id FROM users WHERE email='$MISP_ADMIN_EMAIL';
SELECT COUNT(*) AS api_keys_for_user FROM auth_keys WHERE user_id=(SELECT id FROM users WHERE email='$MISP_ADMIN_EMAIL');
SQL
# Verificar via query separada (mas robusto)
if docker exec taxfisco-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -e "SELECT COUNT(*) FROM users WHERE email='$MISP_ADMIN_EMAIL' AND role_id=1" 2>/dev/null | grep -q "^1$"; then
    print_ok "Usuario MISP $MISP_ADMIN_EMAIL insertado/actualizado"
    print_info "API key: $MISP_API_KEY"
    # Verificar API key
    if docker exec taxfisco-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp -e "SELECT COUNT(*) FROM auth_keys WHERE user_id=(SELECT id FROM users WHERE email='$MISP_ADMIN_EMAIL')" 2>/dev/null | grep -q "^1$"; then
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
echo " 4/6 - Grafana password"
echo "================================================================"
print_info "Aplicando GRAFANA_PASSWORD=$GRAFANA_PASSWORD..."
docker exec taxfisco-grafana grafana cli admin reset-admin-password "$GRAFANA_PASSWORD" > /tmp/grafana_reset.log 2>&1
if grep -qE "successfully|Admin password changed" /tmp/grafana_reset.log 2>&1; then
    print_ok "Grafana password reseteado a: $GRAFANA_PASSWORD"
else
    # A veces solo imprime en stderr
    if docker exec taxfisco-grafana grafana cli admin reset-admin-password "$GRAFANA_PASSWORD" 2>&1 | grep -q "successfully"; then
        print_ok "Grafana password reseteado"
    else
        print_fail "Grafana reset fallo (puede que la DB este corrupta; ver /tmp/grafana_reset.log)"
    fi
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 5/6 - TheHive indices (pre-crear)"
echo "================================================================"
print_info "Pre-creando indices 'thehive' y 'thehive_global' en Wazuh Indexer..."
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
    -X PUT "http://wazuh-indexer-proxy:9200/thehive" \
    -H 'Content-Type: application/json' -d '{}' > /tmp/thehive_idx.log 2>&1
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
    -X PUT "http://wazuh-indexer-proxy:9200/thehive_global" \
    -H 'Content-Type: application/json' -d '{}' > /tmp/thehive_idx.log 2>&1
docker run --rm --network taxfisco-soc curlimages/curl -sk -u admin:admin \
    "http://wazuh-indexer-proxy:9200/_cat/indices/thehive*?v" 2>&1 | grep thehive > /tmp/thehive_idx.log
if [ -s /tmp/thehive_idx.log ]; then
    print_ok "Indices TheHive listos"
else
    print_fail "Indices TheHive no se crearon (Wazuh Indexer no respondio)"
fi

# -----------------------------------------------------------------------------
echo ""
echo "================================================================"
echo " 6/6 - Wazuh Dashboard config reaplicar"
echo "================================================================"
print_info "Reaplicando opensearch_dashboards.yml (workaround runtime)..."
# Solo reaplicar si el archivo existe (no commit en el repo porque es efimero)
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
docker cp "$TMPFILE" taxfisco-wazuh-dashboard:/usr/share/wazuh-dashboard/config/opensearch_dashboards.yml 2>&1
docker exec -u root taxfisco-wazuh-dashboard bash -c \
  "chown wazuh-dashboard:wazuh-dashboard /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml && chmod 660 /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml" 2>&1
rm -f "$TMPFILE"
# Solo reiniciar si el archivo fue copiado exitosamente
if docker exec taxfisco-wazuh-dashboard test -f /usr/share/wazuh-dashboard/config/opensearch_dashboards.yml 2>/dev/null; then
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
