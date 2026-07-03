"""
Vistas del módulo de declaraciones juradas - DECOY
"""

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("DECOY: Listado de declaraciones juradas")


def nueva(request):
    """
    *** ENDPOINT DECOY - Vulnerable a XSS stored ***
    El input del usuario se refleja sin escape en la respuesta.
    """
    if request.method == "POST":
        descripcion = request.POST.get("descripcion", "")
        # ====================================================================
        # *** VULNERABILIDAD INTENCIONAL ***
        # XSS stored - reflejamos sin escape. Marcado para honeypot.
        # ====================================================================
        return HttpResponse(
            f"<html><body><h1>DECLARACIÓN REGISTRADA</h1>"
            f"<p>Su declaración: {descripcion}</p>"  # NO ESCAPE - INTENCIONAL
            f"<hr><em>Decoy - honeypot</em></body></html>"
        )

    return render(request, "declaraciones/nueva.html")


def detalle(request, id_declaracion):
    return JsonResponse(
        {
            "decoy": True,
            "id_declaracion": id_declaracion,
            "estado": "PROCESADA",
            "monto": 12345.67,
        }
    )
