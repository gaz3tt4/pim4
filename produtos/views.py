from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Compra
from django.http import HttpResponse
from fornecedores.models import Fornecedor

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def ShowProdutos(request):
    produto = Produto.objects.all()
    context = {
        'produtos': produto,
    }
    return render(request, 'showProdutos.html', context)

def cadastroProdutos(request):
    
    return render(request, 'cadastroProdutos.html')

def storeProdutos(request):
    if request.method == 'POST':
       produto = Produto()
       produto.est_ch_tipo = 'I'
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
        produto.est_ch_tipo = 'I'
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

# def FiltrarProdutos(request):
#     produtos = Produto.objects.filter()
#     context = {
#         'produtos': produtos,
#     }
#     return render(request, 'showProdutos.html', context)
def buyInsumos(request):
    fornecedor = Fornecedor.objects.all()
    produto = Produto.objects.all()
    context = {
        'fornecedores': fornecedor,
        'produtos': produto
    }
    return render(request, 'comprarInsumo.html', context)

def buyInsumo_store(request):
    # fornecedor = get_object_or_404(Fornecedor, fnr_in_id=for_id)
    if request.method == 'POST':
        compra = Compra()
        forn = Fornecedor.objects.get(fnr_in_id= request.POST.get('id_fornecedor'))
        compra.comp_in_idProduto = request.POST.get('Id_Produto')
        compra.comp_in_idFornecedor = forn
        compra.comp_in_quantidade = request.POST.get('Quantidade')
        compra.comp_vl_valor = request.POST.get('Preco')
        print(forn)
        compra.save()

    
    return redirect('showProdutos')