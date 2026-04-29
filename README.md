# AI Interior Designer 🏠✨

## Week 1 to Week 4 Completed (Foundation + Prompt + Core Pipeline Contract)

### ✅ Week 1: Environment and backend foundation
- FastAPI application scaffolded with modular routers and services.
- Centralized settings via environment-aware config (`core/settings.py`).
- Health endpoint includes runtime capability detection (torch/cuda flags).

### ✅ Week 2: Prompt engineering module
- Prompt schema now includes room type, style, lighting, color palette.
- Deterministic prompt template implemented in `services/prompt_builder.py`.
- Negative prompt and generation parameters are part of request contract.

### ✅ Week 3-4: Core generation pipeline contract
- Text-to-image endpoint supports full generation controls:
  - `steps`, `guidance_scale`, `width`, `height`, `seed`, `model_id`
- Provider switch introduced (`GENERATION_PROVIDER`) with mock default.
- Structured generation response includes prompt, selected model, and settings.

## Endpoints
- `GET /health`
- `POST /generate/text-to-image`
- `POST /generate/image-to-image` (placeholder for Week 5-6 ControlNet)
- `GET /history/{user_id}`

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

## Test
```bash
pytest -q
```

## Next (Week 5-6)
- Implement MiDaS/depth preprocessing.
- Integrate ControlNet for structure-preserving redesign.
- Add upload validation and persistent media storage.
