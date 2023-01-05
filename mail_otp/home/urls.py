from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('sendmail', views.sendmail,name="sendmail"),
    path('verify', views.verify,name="verify"),
]