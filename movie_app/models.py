from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    password = models.CharField(max_length=200) 
    phonenumber=models.IntegerField()