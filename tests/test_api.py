from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_prediction_field():
    sample = {"features": [54, 130, 246, 0, 150, 1.0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1]}
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    body = response.json()
    assert "prediction" in body
    assert "heart_disease_probability" in body
