from django.db import models


# Create your models here.
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)    

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantiteEnStock = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')

    def __str__(self):
        return self.nom
