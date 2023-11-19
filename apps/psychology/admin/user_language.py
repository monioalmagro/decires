# Third-party Libraries
from django.contrib import admin
from django.http.request import HttpRequest

# Own Libraries
from apps.psychology.models import UserLanguage


class UserLanguageInline(admin.TabularInline):
    model = UserLanguage
    verbose_name_plural = "Idiomas"
    fields = (
        "language",
        "level",
        "is_active",
        "is_deleted",
    )
    extra = 0

    # def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False

    # def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False

    # def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False
