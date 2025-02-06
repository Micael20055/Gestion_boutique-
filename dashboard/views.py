from django.shortcuts import render
from produits.models import Produit
from ventes.models import Vente
from django.db import models

def tableau_de_bord(request):
    total_ventes = Vente.objects.count()
    total_montant = sum(vente.montant for vente in Vente.objects.all())
    produits_plus_vendus = Produit.objects.annotate(total_ventes=models.Count('ventes')).order_by('-total_ventes')[:5]
    stock_par_categorie = Produit.objects.values('categorie__nom').annotate(total_stock=models.Sum('quantiteEnStock'))

    context = {
        'total_ventes': total_ventes,
        'total_montant': total_montant,
        'produits_plus_vendus': produits_plus_vendus,
        'stock_par_categorie': stock_par_categorie,
    }
    return render(request, 'dashboard/tableau_de_bord.html', context)
