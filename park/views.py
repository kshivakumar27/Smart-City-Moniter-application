
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import *


def home(request):
    return render(request,'home.html')

    
def registerpage(request):    
        return render(request,'register.html')


def loginpage(request):    
        return render(request,'login.html')

def backtohome(request):
    return render(request,'home.html')

def loginmethod(request):
    return render(request,'new.html')

def register(request):
    return render(request,'login.html')