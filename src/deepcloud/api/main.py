from fastapi import FastAPI

from ..config import get_settings
from .routes import router


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.service_name, version=settings.version)
    app.include_router(router)
    return app


app = create_app()
