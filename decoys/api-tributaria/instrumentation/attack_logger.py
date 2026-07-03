"""
Attack Logger with MITRE ATT&CK TTP Detection
==============================================

Motor de detección de Técnicas y Tácticas (TTPs) basado en heurísticas
sobre requests HTTP. Mapea patrones maliciosos a IDs ATT&CK oficiales.

Técnicas ATT&CK cubiertas:
  - T1190  Exploit Public-Facing Application
  - T1078   Valid Accounts
  - T1078.001 Default Accounts
  - T1110   Brute Force
  - T1110.001 Password Guessing
  - T1110.003 Password Spraying
  - T1110.004 Credential Stuffing
  - T1530   Data from Cloud Storage Object
  - T1213   Data from Information Repositories
  - T1087    Account Discovery
  - T1087.001 Local Account
  - T1087.002 Domain Account
  - T1069    Permission Groups Discovery
  - T1003    OS Credential Dumping
  - T1185    Browser Session Hijacking
  - T1056    Input Capture
  - T1056.001 Keylogging
  - T1071    Application Layer Protocol
  - T1071.001 Web Protocols
"""

import json
import re
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict

logger = logging.getLogger("attack-logger")


@dataclass
class AttackEvent:
    """Evento de ataque estructurado con metadatos ATT&CK."""
    timestamp: str
    source_ip: str
    user_agent: str
    method: str
    endpoint: str
    query: Dict[str, Any]
    body: str
    attack_technique_id: str
    attack_technique_name: str
    attack_tactic: str
    severity: str
    description: str
    tlp: str = "AMBER"


class AttackLogger:
    """Detecta y registra TTPs ATT&CK en requests HTTP."""

    # Patrones de payloads sospechosos
    SQL_INJECTION_PATTERNS = [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",
        r"\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))",
        r"((\%27)|(\'))union",
        r"union\s+select",
        r"select.*from",
        r"insert\s+into",
        r"drop\s+table",
        r"or\s+1=1",
        r"and\s+1=1",
        r"sleep\(",
        r"benchmark\(",
        r"pg_sleep",
        r"waitfor\s+delay",
        r"information_schema",
        r"load_file\(",
        r"into\s+outfile",
        r"concat\(",
        r"0x[0-9a-f]+",
    ]

    XSS_PATTERNS = [
        r"<script.*?>",
        r"javascript:",
        r"onerror\s*=",
        r"onload\s*=",
        r"onclick\s*=",
        r"<iframe",
        r"<svg.*?on",
        r"alert\s*\(",
        r"document\.cookie",
        r"document\.write",
        r"eval\s*\(",
        r"String\.fromCharCode",
    ]

    LFI_PATTERNS = [
        r"\.\./\.\./\.\./",
        r"\.\.\\\.\.\\\.\.\\",
        r"/etc/passwd",
        r"/etc/shadow",
        r"/etc/hosts",
        r"/proc/self",
        r"\\windows\\system32",
        r"win\.ini",
        r"boot\.ini",
    ]

    RCE_PATTERNS = [
        r";\s*ls\s",
        r";\s*cat\s",
        r";\s*whoami",
        r"\|\s*nc\s",
        r"\|\s*bash",
        r"\|\s*sh\s",
        r"\$\(.*\)",
        r"`.*`",
        r";\s*id\s",
        r";\s*uname",
        r";\s*wget",
        r";\s*curl",
    ]

    SSTI_PATTERNS = [
        r"\{\{.*\}\}",
        r"\{%.*%\}",
        r"\$\{.*\}",
    ]

    # Endpoints administrativos sensibles
    ADMIN_ENDPOINTS = [
        r"/admin",
        r"/api/v1/admin",
        r"/api/v1/users",
        r"/api/v1/config",
        r"/api/v1/internal",
        r"/api/v1/debug",
        r"/api/v1/backup",
        r"/api/v1/export",
        r"/actuator",
        r"/swagger",
        r"/.env",
        r"/.git",
        r"/wp-admin",
        r"/phpmyadmin",
    ]

    # User agents sospechosos
    SUSPICIOUS_USER_AGENTS = [
        "sqlmap",
        "nikto",
        "nmap",
        "masscan",
        "metasploit",
        "burp",
        "w3af",
        "acunetix",
        "nessus",
        "qualys",
        "nuclei",
        "dirbuster",
        "gobuster",
        "ffuf",
        "hydra",
    ]

    # Paths típicos de escaneo
    SCAN_PATTERNS = [
        r"\.php\?",
        r"\.asp\?",
        r"\.aspx\?",
        r"\.jsp\?",
        r"\.bak$",
        r"\.sql$",
        r"\.git/",
        r"\.svn/",
        r"\.env$",
        r"\.DS_Store",
        r"robots\.txt",
        r"sitemap\.xml",
        r"crossdomain\.xml",
        r"phpinfo\.php",
    ]

    def __init__(self, log_file: Path):
        self.log_file = log_file
        self.attack_count = 0
        # Compilar regex para performance
        self._compile_patterns()

    def _compile_patterns(self):
        self.sql_regex = [re.compile(p, re.IGNORECASE) for p in self.SQL_INJECTION_PATTERNS]
        self.xss_regex = [re.compile(p, re.IGNORECASE) for p in self.XSS_PATTERNS]
        self.lfi_regex = [re.compile(p, re.IGNORECASE) for p in self.LFI_PATTERNS]
        self.rce_regex = [re.compile(p, re.IGNORECASE) for p in self.RCE_PATTERNS]
        self.ssti_regex = [re.compile(p, re.IGNORECASE) for p in self.SSTI_PATTERNS]
        self.admin_regex = [re.compile(p, re.IGNORECASE) for p in self.ADMIN_ENDPOINTS]
        self.scan_regex = [re.compile(p, re.IGNORECASE) for p in self.SCAN_PATTERNS]

    def detect_ttp(self, request_info: Dict[str, Any]) -> Optional[Dict[str, str]]:
        """
        Analiza una request y retorna la TTP ATT&CK detectada (si alguna).
        """
        path = request_info.get("path", "")
        query = request_info.get("query", {})
        body = request_info.get("body", "")
        user_agent = request_info.get("user_agent", "").lower()
        method = request_info.get("method", "")
        client_ip = request_info.get("client_ip", "")

        # Combinar todo el input para análisis
        all_input = f"{path}?{json.dumps(query)} {body}"

        # 1) SQL Injection (T1190)
        for pattern in self.sql_regex:
            if pattern.search(all_input):
                return {
                    "technique_id": "T1190",
                    "technique_name": "Exploit Public-Facing Application",
                    "tactic": "Initial Access",
                    "severity": "HIGH",
                    "description": f"SQL injection pattern detected: {pattern.pattern}",
                }

        # 2) XSS (T1189 si viene de URL, T1059.007 si stored)
        for pattern in self.xss_regex:
            if pattern.search(all_input):
                return {
                    "technique_id": "T1059.007",
                    "technique_name": "JavaScript Execution",
                    "tactic": "Execution",
                    "severity": "MEDIUM",
                    "description": f"XSS payload detected: {pattern.pattern}",
                }

        # 3) LFI / Path Traversal (T1083)
        for pattern in self.lfi_regex:
            if pattern.search(all_input):
                return {
                    "technique_id": "T1083",
                    "technique_name": "File and Directory Discovery",
                    "tactic": "Discovery",
                    "severity": "HIGH",
                    "description": f"Path traversal / LFI pattern detected: {pattern.pattern}",
                }

        # 4) RCE / Command Injection (T1059)
        for pattern in self.rce_regex:
            if pattern.search(all_input):
                return {
                    "technique_id": "T1059",
                    "technique_name": "Command and Scripting Interpreter",
                    "tactic": "Execution",
                    "severity": "CRITICAL",
                    "description": f"OS command injection detected: {pattern.pattern}",
                }

        # 5) SSTI (T1059.006)
        for pattern in self.ssti_regex:
            if pattern.search(all_input):
                return {
                    "technique_id": "T1059.006",
                    "technique_name": "Python Execution",
                    "tactic": "Execution",
                    "severity": "HIGH",
                    "description": f"Server-side template injection: {pattern.pattern}",
                }

        # 6) Accesso a endpoints administrativos (T1078)
        for pattern in self.admin_regex:
            if pattern.search(path):
                return {
                    "technique_id": "T1078",
                    "technique_name": "Valid Accounts",
                    "tactic": "Persistence, Initial Access, Defense Evasion, Privilege Escalation",
                    "severity": "MEDIUM",
                    "description": f"Administrative endpoint access: {path}",
                }

        # 7) Reconocimiento / Scanning (T1595)
        for pattern in self.scan_regex:
            if pattern.search(path):
                return {
                    "technique_id": "T1595.002",
                    "technique_name": "Vulnerability Scanning",
                    "tactic": "Reconnaissance",
                    "severity": "MEDIUM",
                    "description": f"Scanning pattern detected: {pattern.pattern}",
                }

        # 8) User-Agent de herramientas de ataque (T1595.003)
        for sus_ua in self.SUSPICIOUS_USER_AGENTS:
            if sus_ua in user_agent:
                return {
                    "technique_id": "T1595.003",
                    "technique_name": "Wordlist Scanning",
                    "tactic": "Reconnaissance",
                    "severity": "MEDIUM",
                    "description": f"Attack tool User-Agent: {sus_ua}",
                }

        # 9) Credential Stuffing (múltiples logins fallidos)
        if path.endswith("/auth/login") and method == "POST":
            return {
                "technique_id": "T1110.004",
                "technique_name": "Credential Stuffing",
                "tactic": "Credential Access",
                "severity": "HIGH",
                "description": "Login attempt detected (monitor for stuffing patterns)",
            }

        return None

    def log_attack(self, event: AttackEvent) -> None:
        """Registra un evento de ataque en el log."""
        self.attack_count += 1

        with open(self.log_file, "a") as f:
            f.write(json.dumps(asdict(event)) + "\n")

        logger.info(
            f"ATTACK #{self.attack_count}: {event.attack_technique_id} "
            f"({event.attack_tactic}) from {event.source_ip}"
        )

    def get_attack_stats(self) -> Dict[str, int]:
        """Retorna estadísticas agregadas de ataques detectados."""
        stats = {
            "total": 0,
            "by_tactic": {},
            "by_technique": {},
            "by_severity": {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0},
        }
        if not self.log_file.exists():
            return stats
        with open(self.log_file) as f:
            for line in f:
                try:
                    event = json.loads(line)
                    stats["total"] += 1
                    tid = event.get("attack_technique_id", "unknown")
                    tac = event.get("attack_tactic", "unknown")
                    sev = event.get("severity", "LOW")
                    stats["by_technique"][tid] = stats["by_technique"].get(tid, 0) + 1
                    stats["by_tactic"][tac] = stats["by_tactic"].get(tac, 0) + 1
                    stats["by_severity"][sev] = stats["by_severity"].get(sev, 0) + 1
                except json.JSONDecodeError:
                    continue
        return stats
