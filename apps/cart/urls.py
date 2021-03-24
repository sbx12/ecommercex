from django.urls import path

from . import views

urlpatterns = [
    path('mycart', views.cart_detail, name='cart'),
]