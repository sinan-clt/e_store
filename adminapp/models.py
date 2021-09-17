from django.db import models

# Create your models here.


class signup(models.Model):
    username=models.CharField(max_length=20) 
    
class login(models.Model): 
    email=models.EmailField(max_length=30) 
    password=models.CharField(max_length=30)
    user_id=models.ForeignKey(signup,on_delete=models.CASCADE)



class brand(models.Model):
    brand_names=models.CharField(max_length=30)


class category(models.Model):
    categories=models.CharField(max_length=30)
    brand_category_id=models.ForeignKey(brand,on_delete=models.CASCADE)


class sliderr(models.Model):
    text=models.CharField(max_length=100)
    image=models.CharField(max_length=500)
