from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def liste_produits(request):
    # Récupération de tous les produits
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})

def creer_produit(request):
    if request.method == 'POST':
        # Création d'un formulaire avec les données du formulaire
        form = ProduitForm(request.POST)
        if form.is_valid():
            # Sauvegarde du nouveau produit
            form.save()
            return redirect('produits:liste_produits')
    else:
        # Création d'un nouveau formulaire vide
        form = ProduitForm()
    return render(request, 'produits/creer_produit.html', {'form': form})

def modifier_produit(request, produit_id):
    # Récupération du produit à modifier
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        # Création d'un formulaire avec les données du formulaire et l'instance du produit
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            # Sauvegarde des modifications du produit
            form.save()
            return redirect('produits:liste_produits')
    else:
        # Création d'un formulaire pré-rempli avec les données du produit
        form = ProduitForm(instance=produit)
    return render(request, 'produits/modifier_produit.html', {'form': form, 'produit': produit})

def supprimer_produit(request, produit_id):
    # Récupération du produit à supprimer
    produit = get_object_or_404(Produit, id=produit_id)
    # Suppression du produit
    produit.delete()
    return redirect('produits:liste_produits')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie
from .forms import CategorieForm

def liste_categories(request):
    # Récupération de toutes les catégories
    categories = Categorie.objects.all()
    return render(request, 'produits/liste_categories.html', {'categories': categories})

def creer_categorie(request):
    if request.method == 'POST':
        # Création d'un formulaire avec les données du formulaire
        form = CategorieForm(request.POST)
        if form.is_valid():
            # Sauvegarde de la nouvelle catégorie
            form.save()
            return redirect('produits:liste_categories')
    else:
        # Création d'un nouveau formulaire vide
        form = CategorieForm()
    return render(request, 'produits/creer_categorie.html', {'form': form})

def modifier_categorie(request, categorie_id):
    # Récupération de la catégorie à modifier
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == 'POST':
        # Création d'un formulaire avec les données du formulaire et l'instance de la catégorie
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            # Sauvegarde des modifications de la catégorie
            form.save()
            return redirect('produits:liste_categories')
    else:
        # Création d'un formulaire pré-rempli avec les données de la catégorie
        form = CategorieForm(instance=categorie)
    return render(request, 'produits/modifier_categorie.html', {'form': form, 'categorie': categorie})

def supprimer_categorie(request, categorie_id):
    # Récupération de la catégorie à supprimer
    categorie = get_object_or_404(Categorie, id=categorie_id)
    # Suppression de la catégorie
    categorie.delete()
    return redirect('produits:liste_categories')



