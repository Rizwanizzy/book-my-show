from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='userprofile')
    is_theatre = models.BooleanField(default=False)
    # userprofile=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    location=models.CharField(max_length=30)
    address=models.TextField()

    def __str__(self):
        return str(self.user)