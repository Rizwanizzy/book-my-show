from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

def theatre_home(request):      
    return render(request,'theatre/theatre_home.html')
    

def theatre_logout(request):
    auth.logout(request)
    return redirect('home')
