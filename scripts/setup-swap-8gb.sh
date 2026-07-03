#!/bin/bash
# =============================================================================
# Setup Swap 8 GB - TaxFisco Research Lab LITE
# =============================================================================
# Crea 8 GB de swap en el host Linux. Necesario para el perfil lite de 16 GB
# para tener margen cuando hay picos de uso de memoria.
#
# Uso:
#   sudo bash scripts/setup-swap-8gb.sh
#   O desde make: make swap-setup
# =============================================================================

set -e

SWAP_FILE="/swapfile"
SWAP_SIZE="8G"
SWAPPINESS=10  # 0-100. Bajo = prefiere RAM, alto = prefiere swap. 10 es bueno para servidores con RAM limitada.

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar que somos root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Error: Este script debe ejecutarse con sudo${NC}"
    echo "Uso: sudo bash $0"
    exit 1
fi

# Verificar si ya existe swap
if swapon --show | grep -q "$SWAP_FILE"; then
    echo -e "${GREEN}[OK] Swap ya existe y está activo:${NC}"
    swapon --show
    free -h | grep -i swap
    exit 0
fi

# Verificar espacio en disco
echo -e "${YELLOW}Verificando espacio en disco...${NC}"
AVAILABLE=$(df / | tail -1 | awk '{print $4}')
NEEDED=$((8 * 1024 * 1024))  # 8 GB en KB

if [ "$AVAILABLE" -lt "$NEEDED" ]; then
    echo -e "${RED}Error: No hay suficiente espacio en disco.${NC}"
    echo "Disponible: $(df -h / | tail -1 | awk '{print $4}')"
    echo "Necesario: 8 GB mínimo"
    exit 1
fi

echo -e "${YELLOW}Creando archivo de swap de $SWAP_SIZE...${NC}"
fallocate -l $SWAP_SIZE $SWAP_FILE
chmod 600 $SWAP_FILE
mkswap $SWAP_FILE
swapon $SWAP_FILE

# Hacer permanente
if ! grep -q "$SWAP_FILE" /etc/fstab; then
    echo "$SWAP_FILE none swap sw 0 0" >> /etc/fstab
    echo -e "${GREEN}[OK] Swap añadido a /etc/fstab para persistencia${NC}"
fi

# Configurar swappiness (preferencia por RAM)
sysctl vm.swappiness=$SWAPPINESS
if ! grep -q "vm.swappiness" /etc/sysctl.d/99-taxfisco-swap.conf 2>/dev/null; then
    echo "vm.swappiness=$SWAPPINESS" > /etc/sysctl.d/99-taxfisco-swap.conf
    echo -e "${GREEN}[OK] Swappiness configurado a $SWAPPINESS en sysctl${NC}"
fi

# Verificar
echo ""
echo -e "${GREEN}=== Swap creado exitosamente ===${NC}"
swapon --show
echo ""
free -h | grep -E "Mem|Swap"

echo ""
echo -e "${GREEN}El sistema ahora tiene 8 GB de swap disponible.${NC}"
echo -e "${YELLOW}Recomendación: usa 'make lite-up' para levantar el lab.${NC}"
