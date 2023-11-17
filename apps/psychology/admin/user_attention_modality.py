# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import UserAttentionModality


class UserAttentionModalityInline(admin.TabularInline):
    model = UserAttentionModality
    fields = (
        "modality",
        "is_active",
        "is_deleted",
    )
    extra = 0
