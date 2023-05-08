from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('movie/<int:id>', views.movie, name='movie'),
    path('logout/', views.logout, name='logout'),

]
