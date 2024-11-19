from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showClientes/', views.ShowClientes, name='showClientes'),
    path('cadastroClientes', views.cadastroClientes, name='cadastroClientes'),
    path('store', views.storeCliente, name='store'),# rota utilizada para gravar os dados no banco
    path('edit/<int:pk>', views.editCliente, name='editClientes'),
    path('update/<int:pk>', views.updateCliente, name='updateClientes'),
    path('delete/<int:pk>', views.deleteCliente, name='deleteClientes'),
]