from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from .models import Profil,User
from django.contrib.auth import login, authenticate

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



def userAccount(request):
    return render(request, "users/account.html")
