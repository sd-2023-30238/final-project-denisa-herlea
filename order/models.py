from django.db import models


class Order(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    adresa = models.CharField(max_length=250)
    oras = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)
