# Generated by Django 5.1.3 on 2024-11-24 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_remove_vendas_vend_in_idproduto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendasprodutos',
            old_name='vend_in_id',
            new_name='vend_in_id_Produto',
        ),
        migrations.AlterField(
            model_name='vendasprodutos',
            name='vend_in_idVenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.vendas'),
        ),
    ]
