from backend.app.schemas.generation import GenerateRequest


def build_prompt(payload: GenerateRequest) -> str:
    parts = [payload.room_type, payload.style, payload.prompt]
    if payload.colors:
        parts.append("dominant colors: " + ", ".join(payload.colors))
    parts.append("photorealistic interior design, high detail")
    return ", ".join(parts)
