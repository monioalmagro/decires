# Third-party Libraries
import strawberry

# Own Libraries
from apps.core.models import AuthUser


@strawberry.interface()
class UserType:
    original_id: strawberry.ID
    first_name: str | None = None
    last_name: str | None = None
    # carreers: str | None = None
    # attention_modality_enum: AttenionModalityEnum | None = None

    @classmethod
    def from_db_models(cls, instance: AuthUser) -> "UserType":
        return cls(
            original_id=instance.pk,
            first_name=instance.first_name,
            last_name=instance.last_name,
            # carreers=instance.pk,
        )


@strawberry.type()
class ProfessionalType(UserType):
    pass
