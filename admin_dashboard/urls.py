from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin_home/', views.admin_home,name='admin_home'),
    path('admin_movies', views.admin_movies,name='admin_movies'),
    path('add_movie', views.add_movie,name='add_movie'),
    path('update_movie/<int:id>', views.update_movie,name='update_movie'),
    path('delete_movie/<int:id>/', views.delete_movie,name='delete_movie'),
    path('admin_theatres', views.admin_theatres,name='admin_theatres'),
    path('admin_users', views.admin_users,name='admin_users'),
    path('admin_side_booking', views.admin_side_booking,name='admin_side_booking'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

]
