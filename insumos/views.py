from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from insumos.models import Insumo

# Função para renderizar o template index.html
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# Função para exibir os insumos
def ShowInsumos(request):
    lista = Insumo.objects.all().values(
        'ins_in_id', 'ins_st_nome', 'ins_in_quantidade', 'ins_dt_aquisicao',
        'ins_dt_validade', 'ins_in_valor', 'ins_ch_status', 'ins_dt_cadastro',
        'ins_in_fornecedor'
    )
    context = {
        'insumos': lista
    }
    return render(request, 'showInsumos.html', context)