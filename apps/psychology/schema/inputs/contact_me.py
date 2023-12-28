# Standard Libraries
import re

# Third-party Libraries
import strawberry
from pydantic import BaseModel, constr, validator


class ContactMePydanticModel(BaseModel):
    user_id: strawberry.ID
    full_name: str
    email: str
    phone: constr()
    message: str

    @validator("phone")
    @classmethod
    def validate_phone(cls, value):
        pattern = r"^\+\d{2} \(\d{3}\) \d{3}\.\d{2}\.\d{2}$"

        if not re.match(pattern, value):
            raise AssertionError("Número de teléfono con formato incorrecto")

        return value


@strawberry.experimental.pydantic.input(
    model=ContactMePydanticModel,
    all_fields=True,
)
class MutationContactMeInput:
    pass
