from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.show_produtos, name='showProdutos'),
    path('produtos/filtrar/', views.filtrar_produtos, name='filtroProdutos'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastroProdutos'),
    path('produtos/editar/<int:produto_id>/', views.editar_produto, name='editarProduto'),
    path('produtos/excluir/<int:produto_id>/', views.excluir_produto, name='excluirProduto'),
]
