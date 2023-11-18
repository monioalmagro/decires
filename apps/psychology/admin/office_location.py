# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import OfficeLocation


class OfficeLocationInline(admin.TabularInline):
    model = OfficeLocation
    verbose_name_plural = "Centros de atención"
    fields = (
        "location",
        "description",
        "location_type",
        "location_status",
        "long",
        "lat",
        "order",
        "is_active",
        "is_deleted",
    )
    extra = 0
