# AI Interior Designer 🏠✨

A practical, step-by-step guide to start and build an **AI Interior Designer** web app from scratch.

---

## 1) Project Goal

Build a web app where users can:
- Enter a text prompt describing a room.
- Optionally upload an existing room image for redesign.
- Select room type, style, and color palette.
- Generate high-quality interior visuals with Stable Diffusion + ControlNet.
- (Optional) Get furniture recommendations that match the design.

---

## 2) Recommended MVP Scope (Start Here)

For fastest progress, launch with this MVP first:
1. Text-to-image generation.
2. Room type + style + color controls.
3. Basic history of generations.
4. Download generated image.

Add later:
- Image-to-image redesign (ControlNet).
- ESRGAN upscaling.
- Furniture recommendation engine.

---

## 3) Architecture (Implementation View)

```text
Frontend (React or Streamlit)
   -> FastAPI backend
      -> Prompt builder service
      -> Stable Diffusion service (txt2img)
      -> ControlNet service (img2img, optional)
      -> Upscaler service (ESRGAN, optional)
      -> Storage layer (MongoDB + object storage)
```

---

## 4) Week-by-Week Execution Plan (12 Weeks)

## Week 1: Environment Setup & Repo Structure

### Deliverables
- Working Python environment.
- Running FastAPI skeleton.
- Basic frontend skeleton.

### Tasks
1. Create project structure:
   - `backend/` (FastAPI)
   - `frontend/` (React or Streamlit)
   - `ml/` (model pipelines)
   - `data/` (datasets metadata, not raw huge datasets)
   - `infra/` (Docker, deployment configs)
2. Set up Python dependencies:
   - `torch`, `diffusers`, `transformers`, `accelerate`
   - `opencv-python`, `Pillow`, `numpy`
   - `fastapi`, `uvicorn`, `pydantic`
3. Add `.env` and config loader.
4. Add GPU detection script and startup health check.

### Exit Criteria
- `GET /health` returns success.
- One test endpoint works end-to-end from frontend.

---

## Week 2: Prompt Engineering Module

### Deliverables
- Prompt builder that transforms user intent into robust generation prompts.

### Tasks
1. Define controlled vocabularies:
   - Room types (bedroom, kitchen, living room, office, etc.)
   - Styles (minimalist, modern, bohemian, industrial, etc.)
   - Lighting tags
   - Color tokens
2. Build prompt template format:
   - Positive prompt
   - Negative prompt
   - Quality suffix (photorealistic, high detail, 4k, etc.)
3. (Optional) Integrate lightweight LLM enhancement layer.
4. Save generated prompt metadata for reproducibility.

### Exit Criteria
- Given same input options, pipeline produces deterministic prompt string.

---

## Week 3-4: Core Stable Diffusion Text-to-Image Pipeline

### Deliverables
- Working txt2img generation endpoint.

### Tasks
1. Start with one base model:
   - `stabilityai/stable-diffusion-2-1` **or** `runwayml/stable-diffusion-v1-5`
2. Implement generation parameters:
   - seed, steps, guidance scale, width/height
3. Add API endpoint:
   - `POST /generate/text-to-image`
4. Add safeguards:
   - timeout handling
   - memory checks and fallback resolutions
5. Persist outputs:
   - generated image path/URL
   - full prompt, model, parameters, timestamp

### Exit Criteria
- User submits prompt and receives generated image reliably.

---

## Week 5-6: Image-to-Image Redesign with ControlNet

### Deliverables
- Structure-preserving redesign feature with uploaded room photos.

### Tasks
1. Add image upload endpoint and validation.
2. Generate condition map:
   - depth map (MiDaS) or Canny edge
3. Integrate ControlNet model:
   - `lllyasviel/sd-controlnet-depth` (recommended first)
4. Add API endpoint:
   - `POST /generate/image-to-image`
5. Tune strength and conditioning scale for layout preservation.

### Exit Criteria
- Uploaded room retains geometry while style changes according to prompt.

---

## Week 7-8: Frontend Product UI

### Deliverables
- Usable interface for non-technical users.

### Tasks
1. Build form controls:
   - room type selector
   - style dropdown
   - color picker
   - prompt input
2. Add generation controls:
   - model settings panel (optional advanced section)
3. Add output components:
   - gallery cards
   - before/after comparison slider (for img2img)
4. Add progress + error states.

### Exit Criteria
- Full user journey works without backend manual intervention.

---

## Week 9-10: Super Resolution + Polishing

### Deliverables
- Optional upscaling and improved user experience.

### Tasks
1. Integrate Real-ESRGAN as post-process step.
2. Add endpoint:
   - `POST /enhance/upscale`
3. Add download button and history view.
4. Add request quotas/rate limits to protect GPU resources.

### Exit Criteria
- Users can generate and download high-resolution versions.

---

## Week 11-12: Evaluation, Hardening, and Deployment

### Deliverables
- Production-ready demo deployment.

### Tasks
1. Evaluate quality:
   - FID (batch-level)
   - CLIP score (prompt alignment)
   - MOS user survey
   - SSIM for img2img consistency
2. Add observability:
   - request logs, latency, GPU memory usage
3. Containerize with Docker.
4. Deploy to Hugging Face Spaces / RunPod / Streamlit Cloud.
5. Prepare demo video and documentation.

### Exit Criteria
- Public demo URL is stable and documented.

---

## 5) Backend API Contract (Starter)

- `GET /health`
- `POST /generate/text-to-image`
- `POST /generate/image-to-image`
- `POST /enhance/upscale`
- `GET /history/{user_id}`

Suggested request fields:
- prompt, room_type, style, colors, negative_prompt
- steps, guidance_scale, width, height, seed
- image file (for img2img)

---

## 6) Data & Model Strategy

### Datasets (for improvement/fine-tuning)
- ADE20K (scene/room understanding)
- LSUN Rooms
- InteriorNet
- Curated style datasets (Houzz/Pinterest with proper licensing)

### Important note
For initial MVP, **do not block on fine-tuning**. Use pretrained models first, then iterate.

---

## 7) DevOps & Cost Control Checklist

1. Use async job queue for generation (Celery/RQ/Redis) if load increases.
2. Cache repeated prompts where possible.
3. Auto-shutdown idle GPU workers.
4. Add usage caps per user.
5. Track per-image generation cost.

---

## 8) Security & Compliance Checklist

1. Validate and sanitize uploaded files.
2. Set max file size and allowed MIME types.
3. Add auth before exposing public endpoints.
4. Log generation metadata (without sensitive user content where possible).
5. Respect model licenses and dataset copyright terms.

---

## 9) “Start Today” Command Plan

1. Initialize backend and install deps.
2. Run a minimal txt2img script locally.
3. Wrap script in FastAPI endpoint.
4. Connect a minimal frontend form.
5. Test prompt -> image path.
6. Add logging, retries, and timeout handling.
7. Ship MVP.

---

## 10) Success Criteria for MVP

You are ready for demo when:
- Prompt-to-image latency is acceptable (<20-40s on target GPU).
- At least 3 styles generate visually distinct outputs.
- Users can regenerate with same seed for reproducibility.
- History + download work consistently.

---

## 11) Next-Level Extensions

- Personalized style profiles per user.
- Furniture detection + recommendation via catalog APIs.
- AR preview with Three.js/WebXR.
- Multi-room scene planner.
- SaaS billing and team workspaces.

