# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import Specialization
from apps.psychology.schema.interfaces.basic_model_type import BaseModelType


@strawberry.type()
class SpecializationType(BaseModelType):
    @classmethod
    def from_db_model(cls, instance: Specialization) -> "SpecializationType":
        return super().from_db_model(instance=instance)
