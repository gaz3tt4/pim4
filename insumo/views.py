from django.shortcuts import render
from .models import Insumo
# Create your views here.
def show_insumos(request):
    insumos = Insumo.objects.all().values('ins_in_id', 'ins_st_nome', 'ins_in_quantidade', 'ins_in_valor', 'ins_ch_status')
    context = {
        'insumos': insumos  
    }
    
    return render(request, 'showinsumos.html', context)
