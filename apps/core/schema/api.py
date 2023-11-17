# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.schema.queries import ProfessionalQueries


@strawberry.type
class QueriesSummary(
    ProfessionalQueries,
):
    pass


@strawberry.type()
class Queries:
    @strawberry.field()
    async def psychology(self) -> QueriesSummary:
        return QueriesSummary()


schema = strawberry.Schema(query=Queries)
