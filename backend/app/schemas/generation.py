from pydantic import BaseModel, Field
from typing import Optional


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=3)
    room_type: str = "living room"
    style: str = "modern"
    colors: list[str] = Field(default_factory=list)
    negative_prompt: str = "blurry, low quality, distorted"
    steps: int = Field(default=30, ge=10, le=100)
    guidance_scale: float = Field(default=7.5, ge=1.0, le=20.0)
    width: int = Field(default=512, ge=256, le=1024)
    height: int = Field(default=512, ge=256, le=1024)
    seed: Optional[int] = None


class GenerationResult(BaseModel):
    id: str
    message: str
    prompt: str
    negative_prompt: str
    image_url: str
    settings: dict
