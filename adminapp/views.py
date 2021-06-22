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
 
 



