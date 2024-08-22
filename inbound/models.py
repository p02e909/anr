from django.db.models import (
    AutoField,
    CharField,
    Model,
    TextField,
)


class MenuModel(Model):
    id = AutoField(primary_key=True)
    menu_code = CharField(max_length=10)
    menu_name = TextField(max_length=50) 


class ElementModel(Model):
    id = AutoField(primary_key=True)
    element_code = CharField(max_length=10)
    element_name = TextField()
