from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from fornecedores.models import Fornecedor
from fornecedores.urls import *
# Create your views here.

<<<<<<< HEAD

def showfornecedor(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores,
    }
    return render(request, 'showFornecedor.html', context)
=======
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def ShowFornecedor(request):
    lista = Fornecedor.objects.all().values('frn_in_id', 'fnr_st_nome', 'fnr_st_doc', 'fnr_st_cep')
    context = {
        'fornecedores': lista
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

def edit(request, id):
    fornecedor = Fornecedor.objects.get(fnr_in_id=id)
    context = {
        'cliente': fornecedor
    }
    return render(request, 'editFornecedor.html', context)

def update(request, id):
    if request.method == 'POST':
        fornecedor = Fornecedor.objects.get(fnr_in_id=id)
        fornecedor.fnr_st_nome = request.POST.get('Nome')
        fornecedor.fnr_st_doc = request.POST.get('Doc')   
        fornecedor.fnr_st_endereco = request.POST.get('Endereco')
        fornecedor.fnr_st_cidade = request.POST.get('Cidade')
        fornecedor.fnr_st_estado = request.POST.get('Estado')
        fornecedor.fnr_st_telefone = request.POST.get('Telefone')
        fornecedor.fnr_st_email = request.POST.get('Email')
        fornecedor.update()
    return ShowFornecedor(request)
>>>>>>> d660563f8be1f7c1ddf114b16908aac74dc2a6c1
