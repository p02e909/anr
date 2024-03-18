from django.db.models import (
    Model,
    CharField,
    DateField,
    PositiveIntegerField,
)


class OrderModel(Model):
    product_id = CharField(max_length=10, unique=True, verbose_name="Product ID")
    jap_name = CharField(max_length=200, verbose_name="Japanese name")
    eng_name = CharField(max_length=200, verbose_name="English name")
    category = PositiveIntegerField()
    start_date = DateField(blank=True, null=True, verbose_name="Start date")
    end_date = DateField(blank=True, null=True, verbose_name="End date")
