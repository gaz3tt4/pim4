# Generated by Django 5.1.2 on 2024-10-30 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cli_st_estado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
