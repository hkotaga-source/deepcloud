from deepcloud.model import TextClassifier, build_pipeline


def _trained() -> TextClassifier:
    clf = TextClassifier(build_pipeline())
    clf.train(
        ["i love it", "this is great", "awful and broken", "worst ever"],
        ["pos", "pos", "neg", "neg"],
    )
    return clf


def test_predict_returns_label_and_score():
    clf = _trained()
    preds = clf.predict(["love it"])
    label, score = preds[0]
    assert label == "pos"
    assert 0.0 <= score <= 1.0


def test_predict_separates_classes():
    clf = _trained()
    assert clf.predict(["broken mess"])[0][0] == "neg"


def test_save_and_load_roundtrip(tmp_path):
    clf = _trained()
    path = tmp_path / "model.joblib"
    clf.save(path)

    loaded = TextClassifier.load(path)
    assert loaded.predict(["great"])[0][0] == "pos"


def test_load_missing_file_raises(tmp_path):
    import pytest

    with pytest.raises(FileNotFoundError):
        TextClassifier.load(tmp_path / "nope.joblib")
