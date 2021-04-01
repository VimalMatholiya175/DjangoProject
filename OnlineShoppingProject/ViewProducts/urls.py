from django.urls import path

from . import views

urlpatterns = [
    
    path('search',views.search,name='search'),
    path('afilter/<str:selectedCategory>',views.afilter,name='afilter'),
    path('productDetails/<int:id>',views.productDetails,name='productDetails'),
    # path('displayCategory/<str:selectedCategory>',views.displayCategory,name='displayCategory'),

]