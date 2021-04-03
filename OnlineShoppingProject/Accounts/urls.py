from django.urls import path

from .middlewares.auth import isLoggedIn

from . import views

urlpatterns=[

    path('login',views.Login.as_view(),name='login'),
    path('signup',views.SignUp.as_view(),name='signup'),
    path('logout',views.logout),
    path('viewProfile',isLoggedIn(views.ViewProfile.as_view()),name='viewProfile'),
    

]