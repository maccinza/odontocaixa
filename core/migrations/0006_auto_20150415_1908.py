# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150414_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='forma_pagamento',
            field=models.ForeignKey(blank=True, to='core.FormaPagamento', help_text='Indique a forma de pagamento do atendimento.', null=True, verbose_name='Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='valor',
            field=models.FloatField(help_text="Informar o valor (usar 'ponto' como separador decimal) total do atendimento/procedimento realizado.", verbose_name='Valor', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='valor',
            field=models.FloatField(help_text="Indicar o valor (usar 'ponto' como separador decimal) da despesa efetuada.", verbose_name='Valor', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
