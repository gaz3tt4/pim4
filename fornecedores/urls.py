from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('fornecedor/', views.ShowFornecedor, name='showFornecedor'),
    path('cadastroFornecedor', views.cadastro, name='cadastroFornecedor'),
    path('store', views.store, name='store'),
    path('edit/<int:id>', views.edit, name='editFornecedor'),
    path('update/<int:id>', views.update, name='updateFornecedor')
]