from django.urls import path
from . import views

urlpatterns = [
    #main page
    path(r"", views.index, name="index"),
]