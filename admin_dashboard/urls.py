from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_home', views.admin_home,name='admin_home'),
    path('admin_movies', views.admin_movies,name='admin_movies'),
    path('add_movie', views.add_movie,name='add_movie'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

]
