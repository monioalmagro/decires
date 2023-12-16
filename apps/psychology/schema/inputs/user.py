# Third-party Libraries
import strawberry
from pydantic import BaseModel

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
