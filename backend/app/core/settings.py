from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "AI Interior Designer API"
    version: str = "0.4.0"
    default_user_id: str = os.getenv("DEFAULT_USER_ID", "demo-user")
    default_model_id: str = os.getenv("DEFAULT_MODEL_ID", "runwayml/stable-diffusion-v1-5")
    generation_provider: str = os.getenv("GENERATION_PROVIDER", "mock")


settings = Settings()
