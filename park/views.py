
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

def mainpage(request):
    return render(request,'home.html')




def loginmethod(request):
     username   = request.POST['username']
     password   = request.POST['password']

     user = auth.authenticate(username = username , password=password)
#     return render(request,'new.html')

     if user is not None:
         auth.login(request,user)
         return redirect('home.html')
     else:
        messages.info(request,'invalid Credentials')
        print('invalid Credentials')
        return redirect('login.html')




     return render(request,'new.html')

















#def register(request):
#    if request.method == 'POST':
 #       first_name =request.POST['first_name']
  #      last_name = request.POST['last_name']
   #     username = request.POST['username']
    #    email = request.POST['email']
     #   password1 = request.POST['password1']
      #  password2 = request.POST['password2']

#        if password1==password2:
      #      if User.objects.filter(username=username).exists():
       #         messages.info(request,'Username taken')
	#        return redirect('/')
         #   elif User.objects.filter(email=email).exists():
	#	messages.info(request,'Email Taken'),
	 #       return redirect('/')
	  #  else:
           #     user = User.objects.create_user(username=username, password=password2, email=email,name=first_name,)
            #    user.save();
             #   print("usercreated")
#            return redirect('loginpage')
 #       else:
  #          print("password not matching")
   #         return redirect('/')

#    else:
 #       return render(request,'registration/register.html')




#Register
def register(request):
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        email      = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                print("User is not created... Username already exists")
                return redirect('registerpage')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email-ID already exists with a registered User')
                 print("User is not created... Email ID exists")
                 return redirect('registerpage')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("User Created")
                return render(request,'loginpage.html')
        else:
            print("User is not created...")
            print("Password not matching...")
            messages.info(request,'Password not matching...')
            return redirect('registerpage')





#return render(request,'login.html')