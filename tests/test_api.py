from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_prediction_field():
    sample = {
        "Age": 48,
        "Sex": "F",
        "ChestPainType": "ASY",
        "RestingBP": 138,
        "Cholesterol": 214,
        "FastingBS": 0,
        "RestingECG": "Normal",
        "MaxHR": 108,
        "ExerciseAngina": "Y",
        "Oldpeak": 1.5,
        "ST_Slope": "Flat"
    }
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    body = response.json()
    assert "prediction" in body
    assert "heart_disease_probability" in body