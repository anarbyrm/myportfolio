# Generated by Django 4.1.4 on 2022-12-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
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
                ("date", models.DateField(blank=True, null=True)),
                ("info", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
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
                    "level",
                    models.CharField(
                        choices=[
                            ("A1", "Beginner"),
                            ("A2", "Pre-intermediate"),
                            ("B1", "Intermediate"),
                            ("B2", "Upper-intermediate"),
                            ("C1", "Advanced"),
                            ("C2", "Proficiency"),
                        ],
                        max_length=2,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="SoftSkill",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="TechSkill",
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
                    "level",
                    models.CharField(
                        choices=[
                            ("B", "Beginner"),
                            ("P", "Proficient"),
                            ("E", "Expert"),
                        ],
                        max_length=1,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="MyInfo",
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
                ("first_name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                ("field", models.CharField(blank=True, max_length=120, null=True)),
                ("country", models.CharField(blank=True, max_length=120, null=True)),
                ("city", models.CharField(blank=True, max_length=120, null=True)),
                ("bio", models.TextField(blank=True, max_length=120, null=True)),
                ("facebook", models.URLField(blank=True, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("github", models.URLField(blank=True, null=True)),
                (
                    "languages",
                    models.ManyToManyField(blank=True, to="portfolio.language"),
                ),
                (
                    "soft_skills",
                    models.ManyToManyField(blank=True, to="portfolio.softskill"),
                ),
                (
                    "tech_skills",
                    models.ManyToManyField(blank=True, to="portfolio.techskill"),
                ),
            ],
        ),
    ]
