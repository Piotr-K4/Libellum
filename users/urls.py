from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path("register.html", views.register, name="register"),
        path("login.html", views.userlogin, name="login"),
        path("account.html", views.userAccount, name="account"),
        path("settings.html", views.userSettings, name="user-settings"),
        path("editsettings.html", views.userEditSettings, name="user-Editsettings"),
        path("logout.html", views.userLogout, name="logout"),
]

