# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from apps.psychology import psychology_constants
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
    specializations = models.ManyToManyField(
        "Specialization",
        blank=True,
        related_name="user_carreer_set",
    )
    service_method = models.SmallIntegerField(
        choices=psychology_constants.SERVICE_METHOD_CHOICES,
        default=psychology_constants.VIRTUAL,
    )
    service_modality = models.SmallIntegerField(
        choices=psychology_constants.SERVICE_MODALITY_CHOICES,
        default=psychology_constants.INDIVIDUAL,
    )
    order = models.SmallIntegerField(default=1)
    experience_summary = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "carreer"],
                name="unique carreer for user",
            )
        ]

    def __str__(self):
        return f"{self.user} ({self.carreer})"
