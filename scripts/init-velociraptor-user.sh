#!/bin/bash
# =============================================================================
# Init Velociraptor admin user - SIN Research Lab LITE
# =============================================================================
# La imagen wlambert/velociraptor crea el usuario admin en su entrypoint, pero
# docker-compose.yml monta config/velociraptor/server.config.yaml (solo
# lectura), lo que impide ese bootstrap y deja el servidor sin usuarios
# ("Unknown username" en los logs).
#
# Este script crea el usuario admin con rol administrator contra el config
# real del contenedor (/velociraptor/server.config.yaml) y reinicia el
# servicio para que tome el cambio. Es idempotente: si el usuario ya existe,
# solo verifica el acceso.
#
# Uso:
#   bash scripts/init-velociraptor-user.sh
#   O desde make: make velociraptor-setup
# =============================================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

VR_USER="${VELOCIRAPTOR_USER:-admin}"
VR_PASS="${VELOCIRAPTOR_PASSWORD:-Admin1234!}"
GUI_URL="https://localhost:8889"

echo -e "${YELLOW}=== Inicializando usuario admin de Velociraptor ===${NC}"

if ! docker ps | grep -q "sin-velociraptor"; then
    echo -e "${RED}Error: Contenedor sin-velociraptor no está corriendo${NC}"
    exit 1
fi

# Verificar si el usuario ya funciona
code=$(curl -sk -o /dev/null -w "%{http_code}" -u "$VR_USER:$VR_PASS" \
    "$GUI_URL/api/v1/GetUserUITraits" --max-time 8 || true)

if [ "$code" = "200" ]; then
    echo -e "${GREEN}[OK] El usuario '$VR_USER' ya existe y autentica correctamente${NC}"
    exit 0
fi

echo "El usuario no existe o no autentica (HTTP $code). Creándolo..."

docker exec sin-velociraptor sh -c \
    "cd /velociraptor && ./velociraptor --config server.config.yaml \
     user add '$VR_USER' '$VR_PASS' --role administrator"

echo "Reiniciando Velociraptor para aplicar el cambio..."
docker restart sin-velociraptor >/dev/null
sleep 20

code=$(curl -sk -o /dev/null -w "%{http_code}" -u "$VR_USER:$VR_PASS" \
    "$GUI_URL/api/v1/GetUserUITraits" --max-time 8 || true)

if [ "$code" = "200" ]; then
    echo -e "${GREEN}[OK] Usuario '$VR_USER' creado y verificado (HTTP 200)${NC}"
else
    echo -e "${RED}Error: la autenticación sigue fallando (HTTP $code)${NC}"
    echo "Revisa los logs: docker logs sin-velociraptor | tail -30"
    exit 1
fi
