from django.urls import path
from inbound import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.upload_csv, name="upload_csv"),
    path("data/", views.show_data, name="show_data"),
]
