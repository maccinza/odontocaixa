# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150505_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_hora', models.DateTimeField(default=datetime.datetime.now, help_text='Informar data/hora de recebimento do pagamento.', verbose_name='Data')),
                ('valor', models.FloatField(help_text="Indicar o valor (usar 'ponto' como separador decimal) do pagamento recebido.", verbose_name='Valor', validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='recebido',
        ),
    ]
