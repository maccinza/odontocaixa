# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(default=datetime.datetime.now, help_text='Informe a data/hora em que o atendimento foi prestado.', verbose_name='Data/hora')),
                ('duracao', models.PositiveIntegerField(help_text='Informar dura\xe7\xe3o do atendimento.', null=True, verbose_name='Dura\xe7\xe3o', blank=True)),
                ('descricao', models.TextField(help_text='Insira uma breve descri\xe7\xe3o sobre o procedimento/atendimento realizado.', max_length=1500, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('valor', models.FloatField(help_text='Informar o valor total do atendimento/procedimento realizado.', verbose_name='Valor', validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(help_text='Informe um nome descritivo para esta forma de pagamento.', unique=True, max_length=75, verbose_name='Nome')),
                ('desconto', models.PositiveIntegerField(default=0, help_text='Informe o valor percentual que esta forma de pagamento acarreta.', verbose_name='Desconto Percentual')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(help_text='Informe o nome do paciente.', max_length=30, verbose_name='Nome')),
                ('sobrenome', models.CharField(help_text='Informe o(s) sobrenome(s) do paciente.', max_length=200, verbose_name='Sobrenome')),
                ('sexo', models.CharField(default=b'F', help_text='Informe o sexo do paciente.', max_length=1, verbose_name='Sexo', choices=[(b'F', b'F'), (b'M', b'M')])),
                ('idade', models.PositiveIntegerField(help_text='Informe a idade do paciente.', verbose_name='Idade')),
                ('email', models.EmailField(help_text='Informe o e-mail do paciente.', max_length=254, null=True, verbose_name='E-mail', blank=True)),
                ('telefone', models.CharField(validators=[django.core.validators.RegexValidator(regex=b'\\d{2} \\d{4,5}\\-\\d{4}$', message='Informe o telefone do paciente seguindo o formato indicado.')], max_length=15, blank=True, help_text='Informe o telefone do paciente seguindo este 99 9999-9999 ou este 99 99999-9999 formato.', null=True, verbose_name='Telefone')),
            ],
        ),
        migrations.AddField(
            model_name='atendimento',
            name='pacientes',
            field=models.ManyToManyField(help_text='Informar o(s) paciente(s) atendidos.', to='core.Paciente', verbose_name='Pacientes'),
        ),
    ]
