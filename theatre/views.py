from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

def theatre_home(request):      
    return render(request,'theatre/theatre_home.html')
    

# def theatre_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user and not user.is_superuser:
#             if user.userprofile.is_theatre:
#                 login(request, user)
#                 return render(request, 'theatre/theatre_home.html',{'user':user})
#             else:
#                 messages.info(request, 'Invalid username or password')
#                 return redirect('theatre_login')
#     return render(request,'theatre/theatre_login.html')

# def theatre_register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name =request.POST['last_name']
#         username=request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         is_theatre=False
#         if request.POST['is_theatre']:
#             is_theatre = True
#         if User.objects.filter(username=username).exists():
#             messages.info(request, 'username is taken')
#             return redirect('theatre_home')
#         elif User.objects.filter(email=email).exists():
#             messages.info(request, 'email is taken')
#             return redirect('theatre_register')
#         else:
#             user = User.objects.create_user(username=username, password=password,email=email,
#                                             first_name=first_name,
#                                             last_name=last_name)
#             user_profile=UserProfile.objects.create(user=user, is_theatre=is_theatre)
#             user.save()
#             user_profile.save()
#             messages.success(request, 'Your account has been created. Please log in.')
#             return redirect('theatre_login')
#     return render(request,'theatre/theatre_register.html')

def theatre_logout(request):
    auth.logout(request)
    return redirect('home')
