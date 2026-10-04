#!/bin/bash
# =============================================================================
# fig.sh - genera una figura de terminal de la evidencia del Prototipo II
# =============================================================================
# Ejecuta un comando REAL, guarda su salida en un .txt (fuente verificable de
# la evidencia) y renderiza ese .txt como figura PNG.
#
# Uso:
#   bash scripts/fig.sh <carpeta> <nombre_base> "<comando>"
#
# Ejemplo:
#   bash scripts/fig.sh 03-aislamiento-red 01_docker-network-ls \
#       "docker network ls --filter name=sin-"
# =============================================================================

set -euo pipefail

CARPETA="$1"
NOMBRE="$2"
COMANDO="$3"

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$RAIZ/evidencias/v2.0-it1/$CARPETA"
TXT="$DEST/$NOMBRE.txt"
PNG="$DEST/$NOMBRE.png"

mkdir -p "$DEST"

# El .txt lleva el comando tal cual, en blanco, y despues la salida real.
{
  echo "\$ $COMANDO"
  echo
  eval "$COMANDO" 2>&1
} > "$TXT"

python3 "$RAIZ/scripts/render-terminal.py" "$PNG" "$TXT"
