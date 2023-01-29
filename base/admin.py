from django.contrib import admin
from .models import Product, Customer


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discount_price','category']


admin.site.register(Customer)


# admin.site.register(Product)