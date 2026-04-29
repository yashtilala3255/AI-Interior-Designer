from uuid import uuid4

from fastapi import APIRouter, File, Form, UploadFile

from backend.app.core.settings import settings
from backend.app.schemas.generation import GenerateRequest, GenerationResult
from backend.app.services import history_store
from backend.app.services.generation_service import generate_from_text

router = APIRouter(prefix="/generate", tags=["generation"])


@router.post("/text-to-image", response_model=GenerationResult)
def text_to_image(payload: GenerateRequest) -> GenerationResult:
    result = generate_from_text(payload)
    history_store.add(settings.default_user_id, result.model_dump())
    return result


@router.post("/image-to-image")
def image_to_image(prompt: str = Form(...), image: UploadFile = File(...)) -> dict:
    generation_id = str(uuid4())
    result = {
        "id": generation_id,
        "message": "Mock image-to-image completed. Plug in ControlNet next.",
        "filename": image.filename,
        "content_type": image.content_type,
        "prompt": prompt,
        "image_url": f"/static/generated/{generation_id}.png",
    }
    history_store.add(settings.default_user_id, result)
    return result
