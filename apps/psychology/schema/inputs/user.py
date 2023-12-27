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
    first_name: str
    last_name: str | None = None

    @validator("first_name", "last_name")
    @classmethod
    def validate_first_name(cls, name):
        if len(name) == 0:
            raise AssertionError("INPUT INVALID")
        return name.strip()

    def validame_algo_externo(self, last_name):
        if last_name == "Mazzurque":
            return True
        raise AssertionError("z§xbcvk,sndfl,bvnsd")


@strawberry.experimental.pydantic.input(
    model=MutationUserPydanticModel,
    all_fields=True,
)
class MutationUserInput:
    pass
