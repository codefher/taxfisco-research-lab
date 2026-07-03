"""Contribuyente app"""
from django.apps import AppConfig


class ContribuyenteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portal.contribuyente"
    label = "contribuyente_app"
