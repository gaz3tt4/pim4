# Generated by Django 5.1.2 on 2024-11-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_cli_st_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cli_st_nome',
            field=models.CharField(max_length=255),
        ),
    ]
