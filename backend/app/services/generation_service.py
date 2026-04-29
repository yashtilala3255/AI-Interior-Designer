from uuid import uuid4

from backend.app.schemas.generation import GenerateRequest, GenerationResult
from backend.app.services.prompt_builder import build_prompt


def generate_from_text(payload: GenerateRequest) -> GenerationResult:
    prompt = build_prompt(payload)
    generation_id = str(uuid4())
    return GenerationResult(
        id=generation_id,
        message="Mock generation completed. Plug in diffusers pipeline next.",
        prompt=prompt,
        negative_prompt=payload.negative_prompt,
        image_url=f"/static/generated/{generation_id}.png",
        settings={
            "steps": payload.steps,
            "guidance_scale": payload.guidance_scale,
            "width": payload.width,
            "height": payload.height,
            "seed": payload.seed,
        },
    )
