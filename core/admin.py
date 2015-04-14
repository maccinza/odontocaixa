# -*- coding: utf-8 -*-
from django.contrib import admin


from core.models import FormaPagamento, Paciente, Atendimento

class AtendimentoAdmin(admin.ModelAdmin):
    filter_horizontal = ['pacientes']

admin.site.register(FormaPagamento)
admin.site.register(Paciente)
admin.site.register(Atendimento, AtendimentoAdmin)