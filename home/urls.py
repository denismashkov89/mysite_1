from operator import index
from django.contrib.auth import views
from django.urls import include, path
from .views import *

urlpatterns = [
    path("", index,name= "index"),
    path('', include ("home.urls")),
]



