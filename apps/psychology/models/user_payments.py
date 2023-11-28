# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from utils.models import AuditableMixin

User = get_user_model()


class UserPayment(AuditableMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_payment_set",
    )
    was_paid = models.BooleanField(default=False)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.was_paid}"

    @property
    def month(self) -> int:
        if self.created_at:
            return getattr(self.created_at, "month", "None")
