from __future__ import annotations

from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from .preprocess import normalize


def build_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(preprocessor=normalize, ngram_range=(1, 2), min_df=1)),
            ("clf", LogisticRegression(max_iter=1000, C=4.0)),
        ]
    )


class TextClassifier:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    @classmethod
    def load(cls, path: str | Path) -> TextClassifier:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"model not found: {path}")
        return cls(joblib.load(path))

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, path)

    def train(self, texts: list[str], labels: list[str]) -> None:
        self.pipeline.fit(texts, labels)

    def predict(self, texts: list[str]) -> list[tuple[str, float]]:
        probs = self.pipeline.predict_proba(texts)
        classes = self.pipeline.classes_
        out: list[tuple[str, float]] = []
        for row in probs:
            idx = int(row.argmax())
            out.append((str(classes[idx]), float(row[idx])))
        return out
