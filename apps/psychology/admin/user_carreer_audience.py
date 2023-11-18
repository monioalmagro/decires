# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import UserCarreerAudience


class UserCarreerAudienceInline(admin.TabularInline):
    model = UserCarreerAudience
    fields = (
        "audience",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = ("audience",)
    extra = 0
