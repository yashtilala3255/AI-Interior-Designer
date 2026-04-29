from fastapi import APIRouter

from backend.app.services import history_store

router = APIRouter(prefix="/history", tags=["history"])


@router.get("/{user_id}")
def get_history(user_id: str) -> dict:
    return {"user_id": user_id, "items": history_store.get(user_id)}
