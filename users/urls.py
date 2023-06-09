from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("user_profile", views.user_profile, name="user_profile"),
    path("bookings", views.bookings, name="bookings"),
    path("cancel_booking", views.cancel_booking, name="cancel_booking"),
]
