from django.urls import path

from .middlewares.auth import isLoggedIn
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[

    path('login',views.Login.as_view(),name='login'),
    path('signup',views.SignUp.as_view(),name='signup'),
    path('logout',views.logout),
    path('viewProfile',isLoggedIn(views.ViewProfile.as_view()),name='viewProfile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword/sendEmail.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='resetPassword/emailConfirmation.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='resetPassword/newPassword.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPassword/resetComplete.html'), name ='password_reset_complete'),

]