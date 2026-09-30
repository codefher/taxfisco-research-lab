#!/bin/bash
# =============================================================================
# Setup Wazuh Index for TheHive - SIN Research Lab LITE
# =============================================================================
# En el perfil lite, TheHive y Cortex usan el mismo Elasticsearch de Wazuh.
# Este script crea el índice "thehive" en Wazuh Indexer para evitar conflictos.
#
# Uso:
#   bash scripts/setup-wazuh-index-for-thehive.sh
#   O desde make: make thehive-setup
# =============================================================================

set -e

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

WAZUH_INDEXER_URL="https://172.22.0.11:9200"
WAZUH_INDEXER_HOST_PORT="https://localhost:9200"
INDEX_NAME="thehive"

echo -e "${YELLOW}=== Configurando índice TheHive en Wazuh Indexer ===${NC}"

# Verificar que Wazuh Indexer está corriendo
echo "Verificando que Wazuh Indexer está disponible..."
if ! curl -sk -o /dev/null -w "%{http_code}" "$WAZUH_INDEXER_HOST_PORT" | grep -q "200"; then
    echo -e "${RED}Error: Wazuh Indexer no está disponible en $WAZUH_INDEXER_HOST_PORT${NC}"
    echo "Asegúrate de que el lab está corriendo: docker compose ps"
    exit 1
fi

echo -e "${GREEN}[OK] Wazuh Indexer disponible${NC}"

# Verificar que el contenedor wazuh.indexer está corriendo
if ! docker ps | grep -q "sin-wazuh-indexer"; then
    echo -e "${RED}Error: Contenedor sin-wazuh-indexer no está corriendo${NC}"
    exit 1
fi

# Crear el índice thehive con settings optimizados para Wazuh Indexer compartido
echo "Creando índice '$INDEX_NAME' en Wazuh Indexer..."

docker exec sin-wazuh-indexer bash -c "
curl -sk -X PUT 'https://localhost:9200/$INDEX_NAME' \
  -H 'Content-Type: application/json' -d '{
    \"settings\": {
      \"number_of_shards\": 1,
      \"number_of_replicas\": 0,
      \"refresh_interval\": \"5s\"
    },
    \"mappings\": {
      \"properties\": {
        \"_type\": {\"type\": \"keyword\"},
        \"_createdAt\": {\"type\": \"date\"},
        \"_createdBy\": {\"type\": \"keyword\"},
        \"_id\": {\"type\": \"keyword\"},
        \"_updatedAt\": {\"type\": \"date\"},
        \"_updatedBy\": {\"type\": \"keyword\"},
        \"case\": {\"type\": \"object\"},
        \"title\": {\"type\": \"text\"},
        \"description\": {\"type\": \"text\"},
        \"severity\": {\"type\": \"integer\"},
        \"tlp\": {\"type\": \"integer\"},
        \"tags\": {\"type\": \"keyword\"}
      }
    }
  }'
"

echo ""
echo -e "${YELLOW}Verificando creación del índice...${NC}"
if curl -sk "$WAZUH_INDEXER_HOST_PORT/_cat/indices/$INDEX_NAME?v" | grep -q "$INDEX_NAME"; then
    echo -e "${GREEN}[OK] Índice '$INDEX_NAME' creado correctamente${NC}"
else
    echo -e "${YELLOW}El índice ya existe o no se pudo crear (no es crítico)${NC}"
fi

# Listar todos los índices para ver el estado
echo ""
echo -e "${YELLOW}=== Índices actuales en Wazuh Indexer ===${NC}"
curl -sk "$WAZUH_INDEXER_HOST_PORT/_cat/indices?v" | head -20

# Verificar TheHive
echo ""
echo -e "${YELLOW}=== Verificando conectividad de TheHive ===${NC}"
if docker ps | grep -q "sin-thehive"; then
    sleep 10
    if curl -sk -o /dev/null -w "%{http_code}" "http://localhost:9000/api/v1/query" | grep -qE "200|401|403"; then
        echo -e "${GREEN}[OK] TheHive está respondiendo${NC}"
    else
        echo -e "${YELLOW}TheHive aún está arrancando. Espera 1-2 minutos.${NC}"
    fi
else
    echo -e "${YELLOW}TheHive no está corriendo todavía${NC}"
fi

echo ""
echo -e "${GREEN}=== Configuración completada ===${NC}"
echo ""
echo "TheHive ahora usa el índice '$INDEX_NAME' en el Elasticsearch de Wazuh."
echo "Cortex también usa el mismo ES con índice 'cortex'."
echo ""
echo "Si ves errores en TheHive:"
echo "  1. docker logs sin-thehive | tail -50"
echo "  2. docker compose restart thehive"
