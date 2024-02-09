from django.forms import ModelForm, widgets
from django import forms
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
        labels = {
            "title":"Tytuł",
            "author":"Autor",
            "category":"Kategoria",
            "description":"Opis",
            "source":"Źródło",
            "publisher":"Wydawca",
            "date_realease":"Data wydania",
            "isbn":"ISBN",
            "pages":"Liczba stron",
            "language":"Język",
        }

 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['image'].widget.attrs['class'] = "addbook__basicInfo__inputFile--button"
        self.fields['image'].widget.attrs['id'] = "upload"
    