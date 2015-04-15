# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_despesa'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='data_hora',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Informar data/hora de efetua\xe7\xe3o da despesa.', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(default='Fixa', help_text='Informa a categoria da despesa.', max_length=20, verbose_name='Categoria', choices=[('Fixa', 'Fixa'), ('Compra', 'Compra')]),
        ),
    ]
