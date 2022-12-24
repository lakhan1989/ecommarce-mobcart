from django.contrib import admin
from .models import Products, Orders, Cart

# Register your models here.
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Cart)
