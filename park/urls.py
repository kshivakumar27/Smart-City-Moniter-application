from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register.html",views.registerpage, name = "registerpage"),
    path("login.html",views.loginpage, name = "loginpage"),
    path("home.html",views.backtohome, name = "backtohome"),
    path("loginmethod",views.loginmethod, name = "loginmethod"),
    path("register",views.register, name = "register"),
]