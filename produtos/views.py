from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Compra, Plantar
from django.http import HttpResponse
from fornecedores.models import Fornecedor
from datetime import date
from datetime import datetime


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def ShowProdutos(request):
    compras = Compra.objects.all()
    compras_id_nome = list(compras.values_list('comp_in_idProduto', flat=True))
    
    produtos = Produto.objects.filter(est_in_id__in=compras_id_nome).values_list('est_st_nome',  flat=True)
    produto = Produto.objects.filter(est_in_id__in=compras_id_nome).values_list('est_ch_tipo', flat=True)
    context = {
        'compras': compras
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

        # Obtém o fornecedor
        forn_id = request.POST.get('id_fornecedor')
        forn = Fornecedor.objects.get(fnr_in_id=forn_id)

        # Obtém o produto
        prod_id = request.POST.get('Produto')
        produto = Produto.objects.get(est_in_id=prod_id)

        # Obetém e valida a data da compra
        data_compra = request.POST.get('Data_Compra')
        if data_compra:
            data_compra = datetime.strptime(data_compra, '%Y-%m-%d').date()

        # Valida e processa os demais campos
        quantidade = int(request.POST.get('Quantidade'))
        preco = float(request.POST.get('Preco'))

        compra = Compra(
        comp_in_idProduto = produto,
        comp_in_idFornecedor = forn,
        comp_in_quantidade = quantidade,
        comp_vl_valor = preco,
        comp_dt_compra = data_compra
        )
        compra.save()
    return redirect('showProdutos')



def showPlantar(request):
    compras = Compra.objects.all()
    compras_id_nome = list(compras.values_list('comp_in_idProduto', flat=True))
    
    produtos = Produto.objects.filter(est_in_id__in=compras_id_nome).values_list('est_st_nome',  flat=True)
    context = {
        'compras': compras
    }
    return render(request, 'Plantar.html', context)


# def storePlantar(request):
#     if request.method == 'POST':
#         qntComprada = Compra.objects.filter(comp_in_idProduto=request.POST.get('Id_Produto')).values_list('comp_in_quantidade', flat=True).first()
#         qntComprada = int(qntComprada)
#         qntPlantada = request.POST.get('Quantidade')
#         if qntPlantada > qntComprada:
#             return redirect('index', {'error': 'Quantidade de produtos insuficiente'})
#         plantar = Plantar()
#         plantar.plan_in_idProduto = request.POST.get('Id_Produto')
#         plantar.plan_in_quantidade = request.POST.get('Quantidade')
#         plantar.plan_dt_plantar = request.POST.get('Data_Plantar')
#         plantar.plan_dt_colher = request.POST.get('Data_Colher')
#         plantar.save()
#         print(qntComprada)
#     return redirect('index', {'massage': 'Produto plantado com sucesso'})

## Metodo com erro de validação -- corrigir pois nao esta conseguindo puxar a quantidade comprada para comparar com a quantidade plantada

def storePlantar(request):
    if request.method == 'POST':
        # Obter a quantidade comprada do banco
        qntComprada = Compra.objects.filter(
            comp_in_idProduto=request.POST.get('Id_Produto')
        ).values_list('comp_in_quantidade', flat=True).first()
        
        # Lidar com None retornado por `.first()`
        qntComprada = int(qntComprada) if qntComprada is not None else 0
        
        # Obter a quantidade plantada do formulário
        qntPlantada_str = request.POST.get('Quantidade')
        qntPlantada = int(qntPlantada_str) if qntPlantada_str else 0
        
        # Verificar se a quantidade plantada excede a quantidade comprada
        if qntPlantada > qntComprada:
            from django.contrib import messages
            messages.error(request, 'Quantidade de produtos insuficiente.')
            return redirect('index')
        
        # Salvar os dados da plantação
        plantar = Plantar()
        plantar.plan_in_idProduto = request.POST.get('Id_Produto')
        plantar.plan_in_quantidade = qntPlantada
        plantar.plan_dt_plantar = request.POST.get('Data_Plantar')
        plantar.plan_dt_colher = request.POST.get('Data_Colher')
        plantar.save()
        
        from django.contrib import messages
        messages.success(request, 'Produto plantado com sucesso!')
        return redirect('index')
    
    return redirect('index')