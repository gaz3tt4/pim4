from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from .models import Vendas, VendasProdutos
from produtos.models import Compra, Produto, Plantar
from clientes.models import Cliente
from fornecedores.models import Fornecedor


def ListarVendas(request):
    vendas = Vendas.objects.all()
    context = {
        'vendas': vendas
    }
    return render(request, 'showVendas1.html', context)


def Vendas(request):
    lista_estoque = Plantar.objects.all()
    clientes = Cliente.objects.all()
    
    context = {
        'lista_estoque': lista_estoque,
        'clientes': clientes,
    }
    return render(request, 'VendasA.html', context)

def salvarVenda(request):
    if request.method == "POST":
        idCliente = request.POST.get('IdCliente')
        idCliente = Cliente.objects.get(cli_in_id=idCliente)

        DataVenda = request.POST.get('DataVenda')
        qnt = request.POST.get('Quantidade')
        prc = request.POST.get('Preco')
        Total = calculaVLTOTAL(qnt, prc)
        venda = Vendas(
            vend_in_idCliente = idCliente,
            vend_dt_venda = DataVenda,
            vend_vl_total = Total
        )
        venda.save()
        

        
        produtos = Vendas.objects.all(vend_in_idVenda=venda.vend_in_id)
        for produto in produtos:
            produto.vend_in_idVenda = venda.vend_in_id
            produto.vend_in_idProduto = request.POST.get('IdProduto')
            produto.vend_in_quantidade = request.POST.get('Quantidade')
            produto.vend_vl_valorProduto = request.POST.get('Preco')
            SalvarVendasProdutos(produto.vend_in_id, produto.vend_in_idProduto, produto.vend_in_quantidade, produto.vend_vl_valorProduto)
        

    return redirect('index')

def SalvarVendasProdutos(vend_in_idVenda, vend_in_idProduto, vend_in_quantidade, vend_vl_valorProduto):
        vp = VendasProdutos(
            vend_in_idVenda = vend_in_idVenda,
            vend_in_idProduto = vend_in_idProduto,
            vend_in_quantidade = vend_in_quantidade,
            vend_vl_valorProduto = vend_vl_valorProduto
        )
        vp.save()
         



def adicionarItem(request):
    clientes = Cliente.objects.all()
    lista_estoque = Plantar.objects.all()
    return render(request, 'Showvendas.html', {'clientes': clientes, 'lista_estoque': lista_estoque})


def calculaVLTOTAL(quantidade, preco):
        valor_total = sum(
             float(quantidade) * float(preco.replace('R$', '').replace(',', '.'))
             for quantidade, preco in zip(quantidade, preco)
        )
        return valor_total


# def salvarVenda(request):
#     if request.method == "POST":
#         produtos = request.POST.getlist('Produto[]')
#         quantidades = request.POST.getlist('Quantidade[]')        
#         precos = request.POST.getlist('Preco[]')
#         cliente_id = request.POST.get('IdCliente')
#         data_venda = request.POST.get('DataCompra')

#         cliente = get_object_or_404(Cliente, cli_in_id=cliente_id)
        
#         valor_total = sum(
#             float(quantidade) * float(preco.replace('R$', '').replace(',', '.'))
#             for quantidade, preco in zip(quantidades, precos)
#         )

#         # Registro da venda
#         venda = Vendas.objects.create(
#             vend_in_idCliente=cliente,
#             vend_vl_total=valor_total,
#             vend_dt_venda=data_venda,
#         )

#         # Salva os produtos associados à venda
#         for produto, quantidade, preco in zip(produtos, quantidades, precos):
            
#             produto_id, _ = produto.split('|')
#             produto_obj = get_object_or_404(Plantar, plan_in_id=produto_id) 
            
#             VendasProdutos.objects.create(
#                 vend_in_idVenda=venda,
#                 vend_in_idProduto=produto_obj,
#                 vend_in_quantidade=int(quantidade),
#                 vend_vl_valorProduto=float(preco.replace('R$', '').replace(',', '.')),
#     )

#         return redirect('showVendas') 

#     return redirect('Index')

