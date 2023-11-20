# Standard Libraries
import enum

# Third-party Libraries
import strawberry


@strawberry.enum()
class CarreerServiceMethodEnum(enum.Enum):
    PRESENCIAL = strawberry.enum_value(value=1)
    VIRTUAL = strawberry.enum_value(value=2)
    DOMICILIO = strawberry.enum_value(value=3)


@strawberry.enum()
class CarreerServiceModalityEnum(enum.Enum):
    INDIVIDUAL = strawberry.enum_value(value=1)
    GROUPS = strawberry.enum_value(value=2)
