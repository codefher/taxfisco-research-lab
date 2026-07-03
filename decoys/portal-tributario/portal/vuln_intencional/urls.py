"""URLs vuln intencional"""
from django.urls import path
from . import views

app_name = "vuln"

urlpatterns = [
    path("", views.index, name="index"),
    path("sqli-login/", views.sqli_login, name="sqli_login"),
    path("xss/", views.xss, name="xss"),
    path("lfi/", views.lfi, name="lfi"),
    path("priv-esc/", views.priv_esc, name="priv_esc"),
    path("data-export/", views.data_export, name="data_export"),
    path("cmd-injection/", views.cmd_injection, name="cmd_injection"),
]
