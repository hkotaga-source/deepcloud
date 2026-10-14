import argparse

from deepcloud.cli import train


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the classifier from a CSV")
    parser.add_argument("--data", default="data/sample.csv")
    parser.add_argument("--out", default="models/classifier.joblib")
    train(parser.parse_args())


if __name__ == "__main__":
    main()
