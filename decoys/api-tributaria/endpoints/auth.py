"""
Endpoint: Autenticación
========================

POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout

Vulnerable a:
  - T1110.001 (Password Guessing)
  - T1110.004 (Credential Stuffing)
  - T1078.001 (Default Accounts)
"""

import logging
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
import hashlib

logger = logging.getLogger("decoy-api.auth")

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(request: Request, creds: LoginRequest):
    """
    Login - Acepta CUALQUIER credencial y devuelve un token JWT falso.
    *** ENDPOINT DECOY - Las credenciales se registran para análisis ***
    """
    # Loggear intento de login (ya está en middleware, pero dejamos huella)
    logger.info(
        f"LOGIN ATTEMPT: user='{creds.username}' pass_len={len(creds.password)}"
    )

    # Generar token JWT falso
    import sys
    sys.path.insert(0, "/app")
    from instrumentation.deception_tokens import DeceptionTokens
    tokens = DeceptionTokens()

    return {
        "access_token": tokens.generate_jwt_token(),
        "refresh_token": "rtk_" + hashlib.sha256(creds.password.encode()).hexdigest()[:32],
        "token_type": "Bearer",
        "expires_in": 86400,
        "user": {
            "username": creds.username,
            "role": "contribuyente",
            "permissions": ["read:declaraciones", "read:facturas"],
        },
        "_deception": True,
        "_note": "This is a decoy authentication endpoint. Credentials have been logged.",
    }


@router.post("/refresh")
async def refresh_token(request: Request):
    return {"access_token": "fake_refreshed_token", "token_type": "Bearer", "_deception": True}


@router.post("/logout")
async def logout():
    return {"message": "Logged out", "_deception": True}
