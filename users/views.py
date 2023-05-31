from django.shortcuts import render
from theatre.models import *
from django.http import JsonResponse
from theatre.models import *
from .models import *

# Create your views here.
def user_profile(request):
    return render(request,'users/user_profile.html')

def update_booking_cancellation_request(booking, theatre, user, reason, status):
    booking_cancellation_request, created = BookingCancellationRequest.objects.get_or_create(booking=booking)
    if not created:
        booking_cancellation_request.theatre = theatre
        booking_cancellation_request.user = user
        booking_cancellation_request.reason = reason
    booking_cancellation_request.status = status
    booking_cancellation_request.save()

def bookings(request):
    user=request.user
    booking_details=BookedSeat.objects.filter(user=user).order_by('-id')
    booking_ids = booking_details.values_list('id', flat=True)
    cancel_requests = BookingCancellationRequest.objects.filter(booking__in=booking_ids)

    if request.method == 'POST':
        # Assuming you have form inputs for the booking_cancellation_request fields
        theatre = request.POST.get('theatre')
        reason = request.POST.get('reason')
        status = request.POST.get('status')
        
        # Assuming you have the booking object to update
        booking = BookedSeat.objects.get(id=request.POST.get('booking_id'))
        
        update_booking_cancellation_request(booking, theatre, user, reason, status)
    return render(request,'users/bookings.html',{'booking_details':booking_details,'cancel_requests':cancel_requests})

def cancel_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = BookedSeat.objects.get(id=booking_id)
        theatre=booking.theatre
        reason = request.POST.get('reason')
        user=request.user
        # Check if a cancellation request already exists for the booking
        cancellation_request = BookingCancellationRequest.objects.filter(booking=booking).first()
        if cancellation_request:
            return JsonResponse({'status': 'error', 'message': 'Cancellation request already exists.'})
        
        cancellation_request = BookingCancellationRequest.objects.create(booking=booking,theatre=theatre,reason=reason, status='pending',user=user)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})