from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from fornecedores.models import Fornecedor
from django.http import HttpResponse

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def ShowProdutos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'showProdutos.html', context)

def cadastroProdutos(request):
    
    return render(request, 'cadastroProdutos.html')

def storeProdutos(request):
    if request.method == 'POST':
       produto = Produto()
       produto.est_ch_tipo = request.POST.get('Tipo')
       produto.est_in_id = request.POST.get('Id_Produto')
       produto.est_st_nome = request.POST.get('Nome') 
       produto.save()
    return redirect('showProdutos')

def editProdutos(request, pk):
    produto = get_object_or_404(Produto, est_in_id=pk)
    context = {
        'produto': produto
    }
    return render(request, 'editProdutos.html', context)

def updateProdutos(request, pk):
    produto = get_object_or_404(Produto, est_in_id=pk)
    produto.Produto = Produto
    if request.method == 'POST':
        produto.est_ch_tipo = request.POST.get('Tipo')
        produto.est_in_id = request.POST.get('Id_Produto')
        produto.nome = request.POST.get('Nome')
        produto.preco = request.POST.get('Preco')
        produto.quantidade = request.POST.get('Quantidade')
        produto.save()
    return redirect('showProdutos')


def deleteProdutos(request, pk):
    produto = get_object_or_404(Produto, id=pk)
    produto.delete()
    return redirect('showProdutos')

def FiltrarProdutos(request):
    produtos = Produto.objects.filter()
    context = {
        'produtos': produtos,
    }
    return render(request, 'showProdutos.html', context)