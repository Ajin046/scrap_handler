from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('scrap_select/', views.sc_select, name="sc_select"),
    path('user_profile/', views.user_pro, name="user_pro"),
    path('user_confirm/<str:items>', views.user_con, name="user_con"),

]
