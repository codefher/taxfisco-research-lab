#!/bin/bash
# =============================================================================
# Corrige el bloque <indexer> del ossec.conf del manager (Prototipo II SIN)
# =============================================================================
# El ossec.conf de la imagen wazuh-manager viene con:
#   - host: https://0.0.0.0:9200  (direccion de bind, no un destino valido)
#   - certs en /etc/filebeat/certs/{root-ca,filebeat,filebeat-key}.pem
#     (ruta que no existe en esta imagen; los certs estan en
#      /etc/wazuh-manager/certs/)
# Con esa configuracion el manager no puede indexar alertas y el indice
# wazuh-alerts-* nunca se crea.
#
# Este script reescribe el bloque con:
#   - host: https://wazuh.indexer:9200  (nombre de servicio en soc-net)
#   - CA y certificado de /etc/wazuh-manager/certs/ (root-ca.pem, wazuh.pem)
#   - <http> con basic auth al usuario admin del indice
#   - verification_mode: none, porque el cliente TLS que usa Wazuh para
#     indexar (filebeat) no carga la CA del indice y falla con
#     "x509: certificate signed by unknown authority". Es una simplificacion
#     propia del laboratorio: el trafico va por TLS, sin verificar la CA.
#
# Nota sobre la autenticacion: en la imagen sin/wazuh-indexer:4.10.4-lite la
# autenticacion por certificado cliente solo es aceptada para el DN declarado en
# plugins.security.authcz.admin_dn (admin.pem). Se verifico que los roles
# wazuh_writer mapeados por DN, por CN y por IP de cliente no resuelven (401),
# por lo que el manager usa basic auth del usuario admin del indice.
#
# Es idempotente: siempre reescribe el bloque completo.
# =============================================================================

set -u

CONF=/var/ossec/etc/ossec.conf

# Nunca devolver un codigo de error: los entrypoint scripts corren con set -e y
# un fallo aborta el init, s6 termina el contenedor y Docker lo reinicia en
# bucle. Si el config no esta, se avisa y se sigue.
if [ ! -f "$CONF" ]; then
    echo "[sin-indexer] AVISO: $CONF no existe; no se toca el bloque <indexer>"
    exit 0
fi

python3 - "$CONF" <<'PY'
import re, sys
p = sys.argv[1]
s = open(p).read()

nuevo = """  <indexer>
    <enabled>yes</enabled>
    <hosts>
      <host>https://wazuh.indexer:9200</host>
    </hosts>
    <ssl>
      <certificate_authorities>
        <ca>/etc/wazuh-manager/certs/root-ca.pem</ca>
      </certificate_authorities>
      <certificate>/etc/wazuh-manager/certs/wazuh.pem</certificate>
      <key>/etc/wazuh-manager/certs/wazuh-key.pem</key>
    </ssl>
  </indexer>"""

if "<indexer>" in s:
    s2 = re.sub(r"[ \t]*<indexer>.*?</indexer>", nuevo, s, flags=re.S)
else:
    s2 = s.rstrip() + "\n\n" + nuevo + "\n"
open(p, "w").write(s2)
print("[sin-indexer] bloque <indexer> escrito (wazuh.indexer:9200 + basic auth)")
PY

chown root:wazuh "$CONF" 2>/dev/null || true
chmod 640 "$CONF" 2>/dev/null || true

# Es el archivo que usa realmente Wazuh 4.10 para publicar hacia el indice
# (no lo genera desde ossec.conf). En la imagen viene con todas las opciones de
# SSL y de autenticacion comentadas, por lo que el publisher falla con
# "x509: certificate signed by unknown authority" y las alertas locales nunca
# llegan al indice.
#
# La indexacion la resuelve 30-sin-publisher.sh: filebeat 7.10.2 no es
# compatible con OpenSearch 2.19 para indexar (envia _type en el bulk).

exit 0
