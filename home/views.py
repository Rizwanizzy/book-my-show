from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib import messages
from theatre.models import *
from django.urls import reverse
from theatre.models import *
from .models import *
from admin_dashboard.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if request.method == 'POST':
        if 'login-submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not  None:
                try:
                    profile = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    profile = None
                if profile is not None and profile.is_theatre:
                    request.session['theatre']=username
                    login(request, user)
                    return redirect(reverse('theatre_home'))
                else:
                    login(request, user)
                    if user.is_superuser:
                        request.session['admin']=username
                        return redirect(reverse('admin_home'))
                    else:
                        request.session['user']=username
                        return redirect(reverse('home'))
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('home')
        elif 'signup-submit' in request.POST:
            first_name = request.POST['first_name']
            last_name =request.POST['last_name']
            username=request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            is_theatre=request.POST.get('type')=='theatre'
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('home')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return redirect('home')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,last_name=last_name)
                profile=UserProfile(user=user,is_theatre=is_theatre)
                profile.save()
                
                messages.success(request, 'Your account has been created. Please log in.')
                return redirect('home')
    movies=Movies.objects.all()
    banners=Movies.objects.all()[:4]
    now_playing=Movies.objects.all()[:3]
    return render(request,'home/home.html',{'movies':movies,'banners':banners,'now':now_playing})


def movie(request,id):
    mov=Movies.objects.get(id=id)
    return render(request,'home/movie.html',{'mov':mov})


def user_logout(request):
    if 'user' in request.session:
        request.session.flush()
    logout(request)
    return redirect('home')

