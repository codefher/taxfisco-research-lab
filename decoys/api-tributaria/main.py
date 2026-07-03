"""
TaxFisco Decoy API - Main Application
=====================================

Decoy API REST que simula una API tributaria real con instrumentación
de MITRE ATT&CK. Cada interacción maliciosa se registra con:
  - timestamp
  - IP origen
  - user agent
  - endpoint
  - técnica ATT&CK inferida
  - payload sospechoso
  - nivel de amenaza (TLP:AMBER)

Endpoints fiscales simulados (TaxFisco Research Lab):
  - /api/v1/contribuyentes/{nit}  - Consulta de contribuyente
  - /api/v1/declaraciones         - Declaración jurada (POST)
  - /api/v1/facturas/{cuf}        - Consulta de factura
  - /api/v1/auth/login            - Autenticación
  - /api/v1/admin/users           - Administración (vulnerable)
  - /api/v1/reportes              - Reportes financieros
"""

import json
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, List

from fastapi import FastAPI, Request, Response, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Configurar logging
LOG_DIR = Path("/var/log/decoy-api")
LOG_DIR.mkdir(parents=True, exist_ok=True)

ATTACK_LOG_FILE = LOG_DIR / "attacks.json"
ALL_REQUESTS_FILE = LOG_DIR / "all_requests.jsonl"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "decoy-api.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("decoy-api")

# Path para importar módulos locales
sys.path.insert(0, str(Path(__file__).parent))

from instrumentation.attack_logger import AttackLogger, AttackEvent  # noqa: E402
from instrumentation.deception_tokens import DeceptionTokens  # noqa: E402
from endpoints import (  # noqa: E402
    nit,
    declaracion_jurada,
    factura,
    auth,
    admin,
    reportes,
)

# ============================================================================
# App initialization
# ============================================================================

app = FastAPI(
    title="TaxFisco Decoy API",
    description="Decoy API for TaxFisco Research Lab - Honeypot Thesis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

attack_logger = AttackLogger(log_file=ATTACK_LOG_FILE)
deception_tokens = DeceptionTokens()


# ============================================================================
# Middleware - Captura TODAS las requests
# ============================================================================

@app.middleware("http")
async def capture_all_requests(request: Request, call_next):
    """Captura todas las requests y las loguea para análisis forense."""
    # Capturar información
    body_bytes = await request.body()
    body_str = body_bytes.decode("utf-8", errors="ignore") if body_bytes else ""

    request_info = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "method": request.method,
        "path": request.url.path,
        "query": dict(request.query_params),
        "headers": dict(request.headers),
        "client_ip": request.client.host if request.client else "unknown",
        "body": body_str[:5000] if body_str else "",
        "user_agent": request.headers.get("user-agent", "unknown"),
    }

    # Loguear todas las requests
    with open(ALL_REQUESTS_FILE, "a") as f:
        f.write(json.dumps(request_info) + "\n")

    # Detectar TTP ATT&CK
    ttp = attack_logger.detect_ttp(request_info)

    # Si es sospechoso, loguear como attack
    if ttp:
        attack_event = AttackEvent(
            timestamp=request_info["timestamp"],
            source_ip=request_info["client_ip"],
            user_agent=request_info["user_agent"],
            method=request_info["method"],
            endpoint=request_info["path"],
            query=request_info["query"],
            body=request_info["body"],
            attack_technique_id=ttp["technique_id"],
            attack_technique_name=ttp["technique_name"],
            attack_tactic=ttp["tactic"],
            severity=ttp["severity"],
            description=ttp["description"],
            tlp="AMBER",
        )
        attack_logger.log_attack(attack_event)
        logger.warning(
            f"ATT&CK {ttp['technique_id']} ({ttp['tactic']}) "
            f"from {request_info['client_ip']} on {request_info['path']}"
        )

    # Procesar request
    response = await call_next(request)

    # Añadir header de identificación (deception marker)
    response.headers["X-TaxFisco-Env"] = "decoy-research-lab"
    response.headers["X-Powered-By"] = "TaxFisco/1.0"

    return response


# ============================================================================
# Health & Info endpoints
# ============================================================================

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "taxfisco-decoy-api", "version": "1.0.0"}


@app.get("/")
async def root():
    return {
        "service": "TaxFisco Decoy API",
        "version": "1.0.0",
        "description": "Decoy API for honeypot research thesis",
        "endpoints": [
            "/api/v1/contribuyentes/{nit}",
            "/api/v1/declaraciones",
            "/api/v1/facturas/{cuf}",
            "/api/v1/auth/login",
            "/api/v1/admin/users",
            "/api/v1/reportes",
        ],
        "deception_markers": deception_tokens.list_active_markers(),
    }


# ============================================================================
# Mount fiscal endpoints
# ============================================================================

app.include_router(nit.router, prefix="/api/v1/contribuyentes", tags=["contribuyentes"])
app.include_router(declaracion_jurada.router, prefix="/api/v1/declaraciones", tags=["declaraciones"])
app.include_router(factura.router, prefix="/api/v1/facturas", tags=["facturas"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])
app.include_router(reportes.router, prefix="/api/v1/reportes", tags=["reportes"])


# ============================================================================
# Decoy admin endpoints (intentionally vulnerable)
# ============================================================================

@app.get("/api/v1/admin/export-all")
async def export_all_data():
    """Endpoint trampa. Acceder aquí es un ATT&CK T1530 (Data from Cloud Storage Object)."""
    attack_logger.log_attack(AttackEvent(
        timestamp=datetime.utcnow().isoformat() + "Z",
        source_ip="0.0.0.0",
        user_agent="unknown",
        method="GET",
        endpoint="/api/v1/admin/export-all",
        query={},
        body="",
        attack_technique_id="T1530",
        attack_technique_name="Data from Cloud Storage Object",
        attack_tactic="Collection",
        severity="HIGH",
        description="Attacker accessed decoy admin export endpoint - bait triggered",
        tlp="RED",
    ))
    return JSONResponse(
        status_code=200,
        content={
            "_warning": "This is a decoy endpoint. Access has been logged.",
            "fake_data": {
                "total_contribuyentes": 1_247_893,
                "total_recaudado_2024": "B$ 4_287_392_115.50",
                "sample_data": deception_tokens.generate_fake_export(),
            },
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        access_log=True,
    )
