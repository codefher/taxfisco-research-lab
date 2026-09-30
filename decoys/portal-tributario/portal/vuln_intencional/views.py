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
    return JsonResponse({"vulnerabilities": vulns, "service": "sin-portal"})


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
                    "authenticated": True,
                    "user": "administrador",
                    "role": "admin",
                    "session_token": "8f2a1c94e7b3d065f1a8c2b4e9d7f035",
                    "expires_in": 3600,
                }
            )

        return JsonResponse(
            {
                "authenticated": False,
                "error": "Credenciales inválidas",
            }
        )

    return HttpResponse(
        "<form method='POST'>"
        "<input name='username' placeholder='NIT o usuario'>"
        "<input name='password' type='password' placeholder='Contraseña'>"
        "<button>Continuar</button>"
        "</form>"
    )


def xss(request):
    """
    T1059.007 - XSS Reflected
    ==========================
    Refleja el input del usuario sin escape.
    """
    name = request.GET.get("name", "Contributor")
    return HttpResponse(
        f"<html><body><h1>Hola, {name}!</h1>"
        f"<p>Bienvenido al portal de contribuyentes.</p>"
        f"</body></html>"
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
                "requested_file": real_path,
                "content": "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin",
            }
        )

    return HttpResponse(real_path, content_type="text/plain")


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
                "username": "administrador",
                "role": "admin",
                "permissions": ["read", "write", "delete", "export"],
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.K1QyZjc0",
            }
        )
    return JsonResponse(
        {
            "username": "contribuyente",
            "role": role,
            "permissions": ["read"],
        }
    )


def data_export(request):
    """
    T1530 - Mass Data Export
    =========================
    Endpoint que simula exportar todos los contribuyentes.
    """
    return JsonResponse(
        {
            "total_records": 1_247_893,
            "generated_at": "2024-12-15 08:42:11",
            "records": [
                {
                    "nit": f"1000000{i}",
                    "razon_social": f"EMPRESA COMERCIAL {i} S.A.",
                    "estado": "Activo",
                    "domicilio": "La Paz",
                }
                for i in range(1, 21)
            ],
        }
    )


def cmd_injection(request):
    """
    T1059 - Command Injection
    ==========================
    Endpoint vulnerable a command injection (simulado).
    """
    host = request.GET.get("host", "localhost")
    return HttpResponse(
        f"PING {host} (127.0.0.1): 56 data bytes\n"
        f"64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.042 ms\n"
        f"64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.038 ms\n\n"
        f"--- {host} ping statistics ---\n"
        f"2 packets transmitted, 2 received, 0% packet loss",
        content_type="text/plain",
    )
