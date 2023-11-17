# Third-party Libraries
from django.db import models


class AuditableMixin(models.Model):
    created_at: str = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="Fecha de Creación",
    )
    updated_at: str = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de modificación",
    )
    is_active: bool = models.BooleanField(
        default=True,
        db_index=True,
    )
    is_deleted: bool = models.BooleanField(
        default=False,
        db_index=True,
    )

    class Meta:
        abstract = True
