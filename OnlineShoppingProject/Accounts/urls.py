from django.urls import path

from . import views

urlpatterns=[

    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout),
    path('resetPassword',views.resetPassword,name='resetPassword.html'),
    path('viewProfile',views.viewProfile,name='viewProfile.html'),

]