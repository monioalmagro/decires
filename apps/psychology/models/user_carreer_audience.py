# Third-party Libraries
from django.db import models

# Own Libraries
from utils.models import AuditableMixin


class UserCarreerAudience(AuditableMixin):
    user_carreer = models.ForeignKey(
        "UserCarreer",
        on_delete=models.PROTECT,
        related_name="user_carreer_audience_set",
    )
    audience = models.ForeignKey(
        "Audience",
        on_delete=models.PROTECT,
        related_name="user_carreer_audience_set",
    )

    def __str__(self):
        return f"{self.audience}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_carreer", "audience"],
                name="unique audience for user carreer",
            )
        ]
