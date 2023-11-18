# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from apps.psychology import psychology_constants
from utils.models import AuditableMixin

User = get_user_model()


class AttentionModes(AuditableMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="attention_modality_set",
    )
    modality = models.SmallIntegerField(
        choices=psychology_constants.MODALITY_CHOICES,
        db_index=True,
    )
    order = models.SmallIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "modality"],
                name="unique modality for user",
            )
        ]

    def __str__(self):
        return f"{self.user}, ({self.get_modality_display()})"
