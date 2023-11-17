# Third-party Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Own Libraries
from apps.core.models import AuthUser


@admin.register(AuthUser)
class UserAdmin(UserAdmin):
    list_display = ("id", "username", "email")

    fieldsets = (
        ("Usuario", {"fields": ("username", "image_profile")}),
        (
            "Información personal",
            {
                "classes": ("collapse",),
                "fields": (
                    "first_name",
                    "last_name",
                    "nro_dni",
                    "nro_matricula",
                    "cuit",
                    "phone",
                    "gender",
                    "attention_address",
                ),
            },
        ),
        (
            "Permisos",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "password",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Auditoria",
            {
                "classes": ("collapse",),
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )

    search_fields = (
        "email",
        "nro_dni",
        "nro_matricula",
        "cuit",
        "first_name__icontains",
        "last_name__icontains",
    )
    list_filter = ("is_staff", "is_superuser")
    readonly_fields = (
        "date_joined",
        "last_login",
    )

    # list_select_related = ()
    show_full_result_count = False
    actions_selection_counter = False
    ordering = ("id",)
