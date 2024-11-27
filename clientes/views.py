from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from clientes.models import Cliente
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from sqlalchemy import create_engine
import pandas as pd
from .utils import validar_nome, edita_cliente, validar_doc, sanitiza_telefone, validar_email, validar_telefone, validar_endereco, validar_cidade, registra_cliente_no_banco
# Create your views here.
# função index retorna a viwe index html pasta template

usuario = 'root'
senha = 'pim'
host = '34.133.125.23'
banco = 'PimT'

connection_string = f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}'

engine = create_engine(connection_string)

def index(request):
    return render(request, 'showClientes.html')

def ShowClientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'showClientes.html', context)

def cadastroClientes(request):
    # template = loader.get_template('cadastroClientes.html')
    return render(request, 'cadastroClientes.html')

def storeCliente(request):
    if request.method == 'POST':
        nome = request.POST.get('Nome')
        if validar_nome(nome):
            doc = request.POST.get('Doc')
            tipo = request.POST.get('Tipo')
            if validar_doc(tipo, doc, request):  # Request é passado para caso a função precise enviar messages
                endereco = request.POST.get('Endereco')
                if validar_endereco(endereco):
                    estado = request.POST.get('Estado')
                    cidade = request.POST.get('Cidade')
                    if validar_cidade(cidade, estado):
                        telefone = sanitiza_telefone(request.POST.get('Telefone'))
                        if validar_telefone(telefone):
                            email = request.POST.get('Email')
                            if validar_email(email):
                                messages.success(request, "Cliente cadastrado com sucesso.")
                                registra_cliente_no_banco(nome, doc, tipo, endereco, cidade, estado, telefone, email)
                                return redirect('showClientes')
                            else:
                                messages.error(request, "Email inválido")
                        else:
                            messages.error(request, "Telefone inválido.")
                    else:
                        messages.error(request, "Cidade inexistente.")
                else:
                    messages.error(request, "Endereço inválido.")
            else:
                pass # Messages já são passadas na função validar_doc
        else:
            messages.error(request, "O nome deve conter somente caracteres.")
    return render(request, 'cadastroClientes.html')

def editCliente(request, id_cli):
    cliente = get_object_or_404(Cliente, pk=id_cli)
    context = {
        'cliente': cliente
    }
    return render(request, 'editClientes.html', context)

def updateCliente(request, id_cli):
    cliente = get_object_or_404(Cliente, pk=id_cli)
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
                                edita_cliente(cliente, nome, doc, tipo, endereco, cidade, estado, telefone, email)
                                messages.success(request, "Cliente editado com sucesso.")
                                return redirect('showClientes')
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
        'cliente' : cliente
    }
    return render(request, 'editClientes.html', context)

def deleteCliente(request, id_cli):
    cliente = get_object_or_404(Cliente, pk=id_cli)
    cliente.delete()
    messages.success(request, "Cliente excluído com sucesso.")
    return ShowClientes(request)

def gerar_relatorio(request):

    query = 'SELECT * FROM clientes_cliente'

    df = pd.read_sql(query, engine)

    # Criando a resposta HTTP com o tipo MIME adequado para arquivos Excel
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="relatorio_clientes.xlsx"'

    # Usando pandas para escrever o DataFrame no arquivo Excel diretamente na resposta HTTP
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Clientes')  # Não incluir o índice na planilha

    return response
