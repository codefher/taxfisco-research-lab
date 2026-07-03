"""URLs declaraciones"""
from django.urls import path
from . import views

app_name = "declaraciones"

urlpatterns = [
    path("", views.index, name="index"),
    path("nueva/", views.nueva, name="nueva"),
    path("detalle/<str:id_declaracion>/", views.detalle, name="detalle"),
]
