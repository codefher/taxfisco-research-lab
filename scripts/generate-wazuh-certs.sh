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

CERTS_DIR="/mnt/f/Maestria/laboratorio/lab-1-lite/config/wazuh/certs"
DAYS_VALID=3650
COUNTRY="BO"
STATE="LP"
LOCALITY="LaPaz"
ORG="TaxFisco"
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
    -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORG/OU=$OU/CN=TaxFisco-RootCA" 2>/dev/null

# Para el manager (que verifica al indexer)
cp root-ca.pem root-ca-manager.pem
echo "  ✓ Root CA"

# Helper para generar cert firmado por Root CA
gen_cert() {
    local name=$1
    local cn=$2
    openssl genrsa -out "${name}-key.pem" 2048 2>/dev/null
    openssl req -new -key "${name}-key.pem" -out "${name}.csr" \
        -subj "/C=$COUNTRY/ST=$STATE/L=$LOCALITY/O=$ORG/OU=$OU/CN=$cn" 2>/dev/null
    openssl x509 -req -in "${name}.csr" -CA root-ca.pem -CAkey root-ca.key \
        -CAcreateserial -out "${name}.pem" -days $DAYS_VALID -sha256 2>/dev/null
    rm -f "${name}.csr"
}

# -----------------------------------------------------------------------------
# 2. Certs por servicio (formato 4.10: nombre.pem + nombre-key.pem)
# -----------------------------------------------------------------------------
gen_cert "indexer"  "wazuh-indexer"
echo "  ✓ indexer cert (indexer.pem + indexer-key.pem)"

gen_cert "dashboard" "wazuh-dashboard"
echo "  ✓ dashboard cert (dashboard.pem + dashboard-key.pem)"

gen_cert "wazuh"     "wazuh-manager"
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
