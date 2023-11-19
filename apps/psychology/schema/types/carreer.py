# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import Carreer
from apps.psychology.schema.interfaces.basic_model_type import BaseModelType


@strawberry.type()
class CarreerType(BaseModelType):
    @classmethod
    def from_db_model(cls, instance: Carreer) -> "CarreerType":
        return super().from_db_model(instance=instance)
