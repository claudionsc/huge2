from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/huge2"
    app_name: str = "ALVI"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = True
    secret_key: str = "dev-secret-key-change-in-production"
    tailwind_cdn: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()