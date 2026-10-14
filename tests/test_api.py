from fastapi.testclient import TestClient

from deepcloud.api.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["service"] == "deepcloud"


def test_ready_reports_loaded_model():
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json()["ready"] is True


def test_predict_single_text():
    r = client.post("/predict", json={"texts": ["absolutely love this product"]})
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 1
    assert body["predictions"][0]["label"] in {"positive", "negative"}


def test_predict_batch():
    r = client.post("/predict", json={"texts": ["great", "awful"]})
    assert r.status_code == 200
    assert r.json()["count"] == 2


def test_predict_rejects_empty_batch():
    r = client.post("/predict", json={"texts": []})
    assert r.status_code == 422


def test_predict_rejects_oversized_batch():
    r = client.post("/predict", json={"texts": ["x"] * 100})
    assert r.status_code == 422
