#!/usr/bin/env python3
"""
Convierte los dashboards de Grafana del Prototipo II de PPL a consultas del
datasource "elasticsearch" de Grafana.

Por que
-------
Los dashboards de config/grafana/dashboards/*.json estan escritos con PQL
(Piped Processing Language de OpenSearch) porque el datasource previsto era
"grafana-opensearch-datasource". Esa imagen no esta instalada en Grafana 11.2
("Unable to find datasource plugin"), asi que el laboratorio usa el datasource
"elasticsearch" incluido en Grafana, que habla las consultas de Elasticsearch
(Lucene + metricas/agregaciones). Con PPL los paneles quedan en "No data".

Este script reescribe cada target PPL a su equivalente en el formato del
datasource elasticsearch, conservando el panel, el titulo y los umbrales.

Uso:
    python3 scripts/convert-grafana-ppl-to-lucene.py [--check]
    con --check solo informa de los targets queconverted, sin escribir.
"""

import argparse
import glob
import json
import os
import re
import sys

DASHBOARDS = "config/grafana/dashboards/sin-*.json"

# Tipos de metrica del datasource elasticsearch de Grafana.
AGG_TYPES = {
    "count()": ("count", None),
    "avg(": ("avg", None),
    "max(": ("max", None),
    "min(": ("min", None),
    "sum(": ("sum", None),
}


def parse_where(query):
    """Extrae la clausula where de una consulta PPL y la pasa a Lucene."""
    m = re.search(r"\|\s*where\s+(.+?)\s*(?:\||$)", query)
    if not m:
        return "*", None
    clause = m.group(1).strip()
    cond = re.match(r"^([\w.]+)\s*(>=|<=|>|<|==|!=)\s*([\w.\"']+)$", clause)
    if cond:
        field, op, value = cond.group(1), cond.group(2), cond.group(3).strip("\"'")
        try:
            value = float(value) if re.match(r"^-?\d+(\.\d+)?$", value) else value
        except ValueError:
            pass
        if op == ">=":
            return f"{field}:>={value}", None
        if op == "<=":
            return f"{field}:<={value}", None
        if op in (">", ">"):
            return f"{field}:>{value}", None
        if op == "<":
            return f"{field}:<{value}", None
        if op == "!=":
            return f"-{field}:{value}", None
        return f"{field}:{value}", None
    return "*", None


def make_bucket_agg(term):
    """Traduce el 'by' de PPL a una agregacion de Grafana."""
    m = re.match(r"span\(([\w.]+),\s*(\d+[smhd])\)", term)
    if m:
        return {
            "type": "date_histogram",
            "field": "@timestamp" if m.group(1) == "timestamp" else m.group(1),
            "id": "2",
            "settings": {"interval": m.group(2), "min_doc_count": 0, "extended_bounds": {}},
        }
    return {
        "type": "terms",
        "field": term,
        "id": "2",
        "settings": {"min_doc_count": 1, "order": "desc", "size": 10},
    }


def convert_target(target, panel_type="stat"):
    """Devuelve el target convertido, o None si no se reconoce la consulta."""
    query = target.get("query") or ""
    if "|" not in query:
        return None

    # Campos del head/fields: se ignoran; el panel table usa raw_documents.
    lucene, _ = parse_where(query)

    # stats count() as X
    m = re.search(r"stats\s+count\(\)\s+as\s+(\w+)(.*)$", query)
    if m:
        rest = m.group(2) or ""
        by = re.search(r"\bby\s+(.+?)(?:\s*\|.*)?$", rest)
        out = {
            "datasource": target.get("datasource", "WazuhIndexer"),
            "refId": target.get("refId", "A"),
            "query": lucene,
            "timeField": "@timestamp",
        }
        if by:
            out["metrics"] = [{"type": "count", "id": "1"}]
            out["bucketAggs"] = [make_bucket_agg(by.group(1).strip())]
        else:
            out["metrics"] = [{"type": "count", "id": "1"}]
            out["bucketAggs"] = [make_bucket_agg("span(timestamp, 1d)")]
        return out

    # stats avg/max/min/sum(campo) as X
    m = re.search(r"stats\s+(avg|max|min|sum)\(([\w.]+)\)\s+as\s+(\w+)", query)
    if m:
        agg, field, _alias = m.group(1), m.group(2), m.group(3)
        return {
            "datasource": target.get("datasource", "WazuhIndexer"),
            "refId": target.get("refId", "A"),
            "query": lucene,
            "timeField": "@timestamp",
            "metrics": [{"type": agg, "field": field, "id": "1"}],
            "bucketAggs": [make_bucket_agg("span(timestamp, 1d)")],
        }

    # sort/head/fields: tabla de documentos
    if re.search(r"\|\s*(sort|head|fields)", query):
        return {
            "datasource": target.get("datasource", "WazuhIndexer"),
            "refId": target.get("refId", "A"),
            "query": lucene,
            "timeField": "@timestamp",
            "metrics": [{"type": "raw_documents", "id": "1"}],
            "bucketAggs": [],
            "sort": [{"@timestamp": {"order": "desc", "unmapped_type": "date"}}],
        }

    return None


def convert_dashboard(path, check_only=False):
    with open(path) as fh:
        dash = json.load(fh)
    converted = skipped = 0
    for panel in dash.get("panels", []):
        for target in panel.get("targets", []):
            if not target.get("query"):
                continue
            new = convert_target(target, panel.get("type", "stat"))
            if new is None:
                skipped += 1
                print(f"  [sin convertir] {os.path.basename(path)} / {panel.get('title')}: {target['query'][:70]}")
                continue
            if new == target:
                converted += 1
                continue
            # El panel stat/bargauge/piechart reduce los buckets: para un
            # count el total es la suma de los dias; para avg/max, la media o
            # el maximo de los buckets.
            calc = None
            metrics = new.get("metrics", [])
            if metrics:
                t = metrics[0].get("type")
                calc = {"count": "sum", "avg": "mean", "max": "max",
                        "min": "min", "sum": "sum"}.get(t)
            if calc and panel.get("type") in ("stat", "bargauge", "piechart"):
                panel.setdefault("options", {}).setdefault("reduceOptions", {})
                panel["options"]["reduceOptions"]["calcs"] = [calc]
            ref = target.get("refId")
            panel["targets"] = [
                new if (t.get("refId") == ref and t.get("query") == target.get("query")) else t
                for t in panel["targets"]
            ]
            converted += 1
    if not check_only and converted:
        with open(path, "w") as fh:
            json.dump(dash, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    return converted, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="solo informa, no escribe")
    args = ap.parse_args()

    total = skipped = 0
    for path in sorted(glob.glob(DASHBOARDS)):
        c, s = convert_dashboard(path, args.check)
        total += c
        skipped += s
        print(f"{os.path.basename(path)}: {c} target(s) convertidos, {s} sin convertir")
    print(f"\nTotal: {total} convertidos, {skipped} sin convertir")
    return 0 if skipped == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
