from django.contrib import admin
from django.urls import path,include
from shoppingatozapp import views

urlpatterns = [
    path('',views.index),
    path('cart',views.cart, name = 'cart'),
    path('shop',views.shop, name = 'shop'),
    path('checkout',views.checkout, name = 'checkout'),
]