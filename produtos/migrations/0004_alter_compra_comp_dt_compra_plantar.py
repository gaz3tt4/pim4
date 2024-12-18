# Generated by Django 5.1.2 on 2024-11-22 00:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_compra_comp_in_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='comp_dt_compra',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='Plantar',
            fields=[
                ('plan_in_id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_in_quantidade', models.IntegerField()),
                ('plan_dt_plantar', models.DateField(default=datetime.date.today)),
                ('plan_dt_colher', models.DateField(blank=True, null=True)),
                ('plan_in_contagem', models.IntegerField(blank=True, null=True)),
                ('plan_in_idProduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
