from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True, max_length=254)
    data = models.DateField(null=True, blank=True)
    escolhido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome