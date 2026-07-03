#!/bin/bash
# ============================================================================
# Escenario S01: Reconocimiento (T1595 - Active Scanning)
# ============================================================================
# Herramientas: nmap
# Target: Decoy API, Decoy Portal, Honeypots
# Detección: Suricata rule 2024001, Wazuh rule 100250
# ============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

DECOY_API="172.20.0.20"
DECOY_PORTAL="172.20.0.21"
HONEYPOT_COWRIE="172.20.0.50"
ATTACKER_IP="172.20.0.99"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S01: Reconocimiento (T1595)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

# Timestamp inicial
echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. Network sweep de la DMZ
echo "[*] Fase 1: Network sweep DMZ (172.20.0.0/24)"
nmap -sn 172.20.0.0/24 -oN "$EVIDENCE_DIR/nmap_ping_sweep.txt" 2>/dev/null

# 2. Service scan contra decoys
echo "[*] Fase 2: Service scan"
nmap -sV -p- --open $DECOY_API -oN "$EVIDENCE_DIR/nmap_decoy_api.txt" 2>/dev/null
nmap -sV -p- --open $DECOY_PORTAL -oN "$EVIDENCE_DIR/nmap_decoy_portal.txt" 2>/dev/null
nmap -sV -p 22,2222,2323,8080 $HONEYPOT_COWRIE -oN "$EVIDENCE_DIR/nmap_honeypot.txt" 2>/dev/null

# 3. OS detection
echo "[*] Fase 3: OS fingerprinting"
nmap -O $DECOY_API -oN "$EVIDENCE_DIR/nmap_os_detection.txt" 2>/dev/null

# 4. Generar reporte
END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S01-reconocimiento",
  "technique_id": "T1595",
  "technique_name": "Active Scanning",
  "tactic": "Reconnaissance",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["nmap"],
  "targets_scanned": ["$DECOY_API", "$DECOY_PORTAL", "$HONEYPOT_COWRIE"],
  "attacker_ip": "$ATTACKER_IP",
  "evidence_files": [
    "nmap_ping_sweep.txt",
    "nmap_decoy_api.txt",
    "nmap_decoy_portal.txt",
    "nmap_honeypot.txt",
    "nmap_os_detection.txt"
  ],
  "expected_detection": [
    "Suricata rule 2024001 (Nmap user agent)",
    "Wazuh rule 100250 (Recon tool detection)"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S01 ejecutado. Evidencia en: $EVIDENCE_DIR"
