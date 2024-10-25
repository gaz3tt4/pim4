from django.db import models

# Create your models here.
class clientes(models.Model):
    nome = models.CharField(max_length=100)
    Doc = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)