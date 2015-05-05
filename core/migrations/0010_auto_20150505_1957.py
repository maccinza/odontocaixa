# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150505_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='pacientes',
        ),
        migrations.RemoveField(
            model_name='despesa',
            name='data_hora',
        ),
        migrations.RemoveField(
            model_name='pagamento',
            name='data_hora',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(blank=True, to='core.Paciente', help_text='Informar o(s) paciente(s) atendidos.', null=True, verbose_name='Pacientes'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='data',
            field=models.DateTimeField(default=datetime.date.today, help_text='Informar data de efetua\xe7\xe3o da despesa.', verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='data',
            field=models.DateTimeField(default=datetime.date.today, help_text='Informar data de recebimento do pagamento.', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateField(default=datetime.date.today, help_text='Informe a data em que o atendimento foi prestado.', verbose_name='Data'),
        ),
    ]
