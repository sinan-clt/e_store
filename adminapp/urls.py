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
    
    
]