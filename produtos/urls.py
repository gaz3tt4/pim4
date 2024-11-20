from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showProdutos/', views.ShowProdutos, name='showProdutos'),
    # path('filtrarProdutos/', views.FiltrarProdutos, name='filtrarProdutos'),
    path('cadastrar/', views.cadastroProdutos, name='cadastroProdutos'),
    path('storeProdutos/', views.storeProdutos, name='storeProdutos'),
    path('buy/', views.buyInsumos, name='comprarInsumo'),
    path('buyInsumo/', views.buyInsumo_store, name='buyInsumo_store'),
    path('edit/<int:pk>/', views.editProdutos, name='editarProdutos'),
    path('update/<int:pk>/', views.updateProdutos, name='updateProdutos'),
    path('delete/<int:pk>/', views.deleteProdutos, name='deleteProdutos'),
]
