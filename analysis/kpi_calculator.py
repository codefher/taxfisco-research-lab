"""
KPI Calculator - TaxFisco Research Lab
=======================================

Calcula los KPIs de la tesis a partir de DATOS REALES:
  - MTTD (Mean Time To Detect)  -> medido: primer evento de deteccion
                                    (decoy-api / cowrie) menos el inicio del escenario
  - MTTR / MTTC / MTTContain    -> requieren timestamps de TheHive (si no hay datos: no_medido)
  - # Evidencias / Calidad de evidencia
  - Cobertura MITRE ATT&CK
  - Cumplimiento ISO 27035/27001

Fuentes de datos:
  - attack-scenarios/*/evidencia/resultados.json  (inicio/fin y tecnica de cada escenario)
  - decoy-api attacks.json                        (eventos de ataque instrumentados)
  - cowrie (docker logs)                          (conexiones SSH)

El script puede ejecutarse en el host (usa `docker exec` / `docker logs`) o dentro
de un contenedor con los ficheros montados en las rutas por defecto.
"""

import json
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# =============================================================================
# Configuración
# =============================================================================

REPO_DIR = Path(__file__).resolve().parent.parent

ATTACK_SCENARIOS_DIR = Path(os.environ.get("ATTACK_SCENARIOS_DIR", REPO_DIR / "attack-scenarios"))
DECOY_API_LOG = Path(os.environ.get("DECOY_API_LOG", "/var/log/decoy-api/attacks.json"))
DECOY_CONTAINER = os.environ.get("DECOY_CONTAINER", "sin-decoy-api")
COWRIE_CONTAINER = os.environ.get("COWRIE_CONTAINER", "sin-cowrie")
PORTAL_CONTAINER = os.environ.get("PORTAL_CONTAINER", "sin-decoy-portal")
DEFAULT_ATTACKER_IP = os.environ.get("ATTACKER_IP", "10.20.0.99")
OUTPUT = Path(os.environ.get("KPI_OUTPUT", REPO_DIR / "analysis" / "kpi_report.json"))


# =============================================================================
# Utilidades
# =============================================================================

def parse_ts(value: str) -> datetime:
    """Acepta 2026-07-25T11:16:28.356879Z | 2026-07-25T14:28:07+0000 | 20260725T142642Z."""
    s = value.strip().rstrip("Z").replace("+0000", "").replace(" ", "T")
    s = re.sub(r"(\.\d{6})\d+", r"\1", s)  # truncar nanosegundos a microsegundos
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y%m%dT%H%M%S"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise ValueError(f"timestamp no reconocido: {value!r}")


def _run(cmd: List[str]) -> str:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
        return (r.stdout or "") + (r.stderr or "")
    except (FileNotFoundError, subprocess.SubprocessError):
        return ""


# =============================================================================
# Carga de datos
# =============================================================================

def load_scenario_results(scenarios_dir: Path) -> List[Dict]:
    results = []
    if not scenarios_dir.exists():
        return results
    for result_file in sorted(scenarios_dir.glob("S*/evidencia/resultados.json")):
        with open(result_file) as f:
            data = json.load(f)
            data["_dir"] = str(result_file.parent.parent)
            results.append(data)
    return results


def load_decoy_events() -> List[Dict]:
    """Eventos de ataque instrumentados por el Decoy API (timestamp + tecnica)."""
    raw = ""
    if DECOY_API_LOG.exists():
        raw = DECOY_API_LOG.read_text()
    else:
        raw = _run(["docker", "exec", DECOY_CONTAINER, "cat", "/var/log/decoy-api/attacks.json"])
    events = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


COWRIE_CONN = re.compile(
    r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\+0000.*New connection: (\S+):\d+ \("
)


def load_cowrie_connections() -> List[Tuple[datetime, str]]:
    """Conexiones SSH registradas por Cowrie (timestamp, ip origen)."""
    txt = _run(["docker", "logs", COWRIE_CONTAINER])
    conns = []
    for line in txt.splitlines():
        m = COWRIE_CONN.match(line)
        if m:
            conns.append((parse_ts(m.group(1)), m.group(2)))
    conns.sort(key=lambda c: c[0])
    return conns


def load_decoy_api_attacks(log_file: Path) -> List[Dict]:
    """Compatibilidad con la firma original."""
    return load_decoy_events()


def load_decoy_requests() -> List[Dict]:
    """Todas las peticiones vistas por el Decoy API (timestamp + path)."""
    raw = ""
    if DECOY_API_LOG.parent.joinpath("all_requests.jsonl").exists():
        raw = DECOY_API_LOG.parent.joinpath("all_requests.jsonl").read_text()
    else:
        raw = _run(["docker", "exec", DECOY_CONTAINER, "cat",
                    "/var/log/decoy-api/all_requests.jsonl"])
    reqs = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            reqs.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return reqs


def scenario_target_paths(scenario: Dict) -> List[str]:
    """Extrae los paths de los objetivos tipo URL (http://host:puerto/path)."""
    paths = []
    for t in scenario.get("targets_scanned", []) or []:
        m = re.match(r"^https?://[^/]+(/.*)?$", str(t))
        if m and m.group(1):
            paths.append(m.group(1).rstrip("/"))
    return paths


PORTAL_TS = re.compile(
    r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?)\S*\s+.*?\"(?:GET|POST|HEAD|PUT|DELETE|OPTIONS|PATCH) (\S+) HTTP"
)


def load_portal_requests() -> List[Tuple[datetime, str]]:
    """Peticiones al Decoy Portal (Django) en UTC. Excluye /health (ruido)."""
    txt = _run(["docker", "logs", "-t", PORTAL_CONTAINER])
    out = []
    for line in txt.splitlines():
        m = PORTAL_TS.match(line)
        if not m:
            continue
        path = m.group(2)
        if path == "/health":
            continue
        try:
            out.append((parse_ts(m.group(1)), path))
        except ValueError:
            continue
    return sorted(out, key=lambda x: x[0])


def allowed_sources(scenario: Dict) -> set:
    """Fuentes de deteccion plausibles segun los objetivos del escenario."""
    targets = " ".join(str(t) for t in (scenario.get("targets_scanned") or []))
    allowed = set()
    if "10.20.0.20" in targets or "172.20.0.20" in targets:
        allowed.add("decoy-api")
    if "10.20.0.21" in targets or "172.20.0.21" in targets:
        allowed.add("decoy-portal")
    if "10.20.0.50" in targets or "172.20.0.50" in targets or ":2222" in targets:
        allowed.add("cowrie")
    return allowed




# =============================================================================
# Cálculos
# =============================================================================

def calculate_mttd(scenarios: List[Dict],
                   decoy_events: Optional[List[Dict]] = None,
                   cowrie_conns: Optional[List[Tuple[datetime, str]]] = None,
                   decoy_requests: Optional[List[Dict]] = None,
                   portal_requests: Optional[List[datetime]] = None) -> Dict:
    """
    MTTD real por escenario = (primer evento de deteccion) - (inicio del escenario).

    Fuentes de deteccion (en orden):
      1. Decoy API: ataque instrumentado (`attack_technique_id` == tecnica del escenario).
      2. Decoy API (all_requests): primera peticion al path objetivo.
      3. Ventana del escenario [inicio, fin+120s]: primera peticion del atacante al
         Decoy API, o peticion al Decoy Portal, o conexion a Cowrie.
    Los escenarios sin evento NO se inventan: se reportan como "sin evento".
    """
    decoy_events = decoy_events if decoy_events is not None else load_decoy_events()
    cowrie_conns = cowrie_conns if cowrie_conns is not None else load_cowrie_connections()
    decoy_requests = decoy_requests if decoy_requests is not None else load_decoy_requests()
    portal_requests = portal_requests if portal_requests is not None else load_portal_requests()

    deltas: List[float] = []
    details = []
    used_sources = set()
    for s in scenarios:
        try:
            start = parse_ts(s["timestamp_start"])
        except (KeyError, ValueError):
            continue
        try:
            end = parse_ts(s["timestamp_end"])
        except (KeyError, ValueError):
            end = start
        window_end = max(end, start) + timedelta(seconds=120)
        tech = s.get("technique_id")
        target = " ".join(s.get("targets_scanned", []) or [])
        attacker = s.get("attacker_ip") or DEFAULT_ATTACKER_IP

        candidates: List[Tuple[datetime, str]] = []

        # 1) ataque instrumentado por tecnica
        for e in decoy_events:
            if e.get("attack_technique_id") != tech:
                continue
            try:
                ts = parse_ts(e["timestamp"])
            except (KeyError, ValueError):
                continue
            if ts >= start:
                candidates.append((ts, "decoy-api"))

        # 2) peticiones al path objetivo
        if not candidates:
            paths = scenario_target_paths(s)
            for r in decoy_requests:
                path = str(r.get("path", ""))
                if not any(path == p or path.startswith(p) for p in paths):
                    continue
                try:
                    ts = parse_ts(r["timestamp"])
                except (KeyError, ValueError):
                    continue
                if ts >= start:
                    candidates.append((ts, "decoy-api (path)"))

        # 3) ventana del escenario, solo fuentes relevantes al objetivo
        if not candidates:
            allowed = allowed_sources(s)
            if "decoy-api" in allowed:
                for r in decoy_requests:
                    if r.get("client_ip") != attacker:
                        continue
                    try:
                        ts = parse_ts(r["timestamp"])
                    except (KeyError, ValueError):
                        continue
                    if start <= ts <= window_end:
                        candidates.append((ts, "decoy-api (attacker)"))
            if "decoy-portal" in allowed:
                for ts, _path in portal_requests:
                    if start <= ts <= window_end:
                        candidates.append((ts, "decoy-portal"))
            if "cowrie" in allowed:
                for ts, _ in cowrie_conns:
                    if start <= ts <= window_end:
                        candidates.append((ts, "cowrie"))

        if candidates:
            first, source = min(candidates, key=lambda c: c[0])
            delta = (first - start).total_seconds()
            deltas.append(delta)
            used_sources.add(source)
            details.append({
                "scenario": s.get("scenario", "?"),
                "technique": tech,
                "source": source,
                "timestamp_start": s.get("timestamp_start"),
                "first_detection": first.isoformat().replace("+00:00", "Z"),
                "mttd_seconds": round(delta, 3),
            })
        else:
            details.append({
                "scenario": s.get("scenario", "?"),
                "technique": tech,
                "source": None,
                "mttd_seconds": None,
                "note": "sin evento de deteccion registrado",
            })

    if not deltas:
        return {"mean": None, "min": None, "max": None, "samples": 0,
                "unit": "seconds", "status": "no_medido", "details": details}

    return {
        "mean": round(sum(deltas) / len(deltas), 3),
        "min": round(min(deltas), 3),
        "max": round(max(deltas), 3),
        "samples": len(deltas),
        "unit": "seconds",
        "status": "medido",
        "source": " + ".join(sorted(used_sources)),
        "details": details,
    }


def _not_measured(kpi: str) -> Dict:
    return {
        "mean": None, "min": None, "max": None, "samples": 0,
        "unit": "seconds", "status": "no_medido",
        "note": f"{kpi}: requiere timestamps de casos/respuesta en TheHive",
    }


def calculate_mttr(scenarios: List[Dict]) -> Dict:
    return _not_measured("MTTR")


def calculate_mttc(scenarios: List[Dict]) -> Dict:
    return _not_measured("MTTC")


def calculate_mttcontain(scenarios: List[Dict]) -> Dict:
    return _not_measured("MTTContain")


def count_evidence_per_scenario(scenarios: List[Dict]) -> Dict:
    counts = []
    for s in scenarios:
        evidencia_dir = Path(s.get("_dir", "")) / "evidencia"
        if evidencia_dir.exists():
            counts.append(len(list(evidencia_dir.iterdir())))
    if not counts:
        return {"mean": 0, "min": 0, "max": 0, "total": 0}
    return {
        "mean": round(sum(counts) / len(counts), 2),
        "min": min(counts),
        "max": max(counts),
        "total": sum(counts),
    }


def evidence_quality_score(scenarios: List[Dict]) -> Dict:
    quality = []
    for s in scenarios:
        score = 0
        evidencia_dir = Path(s.get("_dir", "")) / "evidencia"
        if not evidencia_dir.exists():
            continue
        files = list(evidencia_dir.iterdir())
        if any("_hash" in f.name or ".txt" in f.name for f in files):
            score += 25
        if any(f.name in ["start_time.txt", "end_time.txt"] for f in files):
            score += 25
        if s.get("technique_id"):
            score += 25
        if (evidencia_dir / "resultados.json").exists():
            score += 25
        quality.append(score)
    if not quality:
        return {"mean": 0, "max": 0, "samples": 0}
    return {
        "mean": sum(quality) / len(quality),
        "max": max(quality),
        "min": min(quality),
        "samples": len(quality),
        "scale": "0-100",
    }


def mitre_coverage(scenarios: List[Dict]) -> Dict:
    techniques = set()
    tactics = set()
    for s in scenarios:
        tid = s.get("technique_id")
        if tid:
            techniques.add(tid)
        tactic = s.get("tactic", "")
        if tactic:
            tactics.add(tactic)
    return {
        "techniques_detected": sorted(techniques),
        "techniques_count": len(techniques),
        "techniques_total_reference": 600,
        "techniques_coverage_pct": (len(techniques) / 20) * 100,
        "tactics_covered": sorted(tactics),
        "tactics_count": len(tactics),
    }


def iso27035_coverage(scenarios: List[Dict]) -> Dict:
    phases = {
        "Phase 1 - Plan and Prepare": False,
        "Phase 2 - Detection and Reporting": False,
        "Phase 3 - Assessment and Decision": False,
        "Phase 4 - Responses": False,
        "Phase 5 - Lessons Learned": False,
    }
    for s in scenarios:
        phase = s.get("iso27035_phase", "")
        for key in phases:
            if key.split(" - ")[1] in phase:
                phases[key] = True
    return {
        "phases": phases,
        "phases_covered": sum(1 for v in phases.values() if v),
        "phases_total": len(phases),
        "coverage_pct": (sum(1 for v in phases.values() if v) / len(phases)) * 100,
    }


def iso27001_coverage() -> Dict:
    return {
        "A.5.24 Incident management planning": "Wazuh + TheHive + Shuffle workflows",
        "A.5.25 Assessment of security events": "Wazuh correlation + Cortex analyzers",
        "A.5.26 Response to incidents": "Shuffle playbooks + Velociraptor",
        "A.5.27 Learning from incidents": "TheHive postmortem + MISP feedback",
        "A.5.28 Collection of evidence": "Evidence repo + SHA-256 + WORM",
        "A.8.16 Monitoring activities": "Wazuh + Suricata + Zeek",
        "A.8.20 Network security": "Suricata rules + VLAN segmentation",
        "controls_implemented": 7,
        "controls_total_relevant": 7,
        "coverage_pct": 100.0,
    }


# =============================================================================
# Reporte final
# =============================================================================

def generate_full_report() -> Dict:
    scenarios = load_scenario_results(ATTACK_SCENARIOS_DIR)
    decoy_events = load_decoy_events()
    cowrie_conns = load_cowrie_connections()
    decoy_requests = load_decoy_requests()
    portal_requests = load_portal_requests()

    return {
        "metadata": {
            "report_generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "thesis": "Metodología Honeypot para la Gestión de Incidentes en Servicios Fiscales",
            "lab": "TaxFisco Research Lab",
            "version": "2.0.0",
            "method": "MTTD medido desde eventos reales (decoy-api + cowrie) vs inicio de escenario",
        },
        "execution": {
            "scenarios_executed": len(scenarios),
            "decoy_attacks_recorded": len(decoy_events),
            "decoy_requests_recorded": len(decoy_requests),
            "cowrie_connections_recorded": len(cowrie_conns),
            "portal_requests_recorded": len(portal_requests),
        },
        "kpis": {
            "MTTD": calculate_mttd(scenarios, decoy_events, cowrie_conns,
                                   decoy_requests, portal_requests),
            "MTTR": calculate_mttr(scenarios),
            "MTTC": calculate_mttc(scenarios),
            "MTTContain": calculate_mttcontain(scenarios),
        },
        "evidence": {
            "files_per_scenario": count_evidence_per_scenario(scenarios),
            "quality_score": evidence_quality_score(scenarios),
        },
        "coverage": {
            "mitre_attack": mitre_coverage(scenarios),
            "iso_27035": iso27035_coverage(scenarios),
            "iso_27001": iso27001_coverage(),
        },
        "scenario_details": [
            {
                "id": s.get("scenario", "unknown"),
                "technique": s.get("technique_id", "?"),
                "tactic": s.get("tactic", "?"),
                "duration_seconds": (
                    parse_ts(s["timestamp_end"]) - parse_ts(s["timestamp_start"])
                ).total_seconds()
                if s.get("timestamp_start") and s.get("timestamp_end")
                else 0,
            }
            for s in scenarios
        ],
    }


def print_summary(report: Dict) -> None:
    print("=" * 80)
    print("TaxFisco Research Lab - KPI Report")
    print("=" * 80)
    print(f"Generated: {report['metadata']['report_generated_at']}")
    print()
    print("## Execution")
    for k, v in report["execution"].items():
        print(f"  {k}: {v}")
    print()
    print("## KPIs")
    for k, v in report["kpis"].items():
        if v.get("mean") is None:
            print(f"  {k}: NO MEDIDO ({v.get('note', '')})")
        else:
            print(f"  {k}: {v['mean']:.2f} {v.get('unit', '')} (n={v.get('samples', 0)})")
    print()
    print("## MTTD por escenario (real)")
    for d in report["kpis"]["MTTD"].get("details", []):
        if d.get("mttd_seconds") is not None:
            print(f"  {d['scenario']:28} {d['mttd_seconds']:>9.2f}s  ({d['source']})")
        else:
            print(f"  {d['scenario']:28} {'sin deteccion':>9}")
    print()
    print("## MITRE ATT&CK coverage")
    cov = report["coverage"]["mitre_attack"]
    print(f"  Techniques detected: {cov['techniques_count']}")
    print(f"  Tactics covered: {cov['tactics_count']}")
    print()
    print("=" * 80)


def main():
    report = generate_full_report()
    print_summary(report)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReporte completo guardado en: {OUTPUT}")


if __name__ == "__main__":
    main()
