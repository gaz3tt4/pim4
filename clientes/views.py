from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from clientes.models import Cliente
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
# Create your views here.
# função index retorna a viwe index html pasta template

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def ShowClientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'showClientes.html', context)

def cadastroClientes(request):
    # template = loader.get_template('cadastroClientes.html')
    return render(request, 'cadastroClientes.html')

def storeCliente(request):
    if request.method == 'POST':
       cliente = Cliente()
       cliente.cli_st_nome = request.POST.get('Nome')
       cliente.cli_st_tipo = request.POST.get('Tipo')
       cliente.cli_st_doc = request.POST.get('Doc')   
       cliente.cli_st_endereco = request.POST.get('Endereco')
       cliente.cli_st_cidade = request.POST.get('Cidade')
       cliente.cli_st_estado = request.POST.get('Estado')
       cliente.cli_st_telefone = request.POST.get('Telefone')
       cliente.cli_st_email = request.POST.get('Email')
       cliente.save()
    return redirect('showClientes')

def editCliente(request, pk):
    cliente = get_object_or_404(Cliente, cli_in_id=pk)
    context = {
        'cliente': cliente
    }
    
    return render(request, 'editClientes.html', context)

def updateCliente(request, pk):
    cliente = get_object_or_404(Cliente, cli_in_id=pk)
    cliente.Cliente = Cliente
    if request.method == 'POST':
        cliente.cli_st_nome = request.POST.get('Nome')
        cliente.cli_st_tipo = request.POST.get('Tipo')
        cliente.cli_st_doc = request.POST.get('Doc')   
        cliente.cli_st_endereco = request.POST.get('Endereco')
        cliente.cli_st_cidade = request.POST.get('Cidade')
        cliente.cli_st_estado = request.POST.get('Estado')
        cliente.cli_st_telefone = request.POST.get('Telefone')
        cliente.cli_st_email = request.POST.get('Email')
        cliente.save()
    return redirect('showClientes')

def deleteCliente(request, pk):
    cliente = get_object_or_404(Cliente, cli_in_id=pk)
    cliente.delete()
    return redirect('showClientes')