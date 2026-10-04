from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_health():
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"ok": True}
