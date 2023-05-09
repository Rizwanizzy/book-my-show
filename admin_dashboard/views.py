from django.shortcuts import render,redirect
from django.contrib import auth
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from theatre.models import *
# Create your views here.


def admin_home(request):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
        return render(request,'admin_panel/admin_home.html')
    else:
        return redirect('home')


def admin_movies(requset):
    if 'user' in requset.session:
        return redirect('home')
    if 'theatre' in requset.session:
        return redirect('theatre_home')
    if 'admin' in requset.session:
        movies=Movies.objects.all()
        return render(requset,'admin_panel/admin_movies.html',{'movies':movies})
    else:
        return redirect('home')
    

def add_movie(request):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
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
            movie=Movies.objects.create(title=title,description=description,genre=genre,image=image,poster=poster,release_date=release_date,language=language,trailer=trailer,runtime=runtime)
            movie.save()
            return redirect('admin_movies')
        else:
            languages=All_Languages.objects.all()
            return render(request,'admin_panel/add_movie.html',{'languages':languages})
    else:
        return redirect('home')


def update_movie(request,id):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
        movies=Movies.objects.get(id=id)
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
                movie=Movies(id=id,title=title,description=description,genre=genre,image=image,poster=poster,release_date=release_date,language=language,trailer=trailer,runtime=runtime)
                movie.save()
                return redirect('admin_movies')
        else:
            languages=All_Languages.objects.all()
            return render(request,'admin_panel/update_movie.html',{'movies':movies,'languages':languages})
    else:
        return redirect('home')


def delete_movie(request,id):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
        movies=Movies.objects.get(id=id)
        if request.method=='POST':
            movies.delete()
            return redirect('admin_movies')
        else:
            return render(request,'admin_panel/delete_movie.html')
    else:
        return redirect('home')

def admin_theatres(request):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
        theatre=Theatre.objects.filter(is_theatre=True).order_by('id')
        return render(request,'admin_panel/admin_theatres.html',{'theatres':theatre})
    else:
        return redirect('home')

def admin_users(request):
    if 'user' in request.session:
        return redirect('home')
    if 'theatre' in request.session:
        return redirect('theatre_home')
    if 'admin' in request.session:
        users=User.objects.filter(theatre__is_theatre=False)
        return render(request,'admin_panel/admin_users.html',{'users':users})
    else:
        return redirect('home')


def admin_logout(request):
    if 'admin' in request.session:
        request.session.flush()
    logout(request)
    return redirect('home')