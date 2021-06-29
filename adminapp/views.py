from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def adminbase(request):
 return render(request,'adminbase.html')
def admindashboard(request):
 return render(request,'admindashboard.html')
def brands(request):
 return render(request,'brands.html')
def addprod(request):
 return render(request,'addprod.html')
def addbrand(request):
 return render(request,'addbrand.html')
def category(request):
 return render(request,'category.html')
def addcategory(request):
 return render(request,'addcategory.html')
def loginadmin(request):
 return render(request,'loginadmin.html')
def signupadmin(request):
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
 return render(request,'slider.html')
def slider2(request):
 return render(request,'slider2.html')
def addslider(request):
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
 



