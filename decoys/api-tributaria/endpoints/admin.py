"""
Endpoint: Administración
======================

GET /api/v1/admin/users
GET /api/v1/admin/config
GET /api/v1/admin/logs
GET /api/v1/admin/system/cuentas
"""

import logging
from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List

logger = logging.getLogger("sin-api.admin")

router = APIRouter()


@router.get("/users")
async def list_users(request: Request):
    """
    Lista usuarios del sistema - NO REQUIERE AUTENTICACIÓN.
    """
    return {
        "total_users": 47,
        "users": [
            {
                "id": i,
                "username": f"operador{i:02d}@sin.local",
                "nombre": f"Funcionario {i:02d}",
                "role": "administrador" if i < 5 else "operador",
                "estado": "activo",
            }
            for i in range(1, 48)
        ],
    }


@router.get("/config")
async def get_config():
    """Configuración interna del servicio."""
    return {
        "database": {
            "host": "db-interno.sin.local",
            "port": 5432,
            "base": "sin_fiscal",
            "user": "fiscal_admin",
        },
        "almacenamiento": {
            "bucket": "sin-datos-tributarios",
            "region": "sa-east-1",
        },
        "version": "2.4.1",
    }


@router.get("/logs")
async def get_logs(limit: int = 100):
    """Registro de actividad del servicio."""
    return {
        "total_lines": 12_584_293,
        "sample": [
            "2024-12-15 12:34:56 INFO admin_login user=admin@sin.local",
            "2024-12-15 12:35:01 INFO db_query SELECT * FROM contribuyentes",
        ],
    }


@router.get("/system/passwd")
async def listar_cuentas_sistema():
    """Contenido del archivo de cuentas del sistema."""
    return {
        "passwd_content": """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
admin:x:1000:1000:Administrador:/home/admin:/bin/bash
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
"""
    }
