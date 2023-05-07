from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from theatre.models import UserProfile
from django.urls import reverse
# Create your views here.

def home(request):
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
                    return redirect(reverse('theatre_home'))
                else:
                    login(request, user)
                    if user.is_superuser:
                        return redirect(reverse('admin_home'))
                    else:
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
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('home')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return redirect('home')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.success(request, 'Your account has been created. Please log in.')
                return redirect('home')
    return render(request,'home/home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

