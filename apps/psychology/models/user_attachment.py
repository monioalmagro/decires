# Third-party Libraries
from django.contrib.auth import get_user_model
from django.db import models

# Own Libraries
from utils.models import AuditableMixin
from utils.upload_files import upload_attachment_file

User = get_user_model()


class UserAttachment(AuditableMixin):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=upload_attachment_file,
        # storage=storage_share_file,
        max_length=255,
        null=True,
        blank=True,
    )
    media_file = models.FileField(
        upload_to=upload_attachment_file,
        # storage=storage_share_file,
        max_length=255,
        null=True,
        blank=True,
    )
    content_type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    size = models.IntegerField(
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="user_attachment_created_by_set",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="user_attachment_updated_by_set",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.content_type})"
