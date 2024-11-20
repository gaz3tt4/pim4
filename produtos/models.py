from django.db import models

class Produto(models.Model):
    est_in_id = models.AutoField(primary_key=True)  # ID do Produto
    est_ch_tipo = models.CharField(max_length=1)
    est_st_nome = models.CharField(max_length=255)   # Nome do Produto

    def __str__(self):
        return self.est_st_nome
    #  falata fazer makemigrations e migrate


class Compra(models.Model):
    comp_in_id = models.AutoField(primary_key=True)
    comp_in_idFornecedor = models.ForeignKey('fornecedores.Fornecedor', on_delete=models.CASCADE)
    comp_in_idProduto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    comp_in_quantidade = models.CharField(max_length=10)
    comp_in_valor = models.CharField(max_length=10)
    comp_dt_compra = models.DateField()