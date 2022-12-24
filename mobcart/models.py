from django.db import models
from django.contrib.auth.models import User

# Create Prouduct class------------------------------------------.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    rating = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    product_description = models.CharField(max_length=200)
    battery = models.CharField(max_length=50)
    price = models.IntegerField()
    ram = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    display_size = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

# creat orders class ----------------------------------------
class Orders(models.Model):

    PAYMENT_CHOICES = [
        ('upi', 'Upi'),
        ('gpay', 'Gpay'),
        ('phonepay', 'PhonePay'),
        ('paytm', 'Paytm')
    ]

    COUNTRY_CHOICES = [
        ('india', 'India'),
        ('usa', 'Usa'),
        ('indonesia', 'Indonesia'),
        ('mexico', 'Mexico'),
        ('spain', 'Spain')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("Products")
    first_name =  models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    payment_method = models.CharField(choices = PAYMENT_CHOICES, max_length=50)
    country = models.CharField(choices = COUNTRY_CHOICES, max_length=100)
    address_line_1 = models.TextField()  
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

# create cart class--------------------------------------------
class Cart(models.Model):
    user = models.CharField(max_length=100)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user



