# -*- coding: utf-8 -*-

from django.forms import forms, fields, widgets



class FormRelatorio(forms.Form):

    data_inicio = fields.DateTimeField(label=u"Data de Início",
                                       widget=widgets.TextInput(attrs={'class': 'form-control'}))

    data_fim = fields.DateTimeField(label=u"Data de Fim",
                                    widget=widgets.TextInput(attrs={'class': 'form-control'}))
