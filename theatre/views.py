from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from admin_dashboard.models import *
from home.models import UserProfile
from users.models import *
from django.http import JsonResponse
from Book_my_show.settings import KEY,SECRET
from home.forms import *
import razorpay,json
from decimal import Decimal
from datetime import date, timedelta
from django.db.models import Sum
from django.utils import timezone
import decimal
# Create your views here.

def theatre_home(request): 
    if 'user' in request.session:
        return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        # Get today's date
        today = date.today()

        # Get the start and end dates for the current month
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month.replace(month=start_of_month.month+1) - timedelta(days=1)

        # Calculate the total sale price for today
        today_total_price = Theatre_Sale_Report.objects.filter(
            name=request.user,
            date_added__year=today.year,
            date_added__month=today.month,
            date_added__day=today.day
        ).aggregate(total_price=Sum('booking__price'))['total_price'] or 0.00

        today_total_revenue = Theatre_Sale_Report.objects.filter(
            name=request.user,
            date_added__year=today.year,
            date_added__month=today.month,
            date_added__day=today.day
        ).aggregate(total_price=Sum('theatre_earnings'))['total_price'] or 0.00

        # Calculate the sales and revenue data for each day of the week
        sales_data = []
        revenue_data = []
        days_of_week = []

        for i in range(7):
            # Get the date for the corresponding day of the week
            day = today - timedelta(days=today.weekday()) + timedelta(days=i)
            days_of_week.append(day.strftime('%a'))

            # Calculate the total sale price for the day
            day_total_price = Theatre_Sale_Report.objects.filter(
                name=request.user,
                date_added__year=day.year,
                date_added__month=day.month,
                date_added__day=day.day
            ).aggregate(total_price=Sum('booking__price'))['total_price'] or 0.00
            sales_data.append(day_total_price)

            # Calculate the total revenue for the day
            day_total_revenue = Theatre_Sale_Report.objects.filter(
                name=request.user,
                date_added__year=day.year,
                date_added__month=day.month,
                date_added__day=day.day).aggregate(total_price=Sum('theatre_earnings'))['total_price'] or 0.00
            revenue_data.append(day_total_revenue)

        sale_reports=Theatre_Sale_Report.objects.filter(name=request.user)

        # Calculate the total sale price for this month
        month_total_price = Theatre_Sale_Report.objects.filter(name=request.user,date_added__range=(start_of_month, end_of_month)
        ).aggregate(total_price=Sum('booking__price'))['total_price'] or 0.00

        month_total_revenue = Theatre_Sale_Report.objects.filter(name=request.user,date_added__range=(start_of_month, end_of_month)
        ).aggregate(total_price=Sum('theatre_earnings'))['total_price'] or 0.00
        print('sales_data:',sales_data,'revenue_data:',revenue_data,'days_of_week:',days_of_week)
        revenue_data = [float(value) if isinstance(value, decimal.Decimal) else value for value in revenue_data]
        context={
            'sale_reports':sale_reports,
            'today_total_price':today_total_price,
            'month_total_price':month_total_price,
            'today_total_revenue':today_total_revenue,
            'month_total_revenue':month_total_revenue,
            'sales_data': sales_data,
            'revenue_data': revenue_data,
            'days_of_week': days_of_week
        }
        return render(request,'theatre/theatre_home.html',context)
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
        # screens=Screen.objects.filter(theatre_id=request.user.id)
        user_profile=UserProfile.objects.get(user=request.user)
        screens=Screen.objects.filter(theatre=user_profile)
        print('theatre_id',request.user.id)
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
            name=request.POST.get('name')
            price1=request.POST.get('price1')
            price2=request.POST.get('price2') or None
            price3=request.POST.get('price3') or None
            movies_id=request.POST.get('movie')
            rows=request.POST.get('rows')
            columns=request.POST.get('columns')
            show_times = request.POST.getlist('show_times')
            movies=Movies.objects.get(id=movies_id)
            screen=Screen.objects.create(theatre=theatre,name=name,
                                         price1=price1,price2=price2,
                                         price3=price3,movies=movies,
                                         total_seat_rows=rows,total_seat_columns=columns)
            for show_time_id in show_times:
                show_time = Show_Time.objects.get(id=show_time_id)
                screen.show_times.add(show_time)
            screen.save()
            return redirect('theatre_screen')
        else:
            movies=Movies.objects.all()
            shows=Show_Time.objects.all()
            return render(request,'theatre/add_screen.html',{'movies':movies,'shows':shows})
    else:
        return redirect('home')


def update_screen(request,id):
    if 'user' in request.session:
            return redirect('home')
    if 'admin' in request.session:
        return redirect('admin_home')
    if 'theatre' in request.session:
        screen=Screen.objects.get(id=id)
        if request.method=='POST':
            theatre=UserProfile.objects.get(user=request.user)
            name=request.POST.get('name')
            price1=request.POST.get('price1')
            price2=request.POST.get('price2') or None
            price3=request.POST.get('price3') or None
            movies_id=request.POST.get('movie')
            rows=request.POST.get('rows')
            columns=request.POST.get('columns')
            show_times = request.POST.getlist('show_times')
            movies=Movies.objects.get(id=movies_id)
            screen=Screen(id=id,theatre=theatre,name=name,
                          price1=price1,price2=price2,
                          price3=price3,movies=movies,
                          total_seat_rows=rows,total_seat_columns=columns)
            for show_time_id in show_times:
                show_time = Show_Time.objects.get(id=show_time_id)
                screen.show_times.add(show_time)
            screen.save()
            return redirect('theatre_screen')
        else:
            movies = Movies.objects.all()
            shows = Show_Time.objects.all()
            return render(request,'theatre/update_screen.html',{'screens':screen,'movies':movies,'shows':shows})
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


def theatre_side_booking(request):
    bookings=BookedSeat.objects.filter(theatre=request.user).order_by('-id')
    theatre_sale_report=Theatre_Sale_Report.objects.filter(name=request.user).order_by('-id')
    return render(request,'theatre/theatre_side_booking.html',{'theatre_sale_report':theatre_sale_report})

def cancellation_requests(request):  
    user=UserProfile.objects.get(user=request.user)
    cancellation_requests = BookingCancellationRequest.objects.filter(theatre=user,status='pending').order_by('-id')
    return render(request, 'theatre/cancellation_requests.html', {'cancellation_requests': cancellation_requests})

def update_cancellation_request(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        status = request.POST.get('status')
        cancellation_request = BookingCancellationRequest.objects.get(id=request_id)
        cancellation_request.status = status
        cancellation_request.save()
        print('booking_id', cancellation_request.booking.id)
        print('status:', status)
        
        if status == 'accepted':
            booking_id = cancellation_request.booking.id
            booked_seat = BookedSeat.objects.get(id=booking_id)
            # Retrieve the original booking details
            original_theatre_price = booked_seat.price
            original_theatre_earnings = original_theatre_price * Decimal('0.85')
            original_admin_earnings = original_theatre_price * Decimal('0.15')
            
            # Update the booked seats
            booked_seat.booked_seats = ""
            booked_seat.save()

             # Update theatre sale report
            theatre_sale_report = Theatre_Sale_Report.objects.get(booking=booked_seat)
            theatre_sale_report.theatre_earnings -= original_theatre_earnings
            theatre_sale_report.save()

            # Update admin sale report
            admin_sale_report = Admin_Sale_Report.objects.get(theatre_sale_report=theatre_sale_report)
            admin_sale_report.admin_earnings -= original_admin_earnings
            admin_sale_report.save()

            try:
                client = razorpay.Client(auth=(KEY, SECRET))
                paymentId = cancellation_request.booking.payment_id
                refund = client.payment.refund(paymentId, {
                    "amount": int(cancellation_request.booking.price) * 100,
                    "speed": "normal",
                    "notes": {
                        "notes_key_1": "Beam me up Scotty.",
                        "notes_key_2": "Engage"
                    },
                    "receipt": f"Receipt No. {booking_id}"
                })

                if refund['status'] == 'processed':
                    # Refund successful
                    # Add your code here for any additional actions, such as updating the booking or notifying the user
                    print('Refund response:', json.dumps(refund, indent=4))
                    print('Refund processed successfully')
                else:
                    # Refund failed
                    # Handle the refund failure scenario
                    print('Refund response:', json.dumps(refund, indent=4))
                    print('Refund failed')
            except Exception as e:
                print('Error occurred during refund:', str(e))

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def theatre_profile(request):
    user = User.objects.get(username=request.user)
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profile_pic=form.cleaned_data['profile_image']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            location = form.cleaned_data['location']

            # Update the user details
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            # Update the user profile details
            user_profile.profile_image=profile_pic
            user_profile.phone = phone
            user_profile.address = address
            user_profile.location = location
            user_profile.save()
            return redirect('theatre_profile')
    else:
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
        }
        form = UserProfileForm(instance=user_profile,initial=user_data)
        return render(request, 'theatre/theatre_profile.html', {'form':form,'user_profile':user_profile})


def theatre_logout(request):
    if 'theatre' in request.session:
        request.session.flush()
    logout(request)
    return redirect('home')
