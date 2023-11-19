# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.models import OfficeLocation


@strawberry.type()
class OfficeLocationType:
    original_id: strawberry.ID
    location: str

    @classmethod
    def from_db_model(cls, instance: OfficeLocation) -> "OfficeLocationType":
        return cls(
            original_id=instance.pk,
            location=instance.location,
        )
