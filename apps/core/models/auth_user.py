# Third-party Libraries
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Own Libraries
from apps.core import core_constants
from utils.upload_files import upload_user_image_profile


class AuthUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    username = models.CharField(
        _("username"), max_length=30, blank=True, unique=True, db_index=True
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    nro_dni = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    nro_matricula = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    cuit = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    gender = models.SmallIntegerField(
        choices=core_constants.GENDER_CHOICES,
        db_index=True,
        blank=True,
        null=True,
    )
    attention_address = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )
    image_profile = models.ImageField(
        upload_to=upload_user_image_profile,
        # storage=storage_share_file,
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        _name = self.username or self.email
        return f"{_name}"
