# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from utils.models import AuditableMixin

User = get_user_model()


class UserCarreer(AuditableMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_carreer_set",
    )
    carreer = models.ForeignKey(
        "Carreer",
        on_delete=models.CASCADE,
        related_name="user_carreer_set",
    )

    def __str__(self):
        return f"{self.user}"
