from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="katalog"),
    path('seznam/', views.SeznamAut.as_view(), name='auta'),
    path('vypujcky/', views.PrehledVypujcek.as_view(), name='vypujcky'),
    path('zakaznici/', views.SeznamZakazniku.as_view(), name='zakaznici')
]