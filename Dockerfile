FROM python:3.12-slim AS builder

WORKDIR /app
ENV PIP_NO_CACHE_DIR=1
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt


FROM python:3.12-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src

WORKDIR /app
COPY --from=builder /install /usr/local
COPY src ./src
COPY data ./data
COPY scripts ./scripts

RUN python scripts/train.py --data data/sample.csv --out models/classifier.joblib

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "deepcloud.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
