"""
Vistas públicas del Decoy Portal Tributario.

Páginas orientadas al contribuyente (NIT):
  - home            : landing principal
  - login_public    : login del contribuyente (separado del admin Django)
  - register        : registro de nuevo contribuyente
  - logout_public   : cierra sesión
  - dashboard       : panel del contribuyente autenticado
  - consulta_nit    : búsqueda de NIT (honeypot principal)

Todas las vistas pasan show_decoy_banner=True (excepto login/register)
para que la UI muestre el aviso de honeypot — útil para la investigación
académica.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django import forms
from django.db import models
import re


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "txf-input",
            "placeholder": "Ej: 12345678 o usuario@ejemplo.bo",
            "autocomplete": "username",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "txf-input",
            "placeholder": "••••••••",
            "autocomplete": "current-password",
        })
    )


class RegisterForm(forms.Form):
    nit = forms.CharField(
        min_length=7, max_length=12,
        widget=forms.TextInput(attrs={"class": "txf-input", "placeholder": "12345678"})
    )
    razon_social = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "txf-input", "placeholder": "Mi Empresa S.R.L."})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "txf-input", "placeholder": "tu@empresa.bo"})
    )
    password1 = forms.CharField(
        min_length=10,
        widget=forms.PasswordInput(attrs={"class": "txf-input"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "txf-input"})
    )

    def clean_nit(self):
        nit = self.cleaned_data["nit"]
        if not re.match(r"^\d{7,12}$", nit):
            raise forms.ValidationError("El NIT debe tener entre 7 y 12 dígitos.")
        return nit

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if p1 and not re.search(r"[A-Z]", p1):
            raise forms.ValidationError("La contraseña debe incluir al menos una mayúscula.")
        if p1 and not re.search(r"\d", p1):
            raise forms.ValidationError("La contraseña debe incluir al menos un número.")
        return cleaned


# -----------------------------------------------------------------------------
# Vistas públicas
# -----------------------------------------------------------------------------

def home(request):
    return render(request, "home.html", {"show_decoy_banner": True})


def login_public(request):
    if request.user.is_authenticated:
        return redirect("public_dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("public_dashboard")
            messages.error(request, "NIT/correo o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def register(request):
    if request.user.is_authenticated:
        return redirect("public_dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            nit = form.cleaned_data["nit"]
            razon_social = form.cleaned_data["razon_social"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            if User.objects.filter(username=nit).exists():
                messages.error(request, f"Ya existe una cuenta con el NIT {nit}.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, f"Ya existe una cuenta con el email {email}.")
            else:
                user = User.objects.create_user(
                    username=nit, email=email, password=password,
                    first_name=razon_social[:30]
                )
                messages.success(request, f"Cuenta creada exitosamente. Bienvenido, {razon_social}.")
                login(request, user)
                return redirect("public_dashboard")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def logout_public(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("public_home")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("public_login")

    declaraciones_demo = [
        {"periodo": "Nov 2024", "tipo": "IVA", "monto": "Bs. 4.500", "estado": "Presentada", "estado_class": "success", "fecha": "15/11/2024"},
        {"periodo": "Oct 2024", "tipo": "IVA", "monto": "Bs. 4.320", "estado": "Presentada", "estado_class": "success", "fecha": "12/10/2024"},
        {"periodo": "Sep 2024", "tipo": "IT", "monto": "Bs. 1.200", "estado": "Observada", "estado_class": "warning", "fecha": "10/10/2024"},
        {"periodo": "Ago 2024", "tipo": "IVA", "monto": "Bs. 3.980", "estado": "Presentada", "estado_class": "success", "fecha": "14/09/2024"},
    ]

    user_nit = request.user.username
    return render(request, "dashboard.html", {
        "user_nit": user_nit,
        "ultimas_declaraciones": declaraciones_demo,
        "show_decoy_banner": True,
    })


def consulta_nit(request):
    nit_query = request.GET.get("nit", "").strip()
    resultado = None
    error = None

    if nit_query:
        if not re.match(r"^\d{7,12}$", nit_query):
            error = "El NIT debe tener entre 7 y 12 dígitos numéricos."
        else:
            estados = ["success", "warning", "danger"]
            import hashlib
            h = int(hashlib.md5(nit_query.encode()).hexdigest(), 16)
            nit_display = f"{int(nit_query):,}".replace(",", ".")
            resultado = {
                "nit": nit_display,
                "razon_social": f"CONTRIBUYENTE {nit_query[:4]}{nit_query[-2:]} S.R.L.",
                "tipo": ["Persona Natural", "Persona Jurídica", "Unipersonal"][h % 3],
                "actividad": ["Comercio minorista", "Servicios profesionales", "Industria manufacturera", "Construcción"][h % 4],
                "domicilio": ["La Paz", "Santa Cruz", "Cochabamba", "Tarija"][h % 4] + f", Zona {h % 20}",
                "fecha_inscripcion": f"{(h % 28) + 1:02d}/{(h % 12) + 1:02d}/{(h % 14) + 2005}",
                "ultima_actualizacion": "15/11/2024",
                "estado": ["Activo", "Activo", "Activo", "Observado", "Inactivo"][h % 5],
                "estado_class": estados[h % 3],
            }

    return render(request, "consulta_nit.html", {
        "nit_query": nit_query,
        "resultado": resultado,
        "error": error,
        "show_decoy_banner": True,
    })


def facturacion_lista(request):
    facturas_demo = [
        {"cuf": "ABC-DEF-2024-001", "fecha": "20/11/2024", "receptor": "Cliente S.R.L. (NIT 12345678)", "monto": "Bs. 12.450,00", "estado": "Vigente", "estado_class": "success"},
        {"cuf": "ABC-DEF-2024-002", "fecha": "18/11/2024", "receptor": "Distribuidora XYZ (NIT 87654321)", "monto": "Bs. 8.200,00", "estado": "Vigente", "estado_class": "success"},
        {"cuf": "ABC-DEF-2024-003", "fecha": "15/11/2024", "receptor": "Servicios ABC (NIT 11223344)", "monto": "Bs. 4.500,00", "estado": "Anulada", "estado_class": "danger"},
        {"cuf": "ABC-DEF-2024-004", "fecha": "10/11/2024", "receptor": "Constructora Norte (NIT 55667788)", "monto": "Bs. 25.000,00", "estado": "Vigente", "estado_class": "success"},
        {"cuf": "ABC-DEF-2024-005", "fecha": "05/11/2024", "receptor": "Transportes Sur (NIT 99887766)", "monto": "Bs. 1.800,00", "estado": "Vigente", "estado_class": "success"},
    ]

    return render(request, "facturacion/lista.html", {
        "facturas": facturas_demo,
        "show_decoy_banner": True,
    })


def declaraciones_lista(request):
    return redirect("declaraciones:nueva")
