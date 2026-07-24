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
from fastapi.staticfiles import StaticFiles
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

DESCRIPTION = """
## API de Servicios Tributarios — TaxFisco Research Lab

Esta es una **API honeypot (decoy)** que simula los servicios electrónicos
de un ente tributario genérico. Su propósito es **únicamente académico**,
en el marco de la tesis de maestría sobre gestión de incidentes en
servicios fiscales.

### 🎯 Características

- **19 endpoints** que simulan operaciones tributarias reales
- **Instrumentación MITRE ATT&CK** automática en cada request
- **Detección de payloads sospechosos** (SQLi, XSS, command injection)
- **Logging de ataques** a `attacks.json` para análisis posterior
- **Tokens de engaño** plantados para identificar atacantes reales

### ⚠️ Aviso de honeypot

Toda interacción con esta API es **monitoreada y registrada**. Los
endpoints `/api/v1/admin/*` contienen vulnerabilidades controladas
(inyectadas a propósito) para capturar TTPs reales de atacantes.

### 🔍 Endpoints principales

| Recurso | Método | Descripción |
|---|---|---|
| `/api/v1/contribuyentes/{nit}` | GET | Consulta de contribuyente por NIT |
| `/api/v1/declaraciones` | POST | Declaración jurada de impuestos |
| `/api/v1/facturas/{cuf}` | GET | Consulta de factura electrónica |
| `/api/v1/auth/login` | POST | Autenticación (honeypot) |
| `/api/v1/admin/users` | GET | Lista de usuarios (vulnerable) |
| `/api/v1/reportes` | GET | Reportes financieros |

### 📚 Documentación

- **Swagger UI**: `/docs` (esta página)
- **OpenAPI JSON**: `/openapi.json`
- **Repositorio**: TaxFisco Research Lab
"""

TAX_FISCO_LOGO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60" width="200" height="60" style="margin-bottom: 8px;">
  <defs>
    <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0F4C81"/>
      <stop offset="100%" style="stop-color:#0a3a64"/>
    </linearGradient>
  </defs>
  <g transform="translate(8, 8)">
    <rect x="4" y="2" width="36" height="40" rx="6" fill="url(#g1)"/>
    <circle cx="22" cy="20" r="9" fill="none" stroke="#D4A437" stroke-width="2"/>
    <line x1="22" y1="20" x2="22" y2="11" stroke="#D4A437" stroke-width="2"/>
    <line x1="13" y1="20" x2="31" y2="20" stroke="#D4A437" stroke-width="2"/>
    <line x1="22" y1="29" x2="22" y2="36" stroke="#D4A437" stroke-width="2"/>
    <circle cx="22" cy="20" r="1.5" fill="#D4A437"/>
    <rect x="14" y="34" width="16" height="3" fill="#D4A437"/>
  </g>
  <text x="58" y="38" font-family="Inter, system-ui, sans-serif" font-size="26" font-weight="700" fill="#0F4C81" letter-spacing="-0.5">Tax<tspan fill="#D4A437">Fisco</tspan></text>
</svg>
"""

CUSTOM_SWAGGER_CSS = f"""
<style>
  .swagger-ui .topbar {{ display: none; }}
  .swagger-ui .info {{ background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; }}
  .swagger-ui .info .title {{ color: #0F4C81 !important; font-size: 2rem; }}
  .swagger-ui .scheme-container {{ background: #0F4C81; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }}
  .swagger-ui .opblock-tag {{ background: #0F4C81 !important; color: white !important; border-radius: 0.25rem; padding: 0.5rem 1rem; font-size: 1.1rem; }}
  .swagger-ui .opblock {{ border-radius: 0.5rem; box-shadow: 0 1px 3px rgba(15, 76, 129, 0.1); margin-bottom: 1rem; }}
  .swagger-ui .opblock.opblock-get {{ border-color: #0F4C81; }}
  .swagger-ui .opblock.opblock-post {{ border-color: #D4A437; }}
  .swagger-ui .opblock.opblock-delete {{ border-color: #ef4444; }}
  .swagger-ui .btn.execute {{ background: #0F4C81 !important; color: white !important; border-color: #0F4C81 !important; }}
  .swagger-ui .btn.execute:hover {{ background: #0a3a64 !important; }}
  .swagger-ui table thead tr th {{ background: #f1f5f9 !important; color: #0f172a !important; }}
  .swagger-ui .markdown p, .swagger-ui .markdown li {{ color: #0f172a; line-height: 1.6; }}
  .swagger-ui .markdown table {{ border-collapse: collapse; margin: 1rem 0; }}
  .swagger-ui .markdown table th, .swagger-ui .markdown table td {{ border: 1px solid #e2e8f0; padding: 0.5rem 0.75rem; text-align: left; }}
  .swagger-ui .markdown table th {{ background: #f1f5f9; font-weight: 600; }}
  .swagger-ui .info__logo {{
    display: block !important;
    margin: 0 auto 1rem auto !important;
    text-align: center !important;
  }}
  .txf-logo-header {{
    text-align: center;
    padding: 1.5rem 0 0 0;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    border-bottom: 3px solid #D4A437;
  }}
</style>
"""

CUSTOM_SWAGGER_HTML = f"""
<!DOCTYPE html>
<html>
<head>
  <link rel="icon" type="image/svg+xml" href="/static/img/favicon.svg">
  {CUSTOM_SWAGGER_CSS}
</head>
<body>
  <div class="txf-logo-header">
    {TAX_FISCO_LOGO_SVG}
  </div>
  <div id="swagger-ui"></div>
</body>
</html>
"""

app = FastAPI(
    title="TaxFisco — API de Servicios Tributarios",
    description=DESCRIPTION,
    version="2.0.0",
    docs_url="/docs",
    redoc_url=None,
    swagger_ui_parameters={
        "customSiteTitle": "TaxFisco API — Documentación",
        "defaultModelsExpandDepth": -1,
        "docExpansion": "list",
        "filter": True,
        "syntaxHighlight.theme": "nord",
        "tryItOutEnabled": True,
        "persistAuthorization": True,
    },
    contact={
        "name": "TaxFisco Research Lab",
        "url": "https://github.com/codefher/taxfisco-research-lab",
    },
    license_info={
        "name": "MIT (Research use only)",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "contribuyentes",
            "description": "Operaciones de consulta y modificación de contribuyentes",
        },
        {
            "name": "declaraciones",
            "description": "Declaraciones juradas de impuestos",
        },
        {
            "name": "facturas",
            "description": "Facturación electrónica",
        },
        {
            "name": "auth",
            "description": "Autenticación y gestión de sesiones",
        },
        {
            "name": "admin",
            "description": "⚠️ Endpoints administrativos (honeypot — vulnerables)",
        },
        {
            "name": "reportes",
            "description": "Reportes financieros y fiscales",
        },
        {
            "name": "health",
            "description": "Healthchecks y metadata del servicio",
        },
    ],
)

# Inyectar HTML/CSS custom en Swagger UI
app.swagger_ui_html = CUSTOM_SWAGGER_HTML

# Servir archivos estáticos (logo, favicon) para el Swagger UI
import os
STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(parents=True, exist_ok=True)
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

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
