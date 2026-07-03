"""
Endpoint: Reportes financieros
===============================

GET /api/v1/reportes/recaudacion-mensual
GET /api/v1/reportes/top-contribuyentes
GET /api/v1/reportes/facturas-vencidas

Vulnerable a:
  - T1213 (Data from Information Repositories)
  - T1530 (Data from Cloud Storage)
"""

import logging
from fastapi import APIRouter
from datetime import datetime

logger = logging.getLogger("decoy-api.reportes")

router = APIRouter()


@router.get("/recaudacion-mensual")
async def recaudacion_mensual(anio: int = 2024):
    return {
        "anio": anio,
        "total_recaudado": 4_287_392_115.50,
        "por_mes": [
            {"mes": i, "monto": 350_000_000.0 + i * 5_000_000} for i in range(1, 13)
        ],
        "_deception": True,
    }


@router.get("/top-contribuyentes")
async def top_contribuyentes(limit: int = 100):
    return {
        "total": limit,
        "items": [
            {"ranking": i, "nit": f"1000000{i:02d}", "monto_aportado": 50_000_000 - i * 1000}
            for i in range(1, limit + 1)
        ],
        "_deception": True,
    }


@router.get("/facturas-vencidas")
async def facturas_vencidas():
    return {
        "total_vencidas": 12_583,
        "monto_total_vencido": 234_582_341.89,
        "_deception": True,
    }
