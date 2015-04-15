# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_atendimento_recebido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(default='Fixa', help_text='Informa a categoria de uma despesa.', max_length=20, verbose_name='Categoria', choices=[('Fixa', 'Fixa'), ('Compra', 'Compra')])),
                ('descricao', models.TextField(help_text='Inserir breve descri\xe7\xe3o sobre a despesa.', max_length=500, verbose_name='Descri\xe7\xe3o')),
                ('valor', models.FloatField(help_text='Indicar o valor da despesa efetuada.', verbose_name='Valor', validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
