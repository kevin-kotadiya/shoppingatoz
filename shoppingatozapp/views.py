from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def shop(request):
    return render(request,'shop.html')

def checkout(request):
    return render(request,'checkout.html')