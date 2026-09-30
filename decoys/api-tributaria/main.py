"""
API de Servicios Tributarios - Aplicacion principal
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

Endpoints de servicios tributarios:
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
from fastapi.responses import JSONResponse, HTMLResponse
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
logger = logging.getLogger("sin-api")

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
## API de Servicios Tributarios — Impuestos Nacionales

API de servicios electrónicos del Servicio Nacional de Impuestos.
Expone las operaciones tributarias de uso frecuente para contribuyentes
y agentes de pago.

### Características

- **20 endpoints** de operación tributaria y administrativa
- Respuestas en JSON con la estructura normalizada del servicio
- Autenticación por NIT y contraseña con segundo factor
- Documentación interactiva con ejecución de pruebas desde el navegador

### Endpoints principales

| Recurso | Método | Descripción |
|---|---|---|
| `/api/v1/contribuyentes/{nit}` | GET | Consulta de contribuyente por NIT |
| `/api/v1/declaraciones` | POST | Declaración jurada de impuestos |
| `/api/v1/facturas/{cuf}` | GET | Consulta de factura electrónica |
| `/api/v1/auth/login` | POST | Autenticación del contribuyente |
| `/api/v1/admin/users` | GET | Directorio de usuarios internos |
| `/api/v1/reportes` | GET | Reportes financieros |

### Documentación

- **Swagger UI**: `/docs` (esta página)
- **OpenAPI JSON**: `/openapi.json`
"""

TAX_FISCO_LOGO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 92" width="300" height="92"
     style="margin-bottom: 8px;">
  <g>
    <path d="M8 26 L52 16 V80 L8 70 Z" fill="#003055"/>
    <path d="M60 14 L104 4 V68 L60 78 Z" fill="#00BAC2"/>
    <g stroke="#00BAC2" stroke-width="2.4" stroke-linecap="round" fill="none">
      <path d="M36 34 H60"/><path d="M36 44 H60"/><path d="M36 54 H60"/>
    </g>
    <g fill="#00BAC2">
      <circle cx="60" cy="34" r="3.2"/><circle cx="60" cy="44" r="3.2"/><circle cx="60" cy="54" r="3.2"/>
    </g>
  </g>
  <g font-family="Montserrat, system-ui, sans-serif" fill="#003055" font-weight="700">
    <text x="116" y="42" font-size="33" letter-spacing="-0.3">Impuestos</text>
    <text x="116" y="77" font-size="33" letter-spacing="-0.3">Nacionales</text>
  </g>
</svg>
"""

CUSTOM_SWAGGER_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

  body { font-family: 'Montserrat', system-ui, sans-serif; }

  .swagger-ui .topbar { display: none; }
  .swagger-ui .info { background: #ffffff; padding: 1.5rem; border-radius: 0.5rem; }
  .swagger-ui .info .title { color: #003055 !important; font-size: 2rem; font-family: 'Montserrat', sans-serif; }
  .swagger-ui .scheme-container { background: #003055; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
  .swagger-ui .opblock-tag { background: #003055 !important; color: white !important; border-radius: 0.25rem; padding: 0.5rem 1rem; font-size: 1.1rem; }
  .swagger-ui .opblock { border-radius: 0.5rem; box-shadow: 0 1px 3px rgba(0, 48, 85, 0.1); margin-bottom: 1rem; }
  .swagger-ui .opblock.opblock-get { border-color: #00BAC2; }
  .swagger-ui .opblock.opblock-post { border-color: #003055; }
  .swagger-ui .opblock.opblock-delete { border-color: #D22229; }
  .swagger-ui .btn.execute { background: #003055 !important; color: white !important; border-color: #003055 !important; }
  .swagger-ui .btn.execute:hover { background: #00233D !important; }
  .swagger-ui table thead tr th { background: #F4F7F9 !important; color: #343A40 !important; }
  .swagger-ui .markdown p, .swagger-ui .markdown li { color: #343A40; line-height: 1.6; }
  .swagger-ui .markdown h2, .swagger-ui .markdown h3 { color: #003055; }
  .swagger-ui .markdown table { border-collapse: collapse; margin: 1rem 0; }
  .swagger-ui .markdown table th, .swagger-ui .markdown table td { border: 1px solid #DEE2E6; padding: 0.5rem 0.75rem; text-align: left; }
  .swagger-ui .markdown table th { background: #F4F7F9; font-weight: 600; }
  .swagger-ui .info__logo {
    display: block !important;
    margin: 0 auto 1rem auto !important;
    text-align: center !important;
  }
  .txf-logo-header {
    text-align: center;
    padding: 1.5rem 0 0 0;
    background: linear-gradient(135deg, #ffffff 0%, #F4F7F9 100%);
    border-bottom: 22px solid #00A5A9;
  }
</style>
"""

CUSTOM_SWAGGER_HTML = f"""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
  <link rel="shortcut icon" type="image/svg+xml" href="/static/img/favicon.svg">
  <title>Impuestos Nacionales — API</title>
  {CUSTOM_SWAGGER_CSS}
</head>
<body>
  <div class="txf-logo-header">
    {TAX_FISCO_LOGO_SVG}
  </div>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    const ui = SwaggerUIBundle({{
      url: '/openapi.json',
      dom_id: "#swagger-ui",
      layout: "BaseLayout",
      deepLinking: true,
      showExtensions: true,
      showCommonExtensions: true,
      defaultModelsExpandDepth: -1,
      docExpansion: "list",
      filter: true,
      tryItOutEnabled: true,
      persistAuthorization: true,
      presets: [SwaggerUIBundle.presets.apis, SwaggerUIBundle.SwaggerUIStandalonePreset]
    }});
  </script>
</body>
</html>
"""

app = FastAPI(
    title="Impuestos Nacionales — API de Servicios Tributarios",
    description=DESCRIPTION,
    version="2.0.0",
    docs_url="/docs",
    redoc_url=None,
    swagger_ui_parameters={
        "customSiteTitle": "Impuestos Nacionales — API",
        "defaultModelsExpandDepth": -1,
        "docExpansion": "list",
        "filter": True,
        "syntaxHighlight.theme": "nord",
        "tryItOutEnabled": True,
        "persistAuthorization": True,
    },
    contact={
        "name": "Servicio Nacional de Impuestos",
        "url": "https://www.impuestos.gob.bo/",
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
            "description": "Endpoints administrativos internos",
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

# La documentacion se sirve desde una ruta propia para poder inyectar la
# cabecera institucional: asignar app.swagger_ui_html ya no surte efecto
# porque el HTML queda capturado al registrarse la ruta.
app.router.routes = [
    r for r in app.router.routes if getattr(r, "path", None) != "/docs"
]


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    """Documentacion interactiva de la API."""
    return HTMLResponse(CUSTOM_SWAGGER_HTML)

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

    response.headers["X-Powered-By"] = "Impuestos-Nacionales/2.0"

    return response


# ============================================================================
# Health & Info endpoints
# ============================================================================

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "sin-api", "version": "2.0.0"}


@app.get("/")
async def root():
    return {
        "service": "API de Servicios Tributarios",
        "institucion": "Impuestos Nacionales",
        "version": "2.0.0",
        "endpoints": [
            "/api/v1/contribuyentes/{nit}",
            "/api/v1/declaraciones",
            "/api/v1/facturas/{cuf}",
            "/api/v1/auth/login",
            "/api/v1/admin/users",
            "/api/v1/reportes",
        ],
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
    """Exportación masiva de registros de contribuyentes."""
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
        description="Acceso al endpoint administrativo de exportación masiva",
        tlp="RED",
    ))
    return JSONResponse(
        status_code=200,
        content={
            "total_contribuyentes": 1_247_893,
            "total_recaudado_2024": "B$ 4_287_392_115.50",
            "export_data": deception_tokens.generate_export(),
            "generated_at": "2024-12-15 08:42:11",
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
