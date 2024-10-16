# Generated by Django 5.0.4 on 2024-10-16 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0005_remove_transaction_budget"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="is_recurring",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="transaction",
            name="recurring_frequency",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name="RecurringTransaction",
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
                ("next_due_date", models.DateTimeField()),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.transaction",
                    ),
                ),
            ],
        ),
    ]
