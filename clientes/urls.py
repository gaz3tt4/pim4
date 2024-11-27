from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showClientes/', views.ShowClientes, name='showClientes'),
    path('cadastroClientes', views.cadastroClientes, name='cadastroClientes'),
    path('store', views.storeCliente, name='store'),# rota utilizada para gravar os dados no banco
    path('edit/<int:id_cli>', views.editCliente, name='editClientes'),
    path('update/<int:id_cli>', views.updateCliente, name='updateClientes'),
     path('delete/<int:id_cli>', views.deleteCliente, name='deleteClientes'),
    # path('gerar-relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]