from django.urls import path

from . import views

urlpatterns=[

    path('',views.home,name='index'),
    path('addToCart',views.addToCart,name='addToCart'),
    path('iQuantity',views.iQuantity,name='iQuantity'),
    path('dQuantity',views.dQuantity,name='dQuantity'),



]