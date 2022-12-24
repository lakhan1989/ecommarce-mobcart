from django.shortcuts import render, redirect
from .models import Products, Orders, Cart
from django.contrib.auth.models import User
from .data import mobile_data
import os
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from django.contrib.auth import logout as logout_user, authenticate, login as login_user

# Create your views here.

# product list create==============================================
def index(request):
    data = {}
    data["products"] = Products.objects.all()

    for x in mobile_data:
    
        prod = Products.objects.update_or_create(product_name = x["product_name"], rating = x["rating"], product_description = x["product_description"], battery = x["battery"], price = x["price"], ram = x["ram"], color = x["color"], display_size = x["display_size"], camera = x["camera"], storage = x["storage"])

        img_temp = NamedTemporaryFile()
        img_temp.write(urlopen(x["image"]).read())
        img_temp.flush()

        prod.image.save(os.path.basename(x["image"]),File(img_temp))
        prod.save()

    return render(request, "index.html", data)


def home(request):
    data = {}
    data["allproducts"] = Products.objects.all()

    

    return render(request, "home.html", data)
 
# home list create=================================================
def product_list(request):
    data = {}
    data["products"] = Products.objects.all() 
    data["recent_item"] = Products.objects.all().order_by('created_at')[0:4]
    
    return render(request, "product_list.html", data)

# product page create===============================================
def product_page(request, id):
    data = {}
    data["items"] = Products.objects.get(id=id)
    data["recent_item"] = Products.objects.all().order_by('created_at')[0:4]

    if request.method == "POST":
        product = request.POST.get("product")
     
        if product:
            prd = Products.objects.get(id=product)
            
            Cart.objects.create(user="lakhan", product=prd, quantity=3)

            return redirect("product_cart")

    return render(request, "product_page.html", data)

# create cart ====================================================
def product_cart(request):
    data = {}
    
    data["cart_items"] = Cart.objects.all().order_by("-created_at")
    
    return render(request, "product_cart.html", data)

# order checkout fun==============================================
def checkout(request):
    data = {}

    data["orders"] = Orders.objects.all()
  
    if request.method == "POST":
      
        user = User.objects.get(id=1)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        company_name = request.POST.get("company_name")
        payment_method = request.POST.get("payment_method")
        country  = request.POST.get("country")
        address_line_1  = request.POST.get("address_line_1") 
        city  = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        phone_number = request.POST.get("phone_number")
        email  = request.POST.get("email")
        
        cart_items = Cart.objects.all().order_by("-created_at")

        if user and first_name and last_name and company_name and payment_method and country and address_line_1 and city and state and zip_code and phone_number and email:
            
            order = Orders.objects.create(user = user, first_name = first_name, last_name = last_name, company_name = company_name, payment_method = payment_method, country = country, address_line_1 = address_line_1, city = city, state = state, zip_code = zip_code, phone_number = phone_number, email = email)
            order.save()

            for x in cart_items:
                order.products.add(x.product)

            return redirect("thanks")
        
    return render(request, "checkout.html", data)
    

def order_history(request):
    data = {}
    data["orders"] = Orders.objects.all()

    return render(request, "order_history.html", data)


def thanks(request):
    
    return render(request, "thanks.html")


def login(request):
    
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":

        user_name = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=user_name, password=password)
        
        if user:
            login_user(request, user)
            return redirect("home")
        else:
            print("User does not exist.")
    
    return render(request, "login.html")


def register(request):
    
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":

        user_name = request.POST.get("username")
        email_address = request.POST.get("email")
        password = request.POST.get("password")

        if user_name and email_address:

            user = User.objects.create(username = user_name, email = email_address)
            user.set_password(password)
            user.save()

    return render(request, "register.html")

def logout(request):
    logout_user(request)
    return redirect("login")