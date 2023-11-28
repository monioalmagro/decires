# Standard Libraries
from typing import List

# Own Libraries
from apps.core.models import Zone
from utils.adapter import ModelAdapter


class ZoneAdapter(ModelAdapter):
    model_class = Zone

    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[Zone]:
        kwargs["is_active"] = True
        return super().get_objects(limit, offset, order_by, **kwargs)
