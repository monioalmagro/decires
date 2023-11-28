# Standard Libraries
import random
from typing import Any

# Third-party Libraries
from django.utils import timezone
from django.views.generic import TemplateView

# Own Libraries
from config.enviroment_vars import settings

now = timezone.now()


class PsychologyBaseView(TemplateView):
    extra_context = {
        "timestamp": now.isoformat(),
    }

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["site_name"] = settings.SITE_NAME
        context["year"] = now.year
        context["no_cache"] = random.randint(1, 999999999)
        return context