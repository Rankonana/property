from django.urls import path
from . import views

urlpatterns = [

    #house api endpoints
    path('',views.getRoutes),
    path('add-a-house/', views.addAHouse),
    path('add-house-image/', views.addHouseImage),
    path('delete-image/', views.deleteHouseImage),
    path('delete-a-house/', views.deleteHouse),
    path('get-houses/', views.getHouses),
    path('get-houses/<int:property_id>/', views.getHouse, name='get_house'),



    # path('login/', views.login),
    # path('register/', views.register),
    # path('reset-password/', views.resetPassword),
    # path('change-password/', views.changePassword),

]