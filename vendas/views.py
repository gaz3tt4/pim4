from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from .models import Vendas, VendasProdutos
from produtos.models import Compra, Produto
from clientes.models import Cliente
from fornecedores.models import Fornecedor



def ShowProdutos(request):
    lista_estoque = Compra.objects.all()
    clientes = Cliente.objects.all()
    
    context = {
        'lista_estoque': lista_estoque,
        'clientes': clientes,
    }
    return render(request, 'showVendas.html', context)

def adicionarItem(request):
    clientes = Cliente.objects.all()
    lista_estoque = Produto.objects.all()
    return render(request, 'Showvendas.html', {'clientes': clientes, 'lista_estoque': lista_estoque})


def salvarVenda(request):
    if request.method == "POST":
        produtos = request.POST.getlist('Produto[]')
        quantidades = request.POST.getlist('Quantidade[]')
        precos = request.POST.getlist('Preco[]')
        cliente_id = request.POST.get('IdCliente')
        data_venda = request.POST.get('DataCompra')

        
        cliente = get_object_or_404(Cliente, cli_in_id=cliente_id)

        
        valor_total = sum(
            float(quantidade) * float(preco.replace('R$', '').replace(',', '.'))
            for quantidade, preco in zip(quantidades, precos)
        )

        # Salva a venda
        venda = Vendas.objects.create(
            vend_in_idCliente=cliente,
            vend_vl_total=valor_total,
            vend_dt_venda=data_venda,
        )

        # Salva os produtos associados à venda
        for produto, quantidade, preco in zip(produtos, quantidades, precos):
            produto_id, _ = produto.split('|')
            produto_obj = get_object_or_404(Produto, est_in_id=produto_id) 
            VendasProdutos.objects.create(
                vend_in_idVenda=venda,
                vend_in_idProduto=produto_obj,
                vend_in_quantidade=int(quantidade),
                vend_vl_valorProduto=float(preco.replace('R$', '').replace(',', '.')),
    )

        return redirect('showVendas') 

    return redirect('showVendas')

