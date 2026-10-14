from fastapi import APIRouter, HTTPException

from ..config import get_settings
from ..service import ClassificationService
from .schemas import (
    HealthResponse,
    PredictionOut,
    PredictRequest,
    PredictResponse,
    ReadyResponse,
)

router = APIRouter()
service = ClassificationService()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    s = get_settings()
    return HealthResponse(status="ok", service=s.service_name, version=s.version)


@router.get("/ready", response_model=ReadyResponse)
def ready() -> ReadyResponse:
    try:
        service.load()
    except FileNotFoundError:
        return ReadyResponse(ready=False, model_loaded=False)
    return ReadyResponse(ready=True, model_loaded=service.loaded)


@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest) -> PredictResponse:
    try:
        preds = service.predict(req.texts)
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="model not loaded") from None
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from None
    return PredictResponse(
        predictions=[PredictionOut(**p.__dict__) for p in preds],
        count=len(preds),
    )
