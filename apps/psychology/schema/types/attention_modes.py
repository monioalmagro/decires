# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import AttentionModes
from apps.psychology.schema.enums.user_attention_modality import (
    AttenionModalityEnum,
)
from utils.enums import get_enum_instance_by_value


@strawberry.type()
class AttentionModesType:
    modality_enum: AttenionModalityEnum | None = None

    @classmethod
    def from_db_model(cls, instance: AttentionModes) -> "AttentionModesType":
        return cls(
            modality_enum=get_enum_instance_by_value(
                enum_class=AttenionModalityEnum,
                value=instance.modality,
            ),
        )
