from __future__ import annotations

from dataclasses import dataclass

from .config import Settings, get_settings
from .model import TextClassifier
from .preprocess import normalize


@dataclass
class Prediction:
    label: str
    confidence: float
    below_threshold: bool


class ClassificationService:
    def __init__(self, settings: Settings | None = None):
        self.settings = settings or get_settings()
        self._classifier: TextClassifier | None = None

    @property
    def loaded(self) -> bool:
        return self._classifier is not None

    def load(self) -> None:
        if self._classifier is None:
            self._classifier = TextClassifier.load(self.settings.model_path)

    def predict(self, texts: list[str]) -> list[Prediction]:
        if len(texts) > self.settings.max_batch:
            raise ValueError(
                f"batch too large: {len(texts)} > {self.settings.max_batch}"
            )
        self.load()
        assert self._classifier is not None
        cleaned = [normalize(t) for t in texts]
        results = self._classifier.predict(cleaned)
        return [
            Prediction(
                label=label,
                confidence=round(score, 4),
                below_threshold=score < self.settings.confidence_threshold,
            )
            for label, score in results
        ]
