# Third-party Libraries
from django.core import serializers
from django.core.management.base import BaseCommand

# Own Libraries
# Own Libraries]
from apps.core.models import AuthUser, City, Country, Zone
from apps.psychology.models import (
    Audience,
    Carreer,
    ContactMe,
    UserAttachment,
    UserCarreer,
    UserCarreerAudience,
    UserLanguage,
    UserPayment,
)


class Command(BaseCommand):
    help = "Export the first 10 records of MyModel"

    models = (
        (AuthUser, "AuthUser"),
        (Country, "Country"),
        (City, "City"),
        (Zone, "Zone"),
        (Audience, "Audience"),
        (Carreer, "Carreer"),
        (ContactMe, "ContactMe"),
        (UserAttachment, "UserAttachment"),
        (UserCarreer, "UserCarreer"),
        (UserCarreerAudience, "UserCarreerAudience"),
        (UserLanguage, "UserLanguage"),
        (UserPayment, "UserPayment"),
    )

    def handle(self, *args, **options):
        # Obtener los primeros 10 registros del modelo
        for model, model_name in self.models:
            first_10_records = model.objects.all()[:10]

            # Serializar los registros en formato JSON
            data = serializers.serialize("json", first_10_records)

            # Guardar los datos en un archivo
            with open(f"tests/fixtures/json/{model_name}.json", "w") as file:
                file.write(data)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully exported the first 10 records to model_data.json"
            )
        )
