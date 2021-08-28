from django.urls import path
from .import views 

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('hadis/<str:imam>/<str:no>', views.hadis, name = "Hadis"),
    path('perawi', views.perawi, name = "List Imam Perawi"),
    path('carihadis/<str:keyword>', views.carihadis, name = "Cari hadis"),
    path('caridoa', views.caridoa, name = "List Doa"),
]