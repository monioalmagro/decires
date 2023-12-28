# Standard Libraries
import enum

# Third-party Libraries
import strawberry

# Own Libraries
from apps.core import core_constants


@strawberry.enum()
class AuthUserGenderEnum(enum.Enum):
    MASCULINO = strawberry.enum_value(value=core_constants.HOMBRE)
    FEMENINO = strawberry.enum_value(value=core_constants.MUJER)
