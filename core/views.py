# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.forms import FormRelatorio
from datetime import datetime, timedelta
import pytz


@login_required
def relatorio(request):
    sp = pytz.timezone("America/Sao_Paulo")
    utc = pytz.timezone("UTC")

    report_form = None
    if request.method == 'GET':
        inicio = (sp.normalize(utc.localize(datetime.utcnow())) - timedelta(days=7)).strftime("%d/%m/%Y %H:%M:%S")
        fim = (sp.normalize(utc.localize(datetime.utcnow()))).strftime("%d/%m/%Y %H:%M:%S")

        report_form = FormRelatorio(initial={'data_inicio': inicio,
                                             'data_fim': fim})
    elif request.method == 'POST':
        pass

    return render_to_response('relatorio.html',
                              context_instance=RequestContext(request, {'report_form': report_form}))
