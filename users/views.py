from django.shortcuts import render
from theatre.models import *


# Create your views here.
def user_profile(request):
    return render(request,'users/user_profile.html')

def bookings(request):
    user=request.user
    booking_details=BookedSeat.objects.filter(user=user).order_by('-id')
    return render(request,'users/bookings.html',{'booking_details':booking_details})