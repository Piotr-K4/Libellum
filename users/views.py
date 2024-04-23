from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm, UserEditSettingsForm
from .models import Profil,User
from books.models import Book
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.



def register(request):
    form = UserCreateForm()
    context = {"form":form}
    
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    return render(request, "users/register.html", context)
    

def userlogin(request):
    form = UserLoginForm()
    context = {"form":form}

    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']


        try:
            User.objects.get(username=name)
        except:
            print("Nie ma użytkwonnika")
        else:
            user = authenticate(request, username=name, password=password)

            if user is not None:
                login(request, user)
                print("Zalogowany")
                return redirect("index")
            else:
                print("Nie zalogowany")
            




    return render(request, "users/login.html", context)



@login_required(login_url="login")
def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")

    return render(request, "users/logout.html")


@login_required(login_url="login")
def userAccount(request):
    profil = Profil.objects.get(user=request.user)
    bookaddByUser = Book.objects.filter(addedByUser=request.user.profil).count()
    context = {"profil":profil, "bookaddByUser":bookaddByUser}
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def userSettings(request):
    profil = Profil.objects.get(user=request.user)
    context = {"profil":profil}
    return render(request, "users/settings.html", context)

@login_required(login_url="login")
def userEditSettings(request):
    user = request.user.profil
    form = UserEditSettingsForm(instance=user)
    context = {"form":form}


    if request.method == "POST":
        form = UserEditSettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user-settings")


    return render(request, "users/editsettings.html", context)



