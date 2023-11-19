# Standard Libraries
from typing import List

# Own Libraries
from apps.psychology.models import Audience
from utils.adapter import ModelAdapter


class AudienceAdapter(ModelAdapter):
    model_class = Audience

    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[Audience]:
        kwargs["is_active"] = True
        return super().get_objects(limit, offset, order_by, **kwargs)
