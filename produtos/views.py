from django.shortcuts import render, redirect, get_object_or_404
from .models import produtos

def showProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'showProdutos.html', {'produtos': produtos})

def cadastrarProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showProdutos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastroProduto.html', {'form': form})

def editarProduto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('showProdutos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editarProduto.html', {'form': form})

def excluirProduto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('showProdutos')
