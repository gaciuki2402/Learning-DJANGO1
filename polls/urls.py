from django.urls import path
<<<<<<< HEAD
from polls import views
urlpatterns = [
    path("",views.index, name="index"),
    path("about/",views.about, name="about"),
=======

from . import views

urlpatterns=[
    path("lib/", views.lib, name="lib"),
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d

]