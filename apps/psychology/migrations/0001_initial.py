# Generated by Django 4.2.7 on 2023-11-18 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.upload_files


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Audience",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Carreer",
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
                ("name", models.CharField(max_length=150, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserCarreer",
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
                ("order", models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="UserCarreerAudience",
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
                    "audience",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_carreer_audience_set",
                        to="psychology.audience",
                    ),
                ),
                (
                    "user_carreer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_carreer_audience_set",
                        to="psychology.usercarreer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="usercarreer",
            name="audiences",
            field=models.ManyToManyField(
                related_name="user_carreer_set",
                through="psychology.UserCarreerAudience",
                to="psychology.audience",
            ),
        ),
        migrations.AddField(
            model_name="usercarreer",
            name="carreer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_carreer_set",
                to="psychology.carreer",
            ),
        ),
        migrations.AddField(
            model_name="usercarreer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_carreer_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="UserAttachment",
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
                ("name", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=utils.upload_files.upload_attachment_file,
                    ),
                ),
                (
                    "media_file",
                    models.FileField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=utils.upload_files.upload_attachment_file,
                    ),
                ),
                (
                    "content_type",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("size", models.IntegerField(blank=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_attachment_created_by_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_attachment_updated_by_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OfficeLocation",
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
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "long",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=8, null=True
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=8, null=True
                    ),
                ),
                (
                    "location_type",
                    models.SmallIntegerField(
                        choices=[(1, "TYPE_HOUSE"), (2, "TYPE_OFFICE")],
                        db_index=True,
                        default=2,
                    ),
                ),
                (
                    "location_status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "VISIBILITY_DRAFT"),
                            (2, "VISIBILITY_ACTIVE"),
                            (3, "VISIBILITY_INACTIVE"),
                        ],
                        db_index=True,
                        default=2,
                    ),
                ),
                ("order", models.SmallIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="office_location_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ContactMe",
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
                    "full_name",
                    models.CharField(help_text="Visitor[external]", max_length=50),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=50, verbose_name="email address"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, db_index=True, max_length=30, null=True
                    ),
                ),
                ("message", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Professional",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="professional_contact_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Professional",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AttentionModes",
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
                    "modality",
                    models.SmallIntegerField(
                        choices=[(1, "PRESENCIAL"), (2, "VIRTUAL"), (3, "DOMICILIO")],
                        db_index=True,
                    ),
                ),
                ("order", models.SmallIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attention_modality_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="usercarreeraudience",
            constraint=models.UniqueConstraint(
                fields=("user_carreer", "audience"),
                name="unique audience for user carreer",
            ),
        ),
        migrations.AddConstraint(
            model_name="usercarreer",
            constraint=models.UniqueConstraint(
                fields=("user", "carreer"), name="unique carreer for user"
            ),
        ),
        migrations.AddConstraint(
            model_name="attentionmodes",
            constraint=models.UniqueConstraint(
                fields=("user", "modality"), name="unique modality for user"
            ),
        ),
    ]