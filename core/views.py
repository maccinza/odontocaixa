# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.forms import FormRelatorio
from core.models import Atendimento, Despesa
from datetime import timedelta, date, datetime


@login_required
def relatorio(request):

    report_form = None
    total_atendimentos = None
    total_real = None
    total_despesas = None
    a_receber = None
    recebido = None
    inicio = None
    fim = None

    if request.method == 'GET':
        inicio = (date.today() - timedelta(days=7)).strftime("%d/%m/%Y")
        fim = (date.today()).strftime("%d/%m/%Y")

    elif request.method == 'POST':
        total_atendimentos = 0
        total_real = 0
        a_receber = 0
        total_despesas = 0
        recebido = 0
        inicio = request.POST.get('data_inicio')
        fim = request.POST.get('data_fim')

        q_inicio = datetime.strptime(inicio, '%d/%m/%Y').strftime('%Y-%m-%d')
        q_fim = datetime.strptime(fim, '%d/%m/%Y').strftime('%Y-%m-%d')
        atendimentos = Atendimento.objects.filter(data__range=[q_inicio, q_fim])
        despesas = Despesa.objects.filter(data__range=[q_inicio, q_fim])


        for at in atendimentos:
            total_atendimentos += at.valor
            total_real += float(100 - at.forma_pagamento.desconto) * at.valor/float(100)

        for dp in despesas:
            total_despesas += dp.valor

        a_receber = float(total_real - total_despesas)/float(2)

    report_form = FormRelatorio(initial={'data_inicio': inicio,
                                         'data_fim': fim},)

    if total_atendimentos:
        valor_atendimentos = '%.2f' % total_atendimentos
    else:
        valor_atendimentos = None

    if total_real:
        valor_real = '%.2f' % total_real
    else:
        valor_real = None

    if a_receber:
        valor_receber = '%.2f' % a_receber
    else:
        valor_receber = None

    if total_despesas:
        valor_despesas = '%.2f' % total_despesas
    else:
        valor_despesas = None

    return render_to_response('relatorio.html',
                              context_instance=RequestContext(request,
                                                              {'report_form': report_form,
                                                               'valor_atendimentos': valor_atendimentos,
                                                               'valor_real': valor_real,
                                                               'valor_receber': valor_receber,
                                                               'valor_despesas': valor_despesas}))
