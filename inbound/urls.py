from django.urls import path
from . import views

urlpatterns = [
    path("upload-menu", views.upload_menu, name="upload_menu"),
    path("list-menu-uploaded", views.list_menu_uploaded, name="list_menu_uploaded"),
    path("upload-element", views.upload_element, name="upload_element"),
    path("list-element-uploaded", views.list_element_uploaded, name="list_element_uploaded"),
]
