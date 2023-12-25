from django.urls import path
from .views import index, create, edit, delete


urlpatterns = [
    path("", index, name='home'),
    path("create/", create),
    path("edit/<int:id>", edit),
    path("delete/<int:id>", delete),
]