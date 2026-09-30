"""
Pruebas basicas de la instrumentacion de deteccion
"""
import sys
sys.path.insert(0, "/app")

from instrumentation.attack_logger import AttackLogger, AttackEvent
from instrumentation.deception_tokens import DeceptionTokens
from pathlib import Path
import tempfile


def test_attack_detection():
    """Prueba la detección de TTPs ATT&CK."""
    with tempfile.TemporaryDirectory() as tmp:
        log_file = Path(tmp) / "attacks.json"
        logger = AttackLogger(log_file=log_file)

        # Test SQLi
        req = {
            "timestamp": "2024-12-15T12:00:00Z",
            "method": "GET",
            "path": "/api/v1/contribuyentes/1' OR '1'='1",
            "query": {},
            "headers": {"user-agent": "sqlmap/1.5"},
            "client_ip": "10.99.0.10",
            "body": "",
            "user_agent": "sqlmap/1.5",
        }
        ttp = logger.detect_ttp(req)
        assert ttp is not None, "SQLi no detectado"
        assert ttp["technique_id"] == "T1190", f"Expected T1190, got {ttp['technique_id']}"
        print(f"OK - SQLi detectado: {ttp['technique_id']} ({ttp['attack_tactic']})")

        # Test XSS
        req2 = {
            "timestamp": "2024-12-15T12:00:01Z",
            "method": "POST",
            "path": "/api/v1/comentarios",
            "query": {},
            "headers": {"user-agent": "Mozilla/5.0"},
            "client_ip": "10.99.0.10",
            "body": "<script>alert('xss')</script>",
            "user_agent": "Mozilla/5.0",
        }
        ttp2 = logger.detect_ttp(req2)
        assert ttp2 is not None
        assert ttp2["technique_id"] == "T1059.007"
        print(f"OK - XSS detectado: {ttp2['technique_id']}")

        # Test LFI
        req3 = {
            "timestamp": "2024-12-15T12:00:02Z",
            "method": "GET",
            "path": "/api/v1/facturas/../../../etc/passwd",
            "query": {},
            "headers": {"user-agent": "Mozilla/5.0"},
            "client_ip": "10.99.0.10",
            "body": "",
            "user_agent": "Mozilla/5.0",
        }
        ttp3 = logger.detect_ttp(req3)
        assert ttp3 is not None
        print(f"OK - LFI detectado: {ttp3['technique_id']}")

        print("\nTodos los tests de detección pasaron.")


def test_deception_tokens():
    """Prueba la generación de tokens de engaño."""
    tokens = DeceptionTokens()

    aws = tokens.generate_aws_key()
    assert aws["access_key_id"].startswith("AKIA")
    print(f"OK - AWS key generada: {aws['access_key_id'][:15]}...")

    db = tokens.generate_db_connection_string()
    assert db["port"] == 5432
    print(f"OK - DB connection string generada: {db['host']}")

    jwt = tokens.generate_jwt_token()
    assert jwt.count(".") == 2
    print(f"OK - JWT generado: {jwt[:50]}...")

    print("\nTodos los tests de deception tokens pasaron.")


if __name__ == "__main__":
    test_attack_detection()
    test_deception_tokens()
    print("\nAll tests passed.")
