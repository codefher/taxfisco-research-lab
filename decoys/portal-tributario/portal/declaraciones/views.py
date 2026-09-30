"""
Vistas del módulo de declaraciones juradas.
"""

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Listado de declaraciones juradas")


def nueva(request):
    """
    *** ENDPOINT VULNERABLE A XSS STORED ***
    El input del usuario se refleja sin escape en la respuesta.
    """
    if request.method == "POST":
        descripcion = request.POST.get("descripcion", "")
        # ====================================================================
        # *** VULNERABILIDAD INTENCIONAL ***
        # XSS stored - reflejamos sin escape. La petición se registra
        # internamente para detección de incidentes.
        # ====================================================================
        return HttpResponse(
            f"<html><body><h1>DECLARACIÓN REGISTRADA</h1>"
            f"<p>Su declaración: {descripcion}</p>"  # NO ESCAPE - INTENCIONAL
            f"<p>Código de recepción: DJ-2024-000184</p>"
            f"</body></html>"
        )

    return render(request, "declaraciones/nueva.html")


def detalle(request, id_declaracion):
    return JsonResponse(
        {
            "id_declaracion": id_declaracion,
            "periodo": "Noviembre 2024",
            "tipo": "IVA",
            "estado": "PROCESADA",
            "monto": 12345.67,
            "fecha_presentacion": "15/11/2024",
        }
    )
