# Standard Libraries
import logging

# Third-party Libraries
from dotenv import load_dotenv
from pydantic import BaseSettings, Field, SecretStr

logger = logging.getLogger(__name__)
# Standard Libraries
import json

load_dotenv()


class AWSSettings(BaseSettings):
    AWS_REGION_NAME: str = Field(default="us-east-1", env="AWS_REGION_NAME")
    AWS_ACCESS_KEY_ID: str | None = Field(default=None, env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str | None = Field(default=None, env="AWS_SECRET_ACCESS_KEY")
    AWS_ACCOUNT_ID: int | None = Field(default=None, env="AWS_ACCOUNT_ID")
    AWS_STAGE: str = Field(default="qa", env="AWS_STAGE")
    AWS_S3_BUCKET_NAME: str | None = Field(default=None, env="AWS_S3_BUCKET_NAME")

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
        json_loads = json.loads


aws_settings = AWSSettings()


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
    SITE_NAME: str = Field(env="SITE_NAME", default="Redpsidecires")
    DECIRES_URL: str = Field(
        env="DECIRES_URL",
        default="http://localhost:8000",
    )
    GRAPHQL_URL: str = Field(
        env="GRAPHQL_URL",
        default="http://localhost:9000/api/graph/psychology/",
    )
    MEDIA_URL: str | None = Field(default="/media/")
    STATIC_URL: str | None = Field(default="/static/")
    DECIRES_EMAIL: str = Field(default=None, env="DECIRES_EMAIL")
    DEFAULT_THUMBNAIL_FEMALE_IMAGE: str = Field(
        default="assets/img/user/female_user.jpg"
    )
    DEFAULT_THUMBNAIL_MALE_IMAGE: str = Field(default="assets/img/user/male_user.jpg")
    AWS_SETTINGS: AWSSettings | None = aws_settings

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
        json_loads = json.loads


settings = PsychologySettings()
