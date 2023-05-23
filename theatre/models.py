from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import *
from home.models import *
# Create your models here.
    
class Show_Time(models.Model):
    time=models.TimeField()

    def __str__(self):
        return str(self.time)

class Screen(models.Model):
    theatre=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price1=models.DecimalField(max_digits=6, decimal_places=2)
    price2=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price3=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    movies=models.ForeignKey(Movies,on_delete=models.CASCADE)
    show_times=models.ManyToManyField(Show_Time)
    total_seat_rows=models.IntegerField(default=None)
    total_seat_columns=models.IntegerField(default=None)

    def __str__(self) -> str:
        return f"{self.name} - {self.theatre.user}"

class BookedSeat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    booked_seats = models.CharField(max_length=255,default=None)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=255, default='')
    # Additional fields can be added here, such as customer details, booking status, etc.


    def set_booked_seats(self, integer_list):
        self.booked_seats = ','.join(str(i) for i in integer_list)

    def get_booked_seats(self):
        return [int(i) for i in self.booked_seats.split(',')]

    def __str__(self):
        return str(self.screen)