# Third-party Libraries
import strawberry

# Own Libraries
from apps.core.models import AuthUser
from apps.psychology.adapters.attention_modes import AttentionModesAdapter
from apps.psychology.adapters.office_location import OfficeLocationAdapter
from apps.psychology.adapters.user_carreer import UserCarreerAdapter
from apps.psychology.adapters.user_language import UserLanguageAdapter
from apps.psychology.schema.types.attention_modes import AttentionModesType
from apps.psychology.schema.types.office_location import OfficeLocationType
from apps.psychology.schema.types.user_carreer import UserCarreerType
from apps.psychology.schema.types.user_language import UserLanguageType


@strawberry.interface()
class UserType:
    original_id: strawberry.ID
    first_name: str | None = None
    last_name: str | None = None

    @classmethod
    def from_db_models(cls, instance: AuthUser) -> "UserType":
        return cls(
            original_id=instance.pk,
            first_name=instance.first_name,
            last_name=instance.last_name,
        )

    @strawberry.field()
    async def user_carreer_set(self) -> list[UserCarreerType]:
        adapter = UserCarreerAdapter()
        if results := await adapter.get_objects(**{"user_id": self.original_id}):
            return [
                UserCarreerType.from_db_model(instance=carreer) for carreer in results
            ]
        return []

    @strawberry.field()
    async def location(self) -> OfficeLocationType | None:
        adapter = OfficeLocationAdapter()
        if location := await adapter.get_object(**{"user_id": self.original_id}):
            return OfficeLocationType.from_db_model(instance=location)

    @strawberry.field()
    async def attention_modes(self) -> list[AttentionModesType]:
        adapter = AttentionModesAdapter()
        if results := await adapter.get_objects(**{"user_id": self.original_id}):
            return [
                AttentionModesType.from_db_model(instance=attention_mode)
                for attention_mode in results
            ]
        return []

    @strawberry.field()
    async def languages_set(self) -> list[UserLanguageType]:
        adapter = UserLanguageAdapter()
        if results := await adapter.get_objects(**{"user_id": self.original_id}):
            return [
                UserLanguageType.from_db_model(instance=attention_mode)
                for attention_mode in results
            ]
        return []


@strawberry.type()
class ProfessionalType(UserType):
    pass
