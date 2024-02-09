from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.



def index(request):

    return render(request,"main.html")


def books(request):
    books = Book.objects.all()
    context = {"books":books}
    
    return render(request,"books/books.html",context)
    
def book(request,pk):
    book = Book.objects.get(id=pk)
    context = {"book":book}
    
    return render(request,"books/book.html",context)
    

def addbook(request):
    form = BookForm()
    

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    context = {
        "basic":form.visible_fields()[:4],
        "descriptionInfo":form.visible_fields()[4:6],
        "publisherInfo":form.visible_fields()[6:11]
        
        }
    return render(request, "books/addbook.html", context)