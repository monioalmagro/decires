# Standard Libraries
import logging
from typing import List

# Own Libraries
from apps.core.models import AuthUser
from utils.adapter import ModelAdapter
from utils.database import async_database
from apps.psychology.schema.inputs.user import MutationUserPydanticModel

from django.db import DatabaseError, IntegrityError, transaction

logger = logging.getLogger(__name__)


class UserAdapter(ModelAdapter):
    model_class = AuthUser

    @async_database()
    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[AuthUser]:
        kwargs["is_active"] = True
        kwargs["is_verified_profile"] = True

        limit = limit or self.default_limit
        offset = offset or 0

        queryset = self.get_queryset(**kwargs)

        if order_by:
            queryset = queryset.order_by(*order_by)

        queryset = queryset[offset : offset + limit]

        return list(queryset)

    @async_database()
    def create_new_professional(self, _input: MutationUserPydanticModel):
        model = self.get_model_class()
        try:
            with transaction.atomic():
                obj = model.objects.create(
                    email=_input.email,
                    username=_input.username,
                    first_name=_input.first_name,
                    last_name=_input.last_name,
                    is_active=_input.is_active,
                    nro_dni=_input.nro_dni,
                    nro_matricula=_input.nro_matricula,
                    cuit=_input.cuit,
                    phone=_input.phone,
                    gender=_input.gender,
                    facebook_profile=_input.facebook_profile,
                    instagram_profile=_input.instagram_profile,
                    linkedin_profile=_input.linkedin_profile,
                    image_profile=_input.image_profile,
                    is_verified_profile=_input.is_verified_profile,
                    personal_address=_input.personal_address,
                )
                return obj
        except (DatabaseError, IntegrityError) as exp:
            logger.warning(
                "*** UserAdapter.create_new_professional, INTEGRITY "
                f"ERROR, {str(exp)} - {repr(exp)} ***",
                exc_info=True,
            )
            raise IntegrityError(str(exp)) from exp
