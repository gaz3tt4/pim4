from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('showFornecedor/', views.ShowFornecedor, name='showFornecedor'),
    path('cadastroFornecedor', views.cadastro, name='cadastroFornecedor'),
    path('storeFornecedor', views.storeFornecedor, name='storeFornecedor'),
    path('editFornecedor/<int:id_fnr>', views.edit, name='editFornecedor'),
    path('update/<int:id_fnr>', views.update, name='updateFornecedor'),
    path('delete/<int:id_fnr>', views.delete, name='deleteFornecedor'),
    path('gerar-relatorio/', views.gerar_relatorio, name='gerar_relatorio'),
]