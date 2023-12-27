# Third-party Libraries
import strawberry

# Own Libraries
from apps.psychology.schema.inputs.user import MutationUserInput
from apps.psychology.schema.types.user import UserType


class ProfessionalMutations:
    @strawberry.field()
    def new_professional(self, input: MutationUserInput) -> UserType:
        try:
            # SOLID: D: INVERSION DE DEPENDENCIAS
            # run validations
            _input = input.to_pydantic()
            _input.validame_algo_externo("mazzurque")

            _input_dicT: dict = _input.dict(exclude_none=True)

        except AssertionError as exp:
            pass
        except Exception as exp:
            pass
