from django.urls import path,include
from . import views

urlpatterns = [
    path('user/',views.user,name='user'),
    path('shop/',views.shop,name='shop'),
    path('shopprod1/',views.shopprod1,name='shopprod1'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.cart,name='cart'),
    path('log/',views.log,name='log'),
    path('shopprod3/',views.shopprod3,name='shopprod3'),
    path('shopbase/',views.shopbase,name='shopbase'),
    path('shopprod4/',views.shopprod4,name='shopprod4'),
    path('shopprod2/',views.shopprod2,name='shopprod2'),
    path('shopprod5/',views.shopprod5,name='shopprod5'),
    path('shopprod6/',views.shopprod6,name='shopprod6'),
    path('shopprod7/',views.shopprod7,name='shopprod7'),
    path('shopprod8/',views.shopprod8,name='shopprod8'),
    path('shopprod9/',views.shopprod9,name='shopprod9'),
    path('shopprod10/',views.shopprod10,name='shopprod10'),
    path('shopprod11/',views.shopprod11,name='shopprod11'),
    path('shopprod12/',views.shopprod12,name='shopprod12'),
    path('shopprod13/',views.shopprod13,name='shopprod13'),
    path('shopprod14/',views.shopprod14,name='shopprod14'),
    path('shopprod15/',views.shopprod15,name='shopprod15'),
    path('shopprod16/',views.shopprod16,name='shopprod16'),
    path('shopprod17/',views.shopprod17,name='shopprod17'),
    path('shopprod18/',views.shopprod18,name='shopprod18'),
    path('shopprod19/',views.shopprod19,name='shopprod19'),
    path('shopprod20/',views.shopprod20,name='shopprod20'),
    path('shopprodpage2/',views.shopprodpage2,name='shopprodpage2'),
    path('shopprod21/',views.shopprod21,name='shopprod21'),
    path('shopprod22/',views.shopprod22,name='shopprod22'),
    path('shopprod23/',views.shopprod23,name='shopprod23'),
    path('shopprod24/',views.shopprod24,name='shopprod24'),
    path('shopprod25/',views.shopprod25,name='shopprod25'),
    path('shopprod26/',views.shopprod26,name='shopprod26'),
    path('shopprod27/',views.shopprod27,name='shopprod27'),
    path('shopprod28/',views.shopprod28,name='shopprod28'),
    path('shopprod29/',views.shopprod29,name='shopprod29'),
    path('shopprod30/',views.shopprod30,name='shopprod30'),
    path('shopprod31/',views.shopprod31,name='shopprod31'),
    path('shopprod32/',views.shopprod32,name='shopprod32'),
    path('shopshoes/',views.shopshoes,name='shopshoes'),
    path('shopmensfash/',views.shopmensfash,name='shopmensfash'),
    path('shopwatches/',views.shopwatches,name='shopwatches'),
    path('shopexe/',views.shopexe,name='shopexe'),
    path('shopshirts/',views.shopshirts,name='shopshirts'),
    path('shopjeans/',views.shopjeans,name='shopjeans'),
    path('shoptshirt/',views.shoptshirt,name='shoptshirt'),
    path('shopsmartwatches/',views.shopsmartwatches,name='shopsmartwatches'),
    path('shophoodies/',views.shophoodies,name='shophoodies'),
    path('shopcasualshoes/',views.shopcasualshoes,name='shopcasualshoes'),
    path('shopbasenavtest/',views.shopbasenavtest,name='shopbasenavtest'),
    path('shopafterlogin/',views.shopafterlogin,name='shopafterlogin'),
    
    path('changepass/',views.changepass,name='changepass'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment/',views.payment,name='payment'),
    path('paymentcomplete/',views.paymentcomplete,name='paymentcomplete'),
    path('paymentfail/',views.paymentfail,name='paymentfail'),

    # path('editprofile/',views.editprofile,name='editprofile'),
    

    path('viewsingledata/<int:id>',views.viewsingledata,name='viewsingledata'),

    path('update/<int:id>',views.update,name='update'),




    
]