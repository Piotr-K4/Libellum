from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Profil

class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        labels = {
                "first_name":"Imie",
                "last_name":"Nazwisko",
                "username":"Pseudonim",
                "email":"Email",
                }
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = "__all__"

class UserEditSettingsForm(ModelForm):
    class Meta:
        model = Profil
        exclude = ["user",]
        labels = {
                "username":"Pseudonim",
                "profileImage":"Zdjęcie profilowe",
                "dateBirth":"Data urodzenia",
                "sexUser":"Płeć",
                "description":"Opis"
                }

