from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("history_data", views.history_data, name="history_data"),
]