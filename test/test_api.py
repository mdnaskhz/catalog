from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    r = client.get("/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_add_product():
    r = client.post("/products", json={"name": "Pen", "price": 10, "category": "office"})
    assert r.status_code == 200
