from django import forms
from .models import Vente
from produits.models import Produit

class VenteForm(forms.ModelForm):
    # Ajout d'un champ de sélection multiple pour les produits
    produits = forms.ModelMultipleChoiceField(queryset=Produit.objects.all())

    class Meta:
        model = Vente
        # Champs inclus dans le formulaire Vente
        fields = ['client', 'produits', 'montant']
