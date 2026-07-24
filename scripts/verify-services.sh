#!/usr/bin/env bash
# =============================================================================
# TaxFisco Research Lab - Functional Verification Script
# =============================================================================
# Ejecuta 13 health checks funcionales (read-only) sobre los servicios
# del lab. NO genera trafico contra los honeypots.
#
# Uso:
#   bash scripts/verify-services.sh
#
# Lee credenciales de .env. Si .env no existe, las usa las defaults
# que vienen en .env.example.
#
# Exit codes:
#   0 = todos los tests pasaron
#   1 = al menos un test fallo
#
# Requisitos:
#   - docker compose funcionando
#   - lab levantado (make lite-up + thehive-setup)
#   - jq (opcional, mejora output)
# =============================================================================

set -u  # variable no definida = error. NO set -e: queremos continuar tras fallos.

# --- Colores ANSI -------------------------------------------------------------
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    RED='\033[0;31m'
    YELLOW='\033[1;33m'
    BLUE='\033[1;34m'
    CYAN='\033[0;36m'
    BOLD='\033[1m'
    NC='\033[0m'
else
    GREEN=''; RED=''; YELLOW=''; BLUE=''; CYAN=''; BOLD=''; NC=''
fi

# --- Cargar .env --------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(dirname "$SCRIPT_DIR")"
cd "$LAB_DIR"

if [ -f .env ]; then
    set -a; source .env; set +a
    echo -e "${CYAN}[info]${NC} Credenciales cargadas de .env"
else
    echo -e "${YELLOW}[warn]${NC} .env no existe, usando defaults de .env.example"
    set -a; source .env.example; set +a
fi

# Defaults para credenciales que .env.example define
THEHIVE_USER="${THEHIVE_USER:-admin@thehive.local}"
THEHIVE_PASS="${THEHIVE_PASS:-secret}"
MISP_USER="${MISP_USER:-admin@admin.test}"
MISP_PASS="${MISP_PASS:-admin}"
DECOY_USER="${DECOY_USER:-admin}"
DECOY_PASS="${DECOY_PASS:-admin}"
DJANGO_USER="${DJANGO_USER:-admin}"
DJANGO_PASS="${DJANGO_PASS:-admin}"

# --- Helpers ------------------------------------------------------------------
PASS_COUNT=0
FAIL_COUNT=0
RESULTS=()

print_header() {
    echo
    echo -e "${BLUE}${BOLD}== $1 ==${NC}"
}

print_pass() {
    echo -e "  ${GREEN}[PASS]${NC} $1"
    PASS_COUNT=$((PASS_COUNT+1))
    RESULTS+=("PASS|$1")
}

print_fail() {
    echo -e "  ${RED}[FAIL]${NC} $1"
    [ -n "${2:-}" ] && echo -e "         ${YELLOW}$2${NC}"
    FAIL_COUNT=$((FAIL_COUNT+1))
    RESULTS+=("FAIL|$1|${2:-}")
}

# test_name exit_code expected_pattern actual_output
run_test() {
    local name="$1"
    local expected="$2"
    local actual="$3"
    if echo "$actual" | grep -qE "$expected"; then
        print_pass "$name"
    else
        print_fail "$name" "got: ${actual:0:200}"
    fi
}

# Verifica que un contenedor este corriendo
check_container() {
    local name="$1"
    local state
    state=$(docker inspect --format='{{.State.Status}}' "$name" 2>/dev/null)
    if [ "$state" = "running" ]; then
        print_pass "Container $name running"
    else
        print_fail "Container $name" "state: ${state:-not found}"
    fi
}

# --- Pre-flight: todos los contenedores corriendo -----------------------------
print_header "Pre-flight (containers up)"

# 25 contenedores esperados (sin dionaea, esta deshabilitado)
EXPECTED_CONTAINERS=(
    "taxfisco-wazuh-manager"
    "taxfisco-wazuh-indexer"
    "taxfisco-wazuh-dashboard"
    "taxfisco-wazuh-indexer-proxy"
    "taxfisco-misp-core"
    "taxfisco-misp-db"
    "taxfisco-misp-modules"
    "taxfisco-cassandra"
    "taxfisco-thehive"
    "taxfisco-cortex"
    "taxfisco-shuffle"
    "taxfisco-shuffle-frontend"
    "taxfisco-shuffle-db"
    "taxfisco-velociraptor"
    "taxfisco-grafana"
    "taxfisco-cowrie"
    "taxfisco-opencanary"
    "taxfisco-heralding"
    "taxfisco-suricata"
    "taxfisco-zeek"
    "taxfisco-decoy-api"
    "taxfisco-decoy-portal"
    "taxfisco-postgres"
    "taxfisco-attacker"
)

CONTAINERS_UP=0
for c in "${EXPECTED_CONTAINERS[@]}"; do
    if docker inspect --format='{{.State.Status}}' "$c" 2>/dev/null | grep -q running; then
        CONTAINERS_UP=$((CONTAINERS_UP+1))
    fi
done
TOTAL_CONTAINERS=${#EXPECTED_CONTAINERS[@]}
if [ "$CONTAINERS_UP" -eq "$TOTAL_CONTAINERS" ]; then
    print_pass "Containers running ($CONTAINERS_UP/$TOTAL_CONTAINERS)"
else
    print_fail "Containers running" "$CONTAINERS_UP/$TOTAL_CONTAINERS"
fi

# --- Test 1: Wazuh Indexer (via proxy) ---------------------------------------
print_header "Wazuh Stack"
out=$(curl -sk -u "admin:${WAZUH_INDEXER_PASSWORD:-admin}" \
    "http://localhost:9200/_cluster/health" 2>&1)
run_test "Wazuh Indexer health" '"status":"green"|"status":"yellow"' "$out"

out=$(docker exec taxfisco-wazuh-manager /var/ossec/bin/agent_control -l 2>&1)
run_test "Wazuh Manager agents" 'ID:' "$out"

out=$(curl -sk -o /dev/null -w '%{http_code}' "https://localhost:1443" 2>&1)
run_test "Wazuh Dashboard reachable" '^(200|302)$' "$out"

# --- Test 2: TheHive ---------------------------------------------------------
print_header "TheHive"
thehive_token=$(curl -sk -X POST "http://localhost:9000/api/v1/login" \
    -H "Content-Type: application/json" \
    -d "{\"user\":\"$THEHIVE_USER\",\"password\":\"$THEHIVE_PASS\"}" 2>&1)
if echo "$thehive_token" | grep -q "access_token"; then
    print_pass "TheHive login"
    token=$(echo "$thehive_token" | sed -E 's/.*"access_token":"([^"]+)".*/\1/')
    out=$(curl -sk -H "Authorization: Bearer $token" \
        "http://localhost:9000/api/v1/case?range=all" 2>&1)
    run_test "TheHive API (list cases)" '^\[' "$out"
else
    print_fail "TheHive login" "${thehive_token:0:200}"
fi

# --- Test 3: MISP ------------------------------------------------------------
print_header "MISP"
out=$(curl -sk -u "${MISP_USER}:${MISP_PASS}" \
    "https://localhost:8443/servers/getVersion" 2>&1)
run_test "MISP getVersion" 'version' "$out"

# --- Test 4: Shuffle ---------------------------------------------------------
print_header "Shuffle"
out=$(curl -sk "http://localhost:3001/api/v1/verify" 2>&1)
run_test "Shuffle verify" 'success' "$out"

# --- Test 5: Cortex ----------------------------------------------------------
print_header "Cortex"
out=$(curl -sk "http://localhost:9001/api/health" 2>&1)
run_test "Cortex health" 'OK|ok|"status"' "$out"

# --- Test 6: Grafana ---------------------------------------------------------
print_header "Grafana"
out=$(curl -sk -u "admin:${GRAFANA_PASSWORD:-Grafana_2024!}" \
    "http://localhost:3000/api/health" 2>&1)
run_test "Grafana health" 'ok|"database"' "$out"

# --- Test 7: Velociraptor ----------------------------------------------------
print_header "Velociraptor"
out=$(curl -sk "https://localhost:8889/health" 2>&1)
run_test "Velociraptor health" 'OK|ok' "$out"

# --- Test 8: Decoy API -------------------------------------------------------
print_header "Decoy API (FastAPI)"
decoy_token=$(curl -sk -X POST "http://localhost:8090/api/v1/login" \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$DECOY_USER\",\"password\":\"$DECOY_PASS\"}" 2>&1)
if echo "$decoy_token" | grep -qE "access_token|token"; then
    print_pass "Decoy API login"
    token=$(echo "$decoy_token" | sed -E 's/.*"access_token"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')
    if [ -z "$token" ]; then
        token=$(echo "$decoy_token" | sed -E 's/.*"token"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')
    fi
    out=$(curl -sk -H "Authorization: Bearer $token" \
        "http://localhost:8090/api/v1/contribuyentes" 2>&1)
    run_test "Decoy API protected endpoint" '^\[|^\{' "$out"
else
    print_fail "Decoy API login" "${decoy_token:0:200}"
fi

# --- Test 9: Decoy Portal ----------------------------------------------------
print_header "Decoy Portal (Django)"
cookie_jar=$(mktemp)
csrf=$(curl -sk -c "$cookie_jar" -b "$cookie_jar" \
    "http://localhost:8890/admin/login/" 2>&1 | \
    grep -oE 'csrfmiddlewaretoken[^>]+value="[^"]+"' | \
    sed -E 's/.*value="([^"]+)".*/\1/' | head -1)
if [ -z "$csrf" ]; then
    csrf=$(curl -sk -c "$cookie_jar" -b "$cookie_jar" \
        "http://localhost:8890/admin/login/" 2>&1 | \
        grep -oE 'name="csrfmiddlewaretoken" value="[^"]+"' | \
        sed -E 's/.*value="([^"]+)".*/\1/' | head -1)
fi
if [ -n "$csrf" ]; then
    login_code=$(curl -sk -c "$cookie_jar" -b "$cookie_jar" \
        -X POST "http://localhost:8890/admin/login/" \
        -H "Referer: http://localhost:8890/admin/login/" \
        -d "csrfmiddlewaretoken=$csrf&username=$DJANGO_USER&password=$DJANGO_PASS&next=/admin/" \
        -o /dev/null -w '%{http_code}' 2>&1)
    run_test "Decoy Portal login" '^(200|302)$' "$login_code"
    out=$(curl -sk -b "$cookie_jar" "http://localhost:8890/admin/" 2>&1)
    run_test "Decoy Portal admin" 'Django|Site administration|admin' "$out"
else
    print_fail "Decoy Portal CSRF token" "no se pudo extraer"
fi
rm -f "$cookie_jar"

# --- Test 10: Databases ------------------------------------------------------
print_header "Databases"
out=$(docker exec taxfisco-cassandra cqlsh cassandra.thehive 9042 \
    -e "SELECT release_version FROM system.local" 2>&1)
run_test "Cassandra reachable" '^.*4\.1' "$out"

out=$(docker exec taxfisco-postgres env PGPASSWORD="${POSTGRES_PASSWORD:-FiscalDB_2024!}" \
    psql -U fiscal -d taxfisco -c '\dt' 2>&1)
run_test "Postgres fiscal tables" 'contribuyentes' "$out"

# --- Resumen -----------------------------------------------------------------
TOTAL=$((PASS_COUNT+FAIL_COUNT))
echo
echo "==================================================================="
echo -e "  ${BOLD}Total: ${GREEN}${PASS_COUNT} PASS${NC} | ${RED}${FAIL_COUNT} FAIL${NC} / ${TOTAL}${NC}"
echo "==================================================================="

if [ "$FAIL_COUNT" -eq 0 ]; then
    echo -e "  ${GREEN}${BOLD}OK${NC} - todos los servicios funcionan."
    exit 0
else
    echo -e "  ${RED}${BOLD}FAIL${NC} - hay servicios con problemas. Para diagnosticar:"
    echo "          docker logs <container> --tail 50"
    echo "          docker compose ps"
    exit 1
fi
