# -*- coding: utf-8 -*-


from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from datetime import datetime


class FormaPagamento(models.Model):
    u"""Representa as formas de pagamento disponíveis"""

    nome = models.CharField(verbose_name=u"Nome",
                            help_text=u"Informe um nome descritivo para esta forma de pagamento.",
                            max_length=75,
                            unique=True)

    desconto = models.PositiveIntegerField(verbose_name=u"Desconto Percentual",
                                           help_text=u"Informe o valor percentual que esta "
                                                     u"forma de pagamento acarreta.",
                                           default=0)

    def save(self, *args, **kwargs):
        for field_name in ['nome']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(FormaPagamento, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u"Forma de Pagamento"
        verbose_name_plural = u"Formas de Pagamento"


class Paciente(models.Model):
    u"""Representa um paciente da clínica, com o registro de suas informações"""

    OPCOES_SEXO = (('F', 'F'),
                   ('M', 'M'))

    regex_telefone = RegexValidator(regex=r'\d{2} \d{4,5}\-\d{4}$',
                                    message=u"Informe o telefone do paciente seguindo o formato indicado.")

    nome = models.CharField(verbose_name=u"Nome",
                            help_text=u"Informe o nome do paciente.",
                            max_length=30)

    sobrenome = models.CharField(verbose_name=u"Sobrenome",
                                 help_text=u"Informe o(s) sobrenome(s) do paciente.",
                                 max_length=200)

    sexo = models.CharField(verbose_name=u"Sexo",
                            help_text=u"Informe o sexo do paciente.",
                            max_length=1,
                            choices=OPCOES_SEXO,
                            default=OPCOES_SEXO[0][0])

    idade = models.PositiveIntegerField(verbose_name=u"Idade",
                                        help_text=u"Informe a idade do paciente.")

    email = models.EmailField(verbose_name=u"E-mail",
                              help_text=u"Informe o e-mail do paciente.",
                              null=True,
                              blank=True)

    telefone = models.CharField(verbose_name=u"Telefone",
                                help_text=u"Informe o telefone do paciente seguindo este 99 9999-9999 "
                                          u"ou este 99 99999-9999 formato.",
                                validators=[regex_telefone],
                                max_length=15,
                                blank=True,
                                null=True)

    def save(self, *args, **kwargs):
        for field_name in ['nome', 'sobrenome']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Paciente, self).save(*args, **kwargs)

    def __unicode__(self):
        return u" ".join([self.nome, self.sobrenome])

    class Meta:
        verbose_name = u"Paciente"
        verbose_name_plural = u"Pacientes"


class Atendimento(models.Model):
    u"""Representa o atendimento prestado, informando suas características"""

    data = models.DateTimeField(verbose_name=u"Data/hora",
                                help_text=u"Informe a data/hora em que o atendimento foi prestado.",
                                default=datetime.now)

    pacientes = models.ManyToManyField(Paciente,
                                       verbose_name=u"Pacientes",
                                       help_text=u"Informar o(s) paciente(s) atendidos.")

    duracao = models.PositiveIntegerField(verbose_name=u"Duração",
                                          help_text=u"Informar duração do atendimento em minutos.",
                                          null=True,
                                          blank=True)

    descricao = models.TextField(verbose_name=u"Descrição",
                                 help_text=u"Insira uma breve descrição sobre o procedimento/atendimento realizado.",
                                 max_length=1500,
                                 null=True,
                                 blank=True)

    valor = models.FloatField(verbose_name=u"Valor",
                              help_text=u"Informar o valor (usar 'ponto' como separador decimal) total do atendimento/procedimento realizado.",
                              validators=[MinValueValidator(0)])

    forma_pagamento = models.ForeignKey(FormaPagamento,
                                        verbose_name=u"Forma de Pagamento",
                                        help_text=u"Indique a forma de pagamento do atendimento.",
                                        null=True,
                                        blank=True)

    recebido = models.BooleanField(verbose_name=u"Recebido",
                                   help_text=u"Marcar esta opção caso já tenha recebido o valor da consulta.",
                                   default=False)

    def save(self, *args, **kwargs):
        for field_name in ['descricao']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Atendimento, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"Atendimento (%s) - %s" % (self.data.strftime('%d/%m/%Y %H:%M:%S'),
                                           ','.join([u.nome for u in self.pacientes.all()]))

    class Meta:
        verbose_name = u"Atendimento"
        verbose_name_plural = u"Atendimentos"


class Despesa(models.Model):
    u"""Representa as despesas semanais"""

    OPCOES_CATEGORIA =((u'Fixa', u'Fixa'),
                       (u'Compra', u'Compra'))

    data_hora = models.DateTimeField(verbose_name=u"Data",
                                     help_text=u"Informar data/hora de efetuação da despesa.",
                                     default=datetime.now)

    categoria = models.CharField(verbose_name=u"Categoria",
                                 help_text=u"Informa a categoria da despesa.",
                                 max_length=20,
                                 choices=OPCOES_CATEGORIA,
                                 default=OPCOES_CATEGORIA[0][0])

    descricao = models.TextField(verbose_name=u"Descrição",
                                 help_text=u"Inserir breve descrição sobre a despesa.",
                                 max_length=500)


    valor = models.FloatField(verbose_name=u"Valor",
                              help_text=u"Indicar o valor (usar 'ponto' como separador decimal) da despesa efetuada.",
                              validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        for field_name in ['descricao']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Despesa, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"Despesa %s (%s) - Valor: %.2f" % (self.categoria,
                                                   self.data_hora.strftime('%d/%m/%Y %H:%M:%S'),
                                                   self.valor)

    class Meta:
        verbose_name = u"Despesa"
        verbose_name_plural = u"Despesas"