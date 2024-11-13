from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def show_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def filtrar_produtos(request):
    # Lógica para filtrar produtos com base nos dados do formulário
    if request.method == 'POST':
        nome = request.POST.get('Nome')
        produtos = Produto.objects.filter(nome__icontains=nome)
        return render(request, 'produtos.html', {'produtos': produtos})
    return redirect('showProdutos')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showProdutos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastro_produto.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('showProdutos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('showProdutos')
