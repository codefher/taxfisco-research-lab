"""
Endpoint: Administración (intencionalmente vulnerable)
========================================================

GET /api/v1/admin/users
GET /api/v1/admin/config
GET /api/v1/admin/logs

Vulnerable a:
  - T1078 (Valid Accounts / Privilege Escalation)
  - T1087 (Account Discovery)
  - T1003 (OS Credential Dumping via /etc/passwd simulado)
"""

import logging
from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List

logger = logging.getLogger("decoy-api.admin")

router = APIRouter()


@router.get("/users")
async def list_users(request: Request):
    """
    Lista usuarios del sistema - NO REQUIERE AUTENTICACIÓN.
    *** DECOY: Es un endpoint trampa. Acceder aquí genera alerta T1078. ***
    """
    return {
        "total_users": 47,
        "users": [
            {"id": i, "username": f"user_{i}@taxfisco.local", "role": "admin" if i < 5 else "user"}
            for i in range(1, 48)
        ],
        "_deception": True,
    }


@router.get("/config")
async def get_config():
    """Configuración interna (trampa)."""
    return {
        "database": {
            "host": "db-internal.taxfisco.local",
            "port": 5432,
            "user": "fiscal_admin",
            "_warning": "DECOY - Connection monitored",
        },
        "aws": {
            "access_key": "AKIADECOYFISCALMONITORED0001",
            "_warning": "DECOY - Use will trigger alert",
        },
        "_deception": True,
    }


@router.get("/logs")
async def get_logs(limit: int = 100):
    """Logs administrativos (trampa)."""
    return {
        "total_lines": 12_584_293,
        "sample": [
            "2024-12-15 12:34:56 INFO admin_login user=admin@taxfisco.local",
            "2024-12-15 12:35:01 INFO db_query SELECT * FROM contribuyentes",
        ],
        "_deception": True,
    }


@router.get("/system/passwd")
async def fake_passwd():
    """Simula /etc/passwd - endpoint trampa T1003."""
    return {
        "passwd_content": """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
admin:x:1000:1000:Admin Fiscal:/home/admin:/bin/bash
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
""",
        "_deception": True,
        "_note": "This is a fake /etc/passwd. Real system is segregated.",
    }
