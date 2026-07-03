"""URLs facturación"""
from django.urls import path
from . import views

app_name = "facturacion"

urlpatterns = [
    path("", views.index, name="index"),
    path("detalle/<str:cuf>/", views.factura_view, name="detalle"),
]
