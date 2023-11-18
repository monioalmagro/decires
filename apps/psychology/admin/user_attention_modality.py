# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.psychology.models import AttentionModes


class AttentionModesInline(admin.TabularInline):
    model = AttentionModes
    verbose_name_plural = "Modalidad de Atención"
    fields = (
        "modality",
        "order",
        "is_active",
        "is_deleted",
    )
    extra = 0
