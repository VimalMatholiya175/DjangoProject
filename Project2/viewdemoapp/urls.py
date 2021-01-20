from viewdemoapp import views
from django.conf.urls import url

urlpatterns=[
	url('',views.HomePageView.as_view()),
]