# Generated by Django 5.1.2 on 2024-11-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_cli_st_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cli_st_estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]