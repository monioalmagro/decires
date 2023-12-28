# Standard Libraries
import logging

# Third-party Libraries
import strawberry
from strawberry.types import Info

# Own Libraries
from apps.psychology.adapters.contact_me import ContactMeAdapter
from apps.psychology.adapters.user import UserAdapter
from apps.psychology.schema.background_tasks.send_admin_email_notifications import (
    send_message_to_admin_and_professional,
)
from apps.psychology.schema.inputs.contact_me import MutationContactMeInput
from apps.psychology.schema.types.contact_me import ContactMeType
from utils.decorators import mutation_exception_handler

logger = logging.getLogger(__name__)


@strawberry.type()
class ProfessionalMutations:
    @strawberry.field()
    @mutation_exception_handler(log_tag="ProfessionalMutations")
    async def contact_me(
        self,
        info: Info,
        input: MutationContactMeInput,
    ) -> ContactMeType | None:
        _input = input.to_pydantic()

        user_adapter = UserAdapter()
        if not (await user_adapter.get_object(**{"id": _input.user_id})):
            raise AssertionError(f"User not found with ID: {_input.user_id}")

        adapter = ContactMeAdapter()
        if contact_me_instance := await adapter.create_new_contact(_input=_input):
            # background tasks
            info.context["background_tasks"].add_task(
                send_message_to_admin_and_professional,
                adapter,
                contact_me_instance,
            )

            return ContactMeType.from_db_model(instance=contact_me_instance)
