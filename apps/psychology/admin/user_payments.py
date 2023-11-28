# Third-party Libraries
from django.contrib import admin
from django.http.request import HttpRequest

# Own Libraries
from apps.psychology.models import UserPayment


class UserPaymentInline(admin.TabularInline):
    model = UserPayment
    verbose_name_plural = "Pagos"
    fields = (
        "was_paid",
        "concept",
        "month",
        "observations",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "month",
    )
    extra = 0

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "concept",
    )
    raw_id_fields = ("user",)
