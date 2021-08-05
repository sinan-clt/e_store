from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class signupp(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)    
    mobilenumber=models.CharField(max_length=20)


class loggin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    user_id=models.ForeignKey(signupp,on_delete=models.CASCADE)
    
