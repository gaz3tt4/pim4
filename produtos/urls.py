from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.showProdutos, name='showProdutos'),
    path('produtos/filtrar/', views.filtrarProdutos, name='filtroProdutos'),
    path('produtos/cadastrar/', views.cadastrarProduto, name='cadastroProdutos'),
    path('produtos/editar/<int:produto_id>/', views.editarProduto, name='editarProduto'),
    path('produtos/excluir/<int:produto_id>/', views.excluirProduto, name='excluirProduto'),
]
