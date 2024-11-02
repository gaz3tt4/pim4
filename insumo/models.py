from django.db import models

# Create your models here.
class Insumo(models.Model):
    ins_in_id = models.AutoField(primary_key=True)
    ins_st_nome = models.CharField(max_length=30)
    ins_in_quantidade = models.IntegerField()
    ins_dt_aquisicao = models.DateField(null=True, blank=True)
    ins_dt_validade = models.DateField(null=True, blank=True)
    ins_in_valor = models.IntegerField()
    ins_ch_status = models.CharField(max_length=1)
    ins_dt_cadastro = models.DateField()
    ins_in_fornecedor = models.IntegerField()