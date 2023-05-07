from django.shortcuts import render,redirect
from django.contrib import auth

# Create your views here.

def admin_home(request):
    return render(request,'admin_panel/admin_home.html')

def admin_logout(request):
    auth.logout(request)
    return redirect('home')