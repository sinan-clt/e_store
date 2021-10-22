from django.db import reset_queries
from django.http.response import JsonResponse
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
 
    data = category.objects.select_related('brand_category_id')
    
    return render(request,'category.html',{'data':data})
 

def addcategory(request):
    brands=brand.objects.all()
    if request.method=='POST':
        categorie=request.POST['addcategory']
        brandss=request.POST['brands']
        # obj=brand(brand_names=brandss)
        # obj.save()
        obj1=category(categories=categorie,brand_category_id_id=brandss)
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




def addfootwears(request):
    return render(request,'addfootwears.html')   



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


def addprodd(request):
    brands=brand.objects.all()
    # categoris=category.objects.all()

    # data = category.objects.select_related('brand_category_id')

    if request.method=='POST':
        brande=request.POST['brand']
        categoriess=request.POST['category']
        prod_namee=request.POST['prodname']
        desc=request.POST['description']
        rate=request.POST['price']
        dress_size=request.POST['size_dress']
        disc=request.POST['discount']
        # prd_image=request.FILES['prod_image']
        # image_name=str(random())+prd_image.name

        # obj=FileSystemStorage()
        # obj.save(image_name,prd_image)

        products=addprod(brand_id=brande,category_id=categoriess,prod_name=prod_namee,description=desc,price=rate,size_dresses=dress_size,discount=disc)
        products.save()

        return render(request,'addprod.html',{"message":"product added successfully"})

    return render(request,'addprod.html',{"cate":brands})


def changecate(request):
    pro_id=request.POST['brandid']
    data=category.objects.filter(brand_category_id_id=pro_id)
    DataJson=[{'id':x.id,'category':x.categories} for x in data]
    return JsonResponse({'dataitem':DataJson})

def productview(request):
    obj=addprod.objects.all()
    obj2=prod_image.objects.all()
    return render(request,'productview.html',{"prods":obj,"imag":obj2})



    
def updateproduct(request,id):
    if request.method=='POST':
        brande=request.POST['brand']
        categoriess=request.POST['category']
        prod_namee=request.POST['prod_name']
        desc=request.POST['description']
        rate=request.POST['price']
        dress_size=request.POST['size_dress']
        disc=request.POST['discount']

        prd_image=request.FILES['prod_image']

        image_namee=str(random())+prd_image.name

        obj=FileSystemStorage()
        obj.save(image_namee,prd_image)

        addprod.objects.filter(id=id).update(brand=brande,category=categoriess,prod_name=prod_namee,description=desc,discount=disc,price=rate,size_dresses=dress_size,imagee=image_namee)
        return redirect('productview')
    
def deleteproduct(request,id):
    addprod.objects.get(id=id).delete()
    return redirect('productview')

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
        obj.save(imagename,bannerimage)

        bannerr.objects.filter(id=id).update(banner_text=bannertext,banner_image=imagename)
        return redirect('banner')

def deletebanner(request,id):
    bannerr.objects.get(id=id).delete()
    return redirect('banner')

def addprodimages(request):
    brands=brand.objects.all()
    if request.method=='POST':
        product=request.POST['produ']
        prod=request.FILES['prodimages']

        files=str(random())+prod.name

        obj=FileSystemStorage()
        obj.save(files,prod)

        obj1=prod_image(products_id=product,image=files)
        obj1.save()

        return render(request,'addprodimages.html',{"message":"Image added Succesfully"})

    return render(request,'addprodimages.html',{"brnd":brands})

def addimg(request):
    pro_id=request.POST['brandid']
    data=category.objects.filter(brand_category_id_id=pro_id)
    DataJson=[{'id':x.id,'category':x.categories} for x in data]
    return JsonResponse({'dataitem':DataJson})


def changeprod(request):
    prodata=request.POST['catid']
    pro=addprod.objects.filter(category_id=prodata)
    projson=[{'id':x.id,'product':x.prod_name} for x in pro]
    return JsonResponse({'item':projson})

def viewprodslider(request):
    obj=addprod.objects.all()
    obj2=prod_image.objects.all()
    return render(request,'viewprodslider.html',{"prods":obj,"imgs":obj2})

def edtprod(request):
    pro_id=request.POST['brandid']
    data=category.objects.filter(brand_category_id_id=pro_id)
    DataJson=[{'id':x.id,'category':x.categories} for x in data]
    return JsonResponse({'dataitem':DataJson})

def viewproductdata(request,id):
    
    brandds=brand.objects.all()
    # categoryyy=category.objects.all()
    obj=prod_image.objects.all()

    obj1=addprod.objects.get(id=id)
    return render(request,'editprodview.html',{"productss":obj1,"brnds":brandds,"img":obj})

# def viewbannerdata(request,id):
#     singleObj=bannerr.objects.get(id=id)
#     return render(request,'editbanner.html',{"data":singleObj})

def updatebanner(request,id):
    if request.method=='POST':
        bannertext=request.POST['bannerrtext']
        bannerimage=request.FILES['bannerrimage']

        imagename=str(random())+bannerimage.name

        obj=FileSystemStorage()
        obj.save(imagename,bannerimage)

        bannerr.objects.filter(id=id).update(banner_text=bannertext,banner_image=imagename)
        return redirect('banner')

def editbanner(request):
 return render(request,'editbanner.html')
def orders(request):
 return render(request,'orders.html')
def adddiscount(request):
 return render(request,'adddiscount.html')
 



