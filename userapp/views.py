from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import signupp,loggin

# Create your views here.

def user(request):
 return render(request,'user.html')
def shop(request):
 return render(request,'shop.html') 
def shopprod1(request):
 return render(request,'shopprod1.html') 

def signup(request):

    try:
        user=request.POST['user_name']
        user_exist=loggin.objects.filter(username=user).exists()

        if user_exist==False:
            fname=request.POST['first_name']
            print(fname)
            lname=request.POST['last_name']
            email=request.POST['email']
            mobile=request.POST['mobile_number']

            passwordd=request.POST['confrm_pass']

            signupObj=signupp(firstname=fname,lastname=lname,email=email,mobilenumber=mobile)
            signupObj.save()

            loginObj=loggin(username=user,password=passwordd,user_id_id=signupObj.id)
            loginObj.save()

            return render(request,'signup.html',{"message1":"user registered"}) 
        return render(request,'signup.html',{"message2":"username already exist"}) 

    except Exception as e:
      print(e)
    return render(request,'signup.html') 

def login(request):
 return render(request,'login.html') 

def profile(request):
 return render(request,'profile.html') 
def cart(request):
 return render(request,'cart.html')  
def log(request):
 return render(request,'log.html')  
def shopprod3(request):
 return render(request,'shopprod3.html')  
def shopbase(request):
 return render(request,'shopbase.html') 
def shopprod4(request):
 return render(request,'shopprod4.html') 
def shopprod2(request):
 return render(request,'shopprod2.html') 
def shopprod5(request):
 return render(request,'shopprod5.html') 
def shopprod6(request):
 return render(request,'shopprod6.html') 
def shopprod7(request):
 return render(request,'shopprod7.html')
def shopprod8(request):
 return render(request,'shopprod8.html') 
def shopprod9(request):
 return render(request,'shopprod9.html') 
def shopprod10(request):
 return render(request,'shopprod10.html') 
def shopprod11(request):
 return render(request,'shopprod11.html')
def shopprod12(request):
 return render(request,'shopprod12.html') 
def shopprod13(request):
 return render(request,'shopprod13.html') 
def shopprod14(request):
 return render(request,'shopprod14.html')
def shopprod15(request):
 return render(request,'shopprod15.html') 
def shopprod16(request):
 return render(request,'shopprod16.html')  
def shopprod17(request):
 return render(request,'shopprod17.html') 
def shopprod18(request):
 return render(request,'shopprod18.html') 
def shopprod19(request):
 return render(request,'shopprod19.html') 
def shopprod20(request):
 return render(request,'shopprod20.html') 
def shopprodpage2(request):
 return render(request,'shopprodpage2.html')
def shopprod21(request):
 return render(request,'shopprod21.html') 
def shopprod22(request):
 return render(request,'shopprod22.html') 
def shopprod23(request):
 return render(request,'shopprod23.html') 
def shopprod24(request):
 return render(request,'shopprod24.html') 
def shopprod25(request):
 return render(request,'shopprod25.html') 
def shopprod26(request):
 return render(request,'shopprod26.html') 
def shopprod27(request):
 return render(request,'shopprod27.html') 
def shopprod28(request):
 return render(request,'shopprod28.html') 
def shopprod29(request):
 return render(request,'shopprod29.html') 
def shopprod30(request):
 return render(request,'shopprod30.html') 
def shopprod31(request):
 return render(request,'shopprod31.html') 
def shopprod32(request):
 return render(request,'shopprod32.html') 
def shopshoes(request):
 return render(request,'shopshoes.html') 
def shopmensfash(request):
 return render(request,'shopmensfash.html') 
def shopwatches(request):
 return render(request,'shopwatches.html')
def shopexe(request):
 return render(request,'shopexe.html') 
def shopshirts(request):
 return render(request,'shopshirts.html') 
def shopjeans(request):
 return render(request,'shopjeans.html') 
def shoptshirt(request):
 return render(request,'shoptshirt.html')
def shopsmartwatches(request):
 return render(request,'shopsmartwatches.html') 
def shophoodies(request):
 return render(request,'shophoodies.html')
def shopcasualshoes(request):
 return render(request,'shopcasualshoes.html') 
def shopbasenavtest(request):
 return render(request,'shopbasenavtest.html') 
def editprofile(request):
 return render(request,'editprofile.html') 
def checkout(request):
 return render(request,'checkout.html')
def payment(request):
 return render(request,'payment.html')
def paymentcomplete(request):
 return render(request,'paymentcomplete.html')
def paymentfail(request):
 return render(request,'paymentfail.html')