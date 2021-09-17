from django.db import reset_queries
from django.shortcuts import redirect, render
from random import random
from django.http import HttpResponse
from . models import signup,login,brand,sliderr
from django.core.files.storage import FileSystemStorage

# Create your views here.

def adminbase(request):
 return render(request,'adminbase.html')
def admindashboard(request):
 return render(request,'admindashboard.html')

def brands(request):
    brands=brand.objects.all()

    return render(request,'brands.html',{"brands":brands})

def addbrand(request):
    if request.method=='POST':
        brands=request.POST['addbrand']
        obj=brand(brand_names=brands)
        obj.save()
        return redirect('brands')

    return render(request,'addbrand.html')

def viewdata(request,id):
    singleobj=brand.objects.get(id=id)
    return render(request,'editbrand.html',{"data":singleobj})
    
def update(request,id):
    if request.method=='POST':
        brands=request.POST['brand']
        brand.objects.filter(id=id).update(brand_names=brands)
      
        return redirect('brands')

def delete(request,id):
    brand.objects.get(id=id).delete()
    return redirect('brands')

def category(request):
 return render(request,'category.html')

def addcategory(request):
 return render(request,'addcategory.html')


def addprod(request):
 return render(request,'addprod.html')



def loginadmin(request):
    try:
        if request.method=="POST":
            email=request.POST['user_name']
            password=request.POST['password']
            user=login.objects.get(email=email,password=password)

            request.session['user']=user.id
            
            return render(request,'admindashboard.html')
        else:
            return render(request,'loginadmin.html')
    except Exception as e:
        print(e)
    return render(request,'loginadmin.html',{"message2":"Invalid Login Credentials"})

def signupadmin(request):
    try:
        email=request.POST['email']
        user_exist=login.objects.filter(email=email).exists()

        if user_exist==False:
            user_name=request.POST['user_name']
            password=request.POST['password_confirm']
        
            signupObj=signup(username=user_name)
            signupObj.save()
            loginObj=login(email=email,password=password,user_id_id=signupObj.id)
            loginObj.save()

            return render(request,'signupadmin.html',{"message1":"Admin Registered"})

        return render(request,'signupadmin.html',{"message2":"Admin Already Registered"})
        
    except Exception as e:
        print(e)
    return render(request,'signupadmin.html')

def discount(request):
 return render(request,'discount.html')
def productview(request):
 return render(request,'productview.html')
def prodviewpage2(request):
 return render(request,'prodviewpage2.html')
def prodviewpage3(request):
 return render(request,'prodviewpage3.html')
def prodviewpage4(request):
 return render(request,'prodviewpage4.html')
def editprodview(request):
 return render(request,'editprodview.html')
def editbrand(request):
 return render(request,'editbrand.html')
def editcategory(request):
 return render(request,'editcategory.html')
def slider(request):
    obj4=sliderr.objects.all()
    

    return render(request,'slider.html',{"data":obj4})
 

def slider2(request):
 return render(request,'slider2.html')

def addslider(request):
    if request.method=='POST':
        textt=request.POST['slidertext']
        image=request.FILES['imagee']

        image_name=str(random())+image.name
        print(image_name)

        obj=FileSystemStorage()
        obj.save(image_name,image)

        pro=sliderr(text=textt,image=image_name)
        pro.save()

    return render(request,'addslider.html')

def editslider(request):
 return render(request,'editslider.html')
def banner(request):
 return render(request,'banner.html')
def addbanner(request):
 return render(request,'addbanner.html')
def editbanner(request):
 return render(request,'editbanner.html')
def orders(request):
 return render(request,'orders.html')
def adddiscount(request):
 return render(request,'adddiscount.html')
 



