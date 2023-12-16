# Third-party Libraries
import strawberry

# Own Libraries
from apps.core.models import City, Zone


@strawberry.interface()
class ILocationType:
    id: strawberry.ID
    text: str

    @classmethod
    def from_db_model(cls, instance: City | Zone):
        return cls(
            id=instance.id,
            text=instance.name,
        )


@strawberry.type()
class CitySelect2Type(ILocationType):
    pass


@strawberry.type()
class ZoneSelect2Type(ILocationType):
    pass
