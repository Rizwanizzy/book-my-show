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

    def __str__(self):
        return str(self.name)