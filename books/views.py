import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.test import tag
from .models import Book, BookTags, BookCategories, SubBookCategories
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):

    return render(request,"books/index.html")


def books(request):
    books = Book.objects.all()
    tags = BookTags.objects.all()
    categories = BookCategories.objects.all()
    subcategories = SubBookCategories.objects.all()
    context = {"books":books, "tags":tags, "categories":categories, "subcategories":subcategories}
    
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
            tagi = request.POST.get("tags").lower()

            tagi = tagi.split(",")

            for tag in range(len(tagi)):
                tagi[tag] = tagi[tag].lstrip()
                tagi[tag] = tagi[tag].rstrip()


            print(tagi)

            for tag in tagi:
                if not BookTags.objects.filter(name=tag).exists():
                    BookTags.objects.create(name=tag)


            book.save()
            return redirect("index")
        else:
            print(form.errors)
    
    context = {
        "basic":form.visible_fields()[:5],
        "descriptionInfo":form.visible_fields()[5:7],
        "publisherInfo":form.visible_fields()[7:12]
        }
    return render(request, "books/addbook.html", context)
