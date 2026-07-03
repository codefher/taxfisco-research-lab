"""Facturación app"""
from django.apps import AppConfig


class FacturacionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portal.facturacion"
    label = "facturacion_app"
