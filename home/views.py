from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'login-submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'home/home.html',{'user':user})
            else:
                messages.info(request, 'Invalid username or password')
                return render(request, 'home/home.html')
        elif 'signup-submit' in request.POST:
            first_name = request.POST['first_name']
            last_name =request.POST['last_name']
            username=request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return render(request, 'home/home.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return render(request, 'home/home.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.success(request, 'Your account has been created. Please log in.')
                return render(request, 'home/home.html')
    return render(request,'home/home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

# def signup(request):
#     if request.method=='POST':
#         first_name = request.POST['first_name']
#         last_name =request.POST['last_name']
#         username=request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists():
#             messages.info(request, 'username is taken')
#             return render(request, 'home/home.html')
#         elif User.objects.filter(email=email).exists():
#             messages.info(request, 'email is taken')
#             return render(request, 'home/home.html')
#         else:
#             user = User.objects.create_user(username=username, password=password, email=email,
#                                             first_name=first_name,
#                                             last_name=last_name)
#             user.save()
#             messages.success(request, 'Your account has been created. Please log in.')
#             return render(request, 'home/home.html')
#     else:
#         return render(request,'home/home.html')
