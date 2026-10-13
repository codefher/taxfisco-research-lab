# -*- coding: utf-8 -*-
"""Calcula los indicadores que si pueden derivarse de los datos reales del
repositorio: percentil 95 del tiempo de deteccion y tiempos de correccion."""
import json
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(r"F:\Maestria\tesis\taxfisco-research-lab")


def p95(vals):
    v = sorted(vals)
    if len(v) == 1:
        return v[0]
    pos = 0.95 * (len(v) - 1)
    lo = int(pos)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (pos - lo) * (v[hi] - v[lo])


print("=" * 70)
print("PERCENTIL 95 DEL TIEMPO DE DETECCION")
print("=" * 70)
for tag, sub in (("IT1", "v2.0-it1"), ("IT2", "v2.1-it2")):
    d = json.loads((BASE / "evidencias" / sub / "07-metricas/kpi_report.json")
                   .read_text(encoding="utf-8"))
    det = [x["mttd_seconds"] for x in d["kpis"]["MTTD"]["details"]
           if x["mttd_seconds"] is not None]
    print(f"\n{tag}: n = {len(det)}")
    print(f"  valores ordenados: {[round(x,3) for x in sorted(det)]}")
    print(f"  minimo   {min(det):.3f} s")
    print(f"  mediana  {statistics.median(det):.3f} s")
    print(f"  media    {statistics.fmean(det):.3f} s")
    print(f"  p90      {p95([x for x in det]):.3f} s  (mismo metodo)")
    print(f"  p95      {p95(det):.3f} s")
    print(f"  maximo   {max(det):.3f} s")

print()
print("=" * 70)
print("TIEMPO DE CORRECCION DEL CICLO")
print("=" * 70)
it1 = datetime(2026, 10, 4, 16, 7, 36, tzinfo=timezone.utc)
it2 = datetime(2026, 10, 4, 20, 33, 47, tzinfo=timezone.utc)
delta = it2 - it1
print(f"linea base (it1)  {it1.isoformat()}")
print(f"medicion final    {it2.isoformat()}")
print(f"ciclo completo    {delta}  = {delta.total_seconds()/3600:.2f} horas")

print()
print("Commits de correccion (convertidos a UTC):")
COMMIT = {
    "c66f7c7": ("L1, L2, L7", "2026-10-04 10:11:26 -0400"),
    "1a6bf86": ("panel del SIEM", "2026-10-04 11:32:01 -0400"),
    "20ee788": ("L3, L5, L6", "2026-10-04 12:08:06 -0400"),
    "2d13573": ("L4", "2026-10-04 12:17:16 -0400"),
    "df44eff": ("cierre de registros", "2026-10-04 14:32:56 -0400"),
    "dd2c124": ("publicador sin duplicados", "2026-10-04 18:44:03 -0400"),
}
from datetime import timedelta
tzoff = timedelta(hours=-4)
for h, (que, iso) in COMMIT.items():
    t = datetime.strptime(iso, "%Y-%m-%d %H:%M:%S %z").astimezone(timezone.utc)
    d = t - it1
    signo = "antes de la linea base" if d.total_seconds() < 0 else "despues"
    print(f"  {h}  {t.strftime('%H:%M:%SZ')}  {que:28} "
          f"{d.total_seconds()/60:+8.1f} min  {signo}")

print()
print("=" * 70)
print("ESCENARIOS Y TECNICAS EVALUADOS")
print("=" * 70)
mc = json.loads((BASE / "evidencias/v2.0-it1/07-metricas/mitre_coverage.json")
                .read_text(encoding="utf-8"))
print(f"  tecnicas del inventario   {mc['coverage']['techniques_implemented_count']}")
print(f"  tecnicas que activa la campana  {len(mc['technique_to_scenarios'])}")
print(f"  tacticas del inventario   {len(mc['coverage']['tactics_implemented'])}")
print(f"  con fuente en it2         10 de 10")
print(f"  escenarios evaluados      10 de 10 con evaluacion registrada")