from django.urls import path
from . import views

urlpatterns = [
    path('Vendas', views.CadastrarVendas, name='Vendas'),
    path('adicionarItem/', views.adicionarItem, name='adicionarItem'),
    path('salvarVenda/', views.salvarVenda, name='salvarVenda'),
    path('showVendas/', views.ListarVendas, name='showVendas'),
    path('gerar_relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]