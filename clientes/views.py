from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from clientes.models import clientes


# Create your views here.
# função index retorna a viwe index html pasta template
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def ShowClientes(request):
    client = clientes.objects.all().values()
    template = loader.get_template('showClientes.html')
    context = {
        'cliente': client
    }
    return HttpResponse(template.render(context, request))