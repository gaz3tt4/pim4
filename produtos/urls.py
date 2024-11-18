from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showProdutos/', views.ShowProdutos, name='showProdutos'),
    path('cadastrar/', views.cadastroProdutos, name='cadastroProdutos'),
    path('editar/<int:produto_id>/', views.editProdutos, name='editarProduto'),
    path('excluir/<int:produto_id>/', views.excluirProdutos, name='excluirProduto'),
]
