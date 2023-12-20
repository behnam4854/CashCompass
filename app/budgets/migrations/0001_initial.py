# Generated by Django 3.2.7 on 2023-12-09 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_template', models.BooleanField(default=False)),
                ('income', models.DecimalField(decimal_places=0, max_digits=17)),
                ('savings_goal', models.DecimalField(blank=True, decimal_places=0, max_digits=17, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='budgets.budget')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('allocated', models.DecimalField(decimal_places=0, max_digits=17)),
                ('spent', models.DecimalField(decimal_places=0, default=0, max_digits=17)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='budgets.budget')),
            ],
        ),
    ]