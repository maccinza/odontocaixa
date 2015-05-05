# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models


from core.models import FormaPagamento, Paciente, Atendimento, Despesa, Pagamento

class AtendimentoAdmin(admin.ModelAdmin):
    filter_horizontal = ['pacientes']

    search_fields = ['pacientes__nome', 'pacientes__sobrenome', 'descricao']
    list_filter = ['data', 'forma_pagamento']
    formfield_overrides = {
        models.ForeignKey: {'empty_label': None},
    }


class DespesaAdmin(admin.ModelAdmin):

    search_fields = ['descricao']
    list_filter = ['categoria']

class PacienteAdmin(admin.ModelAdmin):

    search_fields = ['nome', 'sobrenome', 'email']


admin.site.register(FormaPagamento)
admin.site.register(Pagamento)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
admin.site.register(Despesa, DespesaAdmin)