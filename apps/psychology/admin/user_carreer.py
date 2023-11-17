# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import UserCarreer


class UserCarreerInline(admin.TabularInline):
    model = UserCarreer
    fields = (
        "carreer",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = ("carreer",)
    extra = 0
