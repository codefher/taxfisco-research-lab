"""
MITRE ATT&CK Coverage Analysis
================================

Genera el reporte de cobertura ATT&CK a partir de los resultados
de los escenarios de ataque ejecutados.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict


# ATT&CK Enterprise v15+ Tactics reference
ATTACK_TACTICS = [
    "Reconnaissance",
    "Resource Development",
    "Initial Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Defense Evasion",
    "Credential Access",
    "Discovery",
    "Lateral Movement",
    "Collection",
    "Command and Control",
    "Exfiltration",
    "Impact",
]

# Técnicas implementadas en la tesis
IMPLEMENTED_TECHNIQUES = [
    "T1595",   # Active Scanning
    "T1595.002",  # Vulnerability Scanning
    "T1595.003",  # Wordlist Scanning
    "T1190",   # Exploit Public-Facing Application
    "T1110.001",  # Password Guessing
    "T1110.004",  # Credential Stuffing
    "T1078",   # Valid Accounts
    "T1078.001",  # Default Accounts
    "T1213",   # Data from Information Repositories
    "T1530",   # Data from Cloud Storage Object
    "T1083",   # File and Directory Discovery
    "T1059",   # Command and Scripting Interpreter
    "T1059.004",  # Unix Shell
    "T1059.006",  # Python
    "T1059.007",  # JavaScript
    "T1105",   # Ingress Tool Transfer
    "T1048.003",  # Exfiltration Over Unencrypted Non-C2 Protocol
]


def analyze_coverage(scenarios_dir: Path) -> dict:
    """Analiza la cobertura ATT&CK de los escenarios ejecutados."""
    scenarios = []
    for scenario_dir in sorted(scenarios_dir.iterdir()):
        result_file = scenario_dir / "evidencia" / "resultados.json"
        if result_file.exists():
            with open(result_file) as f:
                scenarios.append(json.load(f))

    # Mapear técnicas y tácticas detectadas
    techniques_detected = set()
    tactics_detected = set()
    technique_to_scenarios = defaultdict(list)
    tactic_to_techniques = defaultdict(set)

    for s in scenarios:
        tid = s.get("technique_id")
        tac = s.get("tactic", "")
        if tid:
            techniques_detected.add(tid)
            technique_to_scenarios[tid].append(s.get("scenario", "unknown"))
        if tac:
            tactics_detected.add(tac)
            if tid:
                tactic_to_techniques[tac].add(tid)

    # Detección de sub-técnicas (TXXXX.YYY)
    main_techniques = set()
    for t in techniques_detected:
        if "." in t:
            main_techniques.add(t.split(".")[0])
        else:
            main_techniques.add(t)

    return {
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "framework": "MITRE ATT&CK Enterprise v15",
            "scenarios_analyzed": len(scenarios),
        },
        "coverage": {
            "techniques_implemented": sorted(IMPLEMENTED_TECHNIQUES),
            "techniques_implemented_count": len(IMPLEMENTED_TECHNIQUES),
            "techniques_detected": sorted(techniques_detected),
            "techniques_detected_count": len(techniques_detected),
            "techniques_main_count": len(main_techniques),
            "tactics_implemented": sorted(set(t for t in ATTACK_TACTICS if t in ["Reconnaissance", "Initial Access", "Execution", "Discovery", "Credential Access", "Collection", "Command and Control", "Exfiltration"])),
            "tactics_detected": sorted(tactics_detected),
            "tactics_detected_count": len(tactics_detected),
            "tactics_total_reference": len(ATTACK_TACTICS),
            "techniques_implemented_coverage_pct": (len(techniques_detected) / len(IMPLEMENTED_TECHNIQUES)) * 100,
            "tactics_implemented_coverage_pct": (len(tactics_detected) / len(ATTACK_TACTICS)) * 100,
        },
        "matrix": {
            tactic: sorted(list(techs))
            for tactic, techs in tactic_to_techniques.items()
        },
        "technique_to_scenarios": {
            t: sorted(scenarios) for t, scenarios in technique_to_scenarios.items()
        },
        "gap_analysis": {
            "implemented_but_not_detected": sorted(set(IMPLEMENTED_TECHNIQUES) - techniques_detected),
            "tactics_not_covered": sorted(set(ATTACK_TACTICS) - tactics_detected),
        },
    }


def print_matrix(report: dict) -> None:
    """Imprime la matriz ATT&CK con las técnicas cubiertas."""
    print("\n" + "=" * 100)
    print("MITRE ATT&CK Coverage Matrix")
    print("=" * 100)
    print(f"\nImplemented: {report['coverage']['techniques_implemented_count']} techniques")
    print(f"Detected:    {report['coverage']['techniques_detected_count']} techniques")
    print(f"Coverage:    {report['coverage']['techniques_implemented_coverage_pct']:.1f}%\n")

    print(f"{'Tactic':<30} {'Techniques':<10} {'Details'}")
    print("-" * 100)
    for tactic in ATTACK_TACTICS:
        techs = report["matrix"].get(tactic, [])
        if techs:
            print(f"{tactic:<30} {len(techs):<10} {', '.join(techs)}")
        else:
            print(f"{tactic:<30} {0:<10} (not covered)")

    print("\n" + "=" * 100)
    print("Gap Analysis - Tactics NOT covered:")
    for t in report["gap_analysis"]["tactics_not_covered"]:
        print(f"  - {t}")
    print("=" * 100)


def main():
    scenarios_dir = Path("/root/attack-scenarios")
    report = analyze_coverage(scenarios_dir)
    print_matrix(report)
    output = Path("/root/analysis/mitre_coverage.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReporte guardado en: {output}")


if __name__ == "__main__":
    main()
