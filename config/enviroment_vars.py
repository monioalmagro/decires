# Standard Libraries
import logging

# Third-party Libraries
# Third Party Libraries
from dotenv import load_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

load_dotenv()


class PsychologySettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    COMPOSE_PROJECT_NAME: str = Field(
        default="psychology",
        env="COMPOSE_PROJECT_NAME",
    )
    DJANGO_SETTINGS_MODULE: str = Field(
        env="DJANGO_SETTINGS_MODULE",
        default="config.settings.base",
    )
    SECRET_KEY: SecretStr | None = Field(
        default="*",
        env="SECRET_KEY",
    )
    DEBUG: bool = Field(env="DEBUG", default=True)
    JWT_SECRET_KEY: SecretStr | None = Field(
        default="insecure-jwt-secret-key",
        env="JWT_SECRET_KEY",
    )
    DATABASE_URL: str | None = Field(
        default="postgresql://postgres:postgres@postgres:5432/psychology_db",
        env="DATABASE_URL",
    )
    DJANGO_ALLOW_ASYNC_UNSAFE: bool | None = Field(
        default=True,
        env="DJANGO_ALLOW_ASYNC_UNSAFE",
    )


settings = PsychologySettings()
