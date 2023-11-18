# Third-party Libraries
from django.db import models

# Own Libraries
from apps.psychology import psychology_constants
from utils.models import AuditableMixin


class OfficeLocation(AuditableMixin):
    HOUSE = 1
    OFFICE = 2
    LOCATION_TYPE = (
        (HOUSE, "HOUSE"),
        (OFFICE, "OFFICE"),
    )

    user = models.ForeignKey(
        "core.AuthUser",
        on_delete=models.PROTECT,
        related_name="office_location_set",
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    long = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
    )
    lat = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
    )
    location_type = models.SmallIntegerField(
        choices=psychology_constants.LOCATION_TYPE_CHOICES,
        default=psychology_constants.TYPE_OFFICE,
        db_index=True,
    )
    location_status = models.SmallIntegerField(
        choices=psychology_constants.VISIBILITY_STATUS_CHOICES,
        default=psychology_constants.VISIBILITY_ACTIVE,
        db_index=True,
    )

    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.location}"
