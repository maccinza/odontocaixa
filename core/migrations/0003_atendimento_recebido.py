# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150410_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='recebido',
            field=models.BooleanField(default=False, help_text='Marcar esta op\xe7\xe3o caso j\xe1 tenha recebido o valor da consulta.', verbose_name='Recebido'),
        ),
    ]
