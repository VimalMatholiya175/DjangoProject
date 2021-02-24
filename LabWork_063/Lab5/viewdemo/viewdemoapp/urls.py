from django.conf.urls import url
from viewdemoapp import views
urlpatterns = [
 url('', views.HomePageView.as_view()),
]