# Generated by Django 4.1.5 on 2023-01-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="review",
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
                ("title", models.CharField(max_length=64)),
                ("director", models.CharField(max_length=16)),
                ("lead_actor", models.CharField(max_length=16)),
                ("release_year", models.IntegerField()),
                ("genre", models.CharField(max_length=16)),
                ("stats", models.FloatField()),
                ("running_time", models.CharField(max_length=16)),
                ("content", models.TextField()),
            ],
        ),
    ]
