import re
import requests
from .models import Fornecedor
from validate_docbr import CPF , CNPJ
from django.contrib import messages

def validar_nome(nome):

    return not bool(re.search("[!@#$*()_+|?\/<>;.,1234567890\[\]{}=-]", nome))

def validar_doc(tipo, doc, request):

    if tipo == "F":

        if len(doc) == 11:

            cpf = CPF()

            if cpf.validate(doc): return True

            else:
                messages.error(request, "CPF Inexistente.")
                return False

        else:
            messages.error(request, "Tamanho do CPF é inválido.")
            return False

    elif tipo == "J":

        if len(doc) == 14:

            cnpj = CNPJ()

            if cnpj.validate(doc): return True

            else:
                messages.error(request, "CNPJ Inexistente.")
                return False

        else:
            messages.error(request, "Tamanho do CNPJ é inválido.")
            return False

    else:
        messages.error(request, "Tipo inválido.")
        return False

def validar_endereco(endereco):

    # padrao = r"^(Rua|Avenida|Travessa|Alameda|Praça|Largo|Rodovia|Estrada|Beira-Mar|Passagem|Viaduto|Ponte|Caminho|Conjunto|Setor|Zona)\s+[A-Za-zà-úÀ-Ú\s]{1,55}\s+\d{1,5}$"

    if re.match('^[A-Za-zÀ-ÿ\s]+,\s*\d{1,5}$', endereco): return True

    else: return False


def validar_cidade(cidade_procurada, estado):

    if re.match("^[A-Za-záéíóúãõâêîôûàèìòù\s]+$", cidade_procurada):

        cidades = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/distritos")

        cidades_json =cidades.json()

        if cidades:

            for linha in cidades_json:

                if linha['nome'].lower() == cidade_procurada.lower():

                    return True

        return False

    else: return False

def validar_email(email):
    return bool(re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def sanitiza_telefone(telefone):
    return re.sub(r'[^a-zA-Z0-9]', '', telefone)

def validar_telefone(telefone):
   if len(telefone) == 12 or len(telefone) == 13:
    return True
   else:
    return False

def edita_fornecedor(fornecedor, nome, doc, tipo, endereco, cidade, estado, telefone, email):
    fornecedor.fnr_st_nome = nome
    fornecedor.fnr_st_doc = doc
    fornecedor.fnr_ch_tipo = tipo
    fornecedor.fnr_st_endereco = endereco
    fornecedor.fnr_st_cidade = cidade
    fornecedor.fnr_st_estado = estado
    fornecedor.fnr_st_telefone = telefone
    fornecedor.fnr_st_email = email
    fornecedor.save()

def registra_fornecedor_no_banco(nome, doc, tipo, endereco, cidade, estado, telefone, email):
    fornecedor = Fornecedor()
    fornecedor.fnr_st_nome = nome
    fornecedor.fnr_st_doc = doc
    fornecedor.fnr_ch_tipo = tipo
    fornecedor.fnr_st_endereco = endereco
    fornecedor.fnr_st_cidade = cidade
    fornecedor.fnr_st_estado = estado
    fornecedor.fnr_st_telefone = telefone
    fornecedor.fnr_st_email = email
    fornecedor.save()