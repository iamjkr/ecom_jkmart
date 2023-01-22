from django.shortcuts import render
from django.views import View
from .models import Product
from django.db.models import Count

# Create your views here.

def home_page(reuest):
    return render(reuest, 'index.html')


class CategoryView(View):
    def get(self, request,val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'category.html',locals())

class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        print(product)
        title = Product.objects.filter(category=product[0].category).values('title')
        print(val.title)
        return render(request, 'category.html',locals())

class CategoryDetail(View):
    def get(self, request,pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product_detail.html',locals())

