export PYTHONPATH := src

.PHONY: install train serve test lint format docker-build clean

install:
	pip install -r requirements-dev.txt

train:
	python scripts/train.py --data data/sample.csv --out models/classifier.joblib

serve:
	uvicorn deepcloud.api.main:app --reload --port 8000

test:
	pytest --cov=deepcloud --cov-report=term-missing

lint:
	ruff check src tests

format:
	ruff format src tests

docker-build:
	docker build -t deepcloud:latest .

clean:
	rm -rf models/*.joblib .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
