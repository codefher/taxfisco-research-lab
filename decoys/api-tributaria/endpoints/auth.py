"""
Endpoint: Autenticación
=======================

POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
"""

import logging
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
import hashlib
import secrets

logger = logging.getLogger("sin-api.auth")

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(request: Request, creds: LoginRequest):
    """
    Autenticación de contribuyentes mediante NIT o correo electrónico.
    """
    logger.info(
        f"LOGIN ATTEMPT: user='{creds.username}' pass_len={len(creds.password)}"
    )

    # Token de sesión para el contribuyente
    session = secrets.token_urlsafe(32)

    return {
        "access_token": session,
        "refresh_token": "rtk_" + hashlib.sha256(creds.password.encode()).hexdigest()[:32],
        "token_type": "Bearer",
        "expires_in": 86400,
        "user": {
            "username": creds.username,
            "role": "contribuyente",
            "permissions": ["read:declaraciones", "read:facturas", "read:constancias"],
        },
    }


@router.post("/refresh")
async def refresh_token(request: Request):
    return {
        "access_token": secrets.token_urlsafe(32),
        "token_type": "Bearer",
        "expires_in": 3600,
    }


@router.post("/logout")
async def logout():
    return {"message": "Sesión cerrada correctamente"}
