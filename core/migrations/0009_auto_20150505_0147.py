# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150505_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='forma_pagamento',
            field=models.ForeignKey(verbose_name='Forma de Pagamento', to='core.FormaPagamento', help_text='Indique a forma de pagamento do atendimento.', null=True),
        ),
    ]
