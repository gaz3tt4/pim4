from django.urls import path
from . import views

urlpatterns = [
    path('Vendas/', views.Vendas, name='Vendas'),
    path('adicionarItem/', views.adicionarItem, name='adicionarItem'),
    path('salvarVenda', views.salvarVenda, name='salvarVenda'),
    path('showVendas/', views.ListarVendas, name='showVendas'),
]