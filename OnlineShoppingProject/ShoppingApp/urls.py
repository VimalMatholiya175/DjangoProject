from django.urls import path

from . import views

urlpatterns=[

    path('',views.home,name='index'),
    path('viewProduct',views.viewProduct,name='viewProduct.html'),

]