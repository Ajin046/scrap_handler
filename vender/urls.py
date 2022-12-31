from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('signin', views.vendersign_in, name="vendersign_in"),
    path('vsignup', views.vendersign_up, name="vendersign_up"),
    path('venderh', views.vendor_home, name="vendor_home"),
    
]