from django.db import models
import uuid
from users.models import Profil

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

    def __str__(self):
        return self.name


class Book(models.Model):
    image = models.ImageField(upload_to="books/",default="books/default_book.png")
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=True, blank=False)
    category = models.ForeignKey("SubBookCategories", null=True, blank=False,  on_delete=models.SET_NULL)
    description = models.TextField(max_length=2000, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=False)
    date_realease = models.DateField(null=True, blank=False) 
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=False)
    pages = models.PositiveIntegerField(default=0)
    language = models.ForeignKey("Language", null=True, blank=False, on_delete=models.SET_NULL)
    addedByUser = models.ForeignKey(Profil, null=True, blank=False, on_delete=models.SET_NULL)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

    def __str__(self):
        return self.title
    

class BookCategories(models.Model):
    categoryName = models.CharField(max_length=100, null=False, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.categoryName
    
class SubBookCategories(models.Model):
    subCategoryName = models.CharField(max_length=100, null=False, blank=False)
    bookcategory = models.ForeignKey('BookCategories', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.subCategoryName

