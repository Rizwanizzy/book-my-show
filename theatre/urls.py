from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('theatre_home', views.theatre_home,name='theatre_home'),
    # path('theatre_login', views.theatre_login,name='theatre_login'),
    # path('theatre_register', views.theatre_register,name='theatre_register'),
    path('theatre_logout/', views.theatre_logout, name='theatre_logout'),

]
