from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages ,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user,group_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .models import inventory,customerorder,tempcart





def home(request):
    return render(request,'homepage.html')


@unauthenticated_user
def register(request):
   
    form=createuserform()
    if request.method=='POST':
        form=createuserform(request.POST)
        if form.is_valid():
        
            user=form.save()
            is_vendor = request.POST.get('is_vendor')
            is_customer = request.POST.get('is_customer')
            if is_vendor:
                vendor_group = Group.objects.get(name='farmer')
                vendor_group.user_set.add(user)
            elif is_customer:
                customer_group = Group.objects.get(name='customers')
                customer_group.user_set.add(user)
        
            username=form.cleaned_data.get('username')
            messages.success(request,'account was created for user ' + username)
            
            return redirect('loginpage')
            
    context={'form':form}

    return render(request,'register.html',context)
@unauthenticated_user
def loginpage(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect(home) 
        else:
            messages.info(request,' Username or Password is incorrect ')
            
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def cart(request):
    user_id = request.user.id
    
    try:
        # Check if cart object already exists for user
        user_cart = tempcart.objects.get(owner=user_id)
        
        if request.method == 'POST':
            item_id = request.POST['itemid']

            # Add item to cart
            item = inventory.objects.get(id=item_id)
            
            
            user_cart.items.add(item)
        
        # Calculate total price of items in cart
        
        
        item_prices = [itm.price for itm in user_cart.items.all()]
        total_price = sum(item_prices)
        usercart=tempcart.objects.filter(owner=user_id)
        context={'items':usercart,'totalprice':total_price}
        
        
        

    except tempcart.DoesNotExist:
        if request.method == 'POST':
            item_id = request.POST['itemid']
            # Create new cart object for user and add item to it
            user_cart = tempcart.objects.create(owner_id=user_id)
            item = inventory.objects.get(id=item_id)
            user_cart.items.add(item)

            total_price = item.price
            usercart=tempcart.objects.filter(owner=user_id)
            context={'items':usercart,'totalprice':total_price}
            
        else:
            context = {}
            
    
    
    return render(request, 'cart.html', context)

            


@login_required(login_url='loginpage')
def orders(request):
    user = request.user.id
    if request.method == 'POST':
        itemidd = request.POST['itemid']
        totalprice = request.session['totalprice']
        cartiditems = tempcart.objects.get(id=itemidd)
        itemids = cartiditems.items.all()
        customerinstance = User.objects.get(id=user)
        orderobj = customerorder.objects.create(owner=customerinstance, totalprice=totalprice)
        for it in itemids:
            orderobj.items.add(it)
    
        cartiditems.delete()
        return redirect('market')
    itemss = customerorder.objects.filter(owner=user)
    context = {'orders': itemss}
    return render(request, 'orders.html', context)


@login_required(login_url='loginpage')

def cartnormal(request):
    user_id=request.user.id
    usercart=tempcart.objects.filter(owner=user_id)
    user_cart = tempcart.objects.get(owner=user_id)
    item_prices = [itm.price for itm in user_cart.items.all()]
    total_price = sum(item_prices)
    
    context={'items':usercart,'price':total_price}
    return render(request,'cart.html',context)


@login_required(login_url='loginpage')

def removefromcart(request):
    if request.method == 'POST':
        cartid = request.POST['cartid']
        itemid = request.POST['itemid']
        cart_item = tempcart.objects.get(id=cartid)
        item = cart_item.items.get(id=itemid)
        cart_item.items.remove(item)
        return redirect('cartnormal')
    return render(request, 'cart.html')




@login_required(login_url='loginpage')

def market(request):
    items=inventory.objects.exclude(category='suppliments')

    context={'inventory':items}
    
    return render(request,'market.html',context)

@login_required(login_url='loginpage')

def farmersdashboard(request):
    vendor_id=request.user.id
    vendor=User.objects.get(id=vendor_id)
       
    items=inventory.objects.filter(vendor=vendor)
    context={'inventory':items}
    if request.method=='POST':
        id=request.POST['itemid']
        itemdelete=inventory.objects.get(id=id)
        
        itemdelete.delete()
        
        return redirect('farmersdashboard')
    return render(request,'farmersdashboard.html',context)





@login_required(login_url='loginpage')

def suppliments(request):
    items=inventory.objects.filter(category='suppliments')

    context={'inventory':items}
    
    return render(request,'marketbuysuppliments.html',context)

@login_required(login_url='loginpage')

def inventoryitems(request):
    user=request.user.id
    userinstance=User.objects.get(id=user)
    if request.user.groups.filter(name='superuser').exists():
        inventorrry=inventory.objects.all()
        context={'inventory':inventorrry}
        return render(request,'inventory.html',context)
    elif request.user.groups.filter(name='farmer').exists():
        inventorrry=inventory.objects.filter(vendor=userinstance)
        context={'inventory':inventorrry}
        return render(request,'inventory.html',context)
    
    return render(request,'inventory.html')


@login_required(login_url='loginpage')

def customers(request):
    customers_group = Group.objects.get(name='customers')
    customers = customers_group.user_set.all()

    context={'users':customers}
    return render(request,'superusercustomers.html',context)

@login_required(login_url='loginpage')

def sellers(request):
    customers_group = Group.objects.get(name='farmer')
    customers = customers_group.user_set.all()

    context={'users':customers}
    return render(request,'superusercustomers.html',context)
    return render(request,'superusersellers.html')





