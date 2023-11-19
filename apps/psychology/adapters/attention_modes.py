# Standard Libraries
from typing import List

# Own Libraries
from apps.psychology.models import AttentionModes
from utils.adapter import ModelAdapter


class AttentionModesAdapter(ModelAdapter):
    model_class = AttentionModes

    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[AttentionModes]:
        kwargs["is_active"] = True
        return super().get_objects(limit, offset, order_by, **kwargs)
