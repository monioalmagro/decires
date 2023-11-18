# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import Audience


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "is_active",
        "is_deleted",
    )
