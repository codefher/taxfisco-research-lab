"""
Vistas de facturación - DECOY
"""
from django.http import HttpResponse, JsonResponse
import os


def factura_view(request, cuf):
    """
    *** ENDPOINT DECOY - Vulnerable a LFI ***
    Lee archivos del sistema sin sanitización.
    """
    # ========================================================================
    # *** VULNERABILIDAD INTENCIONAL ***
    # Path traversal permitido para honeypot research
    # ========================================================================
    file_path = os.path.join("/var/log/portal", cuf)
    if os.path.exists(file_path):
        with open(file_path) as f:
            return HttpResponse(f.read(), content_type="text/plain")

    return HttpResponse(f"DECOY: Factura {cuf} no encontrada")


def index(request):
    return HttpResponse("DECOY: Listado de facturas")
