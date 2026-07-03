#!/bin/bash
# ============================================================================
# Escenario S03: Brute Force SSH (T1110.001)
# ============================================================================
# Herramientas: hydra
# Target: Cowrie SSH honeypot (172.20.0.50:2222)
# ============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/evidencia"
mkdir -p "$EVIDENCE_DIR"

HONEYPOT_HOST="172.20.0.50"
HONEYPOT_PORT="2222"
WORDLIST="/usr/share/wordlists/rockyou.txt"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "=========================================="
echo "S03: Brute Force SSH (T1110.001)"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

echo "$TIMESTAMP" > "$EVIDENCE_DIR/start_time.txt"

# Crear mini-wordlist si no existe
if [ ! -f /tmp/passwords.txt ]; then
    cat > /tmp/passwords.txt <<'EOF'
admin
123456
password
admin123
root
toor
qwerty
letmein
welcome
monkey
dragon
master
12345
1234
123
test
guest
info
mysql
user
administrator
EOF
fi

if [ ! -f /tmp/users.txt ]; then
    cat > /tmp/users.txt <<'EOF'
root
admin
user
test
oracle
postgres
ftp
www-data
EOF
fi

# 1. Brute force SSH
echo "[*] Fase 1: Hydra SSH brute force contra Cowrie"
hydra -L /tmp/users.txt -P /tmp/passwords.txt -t 4 -f \
    ssh://$HONEYPOT_HOST:$HONEYPOT_PORT \
    -o "$EVIDENCE_DIR/hydra_ssh_results.txt" 2>/dev/null || true

# 2. Verificar credenciales capturadas por Cowrie (acceder a logs)
echo "[*] Fase 2: Esperar a que Cowrie registre los intentos"
sleep 5

END_TIME=$(date -u +"%Y%m%dT%H%M%SZ")
echo "$END_TIME" > "$EVIDENCE_DIR/end_time.txt"

cat > "$EVIDENCE_DIR/resultados.json" <<EOF
{
  "scenario": "S03-bruteforce-ssh",
  "technique_id": "T1110.001",
  "technique_name": "Password Guessing",
  "tactic": "Credential Access",
  "timestamp_start": "$TIMESTAMP",
  "timestamp_end": "$END_TIME",
  "tools_used": ["hydra"],
  "target": "$HONEYPOT_HOST:$HONEYPOT_PORT",
  "users_tested": 8,
  "passwords_tested": 20,
  "evidence_files": ["hydra_ssh_results.txt"],
  "expected_detection": [
    "Wazuh rule 100210 (SSH brute force)",
    "Cowrie log entries for each attempt"
  ],
  "iso27035_phase": "Detection and Reporting (Phase 2)"
}
EOF

echo "[OK] Escenario S03 ejecutado."
