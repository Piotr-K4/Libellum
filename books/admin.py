from django.contrib import admin
from .models import Book, BookCategories, SubBookCategories, Language, BookTags

# Register your models here.


admin.site.register(Book)
admin.site.register(BookCategories)
admin.site.register(SubBookCategories)
admin.site.register(Language)
admin.site.register(BookTags)
