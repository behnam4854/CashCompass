# Generated by Django 5.0.4 on 2024-09-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20231209_2153"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(max_length=20),
        ),
    ]
