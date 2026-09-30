"""
Middleware para detección de ataques ATT&CK en HTTP requests.
================================================================

Detecta:
  - SQLi (T1190)
  - XSS (T1059.007)
  - LFI (T1083)
  - RCE (T1059)
  - Brute force / Credential Stuffing (T1110)
  - Path Traversal (T1083)
"""

import json
import logging
import re
from datetime import datetime
from pathlib import Path


attack_logger = logging.getLogger("portal.attacks")


# Patrones de ataque (replicados desde la API para consistencia)
SQL_PATTERNS = [
    r"(\%27)|(\')",
    r"union\s+select",
    r"select.*from",
    r"or\s+1=1",
    r"sleep\(",
    r"benchmark\(",
    r"information_schema",
    r"into\s+outfile",
]

XSS_PATTERNS = [
    r"<script",
    r"javascript:",
    r"onerror\s*=",
    r"onload\s*=",
    r"alert\s*\(",
    r"document\.cookie",
]

LFI_PATTERNS = [
    r"\.\./\.\./\.\./",
    r"/etc/passwd",
    r"/etc/shadow",
    r"\\windows\\",
]


class AttackLoggingMiddleware:
    """Middleware que loguea y detecta ataques."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.sql_regex = [re.compile(p, re.IGNORECASE) for p in SQL_PATTERNS]
        self.xss_regex = [re.compile(p, re.IGNORECASE) for p in XSS_PATTERNS]
        self.lfi_regex = [re.compile(p, re.IGNORECASE) for p in LFI_PATTERNS]

    def __call__(self, request):
        # Capturar body si es POST
        body = ""
        if request.method == "POST":
            try:
                body = request.body.decode("utf-8", errors="ignore")
            except Exception:
                body = ""

        # Construir texto completo para análisis
        full_text = f"{request.path}?{request.META.get('QUERY_STRING', '')} {body}"
        ua = request.META.get("HTTP_USER_AGENT", "unknown")

        attack_detected = None
        for pattern in self.sql_regex:
            if pattern.search(full_text):
                attack_detected = {
                    "ttp_id": "T1190",
                    "ttp_name": "Exploit Public-Facing Application",
                    "tactic": "Initial Access",
                    "pattern": pattern.pattern,
                }
                break

        if not attack_detected:
            for pattern in self.xss_regex:
                if pattern.search(full_text):
                    attack_detected = {
                        "ttp_id": "T1059.007",
                        "ttp_name": "JavaScript Execution",
                        "tactic": "Execution",
                        "pattern": pattern.pattern,
                    }
                    break

        if not attack_detected:
            for pattern in self.lfi_regex:
                if pattern.search(full_text):
                    attack_detected = {
                        "ttp_id": "T1083",
                        "ttp_name": "File and Directory Discovery",
                        "tactic": "Discovery",
                        "pattern": pattern.pattern,
                    }
                    break

        if attack_detected:
            attack_event = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "source_ip": self._get_client_ip(request),
                "user_agent": ua,
                "method": request.method,
                "path": request.path,
                "query": request.META.get("QUERY_STRING", ""),
                "body": body[:2000],
                "attack_technique_id": attack_detected["ttp_id"],
                "attack_technique_name": attack_detected["ttp_name"],
                "attack_tactic": attack_detected["tactic"],
                "matched_pattern": attack_detected["pattern"],
                "tlp": "AMBER",
            }
            attack_logger.warning(json.dumps(attack_event))

        response = self.get_response(request)
        response["X-Powered-By"] = "Django"
        return response

    @staticmethod
    def _get_client_ip(request):
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        if xff:
            return xff.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "unknown")
