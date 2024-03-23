from django.urls import path
from . import views

app_name = 'adoption'

urlpatterns = [
    path('adoption_summary', views.adoption_summary, name='adoption_summary'),
    path('alba/', views.all_pets_alba, name='all_pets_alba'),
    path('sibiu/', views.all_pets_sibiu, name='all_pets_sibiu'),
    path('cluj/', views.all_pets_cluj, name='all_pets_cluj'),
    path('item/<slug:slug>/', views.animal_detail, name='animal_detail'),
    path('formular/', views.formular, name='formular'),
    path('add/', views.add, name='add'),
]
