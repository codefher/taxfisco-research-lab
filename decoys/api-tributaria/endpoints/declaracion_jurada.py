"""
Endpoint: Declaración Jurada
==============================

POST /api/v1/declaraciones
GET  /api/v1/declaraciones/{id}

Vulnerable a:
  - T1190 (SQL Injection)
  - T1565 (Data Manipulation)
  - T1078 (Valid Accounts)
"""

import logging
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

logger = logging.getLogger("sin-api.declaraciones")

router = APIRouter()


class LineaDeclaracion(BaseModel):
    codigo_formulario: str
    monto: float
    descripcion: Optional[str] = ""


class DeclaracionRequest(BaseModel):
    nit_contribuyente: str
    periodo: str = Field(..., pattern=r"^\d{4}-(0[1-9]|1[0-2])$")
    tipo_declaracion: str  # "IVA" | "IT" | "IUE" | "RC-IVA"
    lineas: List[LineaDeclaracion]
    firma_digital: Optional[str] = None


@router.post("/")
async def crear_declaracion(request: Request, decl: DeclaracionRequest):
    """
    Crear nueva declaración jurada de impuestos.
    """
    return {
        "id_declaracion": f"DJ-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "estado": "RECIBIDA",
        "nit": decl.nit_contribuyente,
        "periodo": decl.periodo,
        "monto_total": sum(l.monto for l in decl.lineas),
        "timestamp_recepcion": datetime.utcnow().isoformat() + "Z",
    }


@router.get("/{id_declaracion}")
async def get_declaracion(id_declaracion: str):
    """Consulta estado de una declaración específica."""
    return {
        "id_declaracion": id_declaracion,
        "estado": "PROCESADA",
        "monto_pagado": 12345.67,
        "fecha_procesamiento": datetime.utcnow().isoformat() + "Z",
    }


@router.get("/")
async def list_declaraciones(limit: int = 10):
    """Lista las declaraciones juradas más recientes."""
    return {
        "total": 12_584_392,
        "items": [
            {
                "id": f"DJ-2024-12-{i:06d}",
                "nit": f"1000000{i}",
                "monto": 1234.56 * i,
                "estado": "PROCESADA",
            }
            for i in range(min(limit, 50))
        ],
    }
