from django.shortcuts import render
from fornecedores.models import Fornecedor
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .utils import validar_nome, validar_doc, validar_endereco, validar_cidade, sanitiza_telefone, validar_telefone, validar_email, registra_fornecedor_no_banco
# Create your views here.


def ShowFornecedor(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores
    }
    return render(request, 'showFornecedor.html', context)

def cadastro(request):
    return render(request, 'cadastroFornecedor.html')

def storeFornecedor(request):
    if request.method == 'POST':
        nome = request.POST.get('Nome')
        if validar_nome(nome):
            doc = request.POST.get('Doc')
            tipo = request.POST.get('Tipo')
            if validar_doc(tipo, doc, request):
                endereco = request.POST.get('Endereco')
                if validar_endereco(endereco):
                    cidade = request.POST.get('Cidade')
                    estado = request.POST.get('Estado')
                    if validar_cidade(cidade, estado):
                        email = request.POST.get('Email')
                        if validar_email(email):
                            telefone = sanitiza_telefone(request.POST.get('Telefone'))
                            if validar_telefone(telefone):
                                messages.success(request, 'Fornecedor cadastrado com sucesso.')
                                registra_fornecedor_no_banco(nome, doc, tipo, endereco, cidade, estado, telefone, email)
                                return redirect('showFornecedor')
                            else:
                                messages.error(request, "Telefone inválido")
                        else:
                            messages.error(request, "Email inválido.")
                    else:
                        messages.error(request, "Cidade inexistente.")
                else:
                    messages.error(request, "Endereço inválido.")
            else:
                pass
        else:
            messages.error(request, "Nome inválido.")
    return render(request, 'cadastroFornecedor.html')

def edit(request, id_fnr):
    fornecedor = get_object_or_404(Fornecedor, pk=id_fnr)
    context = {
        'fornecedor': fornecedor
    }
    return render(request, 'editFornecedor.html', context)

def update(request, id_fnr):
    fornecedor = get_object_or_404(Fornecedor, pk=id_fnr)
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
    return redirect('showFornecedor')

def delete(request, id_fnr):
    cliente = get_object_or_404(Fornecedor, pk=id_fnr)
    cliente.delete()
    return ShowFornecedor(request)
