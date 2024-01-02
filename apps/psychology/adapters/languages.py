# Own Libraries
from apps.psychology.models import Language
from utils.adapter import ModelAdapter


class LanguageAdapter(ModelAdapter):
    model_class = Language

    def get_object(self, **kwargs) -> Language | None:
        kwargs["is_active"] = True
        return super().get_object(**kwargs)
