from django.urls import path
from . import views

urlpatterns = [
    path('showFornecedor/', views.ShowFornecedor, name='showFornecedor'),
    path('cadastroFornecedor', views.cadastro, name='cadastroFornecedor'),
    path('storeFornecedor', views.storeFornecedor, name='storeFornecedor'),
    path('editFornecedor/<int:id_fnr>', views.edit, name='editFornecedor'),
    path('update/<int:id_fnr>', views.update, name='updateFornecedor'),
    path('delete/<int:id_fnr>', views.delete, name='deleteFornecedor'),
]