# Generated by Django 4.2.7 on 2024-03-02 18:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=100,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="last name"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "nro_dni",
                    models.CharField(
                        blank=True, db_index=True, max_length=25, null=True, unique=True
                    ),
                ),
                (
                    "nro_matricula",
                    models.CharField(
                        blank=True, db_index=True, max_length=25, null=True, unique=True
                    ),
                ),
                (
                    "cuit",
                    models.CharField(
                        blank=True, db_index=True, max_length=25, null=True, unique=True
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "gender",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "HOMBRE"), (2, "MUJER")],
                        db_index=True,
                        null=True,
                    ),
                ),
                (
                    "facebook_profile",
                    models.URLField(
                        blank=True, null=True, unique=True, verbose_name="Facebook"
                    ),
                ),
                (
                    "instagram_profile",
                    models.URLField(
                        blank=True, null=True, unique=True, verbose_name="Instagram"
                    ),
                ),
                (
                    "linkedin_profile",
                    models.URLField(
                        blank=True, null=True, unique=True, verbose_name="LinkedIn"
                    ),
                ),
                ("is_verified_profile", models.BooleanField(default=False)),
                ("verified_profile_at", models.DateTimeField(blank=True, null=True)),
                ("personal_address", models.TextField(blank=True, null=True)),
                (
                    "attention_schedule",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "membership_plan",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "BASIC_PLAN"),
                            (2, "PREMIUM_PLAN"),
                            (3, "VIP_PLAN"),
                        ],
                        db_index=True,
                        default=1,
                        help_text="Membership plan",
                        null=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de modificación"
                    ),
                ),
                ("is_active", models.BooleanField(db_index=True, default=True)),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("name", models.CharField(max_length=150)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Ciudad",
                "verbose_name_plural": "Ciudades",
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de modificación"
                    ),
                ),
                ("is_active", models.BooleanField(db_index=True, default=True)),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("name", models.CharField(max_length=150)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("code", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "País",
                "verbose_name_plural": "Paises",
            },
        ),
        migrations.CreateModel(
            name="Zone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de modificación"
                    ),
                ),
                ("is_active", models.BooleanField(db_index=True, default=True)),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("name", models.CharField(max_length=150)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="zone_set",
                        to="core.city",
                    ),
                ),
            ],
            options={
                "verbose_name": "Barrio",
                "verbose_name_plural": "Barrios",
            },
        ),
        migrations.CreateModel(
            name="UserZone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de modificación"
                    ),
                ),
                ("is_active", models.BooleanField(db_index=True, default=True)),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_zone_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_zone_set",
                        to="core.zone",
                    ),
                ),
            ],
            options={
                "verbose_name": "Barrio del usuario",
                "verbose_name_plural": "Barrios de los usuarios",
            },
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="city_set",
                to="core.country",
            ),
        ),
        migrations.AddConstraint(
            model_name="userzone",
            constraint=models.UniqueConstraint(
                fields=("user", "zone"), name="unique zone for user"
            ),
        ),
    ]
