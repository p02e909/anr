# Generated by Django 4.0.10 on 2024-03-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderModel",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "product_id",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="Product ID"
                    ),
                ),
                (
                    "jap_name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Japanese name"
                    ),
                ),
                (
                    "eng_name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="English name"
                    ),
                ),
                ("category", models.PositiveIntegerField()),
                (
                    "start_date",
                    models.DateField(blank=True, null=True, verbose_name="Start date"),
                ),
                (
                    "end_date",
                    models.DateField(blank=True, null=True, verbose_name="End date"),
                ),
            ],
        ),
    ]
