from django.db import models
import datetime
from django.utils.translation import gettext as _
# from theatre.models import Theatre_Sale_Report

# Create your models here.

class All_Languages(models.Model):
    language=models.CharField(max_length=30)

    def __str__(self):
        return self.language

class All_Comments(models.Model):
    comments=models.TextField()



class Movies(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    genre=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to="movie_images",blank=True)
    poster=models.ImageField(upload_to="movie_images",blank=True)
    release_date=models.DateField(_("Date"), default=datetime.date.today)
    language=models.ForeignKey(All_Languages,on_delete=models.CASCADE)
    trailer=models.URLField(max_length=300,blank=True)
    runtime=models.DurationField(blank=True,null=True)
    rating=models.DecimalField(max_digits=3, decimal_places=1,null=True,blank=True)
    comments=models.ForeignKey(All_Comments,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title
    
    

