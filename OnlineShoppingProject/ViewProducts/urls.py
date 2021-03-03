from django.urls import path

from . import views

urlpatterns = [
    
    path('search',views.search,name='search'),
    path('xfilter',views.xfilter,name='xfilter'),
    path('viewDetails',views.viewDetails,name='viewDetails'),
    path('displayCategory',views.displayCategory,name='displayCategory'),


]