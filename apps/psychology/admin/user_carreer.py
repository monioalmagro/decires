# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.admin.user_carreer_audience import (
    UserCarreerAudienceInline,
)
from apps.psychology.models import UserCarreer


class UserCarreerInline(admin.TabularInline):
    model = UserCarreer
    verbose_name_plural = "Titulaciones"
    fields = (
        "carreer",
        "modality",
        "experience_summary",
        "order",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = ("carreer",)
    extra = 0


@admin.register(UserCarreer)
class UserCarreerAdmin(admin.ModelAdmin):
    list_display = ("user", "carreer", "is_active")
    raw_id_fields = (
        "user",
        "carreer",
        "audiences",
    )
    inlines = (UserCarreerAudienceInline,)
