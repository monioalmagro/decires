# Third-party Libraries
from django.contrib import admin
from django.http.request import HttpRequest

# Own Libraries
from apps.psychology.models import ContactMe


class ContactMeInline(admin.TabularInline):
    model = ContactMe
    verbose_name_plural = "Mensajeria interna"
    fields = (
        "full_name",
        "email",
        "phone",
        "message",
        "is_active",
        "is_deleted",
    )
    extra = 0

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
