# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import UserAttachment


@admin.register(UserAttachment)
class UserAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "content_type",
        "media_file",
        "image",
        "created_by",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = (
        "created_by",
        "updated_by",
    )
