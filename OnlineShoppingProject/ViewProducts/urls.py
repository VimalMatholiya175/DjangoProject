from django.urls import path

from . import views

urlpatterns = [
    
    path('search',views.search,name='search'),
    path('xfilter',views.xfilter,name='xfilter'),
    path('productDetails',views.productDetails,name='productDetails'),
    path('displayCategory',views.displayCategory,name='displayCategory'),


]