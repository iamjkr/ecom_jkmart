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
        title = Product.objects.filter(category=val).values('title').annotate(count=Count('id')).order_by('-count')
        return render(request, 'category.html',locals())