# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimento',
            options={'verbose_name': 'Atendimento', 'verbose_name_plural': 'Atendimentos'},
        ),
        migrations.AlterModelOptions(
            name='formapagamento',
            options={'verbose_name': 'Forma de Pagamento', 'verbose_name_plural': 'Formas de Pagamento'},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='duracao',
            field=models.PositiveIntegerField(help_text='Informar dura\xe7\xe3o do atendimento em minutos.', null=True, verbose_name='Dura\xe7\xe3o', blank=True),
        ),
    ]
