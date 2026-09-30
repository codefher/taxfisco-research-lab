"""
Vistas del módulo de contribuyentes.
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import re


def index(request):
    return HttpResponse("Listado de contribuyentes")


def buscar(request):
    """
    *** ENDPOINT VULNERABLE A SQLi ***
    Construye SQL concatenando input del usuario sin parametrizar.
    La petición se registra internamente para detección de incidentes.
    """
    nit = request.GET.get("nit", "")

    # ========================================================================
    # *** VULNERABILIDAD INTENCIONAL - SOLO PARA INVESTIGACIÓN ACADÉMICA ***
    # NO REPLICAR EN PRODUCCIÓN
    # ========================================================================
    fake_query = f"SELECT * FROM contribuyentes WHERE nit = '{nit}' LIMIT 1"
    # ========================================================================

    if re.search(r"(\%27)|(')|or\s+1=1|union\s+select", fake_query, re.IGNORECASE):
        return JsonResponse(
            {
                "results": [],
                "total": 0,
            }
        )

    return JsonResponse(
        {
            "results": [
                {
                    "nit": nit,
                    "razon_social": "CONTRIBUYENTE EJEMPLO S.R.L.",
                    "estado": "Activo",
                }
            ],
            "total": 1,
        }
    )


def detalle(request, nit):
    return JsonResponse(
        {
            "nit": nit,
            "razon_social": "CONTRIBUYENTE EJEMPLO S.R.L.",
            "tipo": "Persona Jurídica",
            "estado": "Activo",
            "domicilio": "La Paz",
            "fecha_inscripcion": "14/03/2011",
        }
    )
