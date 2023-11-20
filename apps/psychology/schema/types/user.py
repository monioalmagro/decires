# Third-party Libraries
import strawberry

# Own Libraries
from apps.core.models import AuthUser
from apps.psychology.adapters.user_carreer import UserCarreerAdapter
from apps.psychology.adapters.user_language import UserLanguageAdapter
from apps.psychology.schema.types.user_carreer import UserCarreerType
from apps.psychology.schema.types.user_language import UserLanguageType


@strawberry.interface()
class UserType:
    original_id: strawberry.ID
    first_name: str | None = None
    last_name: str | None = None
    office_location: str | None = None
    is_verified_profile: bool

    @classmethod
    def from_db_models(cls, instance: AuthUser) -> "UserType":
        return cls(
            original_id=instance.pk,
            first_name=instance.first_name,
            last_name=instance.last_name,
            office_location=instance.office_location,
            is_verified_profile=instance.is_verified_profile,
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
