from django.urls import path
from . import views

app_name = 'petshop'

urlpatterns = [
    path('login_page', views.login_page, name='login_page'),
    path('login_view', views.login_view, name='login_view'),
    path('login_register_view', views.login_register_view, name='login_register_view'),
    path('login_register', views.login_register, name='login_register'),
    path('home', views.home, name='home'),
    path('caini', views.caini, name='caini'),
    path('pisici', views.pisici, name='pisici'),
    path('rozatoare', views.rozatoare, name='rozatoare'),
    path('reptile', views.reptile, name='reptile'),
    path('pasari', views.pasari, name='pasari'),
    path('animale-de-ferma', views.animaleDeFerma, name='animaleDeFerma'),
    path('statistici', views.statistici, name='statistici'),
    path('statistici_view_alba', views.statistici_view_alba, name='statistici_view_alba'),
    path('statistici_view_cluj', views.statistici_view_cluj, name='statistici_view_cluj'),
    path('statistici_view_sibiu', views.statistici_view_sibiu, name='statistici_view_sibiu'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]
