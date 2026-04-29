from backend.app.schemas.generation import GenerateRequest


def build_prompt(payload: GenerateRequest) -> str:
    parts = [
        f"{payload.room_type} interior",
        payload.style,
        f"{payload.lighting} lighting",
        payload.prompt,
    ]
    if payload.colors:
        parts.append("dominant color palette: " + ", ".join(payload.colors))
    parts.append("photorealistic, ultra-detailed, architectural digest style")
    return ", ".join(parts)
