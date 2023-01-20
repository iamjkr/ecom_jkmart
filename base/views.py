from django.shortcuts import render

# Create your views here.

def home_page(reuest):
    return render(reuest, 'index.html')

