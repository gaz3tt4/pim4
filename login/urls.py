from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='loginTemplate'),
<<<<<<< HEAD
    # path('index/', views.index, name='index'),
=======
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
>>>>>>> 20cd9cccac38a9c3ed1eefac2013f029ec2698f6
]