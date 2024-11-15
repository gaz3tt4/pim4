from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from fornecedores.models import Fornecedor
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def ShowFornecedor(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
    }
    return render(request, 'showFornecedor.html', context)

def cadastro(request):
    return render(request, 'cadastroFornecedor.html')

def store(request):
    if request.method == 'POST':
       fornecedor = Fornecedor()
       fornecedor.fnr_st_nome = request.POST.get('Nome')
       fornecedor.fnr_st_doc = request.POST.get('Doc')   
       fornecedor.fnr_st_endereco = request.POST.get('Endereco')
       fornecedor.fnr_st_cidade = request.POST.get('Cidade')
       fornecedor.fnr_st_estado = request.POST.get('Estado')
       fornecedor.fnr_st_telefone = request.POST.get('Telefone')
       fornecedor.fnr_st_email = request.POST.get('Email')
       fornecedor.save()
    return ShowFornecedor(request)

def edit(request, pk):
    fornecedor = get_object_or_404(Fornecedor, fnr_in_id=pk)
    context = {
        'fornecedor': fornecedor
    }
    return render(request, 'editFornecedor.html', context)

def update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, fnr_in_id=pk)
    fornecedor.Fornecedor = Fornecedor
    if request.method == 'POST':
        fornecedor.fnr_st_nome = request.POST.get('Nome')
        fornecedor.fnr_st_doc = request.POST.get('Doc')   
        fornecedor.fnr_st_endereco = request.POST.get('Endereco')
        fornecedor.fnr_st_cidade = request.POST.get('Cidade')
        fornecedor.fnr_st_estado = request.POST.get('Estado')
        fornecedor.fnr_st_telefone = request.POST.get('Telefone')
        fornecedor.fnr_st_email = request.POST.get('Email')
        fornecedor.save()
    return ShowFornecedor(request)

def delete(request, pk):
    cliente = get_object_or_404(Fornecedor, frn_in_id=pk)
    cliente.delete()
    return ShowFornecedor(request)
