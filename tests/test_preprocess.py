from deepcloud.preprocess import clean, normalize, tokenize


def test_clean_strips_urls_and_punctuation():
    assert clean("Check https://example.com now!!!") == "check now"


def test_clean_lowercases_and_collapses_space():
    assert clean("  Hello   WORLD  ") == "hello world"


def test_tokenize_drops_stopwords_and_short_tokens():
    tokens = tokenize("the cat sat on a mat")
    assert "the" not in tokens
    assert "cat" in tokens
    assert "mat" in tokens


def test_normalize_returns_joined_tokens():
    assert normalize("This is GREAT stuff!") == "great stuff"
