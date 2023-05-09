from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('movie/<int:id>', views.movie, name='movie'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
