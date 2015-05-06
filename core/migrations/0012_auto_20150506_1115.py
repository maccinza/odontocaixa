# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150505_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data',
            field=models.DateField(default=datetime.date.today, help_text='Informar data de efetua\xe7\xe3o da despesa.', verbose_name='Data'),
        ),
    ]
