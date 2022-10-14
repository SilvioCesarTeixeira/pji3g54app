from django.db import models

# Create your models here.
class Cadastro(models.Model):
    inputEmpresa = models.CharField(max_length=255, null=True, blank=True)
    inputCNPJ = models.CharField(max_length=18, null=True, blank=True)
    inputEmail = models.EmailField(max_length=100, null=True, blank=True)
    inputTel = models.CharField(max_length=13, null=True, blank=True)
    inputCel = models.CharField(max_length=14, null=True, blank=True)
    inputAddress = models.CharField(max_length=255, null=True, blank=True)
    inputNumber = models.PositiveIntegerField(null=True, blank=True)
    inputAddress2 = models.CharField(max_length=100, null=True, blank=True)
    inputCEP = models.CharField(max_length=9, null=True, blank=True)
    inputCity = models.CharField(max_length=50, null=True, blank=True)
    inputEstado = models.CharField(max_length=20, null=True, blank=True)
    inputTipo = models.BooleanField(null=None, blank=None)

