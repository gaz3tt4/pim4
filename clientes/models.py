from django.db import models

# Create your models here.
class Cliente(models.Model):
    cli_in_id = models.AutoField(primary_key=True)
    cli_st_nome = models.CharField(max_length=50)
    cli_ch_tipo = models.CharField(max_length=1)
    cli_st_doc = models.CharField(max_length=18)
    cli_st_endereco = models.CharField(max_length=150, null=True, blank=True)
    cli_st_cidade = models.CharField(max_length=50, null=True, blank=True)
    cli_st_estado = models.CharField(max_length=2, null=True, blank=True)
    cli_st_telefone = models.CharField(max_length=20, null=True, blank=True)
    cli_st_email = models.CharField(max_length=50, null=True, blank=True)