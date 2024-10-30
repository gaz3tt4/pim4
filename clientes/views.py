from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from clientes.models import Cliente
# Create your views here.
# função index retorna a viwe index html pasta template

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def ShowClientes(request):
    client = Cliente.objects.all().values('cli_in_id', 'cli_st_nome', 'cli_st_doc', 'cli_st_cidade')
    context = {
        'clientes': client
    }
    
    return render(request, 'showClientes.html', context) 


def cadastro(request):
    # template = loader.get_template('cadastroClientes.html')

    return render(request, 'cadastroClientes.html')

def store(request):
    if request.method == 'POST':
       cliente = Cliente()
       cliente.cli_st_nome = request.POST.get('Nome'),
       cliente.cli_st_doc = request.POST.get('Doc'),    
       cliente.cli_st_endereco = request.POST.get('Endereco'),
       cliente.cli_st_cidade = request.POST.get('Cidade'),
       cliente.cli_st_estado = request.POST.get('Estado'),
       cliente.cli_st_telefone = request.POST.get('Telefone'),
       cliente.cli_st_email = request.POST.get('Email')
       cliente.save()
    return render(request, 'showClientes.html')
