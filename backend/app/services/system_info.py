def detect_runtime() -> dict:
    try:
        import torch  # type: ignore

        return {
            "torch_available": True,
            "cuda_available": bool(torch.cuda.is_available()),
            "device_count": int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,
        }
    except Exception:
        return {"torch_available": False, "cuda_available": False, "device_count": 0}
