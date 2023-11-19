# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from apps.psychology import psychology_constants
from utils.models import AuditableMixin

User = get_user_model()


class UserLanguage(AuditableMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_language_set",
    )
    language = models.SmallIntegerField(
        choices=psychology_constants.LANG_CHOICES,
        db_index=True,
        blank=True,
        null=True,
    )
    level = models.SmallIntegerField(
        choices=psychology_constants.LANG_LEVEL_CHOICES,
        db_index=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.get_language_display()}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "language"],
                name="unique language for user",
            )
        ]
