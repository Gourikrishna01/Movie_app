from.views import *;
from django.urls import path

urlpatterns=[
   path('',index,name='index'),
   path('register/',register,name='register'),
   path('login/',login,name='login'),
   path('home/',home,name='home'),
   path('admin_login/',admin_login,name="admin_login"),
   path('adminhome/',adminhome,name='adminhome')
]