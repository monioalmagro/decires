# Standard Libraries
from typing import List

# Own Libraries
from apps.core.models import AuthUser
from utils.adapter import ModelAdapter
from utils.database import async_database


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
