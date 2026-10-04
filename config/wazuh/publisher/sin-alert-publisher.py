#!/usr/bin/env python3
"""
Publicador de alertas Wazuh -> Wazuh Indexer (Prototipo II SIN)
==============================================================

Por que existe este script
--------------------------
El manager corre filebeat 7.10.2, cuya salida Elasticsearch siempre incluye
el parametro `_type` en la metadata de las acciones _bulk. OpenSearch 2.19.5
(wazuh-indexer 4.10.4) lo rechaza:

    400 Bad Request: Action/metadata line [1] contains an unknown parameter [_type]

Se verifico que ningun ajuste de filebeat lo evita (modulo wazuh, input
filestream, input log, es_doc_type vacio). La incompatibilidad es de version
(Beats 7.x contra OpenSearch 2.x), no de configuracion, asi que este script
publica las alertas directamente por HTTP.

Que hace
--------
1. Sigue /var/ossec/logs/alerts/alerts.json leyendo solo lo nuevo (offset en
   bytes persistido en /var/ossec/data_tmp/sin-publisher/offset).
2. Envia los eventos al indice wazuh-alerts del wazuh.indexer por _bulk, con
   autenticacion basica y sin el campo _type.
3. Si el indice no existe, lo crea con el template de wazuh aplicado a mano
   (mappings basicos) la primera vez.

Solo libreria estandar. Ver logs en stderr (los captura docker logs).
"""

import base64
import json
import os
import ssl
import sys
import time
import urllib.request
import urllib.error

ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"
# El offset vive en el volumen persistente del manager: si se guardara en
# /var/ossec/data_tmp, que el init regenera en cada arranque, el publicador
# volveria a publicar todo el historico y el indice se llenaria de duplicados.
STATE_DIR = "/var/ossec/data/sin-publisher"
OFFSET_FILE = os.path.join(STATE_DIR, "offset")
INDEXER = os.environ.get("SIN_INDEXER", "https://wazuh.indexer:9200")
INDEX = os.environ.get("SIN_INDEX", "wazuh-alerts")
USER = os.environ.get("SIN_INDEXER_USER", "admin")
PASSWORD = os.environ.get("SIN_INDEXER_PASS", "admin")
BATCH = 50
FLUSH_SECONDS = 2.0

_ctx = ssl.create_default_context()
_ctx.check_hostname = False
_ctx.verify_mode = ssl.CERT_NONE
_auth = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()


def log(msg):
    sys.stderr.write(f"[sin-publisher] {msg}\n")
    sys.stderr.flush()


def request(method, path, body=None, content_type="application/json"):
    req = urllib.request.Request(
        f"{INDEXER}{path}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Basic {_auth}",
            "Content-Type": content_type,
        },
    )
    with urllib.request.urlopen(req, timeout=20, context=_ctx) as resp:
        return resp.read()


def ensure_index():
    """Crea el indice si falta. Los mappings se dejan dinamicos: el dashboard
    lee los campos de rule.level, rule.description, rule.mitre, etc."""
    try:
        request("HEAD", f"/{INDEX}")
        return
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    body = json.dumps(
        {
            "settings": {"number_of_shards": 1, "number_of_replicas": 0},
            "mappings": {
                "properties": {
                    "timestamp": {"type": "date"},
                    "rule": {
                        "properties": {
                            "level": {"type": "integer"},
                            "description": {"type": "text"},
                            "id": {"type": "keyword"},
                            "groups": {"type": "keyword"},
                            "mitre": {
                                "properties": {
                                    "id": {"type": "keyword"},
                                    "technique": {"type": "keyword"},
                                    "tactic": {"type": "keyword"},
                                }
                            },
                        }
                    },
                    "agent": {
                        "properties": {
                            "id": {"type": "keyword"},
                            "name": {"type": "keyword"},
                        }
                    },
                    "manager": {"properties": {"name": {"type": "keyword"}}},
                }
            },
        }
    ).encode()
    request("PUT", f"/{INDEX}", body)
    log(f"indice {INDEX} creado")


def read_offset():
    try:
        with open(OFFSET_FILE) as fh:
            return int(fh.read().strip() or 0)
    except (OSError, ValueError):
        return 0


def write_offset(value):
    tmp = OFFSET_FILE + ".tmp"
    with open(tmp, "w") as fh:
        fh.write(str(value))
    os.replace(tmp, OFFSET_FILE)


def collect(offset):
    """Lee lineas completas desde offset. Devuelve (eventos, nuevo_offset)."""
    events = []
    try:
        size = os.path.getsize(ALERTS_FILE)
    except OSError:
        return events, offset
    if size < offset:  # el archivo se ha rotado o reiniciado
        offset = 0
    if size == offset:
        return events, offset
    with open(ALERTS_FILE, "r", errors="replace") as fh:
        fh.seek(offset)
        for line in fh:
            if not line.endswith("\n"):
                break  # linea parcial: se leera en la proxima pasada
            offset += len(line.encode("utf-8", "replace"))
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events, offset


def publish(events):
    if not events:
        return True
    lines = []
    for ev in events:
        lines.append(json.dumps({"index": {"_index": INDEX}}))
        lines.append(json.dumps(ev))
    body = ("\n".join(lines) + "\n").encode()
    try:
        resp = json.loads(request("POST", "/_bulk", body,
                                  "application/x-ndjson"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        log(f"error publicando: {e}")
        return False
    if resp.get("errors"):
        first = next(
            (i["index"] for i in resp.get("items", []) if "error" in i["index"]),
            {},
        )
        log(f"errores en bulk: {json.dumps(first)[:200]}")
        return False
    log(f"publicadas {len(events)} alertas")
    return True


def main():
    os.makedirs(STATE_DIR, exist_ok=True)
    ensure_index()
    offset = read_offset()
    log(f"iniciando en offset {offset}")
    pending = []
    last_flush = time.time()
    while True:
        events, offset = collect(offset)
        if events:
            pending.extend(events)
        now = time.time()
        if len(pending) >= BATCH or (pending and now - last_flush >= FLUSH_SECONDS):
            if publish(pending):
                write_offset(offset)
                pending = []
                last_flush = now
            else:
                last_flush = now  # reintenta en el proximo ciclo
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
