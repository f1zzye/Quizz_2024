# Generated by Django 5.1.4 on 2025-01-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_category_create_datetime_category_last_update_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="image",
            field=models.ImageField(default="default.png", upload_to="covers"),
        ),
    ]
