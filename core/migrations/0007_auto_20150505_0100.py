# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150415_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='duracao',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idade',
            field=models.PositiveIntegerField(help_text='Informe a idade do paciente.', null=True, verbose_name='Idade', blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sobrenome',
            field=models.CharField(help_text='Informe o(s) sobrenome(s) do paciente.', max_length=200, null=True, verbose_name='Sobrenome', blank=True),
        ),
    ]
