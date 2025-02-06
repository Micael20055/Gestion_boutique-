from django.db import models
from produits.models import Produit

# Create your models here.


class Vente(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=100)
    produits = models.ManyToManyField(Produit, related_name='ventes')
    date = models.DateField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente {self.id} - {self.client}"
