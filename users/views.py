from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm

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
    

def login(request):
    form = UserLoginForm()
    context = {"form":form}

    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        print(email)
        print(password)


    return render(request, "users/login.html", context)
