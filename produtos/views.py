from unittest import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Compra, Plantar
from django.http import HttpResponse
from fornecedores.models import Fornecedor
from datetime import date
from datetime import datetime
from django.db.models import F, Func, Value, CharField

# index carrega a template de produção, mostra o progresso da plantação
# def index(request):
#     plantas = Plantar.objects.all()
#     plant_in_id_prod = list(plantas.values_list('plan_in_idProduto', flat=True))
#     plantios = list(plantas.values_list('plan_in_id', flat=True))
#     # plantasid = plantas.__repr__('plan_in_id')
#     produtos = Produto.objects.filter(est_in_id__in=plant_in_id_prod).values_list('est_st_nome', flat=True)
#     Plantado = get_object_or_404(Plantar, plan_in_id__in=plantios)
#     dtPlantar = Plantado.plan_dt_plantar
#     dtColher = Plantado.plan_dt_colher
#     progress = percentual(dtPlantar, dtColher)
    

#     context = {
#         'plantas': plantas
#     }
#     print(progress, dtPlantar, dtColher)
#     return render(request, 'index.html', context)


def index(request):
    plantas = Plantar.objects.all()
    plant_in_id_prod = list(plantas.values_list('plan_in_idProduto', flat=True))

    plant_id = list(plantas.values_list('plan_in_id', flat=True))
    
    # Obtendo os produtos relacionados
    #produtos = Produto.objects.filter(est_in_id__in=plant_in_id_prod).values_list('est_st_nome', flat=True)
    produtos = Produto.objects.all()
    #produtos_id = produtos.values_list('plan_in_idProduto', flat=True)
    #produtos_dict = {produto.est_in_id: produto.est_st_nome for produto in produtos_id}

    # Armazenar todos os objetos Plantar
    plantios = Plantar.objects.filter(plan_in_id__in=plant_id)
    
    
    # Iterar sobre cada objeto Plantar
    Dados = []
    for Plantado in plantios:
        plan_in_idProduto = Plantado.plan_in_idProduto
        plan_dt_plantar = Plantado.plan_dt_plantar
        plan_dt_colher = Plantado.plan_dt_colher
        plan_in_id = Plantado.plan_in_id
        #est_st_nome = produtos_dict.get(Plantado.plan_in_idProduto)
        # plant_in_id_produto = Plantado.plan_in_idProduto

        progress = percentual(plan_dt_plantar, plan_dt_colher)
        Dados.append({
            'progress': progress,
            'plan_dt_plantar': plan_dt_plantar,
            'plan_dt_colher': plan_dt_colher,
            'plan_in_id': plan_in_id,
            'plan_in_idProduto': plan_in_idProduto
            #'est_st_nome': est_st_nome
            
        })
    
    context = {
        'plantas': plantas,
        'produtos': produtos,
        'Dados': Dados,
    }
    
    # Imprimindo para debug
    print(Dados)
    return render(request, 'index.html', context)



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
    #qntComprada = Compra.objects.filter(comp_in_id =request.POST.get('Compra')).values_list('comp_in_quantidade', flat=True).first()
    produtos = Produto.objects.filter(est_in_id__in=compras_id_nome).values_list('est_st_nome',  flat=True)

    
    context = {
        'compras': compras
    }
    return render(request, 'Plantar.html', context)


def storePlantar(request):
    if request.method == 'POST':
        prod_id = request.POST.get('IdProduto')
        produto = Produto.objects.get(est_in_id=prod_id)
        quantidade = request.POST.get('Quantidade')
        quantidade = int(quantidade)
        if quantidade < 0:
            return redirect('Plantar', {'message': 'Quantidade inválida'})
        dataPlantar = request.POST.get('Data_Plantio')
        dataPlantar = datetime.strptime(dataPlantar, '%Y-%m-%d').date()
        dataColher= request.POST.get('Data_Colher')
        dataColher = datetime.strptime(dataColher, '%Y-%m-%d').date()
        if dataColher < dataPlantar:
            return redirect('Plantar', {'message': 'Data de colher inválida'})
        prazo = calculaPrazo(dataPlantar, dataColher)
        planta = Plantar(
            plan_in_idProduto = produto,
            plan_in_quantidade = quantidade,
            plan_dt_plantar = dataPlantar,
            plan_dt_colher = dataColher,
            plan_in_contagem = prazo
        )
        planta.save()
        print(produto)
    return redirect('index')

def calculaPrazo(DtPlantio, DtColheita):
    prazo = DtColheita - DtPlantio
    prazo = int(prazo.days)
    return prazo

def percentual(DtPlantio, DtColheita):
    prazo = calculaPrazo(DtPlantio, DtColheita)
    DtHj = date.today()
    somaPrazo = DtHj - DtPlantio
    somaPrazo = int(somaPrazo.days)
    percentual = (somaPrazo * 100) / prazo
    percentual = int(percentual)

    return percentual