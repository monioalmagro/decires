# Own Libraries
from apps.psychology.models import OfficeLocation
from utils.adapter import ModelAdapter


class OfficeLocationAdapter(ModelAdapter):
    model_class = OfficeLocation

    def get_object(self, **kwargs) -> OfficeLocation | None:
        kwargs["is_active"] = True
        return super().get_object(**kwargs)
