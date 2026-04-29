from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.services.prompt_builder import build_prompt
from backend.app.schemas.generation import GenerateRequest


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "runtime" in data


def test_prompt_builder_deterministic() -> None:
    payload = GenerateRequest(
        prompt="cozy setup",
        room_type="bedroom",
        style="minimalist",
        lighting="warm",
        colors=["beige", "white"],
    )
    prompt = build_prompt(payload)
    assert "bedroom interior" in prompt
    assert "warm lighting" in prompt
    assert "beige, white" in prompt


def test_text_to_image_endpoint() -> None:
    payload = {
        "prompt": "cozy bedroom",
        "room_type": "bedroom",
        "style": "minimalist",
        "lighting": "warm",
        "colors": ["beige", "white"],
    }
    response = client.post("/generate/text-to-image", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"]
    assert data["model_id"]


def test_history_endpoint() -> None:
    response = client.get("/history/demo-user")
    assert response.status_code == 200
    assert "items" in response.json()
