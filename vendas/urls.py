from django.urls import path
from . import views

urlpatterns = [
    path('showVendas/', views.ShowProdutos, name='showVendas'),
    path('adicionarItem/', views.adicionarItem, name='adicionarItem'),
    path('salvarVenda', views.salvarVenda, name='salvarVenda'),
]