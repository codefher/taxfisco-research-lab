#!/bin/bash
# Inyecta la ingesta de fuentes del laboratorio SIN en el ossec.conf del manager
# y copia las reglas/decoders custom a su ubicacion definitiva.
#
# Se ejecuta desde /entrypoint-scripts/ antes de que arranque wazuh-control.
set -e

CONF=/var/ossec/etc/ossec.conf
MARKER="sin-lab-localfiles"

if ! grep -q "$MARKER" "$CONF"; then
    cat >> "$CONF" <<'EOF'

<!-- sin-lab-localfiles: ingesta de Suricata y Zeek del Prototipo II -->
<ossec_config>
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/suricata/eve.json</location>
  </localfile>
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/zeek/http.log</location>
  </localfile>
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/zeek/conn.log</location>
  </localfile>
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/zeek/dns.log</location>
  </localfile>
</ossec_config>
EOF
    echo "[sin] localfiles de Suricata/Zeek agregados a ossec.conf"
fi

# Copia reglas y decoders custom desde el volumen /wazuh-config
if [ -d /wazuh-config/rules ]; then
    cp -f /wazuh-config/rules/*.xml /var/ossec/etc/rules/ 2>/dev/null || true
fi
if [ -d /wazuh-config/decoders ]; then
    cp -f /wazuh-config/decoders/*.xml /var/ossec/etc/decoders/ 2>/dev/null || true
fi

# Permisos esperados por Wazuh
chown root:wazuh "$CONF" 2>/dev/null || true
chmod 640 "$CONF" 2>/dev/null || true
chown -R wazuh:wazuh /var/ossec/etc/rules /var/ossec/etc/decoders 2>/dev/null || true
chmod 660 /var/ossec/etc/rules/*.xml /var/ossec/etc/decoders/*.xml 2>/dev/null || true

echo "[sin] configuracion de ingesta aplicada"
