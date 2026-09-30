"""
Vistas de facturación.
"""
from django.http import HttpResponse, JsonResponse
import os


def factura_view(request, cuf):
    """
    *** ENDPOINT VULNERABLE A LFI ***
    Lee archivos del sistema sin sanitización.
    """
    # ========================================================================
    # *** VULNERABILIDAD INTENCIONAL ***
    # Path traversal permitido. La petición se registra internamente
    # para detección de incidentes.
    # ========================================================================
    file_path = os.path.join("/var/log/portal", cuf)
    if os.path.exists(file_path):
        with open(file_path) as f:
            return HttpResponse(f.read(), content_type="text/plain")

    return HttpResponse(f"Factura {cuf} no encontrada")


def index(request):
    return HttpResponse("Listado de facturas")
