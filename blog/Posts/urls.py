from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poster/<str:pk>", views.poster, name="poster")
]