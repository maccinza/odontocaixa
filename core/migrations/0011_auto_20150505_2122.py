# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150505_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(verbose_name='Paciente', to='core.Paciente', help_text='Informar o paciente atendido.'),
        ),
    ]
