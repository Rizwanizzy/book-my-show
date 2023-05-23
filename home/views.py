from django.http import HttpResponseBadRequest
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
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import razorpay
from Book_my_show.settings import KEY,SECRET
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


def cinemas(request):
    cinemas=UserProfile.objects.filter(is_theatre=True)
    return render(request,'home/cinemas.html',{'cinemas':cinemas})


def list_movies(request,id):
    current_date = timezone.now().date()
    upto_six = current_date + timedelta(days=5)
    date_range=[]
    while current_date <= upto_six:
        date_range.append(current_date)
        current_date += timedelta(days=1)
    screens=Screen.objects.filter(theatre=id)
    return render(request,'home/list_movies.html',{'screens':screens,'date_range':date_range})



def theatre_choose(request,id):
    mov=Movies.objects.get(id=id)
    current_date = timezone.now().date()
    upto_six = current_date + timedelta(days=5)
    date_range=[]
    while current_date <= upto_six:
        date_range.append(current_date)
        current_date += timedelta(days=1)
    theatre=Screen.objects.filter(movies_id=id)
    return render(request,'home/theatre_choose.html',{'mov':mov,'theatres':theatre,'date_range':date_range})


def seat_selection(request, theatre_id, screen_id, show_time_id, selected_date):
    screens = Screen.objects.get(id=screen_id)
    global screen_id_selected
    screen_id_selected=screen_id
    show_time = Show_Time.objects.get(id=show_time_id)
    selected_date = selected_date
    date = datetime.strptime(selected_date, '%Y-%m-%d')
    # print(show_time)
    formatted_date = date.strftime('%b %d')
    bookseats=BookedSeat.objects.filter(screen=screens,date=formatted_date,time=show_time)
    booked_seats_list = []  # Create a new list to store booked seats
    for bookseat in bookseats:
        seats = bookseat.booked_seats.split(', ')  # Split the string by comma and space
        seats = [seat.strip("'") for seat in seats]  # Remove single quotes from each seat
        booked_seats_list.extend(seats)
    print(booked_seats_list)
    # print('screen_id',screen_id_selected)
    context = {
        'theatres': screens,
        'times': show_time,
        'selected_date': formatted_date,
        'screen_id': screens,
        'rows': screens.total_seat_rows,
        'columns': screens.total_seat_columns,
        'bookseat': booked_seats_list,
    }
    if request.method == 'POST':
        selected_seats_str = request.POST.get('seats')
        print('in seat selection')
        print('selected_seats_str',selected_seats_str)
        selected_seats = selected_seats_str.split(',') if selected_seats_str else []
        print('selected_seats:',selected_seats)
        theatre = request.POST.get('theatre_name')
        screen = request.POST.get('screen_name')
        movie_title = request.POST.get('movie_title')
        time = request.POST.get('time')
        selected_date = request.POST.get('selected_date')
        seat_count = len(selected_seats)
        price_str = (request.POST.get('total_price'))
        price=float(price_str)
        # print('price type',type(price))
        screen_id=request.POST.get('screen_id')
        print('screen_id',screen_id_selected)
        total_price=price*seat_count
        tax=42.00
        grand_total=total_price+tax
        # booked = BookedSeat(
        #     screen=Screen.objects.get(id=screen_id),
        #     booked_seats=', '.join(selected_seats),
        #     date=selected_date,
        #     time=time
        # )
        # booked.save()
        items={
            'selected_seats': selected_seats,
            'theatre': theatre,
            'screen': screen,
            'movie_title': movie_title,
            'time': time,
            'selected_date': selected_date,
            'seat_count': seat_count,
            'total_price': total_price,
            'grand_total':grand_total
        }
        return render(request,'home/payment.html',items)
    else:
        return render(request, 'home/seat_selection.html', context)

client = razorpay.Client(auth=(KEY, SECRET))
def payment(request):
    DATA = {
        "amount": 5000,
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture":'1'
        }
    payment_order=client.order.create(data=DATA)
    payment_order_id=payment_order['id']
    context={
            'api_key':KEY,
            'order_id':payment_order_id
             }
    if request.method == 'POST':
        selected_seats_list = request.POST.get('selected_seats')
        
        selected_seats = str(selected_seats_list)[1:-1]
        formatted_seats = ', '.join(selected_seats.replace("'", "").split(", "))
        print('selected_seats',selected_seats)
        theatre = request.POST.get('theatre_name')
        screen = request.POST.get('screen_name')
        movie_title = request.POST.get('movie_title')
        time = request.POST.get('time')
        selected_date = request.POST.get('selected_date')
        payment_id = request.POST.get('payment_id')
        seat_list = [seat.strip("' ") for seat in selected_seats.split(",")]
        seat_count = len(seat_list)
        print('seat_count',seat_count)
        price_str = (request.POST.get('total_price'))
        price=float(price_str)
        screen_id=request.POST.get('screen_id')
        total_price=0
        grand_total=0
        total_price=price
        tax=42.00
        grand_total=total_price+tax
        screen_id=Screen.objects.get(id=screen_id_selected)
        booked = BookedSeat(
            screen=Screen.objects.get(id=screen_id_selected),
            booked_seats=selected_seats,
            date=selected_date,
            time=time
        )
        booked.save()
        items={
            'selected_seats': formatted_seats,
            'theatre': theatre,
            'screen': screen,
            'screen_id':screen_id,
            'movie_title': movie_title,
            'time': time,
            'selected_date': selected_date,
            'seat_count': seat_count,
            'total_price': total_price,
            'grand_total':grand_total,
            'payment_id':payment_id,
            
        }
        return render(request,'home/payment_successful.html',items)
    else:
        return render(request, 'home/payment.html',context)


def payment_successful(request):
    return render(request,'home/payment_successful.html')



def user_logout(request):
    if 'user' in request.session:
        request.session.flush()
    logout(request)
    return redirect('home')

