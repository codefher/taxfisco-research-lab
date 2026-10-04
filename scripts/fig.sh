#!/bin/bash
# =============================================================================
# fig.sh - genera una figura de terminal de la evidencia del Prototipo II
# =============================================================================
# Ejecuta un comando REAL, guarda su salida en un .txt (fuente verificable de
# la evidencia) y compone la figura PNG a partir de ese .txt.
#
# El texto de la figura sale del .txt sin modificar una sola caracter; el
# renderizador lo comprueba antes de generar la imagen.
#
# Uso:
#   bash scripts/fig.sh <carpeta> <nombre_base> "<comando>" [iteracion]
#
# Ejemplo:
#   bash scripts/fig.sh 03-aislamiento-red 01_docker-network-ls \
#       "docker network ls --filter name=sin-" v2.1-it2
# =============================================================================

set -euo pipefail

if [ "$#" -lt 3 ]; then
    echo "Uso: bash scripts/fig.sh <carpeta> <nombre_base> \"<comando>\" [iteracion]" >&2
    exit 2
fi

CARPETA="$1"
NOMBRE="$2"
COMANDO="$3"
ITERACION="${4:-v2.0-it1}"

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$RAIZ/evidencias/$ITERACION/$CARPETA"
TXT="$DEST/$NOMBRE.txt"
PNG="$DEST/$NOMBRE.png"

mkdir -p "$DEST"

# El .txt lleva el comando tal cual, en blanco, y despues la salida real.
{
  echo "\$ $COMANDO"
  echo
  eval "$COMANDO" 2>&1
} > "$TXT"

# render-terminal.py recibe primero el .txt y despues el .png.
python3 "$RAIZ/scripts/render-terminal.py" "$TXT" "$PNG"
