from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from fornecedores.models import Fornecedor


def showfornecedor(request):
    fornecedores = Fornecedor.objects.all()
    context = {
        'fornecedores': fornecedores,
    }
    return render(request, 'showFornecedor.html', context)
