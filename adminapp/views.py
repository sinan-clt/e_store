from django.db import reset_queries
from django.shortcuts import redirect, render
from random import random
from django.http import HttpResponse
from . models import *
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
    try:
        brands=request.POST['addbrand']
        brandexist=brand.objects.filter(brand_names=brands).exists()
        if brandexist==False:
            obj=brand(brand_names=brands)
            obj.save()
            return redirect('brands')
        return render(request,'addbrand.html',{"message":"brand already exist"})
    except Exception as e:
        print(e)
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

def categoryy(request):
    brands=brand.objects.all()
    categoris=category.objects.all()
    return render(request,'category.html',{"brands":brands,"categr":categoris})
 

def addcategory(request):
    brands=brand.objects.all()
    if request.method=='POST':
        categorie=request.POST['addcategory']
        brandss=request.POST['brands']
        obj=brand(brand_names=brandss)
        obj.save()
        obj1=category(categories=categorie,brand_category_id_id=obj.id)
        obj1.save()
        return redirect('categoryy')
    return render(request,'addcategory.html',{"brands":brands})



def viewcategorydata(request,id):
    singleObj=category.objects.get(id=id)
    brnds=brand.objects.all()

    return render(request,'editcategory.html',{"data":singleObj,"brndd":brnds})

def updatecategory(request,id):
    if request.method=='POST':
        brandw=request.POST['brande']
        categoris=request.POST['category']
        brand.objects.filter(id=id).update(brand_names=brandw)
        category.objects.filter(id=id).update(categories=categoris)
        return redirect('categoryy')

def deletecategory(request,id):
    category.objects.get(id=id).delete()
    return redirect('categoryy')

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
        return render(request,'addslider.html',{"message":"slider added successfully"})

    return render(request,'addslider.html')

def viewsliderdata(request,id):
    singleobj=sliderr.objects.get(id=id)
    return render(request,'editslider.html',{"data":singleobj})
    
def updateslider(request,id):
    if request.method=='POST':
        slider_text=request.POST['slidertext']
        sliderimg=request.FILES['sliderimagee']

        imagename=str(random())+sliderimg.name
        print(imagename)

        obj=FileSystemStorage()
        obj.save(imagename,sliderimg)

        sliderr.objects.filter(id=id).update(text=slider_text,image=imagename)
        return redirect('slider')


def deleteslider(request,id):
    sliderr.objects.get(id=id).delete()
    return redirect('slider')

def editslider(request):
 return render(request,'editslider.html')

def banner(request):
    obj=bannerr.objects.all()

    return render(request,'banner.html',{"data":obj})

def addbanner(request):
    if request.method=='POST':
        bannertext=request.POST['bannerrtext']
        bannerimage=request.FILES['bannerrimage']

        imgname=str(random())+bannerimage.name
        print(imgname)

        obj3=FileSystemStorage()
        obj3.save(imgname,bannerimage)

        banr=bannerr(banner_text=bannertext,banner_image=imgname)
        banr.save()

        return render(request,'addbanner.html',{"message":"banner added succesfully"})
    return render(request,'addbanner.html')

def viewbannerdata(request,id):
    singleObj=bannerr.objects.get(id=id)
    return render(request,'editbanner.html',{"data":singleObj})

def updatebanner(request,id):
    if request.method=='POST':
        bannertext=request.POST['bannerrtext']
        bannerimage=request.FILES['bannerrimage']

        imagename=str(random())+bannerimage.name

        obj=FileSystemStorage()
        obj.save()

        bannerr.objects.filter(id=id).update(banner_text=bannertext,banner_image=bannerimage)
        return redirect('banner')

def deletebanner(request,id):
    bannerr.objects.get(id=id).delete()
    return redirect('banner')


def editbanner(request):
 return render(request,'editbanner.html')
def orders(request):
 return render(request,'orders.html')
def adddiscount(request):
 return render(request,'adddiscount.html')
 



