# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.adapters.carreer import CarreerAdapter
from apps.psychology.adapters.city import CityAdapter
from apps.psychology.adapters.user import UserAdapter
from apps.psychology.adapters.zone import ZoneAdapter
from apps.psychology.schema.inputs.user import (
    QueryListUserInput,
    QueryRetrieveUserInput,
)
from apps.psychology.schema.types.carreer import CarreerSelect2Type
from apps.psychology.schema.types.city import CitySelect2Type, ZoneSelect2Type
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

    @strawberry.field()
    async def cities(self) -> list[CitySelect2Type]:
        adapter = CityAdapter()
        if results := await adapter.get_objects(order_by=["created_at"]):
            return [CitySelect2Type.from_db_model(instance=city) for city in results]
        return []

    @strawberry.field()
    async def zones(self, city_id: strawberry.ID) -> list[ZoneSelect2Type]:
        adapter = ZoneAdapter()
        if results := await adapter.get_objects(
            order_by=["created_at"],
            **{"city_id": city_id},
        ):
            return [ZoneSelect2Type.from_db_model(instance=zone) for zone in results]
        return []


@strawberry.type()
class ProfessionalQueries:
    @strawberry.field()
    async def get_professional_list(
        self, input: QueryListUserInput
    ) -> list[ProfessionalType]:
        _input = input.to_pydantic()
        adapter = UserAdapter()

        kwargs = {
            "user_carreer_set__carreer_id": _input.carreer,
            "user_carreer_set__service_method": _input.service_method_enum,
            "office_locations__city_id": _input.city,
        }
        if zone := _input.zone:
            kwargs["office_locations__id"] = zone

        if results := await adapter.get_objects(**kwargs):
            return [
                ProfessionalType.from_db_models(instance=professional)
                for professional in results
            ]
        return []

    @strawberry.field()
    async def get_professional(
        self,
        input: QueryRetrieveUserInput,
    ) -> ProfessionalType | None:
        adapter = UserAdapter()
        if result := await adapter.get_object(id=input.original_id):
            return ProfessionalType.from_db_models(instance=result)
