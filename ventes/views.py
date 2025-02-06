from django.shortcuts import render, redirect, get_object_or_404
from .models import Vente
from .forms import VenteForm

def liste_ventes(request):
    # Récupération de toutes les ventes
    ventes = Vente.objects.all()
    return render(request, 'ventes/liste_ventes.html', {'ventes': ventes})

def creer_vente(request):
    if request.method == 'POST':
        # Création d'un formulaire avec les données du formulaire
        form = VenteForm(request.POST)
        if form.is_valid():
            # Création d'une nouvelle vente sans la sauvegarder
            vente = form.save(commit=False)
            # Calcul du montant total de la vente
            vente.montant = sum(produit.prix for produit in form.cleaned_data['produits'])
            # Sauvegarde de la nouvelle vente
            vente.save()
            # Sauvegarde des produits associés à la vente
            form.save_m2m()
            return redirect('ventes:liste_ventes')
    else:
        # Création d'un nouveau formulaire vide
        form = VenteForm()
    return render(request, 'ventes/creer_vente.html', {'form': form})
