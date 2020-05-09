from django.urls import path

from . import views

urlpatterns = [
    path("", views.index) #When the user goes to an empty route, go to views.py and use the index function
]
