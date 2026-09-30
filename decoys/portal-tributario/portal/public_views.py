"""
Vistas públicas del Portal de Contribuyentes.

Páginas orientadas al contribuyente (NIT):
  - home            : landing principal
  - login_public    : login del contribuyente en dos pasos (usuario/clave + 2FA)
  - register        : registro de nuevo contribuyente
  - logout_public   : cierra sesión
  - dashboard       : panel del contribuyente autenticado
  - consulta_nit    : búsqueda de NIT

Las páginas se presentan como un servicio tributario real: sin avisos,
banners ni marcas que indiquen que se trata de un señuelo.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django import forms
from django.db import models
from django.utils import timezone
import re
import secrets
from datetime import datetime


# Longitud del código de verificación en dos pasos
OTP_LENGTH = 6
# Ventana de validez del código, en segundos
OTP_TTL = 300


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
    return render(request, "home.html")


def _mask_target(username):
    """Enmascara el identificador para mostrarlo en la pantalla de verificación."""
    if "@" in username:
        local, _, domain = username.partition("@")
        masked = local[:2] + "*" * max(len(local) - 2, 1)
        return f"{masked}@{domain}"
    if len(username) <= 4:
        return username[0] + "*" * (len(username) - 1)
    return username[:2] + "*" * (len(username) - 4) + username[-2:]


def _issue_otp(request, user):
    """
    Genera el código de verificación de segundo factor.

    El código se entrega por el canal simulado de notificación del
    contribuyente. Cada verificación queda registrada para detección
    de incidentes.
    """
    code = "".join(str(secrets.randbelow(10)) for _ in range(OTP_LENGTH))
    request.session["otp_code"] = code
    request.session["otp_user"] = user.pk
    request.session["otp_issued_at"] = timezone.now().isoformat()
    request.session["otp_target"] = _mask_target(user.username)
    return code


def _otp_is_valid(request, submitted):
    """Comprueba el código recibido contra la sesión y su ventana de validez."""
    expected = request.session.get("otp_code")
    if not expected or not submitted:
        return False
    issued_at = request.session.get("otp_issued_at")
    if issued_at:
        age = (timezone.now() - datetime.fromisoformat(issued_at)).total_seconds()
        if age > OTP_TTL:
            return False
    return secrets.compare_digest(str(expected), str(submitted).strip())


def login_public(request):
    if request.user.is_authenticated:
        return redirect("public_dashboard")

    if request.method == "POST":
        stage = request.POST.get("stage", "credentials")

        # ------------------------------------------------------------------
        # Paso 1 — NIT / usuario + contraseña
        # ------------------------------------------------------------------
        if stage == "credentials":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    _issue_otp(request, user)
                    return render(request, "login.html", {
                        "form": form,
                        "auth_stage": "otp",
                        "otp_target": request.session["otp_target"],
                    })
                form.add_error(None, "NIT/correo o contraseña incorrectos.")
            else:
                return render(request, "login.html", {
                    "form": form,
                    "auth_stage": "credentials",
                })

            return render(request, "login.html", {
                "form": form,
                "auth_stage": "credentials",
            })

        # ------------------------------------------------------------------
        # Paso 2 — código de verificación
        # ------------------------------------------------------------------
        if stage == "otp":
            user_pk = request.session.get("otp_user")
            otp_target = request.session.get("otp_target", "")
            user = User.objects.filter(pk=user_pk).first() if user_pk else None

            submitted = request.POST.get("otp_code", "")
            if user is not None and _otp_is_valid(request, submitted):
                login(request, user)
                for key in ("otp_code", "otp_user", "otp_issued_at", "otp_target"):
                    request.session.pop(key, None)
                messages.success(request, "Verificación completada. Bienvenido.")
                return redirect("public_dashboard")

            return render(request, "login.html", {
                "form": LoginForm(initial={"username": otp_target}),
                "auth_stage": "otp",
                "otp_target": otp_target,
                "otp_error": "El código de verificación es incorrecto o expiró.",
            })

    form = LoginForm()
    return render(request, "login.html", {"form": form, "auth_stage": "credentials"})


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
    })


def declaraciones_lista(request):
    return redirect("declaraciones:nueva")
