from fastapi.testclient import TestClient
from backend.app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_text_to_image_endpoint() -> None:
    payload = {
        "prompt": "cozy bedroom",
        "room_type": "bedroom",
        "style": "minimalist",
        "colors": ["beige", "white"],
    }
    response = client.post("/generate/text-to-image", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"]
    assert "photorealistic interior design" in data["prompt"]


def test_history_endpoint() -> None:
    response = client.get("/history/demo-user")
    assert response.status_code == 200
    assert "items" in response.json()
