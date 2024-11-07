from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('clientes/', views.ShowClientes, name='showClientes'),
    path('cadastroclientes', views.cadastro, name='cadastroClientes'),
    path('store', views.store, name='store'),# rota utilizada para gravar os dados no banco
    path('edit/<int:pk>', views.edit, name='editClientes'),
    path('update/<int:pk>', views.update, name='updateClientes'),
    path('delete/<int:pk>', views.delete, name='deleteClientes'),
]