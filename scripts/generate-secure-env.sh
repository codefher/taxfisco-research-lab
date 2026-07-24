#!/bin/bash
# =============================================================================
# generate-secure-env.sh
# Genera un .env con contraseñas aleatorias seguras
# =============================================================================

set -e

cd /mnt/f/Maestria/laboratorio/lab-1-lite

if [ -f .env ]; then
    echo "ERROR: .env ya existe. Bórralo primero si quieres regenerar."
    exit 1
fi

cp .env.example .env

# Generar contraseñas aleatorias (32 chars hex = 64 chars pero nos quedamos con 32)
genpass() { openssl rand -hex 16; }
gensecret() { openssl rand -hex 32; }

# Reemplazar contraseñas
sed -i "s|ChangeMe_Strong!|$(genpass)|g" .env
sed -i "s|ChangeMe_MISP_Admin_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_MISP_DB_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_MISP_Root_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_TheHive_Secret_2024|$(gensecret)|g" .env
sed -i "s|ChangeMe_Cortex_Secret_2024|$(gensecret)|g" .env
sed -i "s|ChangeMe_Shuffle_DB_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_Grafana_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_Postgres_Fiscal_2024!|$(genpass)|g" .env
sed -i "s|ChangeMe_Django_Portal_2024!|$(gensecret)|g" .env
sed -i "s|ChangeMe_DecoyAPI_Token_2024|$(gensecret)|g" .env

echo "OK - .env generado con contraseñas aleatorias"
echo ""
echo "Credenciales generadas (NO compartir):"
grep -E "PASSWORD|SECRET|TOKEN" .env | sed 's/=.*/=***REDACTED***/'
