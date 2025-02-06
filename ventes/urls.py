from django.urls import path
from . import views

app_name = 'ventes'
urlpatterns = [
    # /ventes/ : URL menant à la page de la liste des ventes
    path('', views.liste_ventes, name='liste_ventes'),
    # /ventes/nouvelle/ : URL menant à la page de création d'une nouvelle vente
    path('nouvelle/', views.creer_vente, name='creer_vente'),
]
