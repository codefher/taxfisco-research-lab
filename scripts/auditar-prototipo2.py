# -*- coding: utf-8 -*-
"""Comprobacion aritmetica y de consistencia del Prototipo II."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(r"F:\Maestria\tesis\taxfisco-research-lab\evidencias")

it1 = json.loads((BASE / "v2.0-it1/07-metricas/kpi_report.json").read_text(encoding="utf-8"))
it2 = json.loads((BASE / "v2.1-it2/07-metricas/kpi_report.json").read_text(encoding="utf-8"))

d1 = {d["scenario"]: d for d in it1["kpis"]["MTTD"]["details"]}
d2 = {d["scenario"]: d for d in it2["kpis"]["MTTD"]["details"]}

print("ESC  IT1 tecnica     IT1 s      IT1 fuente                | IT2 tecnica     IT2 s      IT2 fuente")
print("-" * 110)
for esc in sorted(d1):
    a, b = d1[esc], d2[esc]
    v1 = a["mttd_seconds"]
    v2 = b["mttd_seconds"]
    s1 = "-" if v1 is None else f"{v1:g}"
    s2 = "-" if v2 is None else f"{v2:g}"
    print(f"{esc:4} {a['technique']:13} {s1:9} {str(a['source'])[:24]:25} | "
          f"{b['technique']:13} {s2:9} {b['source']}")

print()
print("=== REDUCCIONES (solo escenarios con valor en ambas) ===")
for esc in sorted(d1):
    v1, v2 = d1[esc]["mttd_seconds"], d2[esc]["mttd_seconds"]
    if v1 is None or v2 is None:
        print(f"{esc}: no comparable (it1={v1}, it2={v2})")
        continue
    red = (v1 - v2) / v1 * 100
    print(f"{esc}: {v1:g} -> {v2:g}  = {red:+.2f} %")

print()
print("=== MEDIAS ===")
vals1 = [d["mttd_seconds"] for d in d1.values() if d["mttd_seconds"] is not None]
vals2 = [d["mttd_seconds"] for d in d2.values() if d["mttd_seconds"] is not None]
print("it1 media recalculada:", round(sum(vals1) / len(vals1), 4), "n =", len(vals1),
      "| declarada:", it1["kpis"]["MTTD"]["mean"])
print("it2 media recalculada:", round(sum(vals2) / len(vals2), 4), "n =", len(vals2),
      "| declarada:", it2["kpis"]["MTTD"]["mean"])
print("it1 min/max recalculado:", min(vals1), max(vals1),
      "| declarados:", it1["kpis"]["MTTD"]["min"], it1["kpis"]["MTTD"]["max"])
print("it2 min/max recalculado:", min(vals2), max(vals2),
      "| declarados:", it2["kpis"]["MTTD"]["min"], it2["kpis"]["MTTD"]["max"])

print()
print("=== SCENARIO_DETAILS (duracion) ===")
print("it1:", [(s["id"], s["technique"], s["duration_seconds"]) for s in it1["scenario_details"]])
print("it2:", [(s["id"], s["technique"], s["duration_seconds"]) for s in it2["scenario_details"]])

print()
print("=== TECNICAS DETECTADAS ===")
print("it1:", it1["coverage"]["mitre_attack"]["techniques_detected"])
print("it2:", it2["coverage"]["mitre_attack"]["techniques_detected"])
print("tacticas it1:", it1["coverage"]["mitre_attack"]["tactics_covered"])
print("tacticas it2:", it2["coverage"]["mitre_attack"]["tactics_covered"])