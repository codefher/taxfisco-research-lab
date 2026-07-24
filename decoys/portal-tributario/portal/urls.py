"""
URL Configuration for Decoy Portal Tributario

Separa:
  - Rutas públicas del contribuyente (NIT, login, dashboard)
  - Rutas admin (Django admin)
  - Rutas de submódulos (contribuyente, declaraciones, facturacion, vuln)
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from portal import public_views


def health(request):
    return JsonResponse({"status": "healthy", "service": "taxfisco-decoy-portal"})


def root(request):
    return JsonResponse(
        {
            "service": "TaxFisco Decoy Portal Tributario",
            "version": "2.0.0",
            "description": "Decoy portal for honeypot research - intentionally vulnerable",
            "endpoints": [
                "/ (landing)",
                "/login/",
                "/registro/",
                "/dashboard/",
                "/consulta-nit/",
                "/declaraciones/",
                "/facturacion/",
                "/admin/",
                "/vuln/",
            ],
        }
    )


urlpatterns = [
    path("", public_views.home, name="public_home"),
    path("health/", health, name="health"),
    path("login/", public_views.login_public, name="public_login"),
    path("registro/", public_views.register, name="public_register"),
    path("logout/", public_views.logout_public, name="public_logout"),
    path("dashboard/", public_views.dashboard, name="public_dashboard"),
    path("consulta-nit/", public_views.consulta_nit, name="public_consulta_nit"),
    path("facturacion/", public_views.facturacion_lista, name="public_facturacion"),
    path("declaraciones/", include("portal.declaraciones.urls")),
    path("admin/", admin.site.urls),
    path("contribuyentes/", include("portal.contribuyente.urls")),
    path("vuln/", include("portal.vuln_intencional.urls")),
]
