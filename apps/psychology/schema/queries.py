# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.adapters.carreer import CarreerAdapter
from apps.psychology.adapters.user import UserAdapter
from apps.psychology.schema.types.carreer import CarreerSelect2Type
from apps.psychology.schema.types.user import ProfessionalType


@strawberry.type()
class Select2Queries:
    @strawberry.field()
    async def carreers(self) -> list[CarreerSelect2Type]:
        adapter = CarreerAdapter()
        if results := await adapter.get_objects():
            return [
                CarreerSelect2Type.from_db_model(instance=carreer)
                for carreer in results
            ]
        return []


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
