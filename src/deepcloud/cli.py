from __future__ import annotations

import argparse
import csv

import uvicorn

from .config import get_settings
from .model import TextClassifier, build_pipeline


def train(args: argparse.Namespace) -> None:
    texts: list[str] = []
    labels: list[str] = []
    with open(args.data, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            texts.append(row["text"])
            labels.append(row["label"])

    clf = TextClassifier(build_pipeline())
    clf.train(texts, labels)
    clf.save(args.out)
    print(f"trained on {len(texts)} rows -> {args.out}")


def serve(args: argparse.Namespace) -> None:
    settings = get_settings()
    uvicorn.run(
        "deepcloud.api.main:app",
        host=args.host,
        port=args.port,
        log_level=settings.log_level,
    )


def main() -> None:
    parser = argparse.ArgumentParser(prog="deepcloud")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_train = sub.add_parser("train", help="train the classifier")
    p_train.add_argument("--data", required=True)
    p_train.add_argument("--out", default="models/classifier.joblib")
    p_train.set_defaults(func=train)

    p_serve = sub.add_parser("serve", help="run the API")
    p_serve.add_argument("--host", default="0.0.0.0")
    p_serve.add_argument("--port", type=int, default=8000)
    p_serve.set_defaults(func=serve)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
