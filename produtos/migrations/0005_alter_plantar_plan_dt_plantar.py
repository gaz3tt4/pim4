# Generated by Django 5.1.2 on 2024-11-23 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_compra_comp_dt_compra_plantar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantar',
            name='plan_dt_plantar',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
