# AI Interior Designer 🏠✨

## Current Status (v0.3 scaffold)

Implemented foundation:
- FastAPI app with router-based structure
- Generation router (`/generate/text-to-image`, `/generate/image-to-image`)
- History router (`/history/{user_id}`)
- Shared settings module (`backend/app/core/settings.py`)
- Prompt builder + generation service layers
- Streamlit UI for prompt submission and history viewing

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Frontend:
```bash
streamlit run frontend/app.py
```

## Immediate Next

1. Replace `generation_service.generate_from_text` mock logic with Diffusers pipeline.
2. Add async background job queue for long-running generation.
3. Swap in-memory `history_store` with MongoDB repository.
4. Add image persistence layer (S3/Cloudflare R2/local media).
