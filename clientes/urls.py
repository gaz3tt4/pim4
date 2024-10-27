from django.urls import path
from . import views

urlpatterns = [
    path('showclientes', views.ShowClientes, name='showClientes'),
]