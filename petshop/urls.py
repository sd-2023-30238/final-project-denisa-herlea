from django.urls import path
from . import views

app_name = 'petshop'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('home', views.login_view, name='login_view'),
    path('login_register_view', views.login_register_view, name='login_register_view'),
    path('login_register', views.login_register, name='login_register'),
    path('home', views.home, name='home'),
]
