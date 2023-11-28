# Standard Libraries
import logging

# Third-party Libraries
# Third Party Libraries
from dotenv import load_dotenv
from pydantic import BaseSettings, Field, SecretStr

logger = logging.getLogger(__name__)
# Standard Libraries
import json

load_dotenv()


class PsychologySettings(BaseSettings):
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

    SITE_NAME: str = Field(env="SITE_NAME", default="Red Decires")
    GRAPHQL_URL: str = Field(
        env="GRAPHQL_URL",
        default="http://localhost:9000/api/graph/psychology/",
    )

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
        json_loads = json.loads


settings = PsychologySettings()
