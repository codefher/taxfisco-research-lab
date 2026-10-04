#!/bin/bash
# =============================================================================
# Inyecta la ingesta de fuentes del laboratorio SIN en el ossec.conf del manager
# y copia las reglas/decoders custom a su ubicacion definitiva.
#
# IMPORTANTE (dos errores ya corregidos aqui):
#   1) Los <localfile> van DENTRO del elemento raiz <ossec_config>. Anadir un
#      segundo elemento raiz al final deja el XML invalido y Wazuh responde
#      "Error reading XML file 'etc/ossec.conf'".
#   2) El init de la imagen (cont-init.d 0-wazuh-init) anade un <ossec_config>
#      sobrante DESPUES del raiz; se absorbe para dejar un unico raiz.
#
# El script NUNCA debe terminar con codigo de salida distinto de cero: los
# entrypoint scripts se ejecutan con set -e y un fallo aborta el init del
# contenedor, s6 lo terminates y Docker lo reinicia en bucle. Si el archivo
# esta danado se restaura desde la copia de seguridad y se avisa, pero se
# devuelve 0 siempre.
#
# Es idempotente y autorreparable.
# =============================================================================

CONF=/var/ossec/etc/ossec.conf
MARKER="sin-lab-localfiles"
BAK=/var/ossec/etc/ossec.conf.sin-bak

if [ ! -f "$CONF" ]; then
    echo "[sin] AVISO: $CONF no existe; nada que hacer"
    exit 0
fi

# Copia de seguridad de la primera version valida que veamos.
if ! grep -q "</ossec_config>" "$CONF" 2>/dev/null; then
    echo "[sin] AVISO: $CONF esta truncado (sin cierre de ossec_config)"
    if [ -f "$BAK" ]; then
        cp -f "$BAK" "$CONF"
        echo "[sin] restaurado desde $BAK"
    else
        echo "[sin] no hay copia de seguridad; se deja como esta"
        exit 0
    fi
fi
# La copia de seguridad solo se actualiza si el archivo actual es valido, para
# no guardar un ossec.conf danado como referencia.
if python3 -c "import xml.etree.ElementTree as ET,sys; ET.parse(sys.argv[1])" "$CONF" 2>/dev/null; then
    cp -f "$CONF" "$BAK"
else
    echo "[sin] AVISO: $CONF no es XML valido; se conserva la copia previa"
fi

python3 - "$CONF" "$MARKER" <<'PY' || echo "[sin] AVISO: no se pudo ajustar ossec.conf (se deja como esta)"
import re, sys

conf, marker = sys.argv[1], sys.argv[2]
s = open(conf).read()

# 0) Localiza el cierre del elemento raiz PRINCIPAL (el primero). El init de la
#    imagen anade un <ossec_config> sobrante detras, asi que hay que trabajar
#    con la primera aparicion, no con rfind.
cierre = s.find("</ossec_config>")
if cierre == -1:
    print("[sin] no se encontro el cierre de <ossec_config>; no se modifica")
    sys.exit(0)

# 1) Elimina cualquier bloque previo del marcador, dentro del raiz o anadido
#    despues (XML invalido).
s = re.sub(r"[ \t]*<!--\s*" + marker + r".*?</ossec_config>\n", "", s, flags=re.S)
s = re.sub(r"[ \t]*<ossec_config>(?:(?!</ossec_config>).)*?" + marker +
           r"(?:(?!</ossec_config>).)*?</ossec_config>\n", "", s, flags=re.S)
cierre = s.find("</ossec_config>")
if cierre == -1:
    print("[sin] no se encontro el cierre de <ossec_config>; no se modifica")
    sys.exit(0)

# 2) Absorbe en el raiz los localfile del bloque sobrante que anade la imagen y
#    elimina ese segundo raiz, dejando un unico elemento raiz valido.
raiz = s[:cierre]
resto = s[cierre + len("</ossec_config>"):]
extras = re.findall(r"<localfile>.*?</localfile>", resto, flags=re.S)
for lf in extras:
    if lf not in raiz:
        raiz += "  " + lf.strip() + "\n"
if extras:
    print(f"[sin] absorbidos {len(extras)} localfile del bloque anadido por la imagen")

# 3) Inserta los localfile de Suricata/Zeek dentro del raiz.
raiz += """
  <!-- sin-lab-localfiles: ingesta de Suricata y Zeek del Prototipo II -->
  <localfile>
    <log_format>json</log_format>
    <location>/var/log/suricata/alert-events.json</location>
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
"""

open(conf, "w").write(raiz + "</ossec_config>\n")
print("[sin] localfiles de Suricata/Zeek insertados en ossec.conf")
PY

# Valida el XML resultante; si falla, restaura la copia de seguridad.
python3 - "$CONF" "$BAK" <<'PY' || echo "[sin] AVISO: ossec.conf no valido"
import shutil, sys, xml.etree.ElementTree as ET
try:
    ET.parse(sys.argv[1])
    print("[sin] ossec.conf valida")
except Exception as e:
    print(f"[sin] ERROR: ossec.conf invalido ({e}); se restaura la copia")
    shutil.copy(sys.argv[2], sys.argv[1])
PY

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
exit 0
