from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showProdutos/', views.ShowProdutos, name='showProdutos'),
    path('filtrarProdutos/', views.FiltrarProdutos, name='filtrarProdutos'),
    path('cadastrar/', views.cadastroProdutos, name='cadastroProdutos'),
    path('storeProdutos/', views.storeProdutos, name='storeProdutos'),
    path('buy/<int:pk>/', views.buyProdutos, name='buyProdutos'),
    path('edit/<int:pk>/', views.editProdutos, name='editarProdutos'),
    path('update/<int:pk>/', views.updateProdutos, name='updateProdutos'),
    path('delete/<int:pk>/', views.deleteProdutos, name='deleteProdutos'),
]
