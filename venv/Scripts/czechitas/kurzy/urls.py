from django.urls import path
from . import views

urlpatterns = [
    path('', views.SeznamKurzuView.as_view(), name='index_kurzy'),
    path("<int:pk>", views.DetailKurzuView.as_view(), name="detail_kurzu"),
    path('prihlaska/', views.VytvorPrihlasku.as_view(), name="prihlaska"),
    path('prihlaska/potvrzeni/', views.PotvrzeniPrihlasky.as_view(), name="potvrzeni_prihlasky")
]
