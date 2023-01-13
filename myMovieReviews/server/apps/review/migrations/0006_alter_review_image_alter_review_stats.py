# Generated by Django 4.1.5 on 2023-01-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0005_alter_review_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="stats",
            field=models.FloatField(max_length=1),
        ),
    ]
