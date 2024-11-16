# Generated by Django 5.1 on 2024-10-07 15:20

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategorieProject",
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
                ("label", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="categori-images")),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("label", models.CharField(max_length=150)),
                ("level", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Technologies",
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
                ("name", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        upload_to="image-technologie",
                        verbose_name="une image un un logo representant la technologie",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to="project-cover")),
                ("url", models.URLField(blank=True, null=True)),
                ("published_at", models.DateTimeField()),
                ("status", models.CharField(default=1, max_length=20)),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="portfolio.categorieproject",
                    ),
                ),
                (
                    "technologies",
                    models.ManyToManyField(
                        related_name="technologies", to="portfolio.technologies"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImageProject",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("image", models.ImageField(upload_to="image-project")),
                (
                    "catption",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="une brève description de l'image (facultatif)",
                    ),
                ),
                (
                    "projet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="portfolio.projects",
                    ),
                ),
            ],
        ),
    ]
