from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showProdutos/', views.ShowProdutos, name='showProdutos'),
    path('filtrarProdutos/', views.FiltrarProdutos, name='filtrarProdutos'),
    path('cadastrar/', views.cadastroProdutos, name='cadastroProdutos'),
    path('storeProdutos/', views.storeProdutos, name='storeProdutos'),
    path('edit/<int:produto_id>/', views.editProdutos, name='editarProdutos'),
    path('update/<int:produto_id>/', views.updateProdutos, name='updateProdutos'),
    path('delete/<int:produto_id>/', views.deleteProdutos, name='deleteProdutos'),
]
