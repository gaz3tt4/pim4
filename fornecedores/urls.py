from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('showFornecedor/', views.ShowFornecedor, name='showFornecedor'),
    path('cadastroFornecedor', views.cadastro, name='cadastroFornecedor'),
    path('storeFornecedor', views.storeFornecedor, name='storeFornecedor'),
    path('edit/<int:id>', views.edit, name='editFornecedor'),
    path('update/<int:id>', views.update, name='updateFornecedor'),
    path('delete/<int:id>', views.delete, name='deleteFornecedor'),
]