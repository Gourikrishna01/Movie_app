from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from.models import*
from django.contrib import messages
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        fullname=request.POST['fullname']
        email=request.POST['email']
        password=request.POST['password']
        phonenumber=request.POST['phonenumber']
        new_user=User.objects.create(username=username,fullname=fullname,email=email,password=password,phonenumber=phonenumber)
     
        new_user.save()
        return redirect('login')
    else:
        return render(request,'Register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('adminhome')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'Admin/login.html')
    return render(request, 'Admin/login.html')


def adminhome(request):
    return render(request,'Admin/Admin_home.html')