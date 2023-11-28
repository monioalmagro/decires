# Third-party Libraries
from django.db import models

# Own Libraries
from utils.models import AuditableMixin, SlugMixin


class Zone(AuditableMixin, SlugMixin):
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="zone_set",
    )

    def __str__(self) -> str:
        return f"{self.name}"
