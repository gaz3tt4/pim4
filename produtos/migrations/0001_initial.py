# Generated by Django 5.1.2 on 2024-11-15 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0002_rename_frn_in_id_fornecedor_fnr_in_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('est_in_id', models.AutoField(primary_key=True, serialize=False)),
                ('est_st_nome', models.CharField(max_length=255)),
                ('est_ch_tipo', models.CharField(max_length=1)),
                ('est_st_quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('est_st_valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('est_in_idFornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor')),
            ],
        ),
    ]
