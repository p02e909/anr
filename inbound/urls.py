from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_csv, name="upload_csv"),
    path("data/", views.show_data, name="show_data"),
]
