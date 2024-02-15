from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):

    return render(request,"books/index.html")


def books(request):
    books = Book.objects.all()
    context = {"books":books}
    
    return render(request,"books/books.html",context)
    
def book(request,pk):
    book = Book.objects.get(id=pk)
    context = {"book":book}
    
    return render(request,"books/book.html",context)
    

@login_required(login_url="login")
def addbook(request):
    form = BookForm()
    

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.addedByUser = request.user.profil
            book.save()
            return redirect("index")
        else:
            print(form.errors)
    
    context = {
        "basic":form.visible_fields()[:4],
        "descriptionInfo":form.visible_fields()[4:6],
        "publisherInfo":form.visible_fields()[6:11]
        
        }
    return render(request, "books/addbook.html", context)
