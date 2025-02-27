from django.db import models

# Create your models here.
from django.db import models

class Adrress(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    localidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)