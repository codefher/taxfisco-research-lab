"""
Módulo de Vulnerabilidades Intencionales
==========================================

Cada endpoint aquí es INTENCIONALMENTE vulnerable con fines de honeypot research.
NO USAR EN PRODUCCIÓN. Cada función documenta la TTP ATT&CK que atrae.

Vulnerabilidades implementadas:
  - T1190 SQL Injection (login bypass)
  - T1059.007 XSS reflected
  - T1083 LFI / Path Traversal
  - T1078 Privilege Escalation (admin access)
  - T1530 Data Export
"""

import os
import json
import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    """Índice de vulnerabilidades disponibles (educativo)."""
    vulns = [
        {"id": "T1190", "name": "SQL Injection Login Bypass", "endpoint": "/vuln/sqli-login/"},
        {"id": "T1059.007", "name": "XSS Reflected", "endpoint": "/vuln/xss/"},
        {"id": "T1083", "name": "LFI / Path Traversal", "endpoint": "/vuln/lfi/"},
        {"id": "T1078", "name": "Privilege Escalation via Cookie", "endpoint": "/vuln/priv-esc/"},
        {"id": "T1530", "name": "Mass Data Export", "endpoint": "/vuln/data-export/"},
        {"id": "T1059", "name": "Command Injection (Ping)", "endpoint": "/vuln/cmd-injection/"},
    ]
    return JsonResponse({"vulnerabilities": vulns, "_warning": "All endpoints are DECOY"})


def sqli_login(request):
    """
    T1190 - SQL Injection login bypass
    ====================================
    Endpoint vulnerable a bypass de autenticación via SQLi.
    """
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # ====================================================================
        # *** VULNERABILIDAD INTENCIONAL - NO REPLICAR ***
        # SQL concatenado sin parametrizar (T1190)
        # ====================================================================
        fake_query = f"SELECT * FROM usuarios WHERE user='{username}' AND pass='{password}'"
        # Simular bypass si contiene OR 1=1
        if "or 1=1" in fake_query.lower() or "' or '" in fake_query.lower():
            return JsonResponse(
                {
                    "decoy": True,
                    "auth_bypassed": True,
                    "admin": True,
                    "fake_session": "ADMIN_DECOY_SESSION_TOKEN",
                    "_mitre_attack": "T1190 - SQL Injection",
                    "_warning": "This is a decoy. Real auth uses parameterized queries.",
                }
            )

        return JsonResponse(
            {
                "decoy": True,
                "auth_bypassed": False,
                "echo_query": fake_query,
                "_mitre_attack": "T1190 - SQL Injection attempt",
            }
        )

    return HttpResponse(
        "<form method='POST'>"
        "<input name='username' placeholder='user'>"
        "<input name='password' type='password' placeholder='pass'>"
        "<button>Login</button>"
        "</form>"
    )


def xss(request):
    """
    T1059.007 - XSS Reflected
    ==========================
    Refleja el input del usuario sin escape.
    """
    name = request.GET.get("name", "World")
    return HttpResponse(
        f"<html><body><h1>Hola, {name}!</h1>"
        f"<p>Esta página refleja input sin escape. Intencional.</p>"
        f"<hr><em>Decoy - T1059.007</em></body></html>"
    )


def lfi(request):
    """
    T1083 - LFI / Path Traversal
    =============================
    Permite leer archivos del sistema.
    """
    file = request.GET.get("file", "/etc/passwd")

    # ====================================================================
    # *** VULNERABILIDAD INTENCIONAL ***
    # ====================================================================
    real_path = file  # Sin sanitización

    if real_path.startswith("/etc/") or ".." in real_path:
        return JsonResponse(
            {
                "decoy": True,
                "requested_file": real_path,
                "_mitre_attack": "T1083 - File and Directory Discovery",
                "_warning": "This is a decoy. Real LFI is blocked by WAF.",
                "fake_content": "root:x:0:0:root:/root:/bin/bash (FAKE - DECOY)",
            }
        )

    return JsonResponse(
        {
            "decoy": True,
            "requested_file": real_path,
            "_mitre_attack": "T1083 - Path traversal attempt",
        }
    )


def priv_esc(request):
    """
    T1078 - Privilege Escalation via Cookie
    ========================================
    Cambia el rol de usuario si se setea una cookie específica.
    """
    role = request.COOKIES.get("role", "user")
    if role == "admin":
        return JsonResponse(
            {
                "decoy": True,
                "role": "admin",
                "permissions": ["read", "write", "delete", "export"],
                "fake_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.DECOY",
                "_mitre_attack": "T1078 - Valid Accounts",
                "_warning": "Cookie 'role=admin' was set. Access logged.",
            }
        )
    return JsonResponse({"decoy": True, "role": role})


def data_export(request):
    """
    T1530 - Mass Data Export
    =========================
    Endpoint que simula exportar todos los contribuyentes.
    """
    return JsonResponse(
        {
            "decoy": True,
            "total_records": 1_247_893,
            "sample": [
                {"nit": f"1000000{i}", "razon_social": f"EMPRESA {i} S.A. (DECOY)"}
                for i in range(1, 21)
            ],
            "_mitre_attack": "T1530 - Data from Cloud Storage Object",
            "_warning": "Access to this endpoint is logged for honeypot research.",
        }
    )


def cmd_injection(request):
    """
    T1059 - Command Injection
    ==========================
    Endpoint vulnerable a command injection (simulado).
    """
    host = request.GET.get("host", "localhost")
    return JsonResponse(
        {
            "decoy": True,
            "host_requested": host,
            "_mitre_attack": "T1059 - Command and Scripting Interpreter",
            "_warning": "Command injection attempt detected and logged.",
            "fake_output": f"PING {host} (DECOY): 56 data bytes\\n--- DECOY OUTPUT ---",
        }
    )
