from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    frn_in_id = models.AutoField(primary_key=True)
    fnr_st_nome = models.CharField(max_length=30)
    fnr_ch_tipo = models.CharField(max_length=1)
    fnr_st_doc = models.CharField(max_length=18)
    fnr_st_cep = models.CharField(max_length=20, null=True, blank=True)
    fnr_st_telefone = models.CharField(max_length=15, null=True, blank=True)
    fnr_st_email = models.CharField(max_length=50)
    # fnr_in_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)