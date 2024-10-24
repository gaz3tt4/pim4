from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# função index retorna a viwe index html pasta template
def index(request):
    # template = loader.get_template('index.html')
    return HttpResponse('index.html')    