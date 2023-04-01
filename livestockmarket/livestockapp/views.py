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
from .models import suppliments as supp





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
        context={'items':usercart}
        

    except tempcart.DoesNotExist:
        if request.method == 'POST':
            item_id = request.POST['itemid']
            
            # Create new cart object for user and add item to it
            user_cart = tempcart.objects.create(owner_id=user_id)
            item = inventory.objects.get(id=item_id)
            user_cart.items.add(item)
            total_price = item.price
            usercart=tempcart.objects.filter(owner=user_id)
            context={'items':usercart}
            
        else:
            context = {}
            
    
    # request.session['totalprice'] = total_price
    
    return render(request, 'cart.html', context)

            
        
        





@login_required(login_url='loginpage')
def orders(request):
    user = request.user.id
    if request.method == 'POST':
        itemidd = request.POST['itemid']
        totalprice = request.session['totalprice']
        cartiditems = tempcart.objects.get(id=itemidd)
        itemids = cartiditems.items.all()
        for it in itemids:
            customerinstance=User.objects.get(id=user)
            orderobj = customerorder.objects.create(owner=customerinstance, totalprice=totalprice)
            orderobj.items.add(it)
        cartiditems.delete()
        return redirect('items')
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
    items=inventory.objects.all()
    context={'inventory':items}
    
    return render(request,'market.html',context)

@login_required(login_url='loginpage')

def farmersdashboard(request):
    
    return render(request,'farmersdashboard.html')

@login_required(login_url='loginpage')

def course(request):
    
    return render(request,'courseoverveiw.html')

@login_required(login_url='loginpage')

def coursecontent(request):
    
    return render(request,'coursecontent.html')

@login_required(login_url='loginpage')

def statistics(request):
       #write if statement to take to diff page depending on role
    return render(request,'coursecontent.html')

@login_required(login_url='loginpage')

def suppliments(request):
    items=supp.objects.all()
    context={'inventory':items}
    
    return render(request,'marketbuysuppliments.html')

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
       #write if statement to take to diff page depending on role
    return render(request,'superusercustomers.html')

@login_required(login_url='loginpage')

def sellers(request):
       #write if statement to take to diff page depending on role
    return render(request,'superusersellers.html')





