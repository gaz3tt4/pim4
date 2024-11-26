from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='loginTemplate'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
]