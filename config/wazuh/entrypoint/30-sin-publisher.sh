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
# filebeat NO indexa alertas: la version 7.10.2 que trae wazuh-manager 4.10.4
# envia el parametro _type en el bulk y OpenSearch 2.19 lo rechaza con
# 400 "unknown parameter [_type]". La indexacion la hace el publicador propio
# (/wazuh-config/publisher/sin-alert-publisher.py, lanzado por este script).
# El input apunta a un archivo vacio porque filebeat aborta si se queda sin
# entradas, y al salir con error s6 termina el contenedor entero.
setup.ilm.enabled: false
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - $PLACEHOLDER
# Salida a consola en vez de Elasticsearch: con output.elasticsearch filebeat
# 7.10.2 entra en panic al negociar TLS contra OpenSearch 2.19 y sale con
# codigo 2, lo que hace que s6 termine el contenedor entero. Como el input esta
# vacio, la salida no produce nada.
output.console:
  pretty: false
logging.metrics.enabled: false
logging.level: error
YAML
    chown root:wazuh "$FB" 2>/dev/null || true
    chmod 640 "$FB" 2>/dev/null || true
    echo "[sin-publisher] filebeat.yml: input inerte sobre $PLACEHOLDER"
fi

if [ ! -f "$PUB_SRC" ]; then
    echo "[sin-publisher] AVISO: $PUB_SRC no existe; no se lanza el publicador"
    exit 0
fi

mkdir -p "$(dirname "$PUB_DST")"
cp -f "$PUB_SRC" "$PUB_DST"
chmod +x "$PUB_DST"

if pgrep -f "sin-alert-publisher.py" >/dev/null 2>&1; then
    echo "[sin-publisher] el publicador ya esta corriendo"
    exit 0
fi

# nohup + disown: survives al final del init del contenedor (la imagen no
# trae setsid).
nohup python3 "$PUB_DST" >> "$LOG" 2>&1 < /dev/null &
disown 2>/dev/null || true
sleep 4
if pgrep -f "sin-alert-publisher.py" >/dev/null 2>&1; then
    echo "[sin-publisher] publicador lanzado (log: $LOG)"
else
    echo "[sin-publisher] AVISO: el publicador no arranco; ver $LOG"
    tail -5 "$LOG" 2>/dev/null || true
fi

exit 0
