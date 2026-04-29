from fastapi import FastAPI

from backend.app.core.settings import settings
from backend.app.routers.generation import router as generation_router
from backend.app.routers.history import router as history_router

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(generation_router)
app.include_router(history_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ai-interior-designer", "version": settings.version}
