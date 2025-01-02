from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    BASE_URL: str
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str
    DEBUG: bool

    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    JWT_SECRET_KEY: str
    JWT_ISSUER: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_TTL_SECONDS: int
    JWT_REFRESH_TOKEN_TTL_SECONDS: int

    @property
    def async_postgres_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.DATABASE_HOST,
            port=self.DATABASE_PORT,
            username=self.DATABASE_USERNAME,
            password=self.DATABASE_PASSWORD,
            path=self.DATABASE_NAME,
        )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
