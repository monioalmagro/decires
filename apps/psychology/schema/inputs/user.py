# Third-party Libraries
import strawberry
from pydantic import BaseModel, validator

# Own Libraries
from apps.psychology.schema.enums.user_carreer import CarreerServiceMethodEnum


class QueryListPydanticModel(BaseModel):
    carreer: strawberry.ID
    service_method_enum: CarreerServiceMethodEnum
    city: strawberry.ID
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
    is_active: bool
    nro_dni: str
    nro_matricula: str
    cuit: str
    phone: str
    gender: int
    facebook_profile: str
    instagram_profile: str
    linkedin_profile: str
    image_profile: str | None = None
    is_verified_profile: bool
    personal_address: str

    @validator(
        "first_name",
        "last_name",
        "email",
        "last_name",
        "nro_dni",
        "nro_matricula",
        "cuit",
        "phone",
        "personal_address",
    )
    @classmethod
    def validate_first_name(cls, name):
        if len(name) == 0:
            raise AssertionError("INPUT INVALID")
        return name.strip()

    @validator('email')
    def email_format(cls, v):
        if not cls.validate_email(v):
            raise ValueError('Formato de correo electrónico no válido')
        return v

    @classmethod
    def validate_email(cls, email):
        return '@' in email and '.' in email


@strawberry.experimental.pydantic.input(
    model=MutationUserPydanticModel,
    all_fields=True,
)
class MutationUserInput:
    pass
