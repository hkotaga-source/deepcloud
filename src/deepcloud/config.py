from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DEEPCLOUD_", env_file=".env", extra="ignore"
    )

    service_name: str = "deepcloud"
    version: str = "0.1.0"
    model_path: Path = Path("models/classifier.joblib")
    log_level: str = "info"
    max_batch: int = 64
    confidence_threshold: float = 0.5


@lru_cache
def get_settings() -> Settings:
    return Settings()
