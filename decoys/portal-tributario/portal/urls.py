"""
URL Configuration for Decoy Portal Tributario
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "healthy", "service": "taxfisco-decoy-portal"})


def root(request):
    return JsonResponse(
        {
            "service": "TaxFisco Decoy Portal Tributario",
            "version": "1.0.0",
            "description": "Decoy portal for honeypot research - intentionally vulnerable",
            "endpoints": [
                "/contribuyentes/",
                "/declaraciones/",
                "/facturacion/",
                "/admin/",
                "/vuln/",
            ],
        }
    )


urlpatterns = [
    path("", root, name="root"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("contribuyentes/", include("portal.contribuyente.urls")),
    path("declaraciones/", include("portal.declaraciones.urls")),
    path("facturacion/", include("portal.facturacion.urls")),
    path("vuln/", include("portal.vuln_intencional.urls")),
]
