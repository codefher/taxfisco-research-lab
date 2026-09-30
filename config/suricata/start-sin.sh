#!/bin/bash
# Detecta el bridge de la red DMZ (10.20.0.1/24) y captura todo su trafico.
# El contenedor corre en network_mode: host, por lo que ve los bridges del host.
set -e

IFACE=$(ip -o -4 addr show | awk '$4 ~ /^10\.20\.0\.1\// {print $2}' | cut -d@ -f1 | head -1)

if [ -z "$IFACE" ]; then
    echo "[suricata] ERROR: no se encontro el bridge de la DMZ (10.20.0.1/24)" >&2
    exit 1
fi

echo "[suricata] capturando en $IFACE"
mkdir -p /var/run/suricata /var/log/suricata
exec suricata -i "$IFACE" -c /etc/suricata/suricata.yaml --pidfile /var/run/suricata/suricata.pid
