from django.db import models
from datetime import date

class Vendas(models.Model):
    vend_in_id = models.AutoField(primary_key=True)  # O ID da venda deve ser único e autoincrementado
    vend_in_idCliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    vend_vl_total = models.DecimalField(decimal_places=2, max_digits=10)
    vend_dt_venda = models.DateField(default=date.today)

    def __str__(self):
        return f"Venda {self.vend_in_id} - Cliente: {self.vend_in_idCliente}"


class VendasProdutos(models.Model):
    vend_in_id_Produto = models.AutoField(primary_key=True)
    vend_in_idVenda = models.ForeignKey('vendas.Vendas', on_delete=models.CASCADE)
    vend_in_idProduto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    vend_in_quantidade = models.IntegerField()
    vend_vl_valorProduto = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Produto {self.vend_in_idProduto} - Quantidade: {self.vend_in_quantidade}"
