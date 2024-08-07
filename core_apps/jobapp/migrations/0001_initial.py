# Generated by Django 4.1.7 on 2024-07-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobApplication",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("Rejected", "Rejected"),
                            ("Shortlisted", "Shortlisted"),
                            ("Selected", "Selected"),
                        ],
                        max_length=50,
                    ),
                ),
                ("applied_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Job Application",
            },
        ),
        migrations.CreateModel(
            name="JobPost",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("slug", models.SlugField()),
                ("experience_years", models.IntegerField(blank=True, null=True)),
                ("experience_months", models.IntegerField(blank=True, null=True)),
                ("vacancies", models.IntegerField(default=1)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True, verbose_name="Status")),
            ],
            options={
                "verbose_name": "Job Post",
                "ordering": ["-created_on"],
            },
        ),
    ]
