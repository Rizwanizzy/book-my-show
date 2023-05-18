from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('movie/<int:id>', views.movie, name='movie'),
    path('theatre_choose/<int:id>', views.theatre_choose, name='theatre_choose'),
    path('seat_selection/<int:theatre_id>/<int:screen_id>/<int:show_time_id>/<str:selected_date>/', views.seat_selection, name='seat_selection'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
