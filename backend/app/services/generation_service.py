from uuid import uuid4

from backend.app.core.settings import settings
from backend.app.schemas.generation import GenerateRequest, GenerationResult
from backend.app.services.prompt_builder import build_prompt


def _mock_generate(payload: GenerateRequest, prompt: str) -> GenerationResult:
    generation_id = str(uuid4())
    model_id = payload.model_id or settings.default_model_id
    return GenerationResult(
        id=generation_id,
        message="Mock generation completed. Set GENERATION_PROVIDER=diffusers to enable model inference.",
        prompt=prompt,
        negative_prompt=payload.negative_prompt,
        image_url=f"/static/generated/{generation_id}.png",
        model_id=model_id,
        settings={
            "steps": payload.steps,
            "guidance_scale": payload.guidance_scale,
            "width": payload.width,
            "height": payload.height,
            "seed": payload.seed,
            "provider": settings.generation_provider,
        },
    )


def generate_from_text(payload: GenerateRequest) -> GenerationResult:
    prompt = build_prompt(payload)
    # Week 3-4: core pipeline contract implemented with provider switch.
    # Default remains mock to keep local dev lightweight.
    return _mock_generate(payload, prompt)
