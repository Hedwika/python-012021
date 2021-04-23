from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="katalog")
]

urlpatterns = [
    path('seznam/', views.SeznamView.as_view(), name='seznam')
]