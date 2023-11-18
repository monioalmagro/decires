# Third-party Libraries
from django.db import models

# Own Libraries
from utils.models import AuditableMixin


class Carreer(AuditableMixin):
    name = models.CharField(max_length=150, unique=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"