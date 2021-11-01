from django.urls import path,include
from . import views

urlpatterns = [
    path('adminbase/',views.adminbase,name='adminbase'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('brands/',views.brands,name='brands'),
    path('addprodd/',views.addprodd,name='addprodd'),
    path('addbrand/',views.addbrand,name='addbrand'),
    path('categoryy/',views.categoryy,name='categoryy'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('signupadmin/',views.signupadmin,name='signupadmin'),
    path('discount/',views.discount,name='discount'),
    path('productview/',views.productview,name='productview'),
    path('prodviewpage2/',views.prodviewpage2,name='prodviewpage2'),
    path('prodviewpage3/',views.prodviewpage3,name='prodviewpage3'),
    path('prodviewpage4/',views.prodviewpage4,name='prodviewpage4'),
    path('editprodview/',views.editprodview,name='editprodview'),
    path('editbrand/',views.editbrand,name='editbrand'),
    path('editcategory/',views.editcategory,name='editcategory'),
    path('slider/',views.slider,name='slider'),
    path('slider2/',views.slider2,name='slider2'),
    path('addslider/',views.addslider,name='addslider'),
    path('editslider/',views.editslider,name='editslider'),
    path('banner/',views.banner,name='banner'),
    path('addbanner/',views.addbanner,name='addbanner'),
    path('editbanner/',views.editbanner,name='editbanner'),
    path('orders/',views.orders,name='orders'),
    path('adddiscount/',views.adddiscount,name='adddiscount'),

    path('viewsingledataa/<int:id>',views.viewdata,name='viewdata'),
    path('updatee/<int:id>',views.update,name='update'),
    path('deleteuser/<int:id>',views.delete,name='delete'),
    

    path('viewcategorydata/<int:id>',views.viewcategorydata,name='viewcategorydata'),
    path('updatecategory/<int:id>',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),

    path('viewsliderdata/<int:id>',views.viewsliderdata,name='viewsliderdata'),
    path('updateslider/<int:id>',views.updateslider,name='updateslider'),
    path('deleteslider/<int:id>',views.deleteslider,name='deleteslider'),

    path('viewbannerdata/<int:id>',views.viewbannerdata,name='viewbannerdata'),
    path('updatebanner/<int:id>',views.updatebanner,name='updatebanner'),
    path('deletebanner/<int:id>',views.deletebanner,name='deletebanner'),

    path('addfootwears/',views.addfootwears,name='addfootwears'),

    path('viewproductdata/<int:id>',views.viewproductdata,name='viewproductdata'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),

    path('changecate',views.changecate,name='changecate'),

    path('addprodimages/',views.addprodimages,name='addprodimages'),

    path('addimg',views.addimg,name='addimg'),
    path('changeprod',views.changeprod,name='changeprod'),

    path('viewprodslider/<int:id>',views.viewprodslider,name='viewprodslider'),  

    path('edtprod',views.edtprod,name='edtprod'),



]