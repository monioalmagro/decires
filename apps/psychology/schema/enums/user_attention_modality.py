# Standard Libraries
import enum

# Third-party Libraries
import strawberry


@strawberry.enum()
class AttenionModalityEnum(enum.Enum):
    PRESENCIAL = strawberry.enum_value(value=1)
    VIRTUAL = strawberry.enum_value(value=3)
    DOMICILIO = strawberry.enum_value(value=3)