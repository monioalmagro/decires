# Generated by Django 4.2.7 on 2023-11-18 19:56

import django.contrib.auth.models
from django.db import migrations, models
import utils.upload_files


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
                        max_length=30,
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
                    models.URLField(blank=True, null=True, verbose_name="Facebook"),
                ),
                (
                    "instagram_profile",
                    models.URLField(blank=True, null=True, verbose_name="Instagram"),
                ),
                (
                    "linkedin_profile",
                    models.URLField(blank=True, null=True, verbose_name="LinkedIn"),
                ),
                (
                    "image_profile",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=utils.upload_files.upload_user_image_profile,
                    ),
                ),
                ("is_verified_profile", models.BooleanField(default=False)),
                ("verified_profile_at", models.DateTimeField(blank=True, null=True)),
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
    ]
