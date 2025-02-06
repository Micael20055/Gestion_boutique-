from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    # /produits/categories/ : URL affichant la liste des catégories
    path('categories/', views.liste_categories, name='liste_categories'),

    # /produits/categories/nouveau/ : URL menant à la page d'ajout d'une catégorie
    path('categories/nouveau/', views.creer_categorie, name='creer_categorie'),

    # /produits/categories/<id>/modifier/ : URL pour modifier une catégorie spécifique
    path('categories/<int:categorie_id>/modifier/', views.modifier_categorie, name='modifier_categorie'),

    # /produits/categories/<id>/supprimer/ : URL pour supprimer une catégorie spécifique
    path('categories/<int:categorie_id>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),

    # /produits/ : URL affichant la liste des produits
    path('', views.liste_produits, name='liste_produits'),

    # /produits/nouveau/ : URL menant à la page d'ajout d'un produit
    path('nouveau/', views.creer_produit, name='creer_produit'),

    # /produits/<id>/modifier/ : URL pour modifier un produit spécifique
    path('<int:produit_id>/modifier/', views.modifier_produit, name='modifier_produit'),

    # /produits/<id>/supprimer/ : URL pour supprimer un produit spécifique
    path('<int:produit_id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
]
