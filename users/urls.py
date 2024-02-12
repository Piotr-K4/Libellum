from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path("register.html", views.register, name="register"),
        path("login.html", views.userlogin, name="login"),
        path("account.html", views.userAccount, name="account")
]

