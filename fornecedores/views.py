from django.shortcuts import render
from fornecedores.models import Fornecedor
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .utils import validar_nome, validar_doc, edita_fornecedor, validar_endereco, validar_cidade, sanitiza_telefone, validar_telefone, validar_email, registra_fornecedor_no_banco
# Create your views here.

def index(request):
    return redirect('index')

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
                        telefone = sanitiza_telefone(request.POST.get('Telefone'))
                        if validar_telefone(telefone):
                            email = request.POST.get('Email')
                            if validar_email(email):
                                edita_fornecedor(fornecedor, nome, doc, tipo, endereco, cidade, estado, telefone, email)
                                messages.success(request, "Fornecedor editado com sucesso.")
                                return redirect('showFornecedor')
                            else:
                                messages.error(request, "Email inválido.")
                        else:
                            messages.error(request, "Telefone inválido")
                    else:
                        messages.error(request, "Cidade inexistente.")
                else:
                    messages.error(request, "Endereço inválido.")
            else:
                pass
        else:
            messages.error(request, "Nome inválido.")
    context = {
        'fornecedor' : fornecedor
    }
    return render(request, 'editFornecedor.html', context)

def delete(request, id_fnr):
    fornecedor = get_object_or_404(Fornecedor, pk=id_fnr)
    fornecedor.delete()
    messages.success(request, "Fornecedor excluído com sucesso.")
    return ShowFornecedor(request)
