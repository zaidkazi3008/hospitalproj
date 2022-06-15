from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.handlelogin, name='handlelogin'),
    path("dashboard", views.index, name='home'),
    path("consultation" , views.consultation, name='consultation'),
    path("report" , views.report, name='report'),   
    path("signup" , views.handlesignup, name='handlesignup'),
    path("login" , views.handlelogin, name='handlelogin'),
    path("logout" , views.handlelogout, name='handlelogout'),
]