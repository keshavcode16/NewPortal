# Generated by Django 4.1.7 on 2024-07-08 04:43

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "email",
                    models.EmailField(db_index=True, max_length=254, unique=True),
                ),
                ("first_name", models.CharField(max_length=255)),
                (
                    "last_name",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "username",
                    models.CharField(db_index=True, max_length=255, unique=True),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("EMPLOYER", "EMPLOYER"),
                            ("JOB_SEEKER", "JOB_SEEKER"),
                            ("USER_ADMIN", "USER_ADMIN"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("is_verified", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_reset", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("get_notified", models.BooleanField(default=True)),
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
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserGroup",
            fields=[
                (
                    "group_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth.group",
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("EMPLOYER", "EMPLOYER"),
                            ("JOB_SEEKER", "JOB_SEEKER"),
                            ("USER_ADMIN", "USER_ADMIN"),
                        ],
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "user_prefix",
                    models.CharField(max_length=20, verbose_name="User Prefix"),
                ),
            ],
            options={
                "verbose_name": "Permission group",
            },
            bases=("auth.group",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Employer",
            },
            bases=("users.user",),
        ),
        migrations.CreateModel(
            name="JobSeeker",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "higher_qualification",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.qualification",
                    ),
                ),
                (
                    "primary_skills",
                    models.ManyToManyField(blank=True, to="common.skill"),
                ),
            ],
            options={
                "verbose_name": "Job Seeker",
            },
            bases=("users.user",),
        ),
    ]