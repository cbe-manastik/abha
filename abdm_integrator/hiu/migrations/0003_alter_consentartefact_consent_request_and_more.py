# Generated by Django 4.2.5 on 2023-11-30 01:43

from django.db import migrations, models
import django.db.models.deletion
from abdm_integrator.settings import app_settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(app_settings.USER_MODEL),
        ("abdm_hiu", "0002_healthinformationrequest_healthdatareceiver"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consentartefact",
            name="consent_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artefacts",
                to="abdm_hiu.consentrequest",
                to_field="consent_request_id",
            ),
        ),
        migrations.AlterField(
            model_name="consentartefact",
            name="fetch_status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("REQUESTED", "Requested"),
                    ("RECEIVED", "Received"),
                    ("ERROR", "Error occurred"),
                ],
                default="PENDING",
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="consentrequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consent_requests",
                to=app_settings.USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="healthinformationrequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="health_information_requests",
                to=app_settings.USER_MODEL,
            ),
        ),
    ]
