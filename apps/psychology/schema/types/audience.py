# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import Audience
from apps.psychology.schema.interfaces.basic_model_type import BaseModelType


@strawberry.type()
class AudienceType(BaseModelType):
    @classmethod
    def from_db_model(cls, instance: Audience) -> "AudienceType":
        return super().from_db_model(instance=instance)
