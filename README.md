# deepcloud

A text-classification service that runs behind an HTTP API and ships to AWS ECS.

The model is a TF-IDF + logistic regression pipeline wrapped in FastAPI. It is a
starting point for putting a trained model behind an API on the cloud, not a
state-of-the-art classifier.

## Run

```
make install
make train
make serve
```

## API

```
POST /predict   {"texts": ["great product, fast shipping"]}
GET  /health
GET  /ready
```

## Test

```
make test
```

## Deploy

Build and push the image, then apply the infrastructure:

```
make docker-build
docker tag deepcloud:latest <ecr-url>:latest
docker push <ecr-url>:latest
cd infra && terraform init && terraform apply
```

Settings come from environment variables — see `.env.example`.

## Layout

`src/deepcloud` holds the code (config, preprocessing, model, service, API, CLI).
`scripts` and `data` cover training, `tests` the suite, `infra` the Terraform.
