# Third-party Libraries
import strawberry
from django.core.validators import validate_email
from pydantic import BaseModel, validator

# Own Libraries
from apps.psychology.schema.enums.auth_user import AuthUserGenderEnum
from apps.psychology.schema.enums.user_carreer import (
    CarreerServiceMethodEnum,
    CarreerServiceModalityEnum,
)


class QueryListPydanticModel(BaseModel):
    carreer: strawberry.ID
    service_method_enum: CarreerServiceMethodEnum
    city: strawberry.ID | None = None
    zone: strawberry.ID | None = None

    class Config:
        use_enum_values = True


@strawberry.experimental.pydantic.input(
    model=QueryListPydanticModel,
    all_fields=True,
)
class QueryListUserInput:
    pass


@strawberry.input()
class QueryRetrieveUserInput:
    original_id: strawberry.ID


class MutationUserPydanticModel(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str | None = None
    password: str
    password_confirm: str
    nro_dni: str
    nro_matricula: str
    cuit: str
    phone: str
    gender_enum: AuthUserGenderEnum
    service_method_enum: CarreerServiceMethodEnum
    service_modality_enum: CarreerServiceModalityEnum
    facebook_profile: str | None = None
    instagram_profile: str | None = None
    linkedin_profile: str | None = None
    personal_address: str | None = None
    office_locations: list[strawberry.ID] | None = None
    carreer: strawberry.ID | None = None
    languages: list[strawberry.ID] | None = None
    specializations: list[strawberry.ID] = None
    experience_summary: str | None = None
    attachment_ids: list[strawberry.ID] = None

    @validator("experience_summary")
    @classmethod
    def validate_experience_summary(cls, experience_summary):
        if experience_summary:
            experience_summary = experience_summary.strip()
            if len(experience_summary) < 1 or len(experience_summary) > 500:
                raise AssertionError("Experience summary invalid")
        return experience_summary.strip()

    @validator(
        "first_name",
        "last_name",
        "nro_dni",
        "nro_matricula",
        "cuit",
        "phone",
    )
    @classmethod
    def validate_first_name(cls, name):
        if len(name) == 0:
            raise AssertionError("INPUT INVALID")
        return name.strip()

    @validator("username")
    @classmethod
    def username_check(cls, username):
        _username = username.strip()
        if len(_username) == 0:
            raise AssertionError("INPUT USERNAME INVALID")
        return _username

    @validator("email")
    @classmethod
    def email_check(cls, email):
        try:
            if len(email) == 0:
                raise AssertionError("INPUT EMAIL INVALID")
            # django validator
            validate_email(value=email)
        except Exception as exp:
            raise AssertionError(str(exp)) from exp
        return email

    @validator("languages")
    @classmethod
    def languages_check(cls, languages):
        return languages or []

    @validator("password")
    @classmethod
    def validate_password(cls, value):
        # Verificar que la contraseña contiene al menos 1 minúscula
        if not any(char.islower() for char in value):
            raise AssertionError("La contraseña debe contener al menos una minúscula")

        # Verificar que la contraseña contiene al menos 1 mayúscula
        if not any(char.isupper() for char in value):
            raise AssertionError("La contraseña debe contener al menos una mayúscula")

        # Verificar que la contraseña contiene al menos 1 carácter especial
        if not any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]" for char in value):
            raise AssertionError(
                "La contraseña debe contener al menos un carácter especial"
            )

        return value

    @validator("password_confirm")
    @classmethod
    def validate_password_confirm(cls, value, values):
        # Verificar que la contraseña y su confirmación son iguales
        if "password" in values and value != values["password"]:
            raise AssertionError("Las contraseñas no coinciden")

        return value

    class Config:
        use_enum_values = True


@strawberry.experimental.pydantic.input(
    model=MutationUserPydanticModel,
    all_fields=True,
)
class MutationUserInput:
    pass
