from django.shortcuts import render,redirect
from django.contrib import auth
from .models import *

# Create your views here.

def admin_home(request):
    return render(request,'admin_panel/admin_home.html')

def admin_movies(requset):
    movies=Movies.objects.all()
    return render(requset,'admin_panel/admin_movies.html',{'movies':movies})

def add_movie(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        genre=request.POST.get('genre')
        image=request.FILES.get('image')
        poster=request.FILES.get('poster')
        release_date=request.POST.get('release_date')
        language_id=request.POST.get('language')
        trailer=request.POST.get('trailer')
        runtime=request.POST.get('runtime')
        language = All_Languages.objects.get(id=language_id)
        movie=Movies(title=title,description=description,genre=genre,image=image,poster=poster,release_date=release_date,language=language,trailer=trailer,runtime=runtime)
        movie.save()
        return redirect('admin_movies')
    else:
        languages=All_Languages.objects.all()
        return render(request,'admin_panel/add_movie.html',{'languages':languages})

def admin_logout(request):
    auth.logout(request)
    return redirect('home')