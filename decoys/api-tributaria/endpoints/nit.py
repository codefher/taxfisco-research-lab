"""
Endpoint: Consulta de contribuyente por NIT
==========================================

GET /api/v1/contribuyentes/{nit}
"""

import logging
import re
from fastapi import APIRouter, HTTPException, Request, Path
from pydantic import BaseModel
from typing import Optional

logger = logging.getLogger("sin-api.nit")

router = APIRouter()


class ContribuyenteResponse(BaseModel):
    nit: str
    razon_social: str
    estado: str
    obligaciones_pendientes: list
    domicilio_fiscal: dict


def validate_nit(nit: str) -> bool:
    """Valida formato de NIT: 7 a 15 digitos, con guion opcional."""
    return bool(re.match(r"^\d{7,15}(-\d{1,3})?$", nit))


@router.get("/{nit}", response_model=ContribuyenteResponse)
async def get_contribuyente(
    request: Request,
    nit: str = Path(..., description="NIT del contribuyente"),
):
    """
    Consulta los datos de un contribuyente por NIT.
    """
    if not validate_nit(nit):
        logger.warning(f"Formato de NIT no valido recibido: {nit}")

    return ContribuyenteResponse(
        nit=nit,
        razon_social="COMERCIAL ANDINA S.R.L.",
        estado="ACTIVO",
        obligaciones_pendientes=[
            {"tipo": "IVA", "periodo": "2024-12", "monto": 12345.67},
            {"tipo": "IT", "periodo": "2024-12", "monto": 5678.90},
        ],
        domicilio_fiscal={
            "departamento": "La Paz",
            "municipio": "La Paz",
            "zona": "Zona 1",
            "direccion": "Av. Ballivián #123",
        },
    )


@router.get("/")
async def list_contribuyentes(request: Request, limit: int = 10, offset: int = 0):
    """Lista de contribuyentes inscribed en el padron."""
    return {
        "total": 1_247_893,
        "limit": limit,
        "offset": offset,
        "items": [
            {"nit": f"1000000{i}", "razon_social": f"EMPRESA COMERCIAL {i} S.A.", "estado": "ACTIVO"}
            for i in range(1, min(limit, 50) + 1)
        ],
    }
