from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "AI Interior Designer API"
    version: str = "0.3.0"
    default_user_id: str = "demo-user"


settings = Settings()
