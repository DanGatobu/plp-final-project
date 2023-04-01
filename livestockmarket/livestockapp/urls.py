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
    path('course',views.course,name='course'),
    path('coursecontent',views.coursecontent,name='coursecontent'),
    path('statistics',views.statistics,name='statistics'),
    path('suppliments',views.suppliments,name='suppliments'),
    path('inventoryitems',views.inventoryitems,name='inventoryitems'),
    path('customers',views.customers,name='customers'),
    path('sellers',views.sellers,name='sellers'),
    
]