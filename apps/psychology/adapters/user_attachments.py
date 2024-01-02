# Standard Libraries
import logging
from typing import List

# Own Libraries
from apps.psychology.models import UserAttachment
from utils.adapter import ModelAdapter

logger = logging.getLogger(__name__)


class UserAttachmentAdapter(ModelAdapter):
    model_class = UserAttachment

    def get_objects(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order_by: List[str] | None = None,
        **kwargs
    ) -> List[UserAttachment]:
        kwargs["is_active"] = True
        return super().get_objects(limit, offset, order_by, **kwargs)
