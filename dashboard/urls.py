from django.urls import path
from . import views

app_name = 'dashboard'


urlpatterns = [
    # / : URL menant à la page du tableau de bord
    path('', views.tableau_de_bord, name='tableau_de_bord'),
]
