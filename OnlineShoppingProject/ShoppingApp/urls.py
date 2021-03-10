from django.urls import path

from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('addToCart',views.addToCart,name='addToCart'),
    path('changeQty',views.changeQty,name='changeQty'),
    path('viewCart',views.viewCart,name='viewCart'),
    path('removeFromCart',views.removeFromCart,name='removeFromCart'),

]