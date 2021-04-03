from django.urls import path

from Accounts.middlewares.auth import isLoggedIn

from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('addToCart',isLoggedIn(views.addToCart),name='addToCart'),
    path('changeQty/<int:productId>/<str:op>',views.changeQty,name='changeQty'),
    path('viewCart',isLoggedIn(views.viewCart),name='viewCart'),
    path('removeFromCart/<int:productId>',views.removeFromCart,name='removeFromCart'),
    path('checkout',isLoggedIn(views.Checkout.as_view()),name='checkout'),
    path('orders',isLoggedIn(views.orders),name='orders'),
    path('cancelOrder',isLoggedIn(views.cancelOrder),name='cancelOrder'),

]