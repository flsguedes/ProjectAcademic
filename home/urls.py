from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import *

urlpatterns = [ 
    path("auth_login/", AuthLogin, name="auth_login"),
    path("base/", Base, name="base"),
    path("", Index, name="index"),
]