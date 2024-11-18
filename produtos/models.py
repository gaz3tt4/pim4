from django.db import models

class Produto(models.Model):
    est_ch_tipo = models.CharField(max_length=1)
    est_in_id = models.AutoField(primary_key=True)  # ID do Produto
    est_in_idFornecedor = models.ForeignKey('fornecedores.Fornecedor', on_delete=models.CASCADE)  # ID do Fornecedor
    est_st_nome = models.CharField(max_length=255)   # Nome do Produto
    est_st_quantidade = models.DecimalField(max_digits=10, decimal_places=2)  # Quantidade
    est_st_valor = models.DecimalField(max_digits=10, decimal_places=2)       # Valor por Kg

    def __str__(self):
        return self.est_st_nome
    #  falata fazer makemigrations e migrate
