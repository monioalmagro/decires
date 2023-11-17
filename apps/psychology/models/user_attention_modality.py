# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from apps.core import core_constants
from utils.models import AuditableMixin

User = get_user_model()


class UserAttentionModality(AuditableMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="attention_modality_set",
    )
    modality = models.SmallIntegerField(
        choices=core_constants.MODALITY_CHOICES,
        default=core_constants.VIRTUAL,
        db_index=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "modality"],
                name="unique modality for user",
            )
        ]

    def __str__(self):
        return f"{self.user}, ({self.get_modality_display()})"
