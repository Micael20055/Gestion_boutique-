from django import forms
from .models import Produit, Categorie

class ProduitForm(forms.ModelForm):
    # Ajout d'un champ de sélection pour la catégorie
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

    class Meta:
        model = Produit
        # Champs inclus dans le formulaire Produit
        fields = ['nom', 'description', 'prix', 'quantiteEnStock', 'categorie']


from django import forms
from .models import Categorie

class CategorieForm(forms.ModelForm):
    # Définition du formulaire pour le modèle Categorie
    # Seul le champ 'nom' est inclus dans le formulaire
    class Meta:
        model = Categorie
        fields = ['nom']
