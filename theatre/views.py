from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from admin_dashboard.models import *
from home.models import UserProfile
# Create your views here.

def theatre_home(request): 
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        return render(request,'theatre/theatre_home.html')
    else:
        return redirect('home')

def theatre_movies(request):
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        movies=Movies.objects.all()
        return render(request,'theatre/theatre_movies.html',{'movies':movies})
    else:
        return redirect('home')
    
def theatre_screen(request):
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        screens=Screen.objects.all()
        return render(request,'theatre/theatre_screen.html',{'screens':screens})
    else:
        return redirect('home')

def add_screen(request):
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        if request.method=='POST':
            # print('logged in username:',request.user)
            theatre=UserProfile.objects.get(user=request.user)
            name=request.POST['name']
            price1=request.POST['price1']
            price2=request.POST['price2']
            price3=request.POST['price3']
            movies_id=request.POST.get('movie')
            movies=Movies.objects.get(id=movies_id)
            screen=Screen.objects.create(theatre=theatre,name=name,price1=price1,price2=price2,price3=price3,movies=movies)
            screen.save()
            return redirect('theatre_screen')
        else:
            movies=Movies.objects.all()
            return render(request,'theatre/add_screen.html',{'movies':movies})
    else:
        return redirect('home')


def edit_screen(request,id):
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        screen=Screen.objects.get(id=id)
        if request.method=='POST':
            theatre=UserProfile.objects.get(user=request.user)
            name=request.POST['name']
            price1=request.POST['price1']
            price2=request.POST['price2']
            price3=request.POST['price3']
            movies_id=request.POST.get('movie')
            movies=Movies.objects.get(id=movies_id)
            screen=Screen(id=id,theatre=theatre,name=name,price1=price1,price2=price2,price3=price3,movies=movies)
            screen.save()
            return redirect('theatre_screen')
        else:
            movies=Movies.objects.all()
            return render(request,'theatre/edit_screen.html',{'screens':screen,'movies':movies})
    else:
        return redirect('home')

def delete_screen(request,id):
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        screens=Screen.objects.get(id=id)
        if request.method=='POST':
            screens.delete()
            return redirect('theatre_screen')
        else:
            return render(request,'theatre/delete_screen.html')
    else:
        return redirect('home')


def theatre_logout(request):
    if 'theatre' in request.session:
        request.session.flush()
    logout(request)
    return redirect('home')
