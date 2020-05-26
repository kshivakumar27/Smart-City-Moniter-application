from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

#def login(request):
  #  reg = Register.objects.all()
 #   return render(request,'login.html', ('reg': reg))


# Create your views here.
def home(request):
      return render(request,"home.html")

def login(request):
    #   if request.method== 'POST':
    #        username = request.POST['username']
    #      password = request.POST['password']

    #      user = auth.authenticate(username=username,password=password)

    #      if user is not None:
            #         auth.login(request, user)
    #        return redirect("home.html")
    #     else:
    #         messages.info(request,'invalid credentials..')
            #   return redirect('login')
        #
  #  else:
        return render(request, "login.html"),


def register(request):

    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, password=password2, email=email,name=first_name,)
                user.save();
                print("usercreated")
                return redirect(login)
        else:
            print("password not matching")
            return redirect('home.html')

    else:
        return render(request,'register.html'),