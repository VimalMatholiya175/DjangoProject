from django.urls import path

from . import views

urlpatterns=[

    path('login',views.login,name='login'),
    path('register',views.register,name='registration'),
    path('logout',views.logout),
    path('reset',views.reset,name='resetpass.html'),
    path('viewProfile',views.viewProfile,name='viewProfile.html'),

]