#!/bin/bash
# ============================================================================
# Escenario S02: Escaneo de vulnerabilidades web (T1595.002)
# ============================================================================
# Herramientas: nikto, dirb, gobuster
# Target: Decoy Portal, Decoy API
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_API="http://10.20.0.20:8000"
DECOY_PORTAL="http://10.20.0.21:8000"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S02: Escaneo Web (T1595.002)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. Directory brute force
echo "[*] Fase 1: Directory brute force (gobuster)"
gobuster dir -u "$DECOY_PORTAL" -w /usr/share/wordlists/dirb/common.txt \
    -o "$EVIDENCE_DIR/gobuster_portal.txt" 2>/dev/null || true

# 2. Nikto web scanner
echo "[*] Fase 2: Nikto scan"
nikto -h "$DECOY_PORTAL" -o "$EVIDENCE_DIR/nikto_portal.txt" 2>/dev/null || true

# 3. Dirb
echo "[*] Fase 3: Dirb scan"
dirb "$DECOY_PORTAL" /usr/share/wordlists/dirb/common.txt -o "$EVIDENCE_DIR/dirb_portal.txt" 2>/dev/null || true

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S02-escaneo-web",
  "technique_id": "T1595.002",
  "technique_name": "Vulnerability Scanning",
  "tactic": "Reconnaissance",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["gobuster", "nikto", "dirb"],
  "targets_scanned": ["$DECOY_PORTAL", "$DECOY_API"],
  "evidence_files": ["gobuster_portal.txt", "nikto_portal.txt", "dirb_portal.txt"],
  "expected_detection": [
    "Suricata rule 2024003 (Nikto UA)",
    "Suricata rule 2024004 (nuclei UA)",
    "Wazuh rule 100250"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S02 ejecutado."
