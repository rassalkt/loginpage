from django.urls import path
from . import views

urlpatterns=[ 
    path('loginpage/',views.fnlogin,name="loginapp")
]