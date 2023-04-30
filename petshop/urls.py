from django.urls import path
from . import views

app_name = 'petshop'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login', views.login_view, name='login_view'),
    path('login-register-view', views.login_register_view, name='login_register_view'),
    path('login-register', views.login_register, name='login_register'),
    path('home', views.home, name='home'),
    path('caini', views.caini, name='caini'),
    path('pisici', views.pisici, name='pisici'),
    path('rozatoare', views.rozatoare, name='rozatoare'),
    path('reptile', views.reptile, name='reptile'),
    path('pasari', views.pasari, name='pasari'),
    path('animale-de-ferma', views.animaleDeFerma, name='animaleDeFerma'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]
