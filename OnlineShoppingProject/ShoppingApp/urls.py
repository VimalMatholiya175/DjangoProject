from django.urls import path

from Accounts.middlewares.auth import isLoggedIn

from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('addToCart',isLoggedIn(views.addToCart),name='addToCart'),
    path('changeQty',views.changeQty,name='changeQty'),
    path('viewCart',isLoggedIn(views.viewCart),name='viewCart'),
    path('removeFromCart',views.removeFromCart,name='removeFromCart'),
    path('checkout',isLoggedIn(views.Checkout.as_view()),name='checkout'),

]