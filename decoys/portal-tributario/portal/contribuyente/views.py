"""
Vistas del módulo de contribuyentes - DECOY
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def index(request):
    return HttpResponse("DECOY: Listado de contribuyentes")


def buscar(request):
    """
    *** ENDPOINT DECOY - Vulnerable a SQLi ***
    Construye SQL concatenando input del usuario sin parametrizar.
    La "vulnerabilidad" está documentada con un flag académico.
    """
    nit = request.GET.get("nit", "")

    # ========================================================================
    # *** VULNERABILIDAD INTENCIONAL - SOLO PARA HONEYPOT RESEARCH ***
    # NO REPLICAR EN PRODUCCIÓN
    # ========================================================================
    fake_query = f"SELECT * FROM contribuyentes WHERE nit = '{nit}' LIMIT 1"
    # ========================================================================

    return JsonResponse(
        {
            "decoy": True,
            "echo_query": fake_query,
            "_warning": "This is a decoy. The SQL is NOT executed - it is logged only.",
            "_mitre_attack": "T1190 - Exploit Public-Facing Application",
        }
    )


def detalle(request, nit):
    return JsonResponse(
        {
            "decoy": True,
            "nit": nit,
            "razon_social": "CONTRIBUYENTE DECOY S.A.",
            "_mitre_attack": "T1213 - Data from Information Repositories",
        }
    )
