from django.urls import path

from . import views

urlpatterns=[
    path("lib/", views.lib, name="lib"),

]