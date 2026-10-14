import re

URL_RE = re.compile(r"https?://\S+")
NON_WORD_RE = re.compile(r"[^a-z0-9\s]")
SPACE_RE = re.compile(r"\s+")

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "is", "it",
    "this", "that", "for", "on", "with", "as", "at", "be",
}


def clean(text: str) -> str:
    text = text.lower()
    text = URL_RE.sub(" ", text)
    text = NON_WORD_RE.sub(" ", text)
    text = SPACE_RE.sub(" ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    return [t for t in clean(text).split() if t not in STOPWORDS and len(t) > 1]


def normalize(text: str) -> str:
    return " ".join(tokenize(text))
