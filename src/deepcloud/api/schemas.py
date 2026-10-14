from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1)


class PredictionOut(BaseModel):
    label: str
    confidence: float
    below_threshold: bool


class PredictResponse(BaseModel):
    predictions: list[PredictionOut]
    count: int


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class ReadyResponse(BaseModel):
    ready: bool
    model_loaded: bool
