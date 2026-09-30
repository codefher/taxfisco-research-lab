#!/bin/bash
# =============================================================================
# generate-wazuh-certs.sh
# Genera todos los certificados SSL necesarios para Wazuh 4.10.x
# single-node lab
#
# Estructura esperada por Wazuh 4.10:
#   config/wazuh/certs/
#     ├── root-ca.pem
#     ├── root-ca.key
#     ├── root-ca-manager.pem
#     ├── indexer.pem
#     ├── indexer-key.pem
#     ├── dashboard.pem
#     ├── dashboard-key.pem
#     ├── wazuh.pem
#     ├── wazuh-key.pem
#     ├── admin.pem
#     ├── admin-key.pem
#     └── client.keys
# =============================================================================

set -e

CERTS_DIR="$(cd "$(dirname "$0")/.." && pwd)/config/wazuh/certs"
DAYS_VALID=3650
COUNTRY="BO"
STATE="LP"
LOCALITY="LaPaz"
ORG="SIN"
OU="Lab"

# Limpiar certs antiguos
rm -f "$CERTS_DIR"/*.key "$CERTS_DIR"/*.pem "$CERTS_DIR"/*.csr "$CERTS_DIR"/*.srl 2>/dev/null
mkdir -p "$CERTS_DIR"
cd "$CERTS_DIR"

echo "=== Generando certificados Wazuh 4.10.x (formato -key.pem) ==="

# -----------------------------------------------------------------------------
# 1. Root CA
# -----------------------------------------------------------------------------
openssl genrsa -out root-ca.key 2048 2>/dev/null
openssl req -x509 -new -nodes -key root-ca.key -sha256 -days $DAYS_VALID \
    -out root-ca.pem \
    -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORG/OU=$OU/CN=SIN-RootCA" 2>/dev/null

# Para el manager (que verifica al indexer)
cp root-ca.pem root-ca-manager.pem
echo "  ✓ Root CA"

# Helper para generar cert firmado por Root CA con SAN
gen_cert() {
    local name=$1
    local cn=$2
    shift 2
    local sans="$@"
    openssl genrsa -out "${name}-key.pem" 2048 2>/dev/null
    openssl req -new -key "${name}-key.pem" -out "${name}.csr" \
        -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORG/OU=$OU/CN=$cn" 2>/dev/null

    if [ -n "$sans" ]; then
        local san_line="subjectAltName=DNS:${cn}"
        for s in $sans; do
            san_line="${san_line},DNS:${s}"
        done
        printf "subjectAltName=DNS:%s" "$cn" > "${name}.ext"
        for s in $sans; do
            printf ",DNS:%s" "$s" >> "${name}.ext"
        done
        printf "\n" >> "${name}.ext"
        openssl x509 -req -in "${name}.csr" -CA root-ca.pem -CAkey root-ca.key \
            -CAcreateserial -out "${name}.pem" -days $DAYS_VALID -sha256 \
            -extfile "${name}.ext" 2>/dev/null
    else
        openssl x509 -req -in "${name}.csr" -CA root-ca.pem -CAkey root-ca.key \
            -CAcreateserial -out "${name}.pem" -days $DAYS_VALID -sha256 2>/dev/null
    fi
    rm -f "${name}.csr" "${name}.ext"
}

# -----------------------------------------------------------------------------
# 2. Certs por servicio (formato 4.10: nombre.pem + nombre-key.pem)
#    SANs incluyen nombre DNS del servicio (wazuh.indexer) y hostname del container
# -----------------------------------------------------------------------------
gen_cert "indexer"  "wazuh-indexer" "wazuh.indexer" "localhost"
echo "  ✓ indexer cert (indexer.pem + indexer-key.pem)"

gen_cert "dashboard" "wazuh-dashboard" "wazuh.dashboard" "localhost"
echo "  ✓ dashboard cert (dashboard.pem + dashboard-key.pem)"

gen_cert "wazuh"     "wazuh-manager" "wazuh.manager" "localhost"
echo "  ✓ wazuh cert (wazuh.pem + wazuh-key.pem)"

gen_cert "admin"     "admin"
echo "  ✓ admin cert (admin.pem + admin-key.pem)"

# -----------------------------------------------------------------------------
# 3. client.keys (registro de agentes)
# -----------------------------------------------------------------------------
openssl genrsa -out "agent_001_key" 2048 2>/dev/null
openssl genrsa -out "agent_002_key" 2048 2>/dev/null

cat > client.keys <<EOF
001 decoy-api-agent 10.20.0.20 $(cat agent_001_key | base64 -w0)
002 decoy-portal-agent 10.20.0.21 $(cat agent_002_key | base64 -w0)
EOF

chmod 640 client.keys
rm -f agent_*_key

echo "  ✓ client.keys (2 agentes pre-registrados)"

# -----------------------------------------------------------------------------
# 4. Permisos
# -----------------------------------------------------------------------------
chmod 600 *-key.pem
chmod 644 *.pem
chmod 640 client.keys
chmod 600 root-ca.key

# -----------------------------------------------------------------------------
# Resumen
# -----------------------------------------------------------------------------
echo ""
echo "=== Certificados generados en $CERTS_DIR ==="
ls -la "$CERTS_DIR"
