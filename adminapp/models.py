from django.db import models
from django.db.models.deletion import CASCADE

from userapp.views import changepass

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


class bannerr(models.Model):
    banner_text=models.CharField(max_length=100)
    banner_image=models.CharField(max_length=500)

class addprod(models.Model):
    brand=models.ForeignKey(brand,on_delete=CASCADE)
    category=models.ForeignKey(category,on_delete=CASCADE)
    prod_name=models.CharField(max_length=40)
    description=models.CharField(max_length=500)
    price=models.CharField(max_length=30)
    discount=models.CharField(max_length=500)
    size_dresses=models.CharField(max_length=30)
    


class addfootwear(models.Model):
    brand=models.ForeignKey(brand,on_delete=CASCADE)
    category=models.ForeignKey(category,on_delete=CASCADE)
    prod_name=models.CharField(max_length=40)
    description=models.CharField(max_length=500)
    price=models.CharField(max_length=30)
    size_foot=models.CharField(max_length=30)
    # image=models.CharField(max_length=500)

class prod_image(models.Model):
    products=models.ForeignKey(addprod,on_delete=CASCADE)
    image=models.CharField(max_length=300)
