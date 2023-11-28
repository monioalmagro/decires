# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.core.models import Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "city", "is_active")
