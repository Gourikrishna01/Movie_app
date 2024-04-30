from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(User, primary_key=True,max_length=10)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200) 
    phonenumber = models.CharField(max_length=15)  # Changed to CharField to store phone numbers as strings
