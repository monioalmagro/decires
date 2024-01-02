# Third-party Libraries
import strawberry

# Own Libraries
from apps.core.models import AuthUser, Zone
from apps.psychology.adapters.user_carreer import UserCarreerAdapter
from apps.psychology.adapters.user_language import UserLanguageAdapter
from apps.psychology.schema.enums.auth_user import AuthUserGenderEnum
from apps.psychology.schema.types.city import ZoneType
from apps.psychology.schema.types.user_carreer import UserCarreerType
from apps.psychology.schema.types.user_language import UserLanguageType


@strawberry.interface()
class UserType:
    original_id: strawberry.ID
    first_name: str | None = None
    last_name: str | None = None
    is_verified_profile: bool
    avatar: str | None = None
    office_locations: list[ZoneType] | None = None
    gender_enum: AuthUserGenderEnum | None = None
    profile_url: str | None = None

    @classmethod
    def from_db_models(cls, instance: AuthUser) -> "UserType":
        return cls(
            original_id=instance.pk,
            first_name=instance.first_name,
            last_name=instance.last_name,
            is_verified_profile=instance.is_verified_profile,
            avatar=instance.avatar,
            office_locations=cls.get_zones(
                zone_list=list(instance.office_locations.all())
            ),
            gender_enum=instance.gender,
            profile_url=instance.profile_url,
        )

    @staticmethod
    def get_zones(zone_list: list[Zone] | None = None) -> list[ZoneType]:
        if zone_list := zone_list or []:
            return [ZoneType.from_db_model(instance=zone) for zone in zone_list]
        return []

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
        if results := await adapter.get_objects(
            **{
                "user_id": self.original_id,
                "is_active": True,
                "is_deleted": False,
                "language__is_active": True,
                "language__is_deleted": False,
            }
        ):
            return [
                UserLanguageType.from_db_model(instance=attention_mode)
                for attention_mode in results
            ]
        return []


@strawberry.type()
class ProfessionalType(UserType):
    pass
