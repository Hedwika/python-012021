from django.urls import path
from . import views

urlpatterns = [
    path("", views.KurzyView.as_view(), name="index")
]