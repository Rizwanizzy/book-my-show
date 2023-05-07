from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_home', views.admin_home,name='admin_home'),
    # path('theatre_login', views.theatre_login,name='theatre_login'),
    # path('theatre_register', views.theatre_register,name='theatre_register'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

]
