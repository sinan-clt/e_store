from django.urls import path,include
from . import views

urlpatterns = [
    path('adminbase',views.adminbase,name='adminbase'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('brands',views.brands,name='brands'),
    path('addprod',views.addprod,name='addprod'),
    path('addbrand',views.addbrand,name='addbrand'),
    path('category',views.category,name='category'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('signupadmin',views.signupadmin,name='signupadmin'),
    path('discount',views.discount,name='discount'),
    path('productview',views.productview,name='productview'),
    path('prodviewpage2',views.prodviewpage2,name='prodviewpage2'),
    path('prodviewpage3',views.prodviewpage3,name='prodviewpage3'),
    path('prodviewpage4',views.prodviewpage4,name='prodviewpage4'),
    path('editprodview',views.editprodview,name='editprodview'),
    path('editbrand',views.editbrand,name='editbrand'),
    path('editcategory',views.editcategory,name='editcategory'),
    path('slider',views.slider,name='slider'),
    path('slider2',views.slider2,name='slider2'),
    path('addslider',views.addslider,name='addslider'),
    path('editslider',views.editslider,name='editslider'),
    path('banner',views.banner,name='banner'),
    path('addbanner',views.addbanner,name='addbanner'),
    path('editbanner',views.editbanner,name='editbanner'),
    path('orders',views.orders,name='orders'),
    path('adddiscount',views.adddiscount,name='adddiscount'),

    


    
    
]