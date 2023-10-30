# Generated by Django 4.2.5 on 2023-09-28 07:15

from django.db import migrations, models
import django.db.models.deletion

from abdm_integrator.settings import app_settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(app_settings.USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsentRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gateway_request_id", models.UUIDField(unique=True)),
                ("consent_request_id", models.UUIDField(null=True, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("GRANTED", "Granted"),
                            ("REVOKED", "Revoked"),
                            ("EXPIRED", "Expired"),
                            ("DENIED", "Denied"),
                            ("PENDING", "Pending request from Gateway"),
                            ("REQUESTED", "Requested"),
                            ("ERROR", "Error occurred"),
                        ],
                        default="PENDING",
                        max_length=40,
                    ),
                ),
                ("details", models.JSONField(null=True)),
                ("error", models.JSONField(null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("health_info_from_date", models.DateTimeField()),
                ("health_info_to_date", models.DateTimeField()),
                ("health_info_types", models.JSONField(default=list)),
                ("expiry_date", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="consent_requests",
                        to=app_settings.USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConsentArtefact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gateway_request_id", models.UUIDField(null=True, unique=True)),
                ("artefact_id", models.UUIDField(unique=True)),
                ("details", models.JSONField(null=True)),
                ("error", models.JSONField(null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "consent_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="artefacts",
                        to="abdm_hiu.consentrequest",
                        to_field="consent_request_id",
                    ),
                ),
                (
                    "fetch_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("REQUESTED", "Requested"),
                            ("RECEIVED", "Received"),
                            ("ERROR", "Error occurred"),
                        ],
                        default="REQUESTED",
                        max_length=40,
                    ),
                ),
            ],
        ),
    ]
