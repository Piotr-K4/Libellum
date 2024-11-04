from re import L
from django.forms import ModelForm, widgets
from django import forms
from .models import Book


class BookForm(ModelForm):
    tags = forms.CharField(label="Tagi", widget=forms.TextInput)
    class Meta:
        model = Book
        # fields = "__all__"
        exclude = ["addedByUser",]
        
        labels = {
            "title":"Tytuł",
            "author":"Autor",
            "category":"Kategoria",
            "tags":"Tagi",
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
        
        self.fields['image'].widget.attrs['style'] = "display: none;"
        self.fields['image'].widget.attrs['id'] = "upload"
        self.fields['date_realease'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['title'].widget.attrs['placeholder'] = "Tytuł"
        self.fields['author'].widget.attrs['placeholder'] = "Autor"
        self.fields['tags'].widget.attrs['placeholder'] = "Tag1, Tag2, "
        self.fields['description'].widget.attrs['placeholder'] = "Ksiązka opowiada o ......"
        self.fields['publisher'].widget.attrs['placeholder'] = "Wydawca"
        self.fields['isbn'].widget.attrs['placeholder'] = "1234567890123"

