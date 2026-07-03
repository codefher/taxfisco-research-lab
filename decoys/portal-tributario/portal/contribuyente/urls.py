"""
URLs del módulo de contribuyentes
"""
from django.urls import path
from . import views

app_name = "contribuyente"

urlpatterns = [
    path("", views.index, name="index"),
    path("buscar/", views.buscar, name="buscar"),
    path("detalle/<str:nit>/", views.detalle, name="detalle"),
]
