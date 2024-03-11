# Third-party Libraries
import strawberry
from django.core.validators import validate_email
from pydantic import BaseModel, validator

# Own Libraries
from apps.psychology.schema.enums.auth_user import (
    AuthUserGenderEnum,
    AuthUserMembershipPlanEnum,
)
from apps.psychology.schema.enums.user_carreer import (
    CarreerServiceMethodEnum,
    CarreerServiceModalityEnum,
)
from config.enviroment_vars import settings


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
    first_name: str
    last_name: str | None = None
    password: str | None = settings.PASSWORD_DEFAULT.get_secret_value()
    password_confirm: str | None = settings.PASSWORD_DEFAULT.get_secret_value()
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
    attention_schedule: str | None = None
    membership_plan_enum: AuthUserMembershipPlanEnum | None = (
        AuthUserMembershipPlanEnum.BASICO
    )

    @validator("experience_summary")
    @classmethod
    def validate_experience_summary(cls, experience_summary):
        if experience_summary:
            experience_summary = experience_summary.strip()
            if len(experience_summary) < 1 or len(experience_summary) > 500:
                raise AssertionError("Experience summary invalid")
        return experience_summary.strip()

    @validator("first_name")
    @classmethod
    def validate_first_name(cls, name):
        if len(name) == 0:
            raise AssertionError("NOMBRE INVALIDO")
        return name.strip()

    @validator("last_name")
    @classmethod
    def validate_last_name(cls, last_name):
        if len(last_name) == 0:
            raise AssertionError("APELLIDO INVALIDO")
        return last_name.strip()

    @validator("nro_dni")
    @classmethod
    def validate_nro_dni(cls, nro_dni):
        if len(nro_dni) == 0:
            raise AssertionError("DNI INVALIDO")
        return nro_dni.strip()

    @validator("nro_matricula")
    @classmethod
    def validate_nro_matricula(cls, nro_matricula):
        if len(nro_matricula) == 0:
            raise AssertionError("MATRICULA INVALIDO")
        return nro_matricula.strip()

    @validator("cuit")
    @classmethod
    def validate_cuit(cls, cuit):
        if len(cuit) == 0:
            raise AssertionError("CUIT INVALIDO")
        return cuit.strip()

    @validator("phone")
    @classmethod
    def validate_phone(cls, phone):
        if len(phone) == 0:
            raise AssertionError("TELEFONO INVALIDO")
        return phone.strip()

    @validator("attention_schedule")
    @classmethod
    def validate_attention_schedule(cls, attention_schedule):
        if len(attention_schedule) == 0:
            raise AssertionError("HORARIO DE ATENCION INVALIDO")
        return attention_schedule.strip()

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
        return languages or ["1"]

    class Config:
        use_enum_values = True


@strawberry.experimental.pydantic.input(
    model=MutationUserPydanticModel,
    all_fields=True,
)
class MutationUserInput:
    pass
