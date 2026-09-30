"""
Endpoint: Factura Electrónica
==============================

GET /api/v1/facturas/{cuf}

Vulnerable a:
  - T1213 (Data from Information Repositories)
  - T1530 (Data from Cloud Storage Object)
"""

import logging
from fastapi import APIRouter, Path

logger = logging.getLogger("sin-api.facturas")

router = APIRouter()


@router.get("/{cuf}")
async def get_factura(cuf: str = Path(..., min_length=20, max_length=30)):
    """Consulta de factura por CUF (Código Único de Facturación)."""
    return {
        "cuf": cuf,
        "estado": "VALIDA",
        "nit_emisor": "10234567891",
        "nit_receptor": "10987654321",
        "monto": 1234.56,
        "fecha_emision": "2024-12-15",
    }


@router.get("/")
async def list_facturas(limit: int = 10):
    return {
        "total": 8_234_512,
        "items": [
            {"cuf": f"CUF-2024-12-{i:016d}", "monto": 100.0 * i}
            for i in range(min(limit, 50))
        ],
    }
