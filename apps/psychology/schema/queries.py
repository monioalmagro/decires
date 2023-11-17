# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.adapters.user import UserAdapter
from apps.psychology.schema.types.user import ProfessionalType


@strawberry.type()
class ProfessionalQueries:
    @strawberry.field()
    async def get_professional_list(self) -> list[ProfessionalType]:
        adapter = UserAdapter()
        if results := await adapter.get_objects():
            return [
                ProfessionalType.from_db_models(instance=professional)
                for professional in results
            ]
        return []
