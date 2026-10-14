import os
from pathlib import Path

import pytest

os.environ.setdefault(
    "DEEPCLOUD_MODEL_PATH", str(Path(__file__).parent / "_test_model.joblib")
)


@pytest.fixture(scope="session", autouse=True)
def trained_model():
    from deepcloud.model import TextClassifier, build_pipeline

    path = Path(os.environ["DEEPCLOUD_MODEL_PATH"])
    texts = [
        "great product love it",
        "works perfectly and fast",
        "terrible waste of money",
        "broke after a single day",
    ]
    labels = ["positive", "positive", "negative", "negative"]

    clf = TextClassifier(build_pipeline())
    clf.train(texts, labels)
    clf.save(path)
    yield
    path.unlink(missing_ok=True)
