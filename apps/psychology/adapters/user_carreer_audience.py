# Standard Libraries
from typing import List

# Own Libraries
from apps.psychology.models import UserCarreerAudience
from utils.adapter import ModelAdapter


class UserCarreerAudienceAdapter(ModelAdapter):
    model_class = UserCarreerAudience

    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[UserCarreerAudience]:
        kwargs["is_active"] = True
        return super().get_objects(limit, offset, order_by, **kwargs)
