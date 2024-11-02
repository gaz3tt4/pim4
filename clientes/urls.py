from django.urls import path
from . import views

urlpatterns = [
    path('showclientes', views.ShowClientes, name='showClientes'),
    path('cadastroclientes', views.cadastro, name='cadastroClientes'),
    path('store', views.store, name='store'),# rota utilizada para gravar os dados no banco
    path('edit/<int:id>', views.edit, name='editClientes'),
    path('update/<int:id>', views.update, name='updateClientes'),
]