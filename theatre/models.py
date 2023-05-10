from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import *
from home.models import *
# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_theatre = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.user)

# class Theatre(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='theatre')
#     is_theatre = models.BooleanField(default=False)
#     # userprofile=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
#     location=models.CharField(max_length=30)
#     address=models.TextField()

#     def __str__(self):
#         return str(self.user)
    
class Screen(models.Model):
    theatre=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price1=models.IntegerField()
    price2=models.IntegerField()
    price3=models.IntegerField()
    movies=models.ForeignKey(Movies,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)