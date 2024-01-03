# Standard Libraries
from typing import Type

# Third-party Libraries
from django.db import IntegrityError
from django.db.models import Q
from strawberry.types import Info

# Own Libraries
from apps.core.models import AuthUser
from apps.psychology.adapters.carreer import CarreerAdapter
from apps.psychology.adapters.contact_me import ContactMeAdapter
from apps.psychology.adapters.languages import LanguageAdapter
from apps.psychology.adapters.specializations import SpecializationAdapter
from apps.psychology.adapters.user import UserAdapter
from apps.psychology.adapters.user_carreer import UserCarreerAdapter
from apps.psychology.adapters.user_language import UserLanguageAdapter
from apps.psychology.adapters.zone import ZoneAdapter
from apps.psychology.models import ContactMe
from apps.psychology.schema.background_tasks.send_admin_email_notifications import (
    send_message_to_admin_and_professional,
)
from apps.psychology.schema.inputs.contact_me import ContactMePydanticModel
from apps.psychology.schema.inputs.user import MutationUserPydanticModel
from apps.psychology.schema.inputs.user_carreer import UserCarreerPydanticModel
from apps.psychology.schema.interfaces.process import (
    BaseMutationProcess,
    BaseValidator,
)


class BaseUserProcess(BaseMutationProcess):
    def __init__(self, validator_instance: Type[BaseValidator]):
        super().__init__(validator_instance)

    def get_user_adapter(self):
        return UserAdapter()


##
class ContactProfessionalValidator(BaseValidator):
    def __init__(self, _input: ContactMePydanticModel):
        super().__init__(_input)

    async def validation_controller(self, user_adapter: UserAdapter):
        await self._validate_user_by_id(user_adapter=user_adapter)

    async def _validate_user_by_id(self, user_adapter: UserAdapter):
        _input = self.input
        if not (await user_adapter.get_object(**{"id": _input.user_id})):
            raise AssertionError(f"User not found with ID: {_input.user_id}")


class ContactProfessionalProcess(BaseUserProcess):
    def __init__(
        self,
        validator_instance: ContactProfessionalValidator,
        _input: ContactMePydanticModel,
    ):
        super().__init__(validator_instance)
        self.validator = validator_instance
        self.user_adapter = self.get_user_adapter()
        self.contact_me_adapter = self.get_contact_me_adapter()
        self.input = _input

    def get_contact_me_adapter(self):
        return ContactMeAdapter()

    @staticmethod
    async def send_background_tasks(
        info: Info,
        callable_function: callable,
        adapter: ContactMeAdapter,
        instance: ContactMe,
    ):
        background_tasks = info.context["background_tasks"]
        background_tasks.add_task(callable_function, adapter, instance)

    async def action(self, info: Info) -> ContactMe | None:
        adapter = self.contact_me_adapter
        _validator = self.validator
        await _validator.validation_controller(user_adapter=self.user_adapter)

        if contact_me_instance := await adapter.create_new_contact(_input=self.input):
            await self.send_background_tasks(
                info=info,
                callable_function=send_message_to_admin_and_professional,
                adapter=adapter,
                instance=contact_me_instance,
            )

            return contact_me_instance


##
class ProfessionalValidator(BaseValidator):
    def __init__(self, _input: MutationUserPydanticModel):
        super().__init__(_input)

    async def _validate_user_unique(self, user_adapter: UserAdapter):
        user_unique_filter = (
            Q(username=self.input.username)
            | Q(email=self.input.email)
            | Q(nro_dni=self.input.nro_dni)
            | Q(nro_matricula=self.input.nro_matricula)
            | Q(cuit=self.input.cuit)
            | Q(facebook_profile=self.input.facebook_profile)
            | Q(instagram_profile=self.input.instagram_profile)
            | Q(linkedin_profile=self.input.linkedin_profile)
        )
        if await user_adapter.get_object(user_unique_filter=user_unique_filter):
            raise IntegrityError(
                "Invalid registration. The provided information is "
                "already in use. Please check your details and try again",
            )

    async def validation_controller(self, user_adapter: UserAdapter):
        await self._validate_user_unique(user_adapter=user_adapter)


class NewProfessionalProcess(BaseUserProcess):
    def __init__(
        self,
        validator_instance: ProfessionalValidator,
        _input: MutationUserPydanticModel,
    ):
        super().__init__(validator_instance)
        self.validator = validator_instance
        self.user_adapter = self.get_user_adapter()
        self.zone_adapter = self.get_zone_adapter()
        self.carreer_adapter = self.get_carreer_adapter()
        self.user_carreer_adapter = self.get_user_carreer_adapter()
        self.specialization_adapter = self.get_specialization_adapter()
        self.language_adapter = self.get_language_adapter()
        self.user_language_adapter = self.get_user_language_adapter()
        self.input = _input

    def get_zone_adapter(self):
        return ZoneAdapter()

    def get_user_carreer_adapter(self):
        return UserCarreerAdapter()

    def get_carreer_adapter(self):
        return CarreerAdapter()

    def get_specialization_adapter(self):
        return SpecializationAdapter()

    def get_language_adapter(self):
        return LanguageAdapter()

    def get_user_language_adapter(self):
        return UserLanguageAdapter()

    async def add_office_locations(self, adapter: UserAdapter, professional: AuthUser):
        if zone_list := await self.zone_adapter.get_objects(
            id__in=self.input.office_locations
        ):
            await adapter.add_zones(obj=professional, zone_list=zone_list)

    async def add_carreer_with_specialization(self, professional: AuthUser):
        if (
            carreer := await self.carreer_adapter.get_object(id=self.input.carreer)
        ) and (
            specialization := await self.specialization_adapter.get_object(
                id=self.input.specialization
            )
        ):
            data = UserCarreerPydanticModel(
                user_id=professional.id,
                carreer_id=carreer.id,
                service_method=self.input.service_method_enum,
                service_modality=self.input.service_modality_enum,
                experience_summary=self.input.experience_summary,
            )

            await self.user_carreer_adapter.add_carrers_to_user(
                data=data,
                specialization=specialization.id,
            )

    async def add_languages(self, professional: AuthUser):
        if language := await self.language_adapter.get_objects(
            id__in=self.input.languages
        ):
            await self.user_language_adapter.add_languages_to_user(
                user=professional, language_list=language
            )

    async def user_set_password(self, adapter: UserAdapter, professional: AuthUser):
        await adapter.set_password(
            obj=professional,
            password=self.input.password,
        )

    async def action(self, info: Info | None = None) -> AuthUser | None:
        adapter = self.user_adapter
        await self.validator.validation_controller(user_adapter=self.user_adapter)
        if new_professional := await adapter.create_new_professional(self.input):
            await self.user_set_password(
                adapter=adapter,
                professional=new_professional,
            )
            await self.add_office_locations(
                adapter=adapter,
                professional=new_professional,
            )
            await self.add_carreer_with_specialization(professional=new_professional)
            await self.add_languages(professional=new_professional)

            return new_professional


##
