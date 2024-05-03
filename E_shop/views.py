from django.shortcuts import render, redirect
from store_app.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def BASE(request):
    return render(request, "main/base.html")


def HOME(request):
    product = Product.objects.filter(status="PUBLISH")

    context = {
        'product': product
    }
    return render(request, "main/index.html", context)


def PRODUCT(request):
     
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    
    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    
    ATOZID = request.GET.get('ATOZ')    
    ZTOAID = request.GET.get('ZTOA')
    
    PRICE_LOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOW = request.GET.get('PRICE_HIGHOLOW')
    
    NEW_PRODUCTID = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID = request.GET.get('OLD_PRODUCT')
    
    if CATID:
        product = Product.objects.filter(categories = CATID, status="PUBLISH")
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price = PRICE_FILTER_ID, status="PUBLISH")
    elif COLORID:
        product = Product.objects.filter(color = COLORID, status="PUBLISH")
    elif BRANDID:
        product = Product.objects.filter(brand = BRANDID, status="PUBLISH")
    elif ATOZID:
        product = Product.objects.filter(status='PUBLISH').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='PUBLISH').order_by('-name')
    elif PRICE_LOWTOHIGHID:
        product = Product.objects.filter(status='PUBLISH').order_by('price')
    elif PRICE_HIGHTOLOW:
        product = Product.objects.filter(status='PUBLISH').order_by('-price')
    elif NEW_PRODUCTID:
        product = Product.objects.filter(status='PUBLISH').order_by('created_data')
    elif OLD_PRODUCTID:
        product = Product.objects.filter(status='PUBLISH').order_by('-created_data')
    else:
        product = Product.objects.filter(status="PUBLISH")
        
    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,
    }
    return render(request, "main/product.html", context)


def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)
    
    context = {'product': product}
    return render(request, "main/search.html", context)

from django.shortcuts import get_object_or_404

def PRODUCT_DETAIL_PAGE(request, id):
    prod = get_object_or_404(Product, id=id)
    context = {'prod': prod}
    return render(request, "main/product_single.html", context)



def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        email_from = settings.EMAIL_HOST_USER

  
            # Sending the email using send_mail function
        send_mail(subject, message, email_from, [samurcazaki@gmail.com])
        # Save the contact details to the database
        contact.save()
        return redirect('home')

    return render(request, "main/contact.html")


def HandleRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # Check if passwords match
        if pass1 != pass2:
            # Redirect back to registration page with an error message
            return render(request, "register/auth.html", {'error': 'Passwords do not match'})
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            # Redirect back to registration page with an error message
            return render(request, "register/auth.html", {'error': 'Username already exists'})
        
        # Create a new user if username is unique and passwords match
        customer = User.objects.create_user(username=username, email=email, password=pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('register')
        
    return render(request, "register/auth.html")


def Handlelogin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)          
            return redirect('home')
        else:
            return redirect('login')
            
    return render(request, "register/auth.html")



def Handlelogout(request):  
    logout(request) 
    return render(request, "main/index.html")


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Card/cart_details.html')









