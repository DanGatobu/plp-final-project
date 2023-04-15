from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('register',views.register,name='register'),
    path('cart',views.cart,name='cart'),
    path('orders',views.orders,name='orders'),
    path('cartnormal',views.cartnormal,name='cartnormal'),
    path('removefromcart',views.removefromcart,name='removefromcart'),
    path('market',views.market,name='market'),
    path('farmersdashboard',views.farmersdashboard,name='farmersdashboard'),
    path('supplimentscart',views.supplimentscart,name='supplimentscart'),
    path('removesupplimentfromcart',views.removesupplimentfromcart,name='removesupplimentfromcart'),
    path('suppliments',views.suppliments,name='suppliments'),
    path('inventoryitems',views.inventoryitems,name='inventoryitems'),
    path('customers',views.customers,name='customers'),
    path('sellers',views.sellers,name='sellers'),
    
]