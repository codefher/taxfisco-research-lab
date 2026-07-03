"""
Endpoint: Consulta de contribuyente por NIT
==========================================

GET /api/v1/contribuyentes/{nit}

Vulnerable a:
  - T1190 (SQL Injection via path parameter)
  - T1213 (Data from Information Repositories)
  - T1087.002 (Domain Account discovery)
"""

import logging
import re
from fastapi import APIRouter, HTTPException, Request, Path
from pydantic import BaseModel
from typing import Optional

logger = logging.getLogger("decoy-api.nit")

router = APIRouter()


class ContribuyenteResponse(BaseModel):
    nit: str
    razon_social: str
    estado: str
    obligaciones_pendientes: list
    domicilio_fiscal: dict


def validate_nit(nit: str) -> bool:
    """Valida formato de NIT (genérico: 7-15 dígitos con posible guión)."""
    return bool(re.match(r"^\d{7,15}(-\d{1,3})?$", nit))


@router.get("/{nit}", response_model=ContribuyenteResponse)
async def get_contribuyente(
    request: Request,
    nit: str = Path(..., description="NIT del contribuyente"),
):
    """
    Consulta datos de un contribuyente por NIT.

    *** ENDPOINT DECOY - Vulnerabilidades controladas con fines académicos ***
    """
    # Detección adicional: si el NIT no pasa validación pero intenta SQLi
    if not validate_nit(nit) and not re.search(r"[a-zA-Z]", nit):
        # Posible intento de SQLi en path
        logger.warning(f"Invalid NIT format received (possible injection): {nit}")

    # Respuesta simulada
    return ContribuyenteResponse(
        nit=nit,
        razon_social="CONTRIBUYENTE GENERICO S.A. (DECOY)",
        estado="ACTIVO",
        obligaciones_pendientes=[
            {"tipo": "IVA", "periodo": "2024-12", "monto": 12345.67},
            {"tipo": "IT", "periodo": "2024-12", "monto": 5678.90},
        ],
        domicilio_fiscal={
            "departamento": "La Paz",
            "municipio": "La Paz",
            "zona": "Zona 1",
            "direccion": "Av. Ficticia #123 (DECOY)",
        },
        _metadata={
            "_deception": True,
            "_note": "This is a decoy endpoint. Access is logged for honeypot research.",
        },
    )


@router.get("/")
async def list_contribuyentes(request: Request, limit: int = 10, offset: int = 0):
    """Lista los primeros N contribuyentes (endpoint trampa)."""
    return {
        "total": 1_247_893,
        "limit": limit,
        "offset": offset,
        "items": [
            {"nit": f"1000000{i}", "razon_social": f"EMPRESA FICTICIA {i} S.A. (DECOY)"}
            for i in range(min(limit, 50))
        ],
        "_deception": True,
    }
