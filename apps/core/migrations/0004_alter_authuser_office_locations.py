# Generated by Django 4.2.7 on 2023-12-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_authuser_office_location_tags_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authuser",
            name="office_locations",
            field=models.ManyToManyField(
                blank=True, related_name="auth_user_set", to="core.zone"
            ),
        ),
    ]
