#!/bin/bash
# =============================================================================
# Publicador de alertas propio (Prototipo II SIN)
# =============================================================================
# El manager corre filebeat 7.10.2, incompatible con OpenSearch 2.19 para
# indexar (envia _type en el bulk y el indice lo rechaza con 400). Este
# script deja filebeat sin entradas para que no genere errores, y lanza el
# publicador propio que indexa alerts.json en wazuh-alerts por HTTP.
#
# Es idempotente: si el publicador ya esta corriendo, no lo duplica.
# =============================================================================

set -u

FB=/etc/filebeat/filebeat.yml
PUB_SRC=/wazuh-config/publisher/sin-alert-publisher.py
PUB_DST=/var/ossec/data_tmp/sin-publisher/sin-alert-publisher.py
LOG=/var/ossec/logs/sin-publisher.log

# Filebeat queda apuntando a un archivo vacio: su version (7.10.2) envia el
# parametro _type en el bulk, que OpenSearch 2.19 rechaza, asi que no puede
# indexar las alertas (de eso se encarga el publicador propio). El input se
# mantiene porque filebeat aborta con "no modules or inputs enabled" si se
# queda sin entradas, y al salir con error se cae el contenedor entero.
PLACEHOLDER=/var/ossec/data_tmp/sin-publisher/.filebeat-placeholder.log
mkdir -p "$(dirname "$PLACEHOLDER")"
touch "$PLACEHOLDER"

if [ -f "$FB" ]; then
    cat > "$FB" <<YAML
# Wazuh - Filebeat configuration file (Prototipo II SIN)
# filebeat esta NEUTRALIZADO (ver 30-sin-publisher.sh): no indexa nada.
# Su version (7.10.2) envia el parametro _type en el bulk y OpenSearch 2.19
# lo rechaza con 400 "unknown parameter [_type]". La indexacion la hace el
# publicador propio (/wazuh-config/publisher/sin-alert-publisher.py).
setup.ilm.enabled: false
logging.metrics.enabled: false
YAML
    chown root:wazuh "$FB" 2>/dev/null || true
    chmod 640 "$FB" 2>/dev/null || true
fi

# ---------------------------------------------------------------------------
# Por que el arranque de filebeat se sustituye
# ---------------------------------------------------------------------------
# s6 exige que el servicio filebeat este vivo. Con el binario real, filebeat
# aborta con SIGABRT (por ejemplo al negociar TLS contra OpenSearch 2.19), sale
# con codigo 2, y s6 interpreta la caida como fin del contenedor: Docker lo
# reiniciaba en bucle (193 reinicios acumulados).
#
# El script de arranque de s6 no sirve para neutralizarlo porque
# /run/s6/services se crea DESPUES de que corran los entrypoint scripts. Lo que
# si existe siempre es el binario, asi que se aparta el real y se deja en su
# lugar un equivalente que solo espera. La indexacion no se pierde porque la
# hace el publicador, que no depende de filebeat.
BIN=/usr/share/filebeat/bin/filebeat
if [ -x "$BIN" ] && [ ! -f "$BIN.sin-indexar" ]; then
    mv "$BIN" "$BIN.sin-indexar" 2>/dev/null || true
fi
if [ -f "$BIN.sin-indexar" ]; then
    cat > "$BIN" <<'SH'
#!/bin/sh
# Sustituido por 30-sin-publisher.sh. El binario real es
# filebeat.sin-indexar, que no se usa: filebeat no puede indexar en
# OpenSearch 2.19 (envia _type en el bulk) y al abortar tumbaba el contenedor
# entero. La indexacion la hace el publicador sin-alert-publisher.py.
while true; do
    sleep 3600 &
    wait $!
done
SH
    chmod +x "$BIN" 2>/dev/null || true
    echo "[sin-publisher] binario de filebeat neutralizado (real en filebeat.sin-indexar)"
fi

if [ ! -f "$PUB_SRC" ]; then
    echo "[sin-publisher] AVISO: $PUB_SRC no existe; no se lanza el publicador"
    exit 0
fi

mkdir -p "$(dirname "$PUB_DST")"
cp -f "$PUB_SRC" "$PUB_DST"
chmod +x "$PUB_DST"

# Control de duplicados por fichero de PID en lugar de pgrep. pgrep contaba
# como coincidencia los procesos de consulta que el propio script lanza, asi
# que el publicador llegaba a arrancar dos veces.
PIDFILE=/var/ossec/run/sin-publisher.pid
mkdir -p "$(dirname "$PIDFILE")"

vivo() {
    [ -s "$PIDFILE" ] || return 1
    local pid
    pid=$(cat "$PIDFILE" 2>/dev/null)
    [ -n "$pid" ] && [ -d "/proc/$pid" ] && grep -qa "sin-alert-publisher" "/proc/$pid/cmdline" 2>/dev/null
}

if vivo; then
    echo "[sin-publisher] el publicador ya esta corriendo (pid $(cat "$PIDFILE"))"
    exit 0
fi

# Si hay procesos huerfanos de un arranque anterior, se retiran antes de
# lanzar el nuevo para no duplicar la indexacion.
for pid in $(pgrep -f "sin-alert-publisher.py" 2>/dev/null || true); do
    [ "$pid" = "$$" ] && continue
    kill -9 "$pid" 2>/dev/null || true
done

# nohup + disown: sobrevive al final del init del contenedor (la imagen no
# trae setsid).
nohup python3 "$PUB_DST" >> "$LOG" 2>&1 < /dev/null &
nuevo=$!
disown 2>/dev/null || true
echo "$nuevo" > "$PIDFILE"
sleep 4

if vivo; then
    echo "[sin-publisher] publicador lanzado (pid $nuevo, log: $LOG)"
else
    echo "[sin-publisher] AVISO: el publicador no arranco; ver $LOG"
    tail -5 "$LOG" 2>/dev/null || true
fi

exit 0
