#!/usr/bin/env python3
"""
Resumen de alertas del SIEM para la evidencia del Prototipo II.

Consulta el indice wazuh-alerts y muestra el total real, el reparto por nivel
y el detalle por regla con su tecnica MITRE. La tecnica se lee del propio
documento (rule.mitre.id) en vez de deducirse del texto de la descripcion, que
era como se obtenian atribuciones incorrectas.

Uso:
    python3 q_alertas.py
"""
import base64
import json
import ssl
import urllib.parse
import urllib.request

INDEXER = "https://localhost:9200"
CRED = base64.b64encode(b"admin:admin").decode()
CTX = ssl._create_unverified_context()

CONSULTA = {
    "size": 0,
    "track_total_hits": True,
    "query": {"bool": {"filter": [{"terms": {"rule.groups": ["suricata", "sin", "ids"]}}]}},
    "aggs": {
        "por_nivel": {"terms": {"field": "rule.level", "size": 8,
                                "order": {"_count": "desc"}}},
        "por_regla": {
            "terms": {"field": "rule.description.keyword", "size": 8,
                      "order": {"_count": "desc"}},
            "aggs": {"tecnica": {"terms": {"field": "rule.mitre.id", "size": 3}}},
        },
    },
}


def main():
    url = (f"{INDEXER}/wazuh-alerts/_search?"
           + urllib.parse.urlencode({"rest_total_hits_as_int": "true"}))
    req = urllib.request.Request(url, data=json.dumps(CONSULTA).encode(),
                                 headers={"Authorization": f"Basic {CRED}",
                                          "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req, context=CTX, timeout=40))
    total = d["hits"]["total"]
    # Con rest_total_hits_as_int=true el total llega como entero plano.
    if isinstance(total, dict):
        total = total["value"]
    aggs = d["aggregations"]

    print(f"Alertas del SIEM derivadas del senuelo: {total}")
    print()
    print(f"{'NIVEL':<8}{'ALERTAS':<12}DESCRIPCION")
    for b in aggs["por_nivel"]["buckets"]:
        print(f"{b['key']:<8}{b['doc_count']:<12}por nivel de regla")
    print()
    print(f"{'TECNICA':<14}{'ALERTAS':<10}DESCRIPCION")
    for b in aggs["por_regla"]["buckets"]:
        # La sub-agregacion llega con su nombre como clave, no bajo "aggs".
        tec = b.get("tecnica", {}).get("buckets", [])
        etiqueta = tec[0]["key"] if tec else "sin tecnica"
        print(f"{etiqueta:<14}{b['doc_count']:<10}{b['key'][:56]}")


if __name__ == "__main__":
    main()
