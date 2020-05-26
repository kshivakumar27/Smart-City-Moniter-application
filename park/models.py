from django.db import models

#Create your models here.

class Register(models.Model):
    Firstname =models.CharField(max_length=100)
    phonenumber =models.IntegerField()
    EmailId = models.CharField(max_length=100)
    Complaints =models.CharField(max_length=100000)




