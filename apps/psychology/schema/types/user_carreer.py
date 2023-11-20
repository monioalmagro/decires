# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.adapters.user_carreer_audience import (
    UserCarreerAudienceAdapter,
)
from apps.psychology.models import UserCarreer
from apps.psychology.schema.enums.user_carreer import (
    CarreerServiceMethodEnum,
    CarreerServiceModalityEnum,
)
from apps.psychology.schema.types.audience import AudienceType
from apps.psychology.schema.types.carreer import CarreerType
from utils.enums import get_enum_instance_by_value


@strawberry.type()
class UserCarreerType:
    original_id: strawberry.ID
    carreer: CarreerType
    service_method_enum: CarreerServiceMethodEnum | None = None
    service_modality_enum: CarreerServiceModalityEnum | None = None
    experience_summary: str | None = None

    @classmethod
    def from_db_model(cls, instance: UserCarreer):
        return cls(
            original_id=instance.id,
            carreer=CarreerType.from_db_model(instance=instance.carreer),
            service_method_enum=get_enum_instance_by_value(
                enum_class=CarreerServiceMethodEnum,
                value=instance.service_method,
            ),
            service_modality_enum=get_enum_instance_by_value(
                enum_class=CarreerServiceModalityEnum,
                value=instance.service_modality,
            ),
            experience_summary=instance.experience_summary,
        )

    @strawberry.field()
    async def audiences_set(self) -> list[AudienceType]:
        adapter = UserCarreerAudienceAdapter()
        if results := await adapter.get_objects(
            **{"user_carreer_id": self.original_id}
        ):
            return [
                AudienceType.from_db_model(instance=user_carreer.audience)
                for user_carreer in results
            ]
        return []
