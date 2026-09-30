#!/bin/bash
# ============================================================================
# Master execution script - SIN Research Lab
# Ejecuta los 10 escenarios secuencialmente y genera todos los análisis
# ============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ATTACK_DIR="$SCRIPT_DIR/attack-scenarios"
ANALYSIS_DIR="$SCRIPT_DIR/analysis"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}SIN Research Lab - Master Execution${NC}"
echo -e "${YELLOW}========================================${NC}"

# Verificar que estamos en el contenedor atacante
if [ ! -d /root/attack-scenarios ]; then
    echo -e "${RED}Error: Este script debe ejecutarse dentro del contenedor 'attacker'${NC}"
    echo "Ejecutar: docker compose exec attacker bash /root/attack-scenarios/run_all.sh"
    exit 1
fi

# 1. Ejecutar los 10 escenarios
echo -e "\n${GREEN}## FASE 1: Ejecución de escenarios de ataque${NC}\n"

SCENARIOS=(
    "S01-reconocimiento"
    "S02-escaneo-web"
    "S03-bruteforce-ssh"
    "S04-sql-injection"
    "S05-credential-stuffing"
    "S06-xss"
    "S07-api-abuse"
    "S08-malware-drop"
    "S09-reverse-shell"
    "S10-exfiltracion-dns"
)

EXEC_LOG="$RESULTS_DIR/execution_log.txt"
echo "SIN - Master Execution Log" > $EXEC_LOG
echo "Started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> $EXEC_LOG

for SCENARIO in "${SCENARIOS[@]}"; do
    echo -e "\n${YELLOW}>>> Ejecutando $SCENARIO${NC}"
    SCENARIO_DIR="$ATTACK_DIR/$SCENARIO"

    if [ -f "$SCENARIO_DIR/ejecutar.sh" ]; then
        echo "[$(date -u +%H:%M:%S)] Running $SCENARIO..." | tee -a $EXEC_LOG
        bash "$SCENARIO_DIR/ejecutar.sh" 2>&1 | tee -a $EXEC_LOG
        echo -e "${GREEN}<<< $SCENARIO completado${NC}"
    else
        echo -e "${RED}<<< $SCENARIO no tiene script ejecutar.sh${NC}"
    fi

    # Pausa entre escenarios
    sleep 2
done

echo -e "\n${GREEN}## FASE 2: Generación de análisis y KPIs${NC}\n"

# 2. Ejecutar análisis de KPIs
echo -e "${YELLOW}>>> Generando reporte de KPIs${NC}"
cd /root/analysis
python3 kpi_calculator.py 2>&1 | tee -a $EXEC_LOG

# 3. Ejecutar análisis de cobertura MITRE
echo -e "\n${YELLOW}>>> Generando matriz de cobertura MITRE ATT&CK${NC}"
python3 mitre_coverage.py 2>&1 | tee -a $EXEC_LOG

# 4. Ejecutar análisis ISO 27035
echo -e "\n${YELLOW}>>> Generando reporte de cumplimiento ISO 27035/27001${NC}"
python3 iso27035_mapping.py 2>&1 | tee -a $EXEC_LOG

# 5. Consolidar todo en un reporte final
echo -e "\n${GREEN}## FASE 3: Reporte final consolidado${NC}\n"
echo "Finished: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> $EXEC_LOG

# Copiar todos los JSON de resultados al directorio results
cp $ANALYSIS_DIR/*.json $RESULTS_DIR/ 2>/dev/null || true

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Ejecución completa${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Resultados disponibles en:"
echo "  - $RESULTS_DIR/execution_log.txt"
echo "  - $RESULTS_DIR/kpi_report.json"
echo "  - $RESULTS_DIR/mitre_coverage.json"
echo "  - $RESULTS_DIR/iso27035_compliance.json"
echo "  - $ATTACK_DIR/*/evidencia/resultados.json"
echo ""
echo "Próximos pasos:"
echo "  1. Revisar dashboard de Grafana: http://localhost:3000"
echo "  2. Revisar casos en TheHive: http://localhost:9000"
echo "  3. Revisar alertas en Wazuh: https://localhost:443"
echo "  4. Revisar IOCs en MISP: https://localhost:8443"
