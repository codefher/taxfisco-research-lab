"""
Deception Tokens - Tokens señuelo para engañar atacantes
=========================================================

Genera:
  - AWS keys falsas
  - Database connection strings
  - API tokens ficticios
  - Credenciales embebidas
  - Datos financieros sintéticos
  - Documentos señuelo
"""

import random
import string
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any


class DeceptionTokens:
    """Generador de tokens de engaño coherentes con dominio fiscal."""

    def __init__(self):
        self.deployed_markers = []
        self._seed_realistic_data()

    def _seed_realistic_data(self):
        """Datos realistas para hacer el engaño convincente."""
        self.dummy_nits = [
            "10234567891", "10987654321", "11456789012",
            "12345678901", "13141516171", "18192021222",
        ]
        self.dummy_companies = [
            "Constructora Andina S.A.",
            "Servicios Financieros del Sur",
            "Distribuidora Comercial López",
            "Importadora Boliviana S.R.L.",
            "Consultoría Estratégica Global",
            "Industrias Manufactureras del Norte",
            "Agropecuaria San Miguel Ltda.",
        ]
        self.dummy_emails = [
            "gerencia@empresa-ficticia.com",
            "contabilidad@grupo-andino.net",
            "admin@consultora-demo.org",
            "finanzas@holding-test.bo",
        ]

    def list_active_markers(self) -> List[str]:
        """Lista los markers de deception desplegados."""
        return self.deployed_markers

    def generate_aws_key(self) -> Dict[str, str]:
        """AWS access key falsa pero con formato válido."""
        access = "AKIA" + "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
        secret = "".join(random.choices(string.ascii_letters + string.digits + "/+", k=40))
        marker = {
            "type": "aws_key",
            "access_key_id": access,
            "secret_access_key": secret,
            "deployed_at": datetime.utcnow().isoformat() + "Z",
        }
        self.deployed_markers.append(marker["access_key_id"])
        return marker

    def generate_db_connection_string(self) -> Dict[str, str]:
        """Connection string a base de datos ficticia."""
        return {
            "type": "db_connection",
            "host": "db-respaldo-interno.sin.local",
            "port": 5432,
            "database": "sin_fiscal_prod",
            "user": "backup_admin",
            "password": "Bkp_" + "".join(random.choices(string.ascii_letters + string.digits, k=12)),
        }

    def generate_api_token(self) -> Dict[str, str]:
        """API token falso."""
        return {
            "type": "api_token",
            "service": "sin-internal-api",
            "token": "tk_" + hashlib.sha256(str(random.random()).encode()).hexdigest()[:32],
            "scopes": ["read:contribuyentes", "read:facturas", "write:declaraciones"],
        }

    def generate_export(self) -> Dict[str, Any]:
        """Export señuelo de datos fiscales."""
        return {
            "export_id": "EXP-" + str(random.randint(100000, 999999)),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "total_records": random.randint(50000, 200000),
            "contribuyentes_sample": [
                {
                    "nit": random.choice(self.dummy_nits),
                    "razon_social": random.choice(self.dummy_companies),
                    "declaraciones_pendientes": random.randint(0, 5),
                    "monto_deuda": round(random.uniform(0, 500000), 2),
                }
                for _ in range(20)
            ],
            "facturas_sample": [
                {
                    "cuf": "".join(random.choices(string.digits, k=55)),
                    "monto": round(random.uniform(100, 50000), 2),
                    "fecha": (datetime.utcnow() - timedelta(days=random.randint(0, 365))).isoformat(),
                }
                for _ in range(20)
            ],
        }

    def generate_credentials(self, role: str = "admin") -> Dict[str, str]:
        """Credenciales embebidas falsas."""
        cuentas = {
            "admin": ("admin_prod", "Adm1n_Pr0d_2024!"),
            "backup": ("backup_usr", "Bkp_2024_F1n4nc!"),
            "auditor": ("auditor_ext", "4ud1t0r_2024*"),
            "developer": ("dev_jr", "D3v_2024_Pr0y3ct0!"),
        }
        user, pwd = cuentas.get(role, cuentas["admin"])
        return {
            "type": "credentials",
            "username": user,
            "password": pwd,
            "role": role,
        }

    def generate_session_cookie(self) -> str:
        """Cookie de sesión falsa pero con aspecto legítimo."""
        token = hashlib.sha256(str(random.random()).encode()).hexdigest()
        return f"SIN_SESSION={token}; Path=/; HttpOnly; SameSite=Strict"

    def generate_jwt_token(self) -> str:
        """JWT falso con claims realistas."""
        import base64
        header = base64.urlsafe_b64encode(b'{"alg":"HS256","typ":"JWT"}').rstrip(b"=").decode()
        payload_data = {
            "sub": "admin@sin.local",
            "name": "Administrator",
            "role": "superadmin",
            "iat": int(datetime.utcnow().timestamp()),
            "exp": int((datetime.utcnow() + timedelta(hours=24)).timestamp()),
        }
        import json
        payload = base64.urlsafe_b64encode(json.dumps(payload_data).encode()).rstrip(b"=").decode()
        signature = hashlib.sha256(f"{header}.{payload}".encode()).hexdigest()[:32]
        return f"{header}.{payload}.{signature}"

    def generate_canary_document(self) -> Dict[str, str]:
        """Documento Word/Excel con token canary embebido."""
        return {
            "type": "canary_document",
            "filename": "declaraciones_juradas_2024_interno.docx",
            "canary_token": "canary-token-" + hashlib.sha256(str(random.random()).encode()).hexdigest()[:16],
            "drop_location_hint": "/var/backups/financial/2024/",
        }
