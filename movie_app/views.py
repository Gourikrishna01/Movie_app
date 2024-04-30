from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from.models import*

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # If authentication fails, you can handle it here, for example, display an error message.
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
  
def home(request):
    return render(request,'home.html')