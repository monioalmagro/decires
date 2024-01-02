# Own Libraries
from apps.psychology.models import Specialization
from utils.adapter import ModelAdapter


class SpecializationAdapter(ModelAdapter):
    model_class = Specialization

    def get_object(self, **kwargs) -> Specialization | None:
        kwargs["is_active"] = True
        return super().get_object(**kwargs)
