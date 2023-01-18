# Generated by Django 4.1.5 on 2023-01-18 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tool",
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
                ("name", models.CharField(max_length=64)),
                ("kind", models.CharField(max_length=64)),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Idea",
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
                ("image", models.ImageField(blank=True, upload_to="posts/%Y%m%d")),
                ("content", models.TextField()),
                ("interest", models.IntegerField(default=0)),
                (
                    "devtool",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="idea_tool",
                        to="posts.tool",
                    ),
                ),
            ],
        ),
    ]
