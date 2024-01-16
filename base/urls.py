from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house-list', views.house_list, name='house_list'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    
]
