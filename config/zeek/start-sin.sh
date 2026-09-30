#!/bin/bash
# Detecta el bridge de la red DMZ (10.20.0.0/24) y captura todo su trafico.
# El contenedor corre en network_mode: host, por lo que ve los bridges del host.
# Se usa /proc/net/route porque la imagen de Zeek no trae el binario 'ip'.
set -e

# 10.20.0.0 en /proc/net/route se representa little-endian como 0000140A
IFACE=$(awk '$2 == "0000140A" {print $1}' /proc/net/route | head -1)

if [ -z "$IFACE" ]; then
    echo "[zeek] ERROR: no se encontro el bridge de la DMZ (10.20.0.0/24)" >&2
    exit 1
fi

echo "[zeek] capturando en $IFACE"
cd /var/log/zeek
exec zeek -i "$IFACE" local
