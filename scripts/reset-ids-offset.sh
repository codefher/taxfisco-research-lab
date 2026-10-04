#!/bin/bash
# =============================================================================
# Reinicia la ingesta IDS de Suricata hacia Wazuh (Prototipo II SIN)
# =============================================================================
# Por que hace falta
# ----------------
# wazuh-logcollector guarda la posicion de lectura de cada localfile en la base
# de datos del manager. alert-events.json crece sin rotar durante toda la
# campana, asi que tras miles de lineas el offset queda desfasado y las alertas
# nuevas dejan de llegar a alerts.json: el sintoma es que Suricata sigue
# escribiendo eventos pero Wazuh no genera ninguna alerta "Suricata: ...".
#
# Verificado el 2026-10-04: truncar el archivo hace que logcollector detecte que
# el tamano se redujo y reinicie la lectura, y las alertas vuelven a fluir.
#
# Uso:
#   bash scripts/reset-ids-offset.sh
#   O desde make: make ids-reset
# =============================================================================

set -u

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

SURICATA=/var/log/suricata/alert-events.json

echo -e "${YELLOW}=== Reiniciando la ingesta IDS de Suricata ===${NC}"

if ! docker ps | grep -q "sin-suricata"; then
    echo -e "${RED}Error: sin-suricata no esta corriendo${NC}"
    exit 1
fi
if ! docker ps | grep -q "sin-wazuh-manager"; then
    echo -e "${RED}Error: sin-wazuh-manager no esta corriendo${NC}"
    exit 1
fi

antes=$(docker exec sin-suricata bash -c "wc -l < $SURICATA" 2>/dev/null | tr -d ' ')
echo "  lineas antes: ${antes:-0}"

# Truncar fuerza a logcollector a reiniciar la lectura del archivo.
docker exec sin-suricata bash -c ": > $SURICATA"
echo -e "${GREEN}[OK] $SURICATA trunco (eve.json se conserva integro)${NC}"

# analysisd se queda atascado con archivos grandes: reiniciarlo.
docker exec sin-wazuh-manager bash -c "/var/ossec/bin/wazuh-control restart analysisd" >/dev/null 2>&1
sleep 8
docker exec sin-wazuh-manager bash -c "/var/ossec/bin/wazuh-control status 2>/dev/null | grep -c running" >/dev/null 2>&1
echo -e "${GREEN}[OK] wazuh-analysisd reiniciado${NC}"

# Comprobar que el publicador sigue vivo (indexa alerts.json en el indice).
if docker exec sin-wazuh-manager bash -c 'pgrep -f sin-alert-publisher.py' >/dev/null 2>&1; then
    echo -e "${GREEN}[OK] publicador de alertas activo${NC}"
else
    echo -e "${YELLOW}AVISO: el publicador no esta corriendo; se relanzara al reiniciar el manager${NC}"
fi

echo ""
echo "Siguiente paso: generar trafico de ataque desde sin-attacker para que"
echo "Suricata registre eventos y Wazuh genere alertas."
